with open("input.txt") as f:
    curr_calories = 0
    calories = []

    for line in f:
        if line == "\n":
            calories.append(curr_calories)
            curr_calories = 0

        else:
            curr_calories += int(line.strip("\n"))

    calories.sort()

    print("Part 1:", calories[-1])  # max calories

    print("Part 2:", calories[-1] + calories[-2] + calories[-3]) # top 3
