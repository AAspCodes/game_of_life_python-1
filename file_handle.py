def load_text_file(file_name):
    with open(file_name, "r") as f:
        data = f.read().split('\n')
        life_cycles = int(data[0])
        world_data = data[1:]
        boolean_world = [[item == "1" for item in list(row)]
                         for row in world_data]
    return life_cycles, boolean_world


def save_text_file(file_name, data, life_cycles):
    with open(file_name, "w") as f:
        f.write(f"{life_cycles}\n" + "\n".join(
            ["".join(['1' if cell_alive else '0'
             for cell_alive in row]) for row in data]))
