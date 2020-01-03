def load_text_file(file_name):
    with open(file_name, "r") as f:
        boolean_world = [[item == "True" for item in row.split(',')]
                         for row in f.read().split("\n")]
    return boolean_world


def save_text_file(file_name, data):
    with open(file_name, "w") as f:
        f.write("\n".join(
            [",".join([str(item) for item in row]) for row in data]))
