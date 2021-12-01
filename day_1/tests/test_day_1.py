import os.path

import day_1.day_1


def test_day_1_part_1():
    input_file = os.path.abspath("./test_input_day_1.txt")
    return_val = day_1.day_1.find_increased_measurements(input_file)

    assert isinstance(return_val, int)
    assert return_val == 7


def test_day_1_part_2():
    input_file = os.path.abspath("./test_input_day_1.txt")
    return_val = day_1.day_1.find_sum_increased_measurements(input_file)

    assert isinstance(return_val, int)
    assert return_val == 5
