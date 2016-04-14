__author__ = 'Robert'

from Board import Board as board
from Board_Management import Board_Management
import json
from datetime import datetime


def main():

    bm=Board_Management(1)

    bm.add_new_game_board((255,255,255),.5,120,520,datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),1)


    data={}
    data['pen_color']=(128,256,120)
    data['pen_width']=.25
    data['room_id']=1
    data['time_stamp']=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    json_data=json.dumps(data)
    bm.update_pen(json_data)

    print(bm.game_board[1][1].pen_color)
    print(bm.game_board[1][0].board_id)
    print(bm.game_board[1][1].board_id)

    data_update_board={}
    data_update_board['start_point']=(1,1)
    data_update_board['end_point']=(4,3)
    data_update_board['room_id']=1

    json_update_board=json.dumps(data_update_board)
    bm.update_board(json_update_board)


    print(bm.game_board[1][1].pixel_changed[1].rgb)
    for pixel in bm.game_board[1][1].pixel_changed:
        print(pixel.point)


    data['pen_color']=(50,506,120)
    data['pen_width']=.25
    data['room_id']=1
    data['time_stamp']=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    json_data=json.dumps(data)
    bm.update_pen(json_data)

    data_update_board['start_point']=(4,3)
    data_update_board['end_point']=(1,1)
    data_update_board['room_id']=1

    json_update_board=json.dumps(data_update_board)
    bm.update_board(json_update_board)

    data_get_board={}
    data_get_board['room_id']=1
    data_get_board['time_stamp']=bm.game_board[1][0].board_id


    json_get_board=json.dumps(data_get_board)
    pixels_changed=bm.get_board(json_get_board)
    print("pixels that have been changed")
    for pixel in pixels_changed:

        print(pixel.point)
        print(pixel.rgb)









if __name__ == "__main__":
    main()