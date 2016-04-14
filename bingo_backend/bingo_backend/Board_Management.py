__author__ = 'Robert'


# need to understand what sort of access management is going to have
# timestamp

from Board import Board
import json
from datetime import datetime
from more_itertools import unique_everseen


class Board_Management:
    def __init__(self, room_id):

        self.game_board={}
        self.game_board[room_id]=[]


    def add_new_game_board(self, pen_color,pen_width,res_width,res_height, time_stamp,room_id):
        """function is to be used to create a new game board for a new room"""

        new_board=Board(pen_color,pen_width,time_stamp,room_id)
        new_board.initialize_new_board(res_width,res_height)
        self.game_board[room_id].append(new_board)



    def update_pen(self,json_obj):
        """{'pen_color':[r,g,b],'room_id': x,'pen_width':y, 'time_stamp':'%Y-%m-%d %H:%M:%S.%f'}"""

        json_str=json.loads(json_obj)
        new_board=Board(json_str['pen_color'],json_str['pen_width'],json_str['time_stamp'],json_str['room_id'])
        self.game_board[json_str['room_id']].append(new_board)


    def update_board(self,json_obj):

        json_str=json.loads(json_obj)
        self.game_board[json_str['room_id']][len(self.game_board[json_str['room_id']])-1].update_board_pixel(json_str['start_point'],json_str['end_point'])

    def get_board(self,json_obj):

        json_str=json.loads(json_obj)
        pixel_changed=self.find_boards(json_str['room_id'],json_str['time_stamp'])
        return pixel_changed


    def find_boards(self,room_id,time_stamp):

        dt_timestamp=datetime.strptime(time_stamp,'%Y-%m-%d %H:%M:%S.%f')

        pixels_changed=[]
        filter_pixel_changed=[]
        flag=False

        for board in self.game_board[room_id]:
            dt_board_id=datetime.strptime(board.board_id,'%Y-%m-%d %H:%M:%S.%f')

            if dt_board_id>dt_timestamp:
                for pixel in board.pixel_changed:
                    pixels_changed.append(pixel)

        pixels_changed.reverse()

        for pixel in pixels_changed:
            for filter_pixel in filter_pixel_changed:
                if pixel.point == filter_pixel.point:
                    flag=True
                    continue

            if flag!=True:
                filter_pixel_changed.append(pixel)
            else:
                flag=False

        return filter_pixel_changed






