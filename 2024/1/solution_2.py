
if __name__ == '__main__':
    left = []
    rigth = []
    with open('./input.txt') as fi:
        for row in fi:
            l, r = row.strip().split('   ')
            left.append(int(l))
            rigth.append(int(r))

    c = []
    for l in left:

        c.append(rigth.count(l)*l)
        
    print(sum(c))