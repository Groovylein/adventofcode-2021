import os
import helper


def get_power_consumption(input_file):
    file_list = helper.get_file_as_str_list(input_file)

    data_len = len(file_list[0])
    gamma = ""
    epsilon = ""
    for i in range(0, data_len):
        # true_count count '0'
        true_count = 0
        # false_count count '1'
        false_count = 0
        for line in file_list:
            if int(line[i]) == 0:
                true_count += 1
            else:
                false_count += 1
        if true_count >= false_count:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print(gamma)
    print(epsilon)
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    my_input_file = os.path.abspath("./input_day_3.txt")

    print(get_power_consumption(my_input_file))
