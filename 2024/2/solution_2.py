
if __name__ == '__main__':

    with open('./input.txt') as fi:
        levels = fi.readlines()

    safe_c = 0
    for level in levels:
        level = [int(_) for _ in level.split(' ')]
        for s in range(len(level)+1):
            l = level[:]
            if s > 0:
                l.pop(s-1)
            pairs = zip(l, l[1:])
            if (all((x>y and abs(x-y) <= 3)  for x, y in zip(l, l[1:])) \
                or all((x<y and abs(x-y) <= 3) for x, y in zip(l, l[1:]))) and len(list(zip(l, l[1:]))) > 0:
                    safe_c += 1
                    break
    
    print(safe_c)