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
    # print(gamma)
    # print(epsilon)
    return int(gamma, 2) * int(epsilon, 2)


def get_oxygen_rating(list_of_diagnostics):
    data_len = len(list_of_diagnostics[0])

    for i in range(0, data_len):
        # true_count count '0'
        true_count = 0
        # false_count count '1'
        false_count = 0
        for line in list_of_diagnostics:
            if int(line[i]) == 0:
                true_count += 1
            else:
                false_count += 1
        for line in list_of_diagnostics:
            if true_count > false_count:
                if int(line[i]) == 1:
                    list_of_diagnostics = [x for x in list_of_diagnostics if x != line]
            else:
                if int(line[i]) == 0:
                    list_of_diagnostics = [x for x in list_of_diagnostics if x != line]
        if len(list_of_diagnostics) == 1:
            break

    return int(list_of_diagnostics[0], 2)


def get_co2_rating(list_of_diagnostics):
    data_len = len(list_of_diagnostics[0])

    for i in range(0, data_len):
        # true_count count '0'
        true_count = 0
        # false_count count '1'
        false_count = 0
        for line in list_of_diagnostics:
            if int(line[i]) == 0:
                true_count += 1
            else:
                false_count += 1

        for line in list_of_diagnostics:
            if true_count > false_count:
                if int(line[i]) == 0:
                    list_of_diagnostics = [x for x in list_of_diagnostics if x != line]
            else:
                if int(line[i]) == 1:
                    list_of_diagnostics = [x for x in list_of_diagnostics if x != line]
        if len(list_of_diagnostics) == 1:
            break

    return int(list_of_diagnostics[0], 2)


def get_life_support_rate(input_file):
    file_list = helper.get_file_as_str_list(input_file)

    oxygen = get_oxygen_rating(file_list.copy())
    co2 = get_co2_rating(file_list.copy())

    return oxygen * co2


if __name__ == "__main__":
    my_input_file = os.path.abspath("./input_day_3.txt")

    print(get_power_consumption(my_input_file))
    print(get_life_support_rate(my_input_file))
