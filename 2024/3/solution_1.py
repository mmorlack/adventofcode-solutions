import re

if __name__ == '__main__':
    with open('./input.txt') as fi:
        s = fi.read().strip()

    ops = re.findall(
        r'(mul\(\d+\,\d+\))',
        s
    )
    muls = []
    for op in ops:
        numbers = [int(_) for _ in re.findall(r'(\d+)\,(\d+)', op)[0]]
        mul = numbers[0] * numbers[1]
        muls.append(mul)
    print(sum(muls))