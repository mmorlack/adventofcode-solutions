
if __name__ == '__main__':

    with open('./input.txt') as fi:
        levels = fi.readlines()

    safe_c = 0
    for level in levels:
        level = [int(_) for _ in level.split(' ')]
        if all((x>y and abs(x-y) <= 3)  for x, y in zip(level, level[1:])) \
            or all((x<y and abs(x-y) <= 3) for x, y in zip(level, level[1:])):
                safe_c += 1
    
    print(safe_c)