def get_file_as_str_list(input_file):
    with open(input_file) as file:
        lines = file.readlines()
        line_list = [line.rstrip() for line in lines]
    return line_list


def get_file_for_bingo(input_file):
    board_list = []
    draw_list = []
    with open(input_file) as file:
        lines = file.readlines()
        for idx in range(0, len(lines)):
            if idx == 0:
                draw_list = lines[idx].rstrip().split(",")
            elif not lines[idx].rstrip():
                continue
            else:
                board_list.append([line.rstrip() for line in lines[idx:(idx + 4)]])
                idx += 4
    return draw_list, board_list
