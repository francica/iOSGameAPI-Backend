__author__ = 'Robert'


from Board_Segment import Board
import json
from Pen import Pen



class Board_Management:
    def __init__(self):

        self.game_board={}
        self.board_counter=0



    def add_new_game_board(self, pen_color,pen_width,room_id):
        """function is to be used to create a new game board for a new room"""
        self.game_board[room_id]=[]

        new_pen=Pen(pen_color,pen_width)

        new_board=Board(new_pen,self.board_counter,room_id)
        new_board.initialize_new_board()

        self.game_board[room_id].append(new_board)
        self.board_counter+=1



    def update_pen(self,json_obj):
        """ {'pen_color':[r,g,b],'room_id': x,'pen_width': y} """

        json_str=json.loads(json_obj)
        new_pen=Pen(json_str['pen_color'],json_str['pen_width'])
        new_board=Board(new_pen,self.board_counter,json_str['room_id'])

        self.game_board[json_str['room_id']].append(new_board)
        self.board_counter+=1


    def update_board(self,json_obj):
        """{'room_id': x, 'start_point': (x,y), 'end_point': (x,y) """

        json_str=json.loads(json_obj)
        self.game_board[json_str['room_id']][len(self.game_board[json_str['room_id']])-1].update_board_pixel(json_str['start_point'],json_str['end_point'])

    def get_board(self,json_obj):

        """{'room_id': x, 'board_id': y}"""

        json_data={}
        json_str=json.loads(json_obj)

        start_point_list,end_point_list, pen_list,board_id_list=self.find_boards(json_str['room_id'],json_str['board_id'])

        if start_point_list==-1:
            return -1

        else:

            for index in range(0,len(board_id_list)):
                json_data[board_id_list[index]]=(start_point_list[index],end_point_list[index]),pen_list[index].pen_color,pen_list[index].pen_width

            json_str=json.dumps(json_data)

            # returns a string in the format {"board_id":[[[start_point],[end_point]],[pen_color],"pen_width"], ...}
            return json_str



    def find_boards(self,room_id,board_id):
        """helper function that returns all the board information from current board_id to latest board_id"""

        # check to make sure that the board is not already the latest board
        if board_id==self.game_board[room_id][len(self.game_board[room_id])-1].board_id:

            return -1

        board_diff=[]
        start_point_list=[]
        end_point_list=[]
        pen_list=[]
        board_id_list=[]

        for board_index in range(0, len(self.game_board[room_id])):

            # get all the boards from the board_id to the latest board
            if self.game_board[room_id][board_index].board_id==board_id:
                board_diff=self.game_board[room_id][board_index+1:]


        if len(board_diff)!=0:

            for board in board_diff:

                # the first index will be the start point and the second index will be the end point
                start_point_list.append(board.pixel_changed[0])
                end_point_list.append(board.pixel_changed[1])

                pen_list.append(board.pen)
                board_id_list.append(board.board_id)


            return start_point_list,end_point_list,pen_list,board_id_list

        # no boards to return error check
        else:
            return -1













