import os
import helper


class Board:
    def __init__(self, board_as_list):
        self.board_as_list = board_as_list.copy()
        self.board_as_dict = self.transform_into_dict(self.board_as_list)

    @staticmethod
    def transform_into_dict(list_to_transform):
        board_as_dict = {0: None,
                         1: None,
                         2: None,
                         3: None}
        idx = 0
        for line in list_to_transform:
            tmp_line_list = line.split()
            board_as_dict[idx] = dict.fromkeys(tmp_line_list, 0)
            idx += 1
        return board_as_dict


if __name__ == "__main__":
    my_input_file = os.path.abspath("./input_day_4.txt")

    draw_list, board_list = helper.get_file_for_bingo(my_input_file)
    # print("draw:", draw_list)
    # print("board:", board_list)
    boards = []
    for board in board_list:
        boards.append(Board(board))
    print(boards[0].board_as_dict)
