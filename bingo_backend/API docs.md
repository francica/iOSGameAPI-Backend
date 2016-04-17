# User & Room services APIs
​
## Two classes in models.py:
		
		class User():
			user_id;
			name;
			score;
		
		class Room():
			room_id;
			owner_id;
			users;
			board_id;
			name;
			status; # waiting or in-game?
			
			#capacity; # room capacity. Fixed for the game or defined by the owner?
		
		//serializers for the two classes are omitted for now.
		
​These classes are made to support db management.
    
## Room APIs

	get_all_rooms()
		# get all rooms in the db
		paras: 
			None
		return: 
			a python list (or a json array) of room objects
	
	get_room(room_id)
		paras:
			room_id
		return:
			a json string of info of a specific room.

	create_room(user_id, room_name)
		# create a new room with userid and name for the room
		paras:
			user_id: room onwer's id
			room_name: name of the room
		return:
			room_id: room_id for the room created.
			
	remove_room(room_id)
		para:
			room_id: targeted room id
		return:
			1 for success, 0 otherwise.
	
	add_player(user_id, room_id)
		paras:
			user_id: room onwer's id
			room_id: room_id of the room	
		return:
			1 for success, 0 otherwise.
			
	remove_player(user_id, room_id)
		paras:
			user_id: user id for the left player
			room_id: room_id of the room	
		return:
			1 for success, 0 otherwise.
	
	get_players(room_id)
		paras: 
			room_id
		return:
			list of user_ids for all users in the room.

	get_owner(room_id)
		paras: 
			room_id
		return:
			user_id of the owner of the room.
			
	update_board(room_id, board_id)
		paras: 
			room_id
			board_id
		return:
			1 for success, 0 otherwise.
			
	get_board(room_id)
		paras: 
			room_id
		return:
			board_id, for the room.
			
	update_status(room_id, status)
		paras: 
			room_id
		return:
			1 for success, 0 otherwise.
			
	get_status(room_id)
		paras: 
			room_id
		return:
			status: status of the room.	
	
	get_name(room_id)
		paras: 
			room_id
		return:
			name: name for the room.
			
	get_number(room_id)
		paras: 
			room_id
		return:
			number of players in the room.
			
## User APIs

	get_users()
		# get all users in the db
		paras: 
			None
		return: 
			a python list (or a json array) of user objects

	get_user(user_id)
		paras:
			user_id
		return:
			a json string of info of a specific user.
	
	add_user(name)
		paras:
			name: non-id string	
		return:
			user_id: new id created in the backend
			
	remove_user(user_id)
		paras:
			user_id: user id for the removed user
		return:
			1 for success, 0 otherwise.

	get_score(user_id)
		paras:
			user_id
		return:
			score of the user
		
	score_update(user_id, score)
		paras: 
			user_id
			score int
		return:
			1 for success, 0 otherwise.
			
	get_name(user_id)
		paras:
			user_id
		return:
			name of the user	

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	
	
	
			