import os
import helper


if __name__ == "__main__":
    my_input_file = os.path.abspath("./input_day_4.txt")

    draw_list, board_list = helper.get_file_for_bingo(my_input_file)
    # print("draw:", draw_list)
    # print("board:", board_list)
