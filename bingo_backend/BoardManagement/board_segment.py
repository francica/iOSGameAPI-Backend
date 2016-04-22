__author__ = 'Robert'
class BoardSegment:

    def __init__(self,pen,board_id,room_id):

        self.pixels_changed=None
        self.pen=pen
        self.room_id=room_id
        self.board_id=board_id


    def initialize_new_board(self):

        self.pixels_changed=()



    def update_board_pixel(self,start_point,end_point):

        self.pixels_changed=(start_point,end_point)










