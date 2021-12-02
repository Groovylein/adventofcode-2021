import os
import day_2.day_2


def test_day_2():
    input_file = os.path.abspath("./test_input_day_2.txt")
    return_val = day_2.day_2.get_final_depth(input_file)

    assert isinstance(return_val, int)
    assert return_val == 150
