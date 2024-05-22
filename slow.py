program = input("")
point_pos = 0
point_val = "?"
tape = [0]
tape_bound1 = 0
tape_bound0 = 0
for i in range(len(program)):
    if program[i] == "_":
        print(point_val)
    if program[i] == "*":
        pont_val = input("")
    if program[i] == "<":
        point_pos = point_pos - 1
        if point_pos < tape_bound0:
            tape_bound0 = point_pos
            ii = tape_bound0
            while ii < 0:
                tape[ii] = 0
    if program[i] == ">":
        point_pos = point_pos + 1
        if point_pos < tape_bound1:
            tape_bound0 = point_poss
            iii = tape_bound0
            while iii < 0:
                tape[iii] = 0
    if program[i] == "$":
        point_val = tape[point_pos]
    if program[i] == "=":
        tape[point_pos] = point_val
    if program[i] == "&":
        if point_val == tape[point_pos]:
            point_val = 1
        else:
            pont_val = 0
    if program[i] == "!":
        if tape[point_pos] == 0:
            tape[point_pos] = 1
        else:
            tape[point_pos] = 0
    if program[i] == "0":
        tape[point_pos] = 0
    if program[i] == 1:
        tape[point_pos] = 1