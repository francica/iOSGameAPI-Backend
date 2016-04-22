from unittest import TestCase

__author__ = 'Robert'
from board_management import BoardManagement
import json

class TestBoardManagement(TestCase):

  def test_add_new_game_board(self):

    bm=BoardManagement()
    bm.add_new_game_board(None, None,1)
    self.assertEqual(None,bm.game_board[1].board_segment_list[0].pen.pen_color)
    self.assertEqual(1,bm.game_board[1].board_id)

  def test_update_pen(self):

    bm=BoardManagement()
    bm.add_new_game_board(None,None,1)

    data={}
    data['pen_color']=(128,256,120)
    data['pen_width']=.25
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_pen(json_data)
    self.assertEqual(.25,bm.game_board[1].board_segment_list[1].pen.pen_width)
    self.assertEqual(2,bm.game_board[1].board_id)

  def test_update_board(self):

    bm=BoardManagement()
    bm.add_new_game_board(None,None,1)

    data={}
    data['pen_color']=(128,256,120)
    data['pen_width']=.25
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_pen(json_data)

    data['start_point']=(2,2)
    data['end_point']=(4,3)
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_board(json_data)

    self.assertEqual(data['start_point'][0],bm.game_board[1].board_segment_list[1].pixels_changed[0][0])



  def test_get_board(self):
    bm=BoardManagement()

    bm.add_new_game_board((255,255,255),.5,1)

    data={}
    data['pen_color']=(128,256,120)
    data['pen_width']=.25
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_pen(json_data)


    data['start_point']=(2,2)
    data['end_point']=(4,3)
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_board(json_data)

    # making a second board

    data['pen_color']=(54,3,4)
    data['pen_width']=.2
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_pen(json_data)

    data['start_point']=(3,9)
    data['end_point']=(43,23)
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_board(json_data)

    # making a third board

    data['pen_color']=(2,29,4)
    data['pen_width']=.8
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_pen(json_data)

    data['start_point']=(12,9)
    data['end_point']=(45,231)
    data['room_id']=1

    json_data=json.dumps(data)
    bm.update_board(json_data)

    # making get_board json obj

    data['room_id']=1
    data['board_id']=1
    json_data=json.dumps(data)

    json_str=bm.get_board(json_data)
    print(json_str)



