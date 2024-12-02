import functools

if __name__ == '__main__':
    left = []
    rigth = []
    with open('./input.txt') as fi:
        for row in fi:
            l, r = row.strip().split('   ')
            left.append(int(l))
            rigth.append(int(r))

    d = []
    while len(left) > 0:
        lm = left.pop(left.index(min(left)))
        rm = rigth.pop(rigth.index(min(rigth)))
        d.append(abs(rm - lm))
        
    print(sum(d))