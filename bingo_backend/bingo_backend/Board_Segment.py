__author__ = 'Robert'
class Board:

    def __init__(self,pen,board_id,room_id):

        self.pixel_changed=None
        self.pen=pen
        self.room_id=room_id
        self.board_id=board_id


    def initialize_new_board(self):

        self.pixel_changed=()



    def update_board_pixel(self,start_point,end_point):

        self.pixel_changed=(start_point,end_point)










