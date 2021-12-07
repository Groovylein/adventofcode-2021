import os
import day_3.day_3


def test_day_3_part_1():
    input_file = os.path.abspath("./test_input_day_3.txt")

    test_power = day_3.day_3.get_power_consumption(input_file)

    assert isinstance(test_power, int)
    assert test_power == 198
