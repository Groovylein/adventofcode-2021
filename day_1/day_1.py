import os
import tempfile


def find_increased_measurements(input_file):
    print(input_file)
    inc_count = 0

    with open(input_file, 'r') as f:
        print(f.read())

    with open(input_file) as file:
        lines = file.readlines()
        line_list = [int(line.rstrip()) for line in lines]

    print(line_list)
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


def find_sum_increased_measurements(input_file):
    sum_list = []
    solution = 0
    with open(input_file) as file:
        lines = file.readlines()
        line_list = [int(line.rstrip()) for line in lines]

    prev_elem = None
    elem_index = 0
    for elem in line_list:
        try:
            next_elem = line_list[elem_index + 1]
        except:
            break
        if prev_elem is not None:
            tmp_sum = prev_elem + elem + next_elem
            sum_list.append(tmp_sum)
        prev_elem = elem
        elem_index += 1

    prev_elem = None
    for elem in sum_list:
        if prev_elem is not None:
            if elem > prev_elem:
                print("PREV_ELEM: ", prev_elem, "| ELEM: ", elem, "| increase")
                solution += 1
            else:
                print("PREV_ELEM: ", prev_elem, "| ELEM: ", elem, "| decrease")

        prev_elem = elem

    return solution


# HERE the real calls for the Day

if __name__ == "__main__":
    my_input_file = os.path.abspath("./input_day_1.txt")
    print(find_increased_measurements(my_input_file))

    print(find_sum_increased_measurements(my_input_file))
