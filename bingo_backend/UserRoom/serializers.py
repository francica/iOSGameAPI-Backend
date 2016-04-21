from rest_framework import serializers
from UserRoom.models import User, Room

class UserManager(object):

	def get_users(self):
		return User.objects.all()

	def get_user(self, user_id):
		return User.objects.get(user_id = user_id)

	def add_user(self, name):
		try:
			temp = User(name = name)
			temp.save()
			return temp.user_id
		except:
			return -1

	def remove_user(self, user_id):
		try:
			temp = User.objects.get(user_id = user_id)
			temp.delete()
			return 1
		except:
			return -1

	def get_score(self, user_id):
		temp = User.objects.get(user_id = user_id)
		if temp == None:
			return -1
		else:
			return temp.score

	def score_update(self, user_id, score):
		temp = User.objects.get(user_id = user_id)
		if temp == None:
			return -1
		else:
			temp.score = score
			temp.save()
			return 1

	def get_name(self, user_id):
		temp = User.objects.get(user_id = user_id)
		if temp == None:
			return ''
		else:
			return temp.name


class RoomManager(object):

	def get_all_rooms(self):
		return Room.objects.all()

	def get_room(self, room_id):
		return Room.objects.get(room_id = room_id)

	def create_room(self, user_id, room_name):
		try:
			temp = Room(owner_id = int(user_id), users = str(user_id), name = room_name)
			temp.save()
			return temp.room_id
		except:
			return -1

	def remove_room(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			temp.delete()
			return 1
		except:
			return -1	

	def add_player(self, user_id, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			if str(user_id) in temp.users.split('-'):
				return 1 #already in 
			temp.users += ('-' + str(user_id))
			temp.save()
			return 1
		except:
			return -1

	def remove_player(self, user_id, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			user_s = temp.users.split('-')
			user_s = [each for each in user_s if each]
			user_s.remove(str(user_id))

			if temp.owner_id == int(user_id):
				if len(user_s) >= 1:
					temp.owner_id = int(user_s[0])
				else:
					self.remove_room(room_id)
					return 1

			user_str = ''
			for each in user_s:
				if each != '':
					user_str += ('-' + each)
			temp.users = user_str
			temp.save()
			return 1
		except:
			return -1	

	def get_players(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			user_s = temp.users.split('-')
			ret = [int(each) for each in user_s if each]
			return ret
		except:
			return None	

	def get_owner(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			return int(temp.owner_id)
		except:
			return None

	def update_board(self, room_id, board_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			temp.board_id = board_id
			temp.save()
			return 1
		except:
			return -1

	def get_board(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			return int(temp.board_id)
		except:
			return None	

	def update_status(self, room_id, status):
		try:
			temp = Room.objects.get(room_id = room_id)
			
			if status:
				self.reset_ingame_score(room_id)

			temp.game_status = status
			temp.save()

			return 1
		except:
			return -1

	def get_status(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			return temp.game_status
		except:
			return -1

	def update_drawer(self, room_id, drawer=None):
		try:
			temp = Room.objects.get(room_id = room_id)
			temp.drawer = drawer
			temp.save()
			return 1
		except:
			return -1

	def get_drawer(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			return temp.drawer
		except:
			return -1

	def get_name(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			return temp.name
		except:
			return -1

	def get_number(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			temp_s = temp.users.split('-')
			temp_s = [each for each in temp_s if each]
			return len(temp_s)
		except:
			return -1

	def get_ingame_score(self, room_id, user_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			scores = eval(temp.scores)
			score = scores[str(user_id)]
			return score
		except:
			return -1

	def update_ingame_score(self, room_id, user_id, score):
		try:
			temp = Room.objects.get(room_id = room_id)
			scores = eval(temp.scores)
			scores[str(user_id)] = score
			temp.scores = str(scores)
			temp.save()
			return 1
		except:
			return -1

	def reset_ingame_score(self, room_id):
		try:
			temp = Room.objects.get(room_id = room_id)
			players = self.get_players(room_id)

			scores = {}
			for each in players:
				scores[str(each)] = 0

			temp.scores = str(scores)
			temp.save()
			return 1
		except:
			return -1
		

