def get_file_as_str_list(input_file):
    with open(input_file) as file:
        lines = file.readlines()
        line_list = [line.rstrip() for line in lines]
    return line_list
