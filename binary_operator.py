from sys import stdin


def parse(seed, data):
    left_par = data[0]
    if not left_par == '(':
        ret, __, _ =  parse_number(data)
        return ret, []
    new_data = data[1:]
    if new_data[0] == left_par:
        a, newer_data = parse(seed, new_data)
        op = newer_data[0]
        newer_data = newer_data[1:]
    else:
        a, op, newer_data = parse_number(new_data)
    if newer_data[0] == left_par:
        b, newer_data = parse(seed, newer_data)
        newer_data = newer_data[1:]
    else:
        b, _, newer_data = parse_number(newer_data)
    ret = operate(op,a,b,seed)
    return ret, newer_data


def parse_number(data):
    idx = 0
    number = ''
    while True:
        try:
            number += str(int(data[idx]))
            idx += 1
        except (ValueError, IndexError):
            break
    number = int(number)
    return number, data[idx], data[idx+1:]


def operate(op, a, b, seed):
    if op == '*':
        f = multiply
    elif op == '+':
        f = add
    elif op == '#':
        f = third
    else:
        raise ValueError 
    return f(a,b,seed)


def multiply(a, b, seed):
    return int(a) * int(b)


def add(a, b, seed):
    return int(a) + int(b)


def third(a, b, seed):
    return hash((int(a), seed, int(b)))


if __name__ == '__main__':
        num_test_cases = int(stdin.readline())
        for idx in range(1, num_test_cases+1):
            num_expressions = int(stdin.readline())
            kdx_list = []
            ret_dict = {}
            kdx = 0
            for jdx in range(1, num_expressions+1):
                data = stdin.readline()
                rets = []
                for seed in range(10):
                    ret, _ = parse(seed, data)
                    rets.append(ret)
                rets = tuple(rets)
                if rets not in ret_dict:
                    kdx += 1
                    temp = kdx
                    ret_dict[rets] = kdx
                else:
                    temp = ret_dict[rets]
                kdx_list.append(str(temp))
            print(f'Case #{str(idx)}: {" ".join(kdx_list)}')
