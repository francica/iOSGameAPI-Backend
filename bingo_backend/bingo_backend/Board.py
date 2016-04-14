__author__ = 'Robert'
from Pixel import Pixel as pixel
class Board:

    def __init__(self,pen_color,pen_width,time_stamp,room_id):
        self.id_counter=0

        self.pixel_changed=[]
        self.pen_color=pen_color
        self.pen_width=pen_width
        self.room_id=room_id
        self.board_id=time_stamp


    def initialize_new_board(self,width_res,height_res):

        for x_coord in range(width_res):
            for y_coord in range(height_res):
                new_pix=pixel(x_coord,y_coord,self.pen_color)
                self.pixel_changed.append(new_pix)
                self.id_counter+=1


    # should the pixels changed in inclusive or exclusive?
    def update_board_pixel(self,start_point,end_point):

        x_axis_val=start_point[0]
        slope=self.find_slope(start_point,end_point)

        if start_point[0]<end_point[0]:

            while x_axis_val<=end_point[0]:

                new_pixel=self.make_new_pixel(slope,end_point,x_axis_val)
                self.pixel_changed.append(new_pixel)

                x_axis_val+=1
        else:

            while x_axis_val>=end_point[0]:

                new_pixel=self.make_new_pixel(slope,end_point,x_axis_val)
                self.pixel_changed.append(new_pixel)
                x_axis_val-=1





    def make_new_pixel(self,slope,point,x_axis_val):

        y_val=slope*(x_axis_val-point[0])+point[1]
        y_val_rounded=int(round(y_val))

        new_pixel=pixel(x_axis_val,y_val_rounded,self.pen_color)

        return new_pixel


    def find_slope(self,start_point,end_point):

        slope=(end_point[1]-start_point[1])/(end_point[0]-start_point[0])


        return slope








