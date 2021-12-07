import os
import day_3.day_3
import helper

input_file = os.path.abspath("./test_input_day_3.txt")
input_list = helper.get_file_as_str_list(input_file)


def test_day_3_part_1():

    test_power = day_3.day_3.get_power_consumption(input_file)

    assert isinstance(test_power, int)
    assert test_power == 198


def test_day_3_part_2_oxygen():

    test_oxygen = day_3.day_3.get_oxygen_rating(input_list.copy())

    assert isinstance(test_oxygen, int)
    assert test_oxygen == 23


def test_day_3_part_2_co2():

    test_co2 = day_3.day_3.get_co2_rating(input_list.copy())

    assert isinstance(test_co2, int)
    assert test_co2 == 10
