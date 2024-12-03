import re

if __name__ == '__main__':
    with open('./input.txt') as fi:
        s = fi.read().strip()

    ops = re.finditer(r'(do\(\)|don\'t\(\))',s)
    commands = []
    for op in ops:
        commands.append([op.start(), op.group()])

    muls = []
    ops_mul = re.finditer(
            r'(mul\(\d+\,\d+\))',
            s
        )
    for op in ops_mul:
       muls.append([op.start(), op.group()])

    muls_ok = []
    for pos, mul in muls:
        if pos < commands[0][0]:
            muls_ok.append(mul)
            continue
        for f, s in zip(commands, commands[1:]):
            if pos > f[0] and pos < s[0] and f[1] == 'do()':
                muls_ok.append(mul)

    muls_s = []
    for op in muls_ok:
        numbers = [int(_) for _ in re.findall(r'(\d+)\,(\d+)', op)[0]]
        mul = numbers[0] * numbers[1]
        muls_s.append(mul)
    print(sum(muls_s))