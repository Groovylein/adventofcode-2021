import os


def find_increased_measurements(input_file):
    inc_count = 0

    with open(input_file) as file:
        lines = file.readlines()
        line_list = [int(line.rstrip()) for line in lines]

    prev_elem = None
    for elem in line_list:
        if prev_elem is not None:
            if elem > prev_elem:
                print("PREV_ELEM: ", prev_elem, "| ELEM: ", elem, "| increase")
                inc_count += 1
            else:
                print("PREV_ELEM: ", prev_elem, "| ELEM: ", elem, "| decrease")

        prev_elem = elem

    return inc_count


# HERE the real calls for the Day

if __name__ == "__main__":
    my_input_file = os.path.abspath("./input_day_1.txt")
    print(find_increased_measurements(my_input_file))
