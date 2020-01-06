def display_life_cycles(life_cycles):
    print(f'Life Cycles: {life_cycles}')


def display_world(world_array):
    living_cells = 0
    display = [[]]
    for row in world_array:
        display_row = []
        for cell in row:
            if cell['alive']:
                living_cells += 1
                display_row.append("*")
            else:
                display_row.append(" ")
        display.append(display_row)

    joined_rows = [(" ".join(row)) for row in display]
    output = "\n".join(joined_rows)
    return output, living_cells


def display_number_living(living_cells):
    print(f'number of living cells: {living_cells}')
    print(f'living cells graphed: {"|" * (living_cells // 10)}')


def newlined_print(output):
    print()
    print(output)

def display(world_array, life_cycles):
    output, living_cells = display_world()
    print(output)
    display_number_living(living_cells)
    display_life_cycles(life_cycles)
