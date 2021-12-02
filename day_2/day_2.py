import os


def get_final_depth(input_file):
    horizontal_pos = 0
    depth = 0

    with open(input_file) as file:
        lines = file.readlines()
        line_list = [line.rstrip() for line in lines]

    for elem in line_list:
        keyword, key_num = elem.split()
        key_num = int(key_num)
        if keyword == "forward":
            horizontal_pos += key_num
        elif keyword == "down":
            depth += key_num
        elif keyword == "up":
            depth -= key_num

    return horizontal_pos * depth


if __name__ == "__main__":
    my_input_file = os.path.abspath("./input_day_2.txt")

    print(get_final_depth(my_input_file))
