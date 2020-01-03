def load_text_file(file_name):
    with open(file_name, "r") as f:
        data = f.read().split('\n')
        life_cycles = int(data[0])
        world_data = data[1:]
        boolean_world = [[item == "True" for item in row.split(',')]
                         for row in world_data]
    return life_cycles, boolean_world


def save_text_file(file_name, data, life_cycles):
    with open(file_name, "w") as f:
        f.write(f"{life_cycles}\n" + "\n".join(
            [",".join([str(item) for item in row]) for row in data]))
