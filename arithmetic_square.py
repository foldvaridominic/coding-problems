from sys import stdin
from collections import defaultdict


class TestCase:

    def __init__(self, idx, *args):
        self.idx = idx
        self.pairs1 = args[0]
        self.pairs2 = args[1]
        self.result = 0

    def get_result(self):
        self.parse_pairs1()
        self.parse_pairs2()

    def parse_pairs1(self):
        for pair in self.pairs1:
            check = pair[2]
            pair = (pair[0], pair[1])
            diff = max(pair) - min(pair)
            if diff % 2:
                continue
            diff /= 2
            self.result += int((diff + min(pair)) == check)

    def parse_pairs2(self):
        max_count = defaultdict(int)
        for pair in self.pairs2:
            diff = max(pair) - min(pair)
            if diff % 2:
                continue
            diff /= 2
            key = min(pair) + diff 
            max_count[key] += 1
        values = max_count.values() or [0]
        self.result += max(values)

    def print_result(self):
        self.get_result()
        print(f'Case #{self.idx}: {self.result}')


if __name__ == '__main__':
    num_test_cases = int(stdin.readline())
    for idx in range(1, num_test_cases+1):
        rows = []
        rows.append([int(x) for x in stdin.readline().split()])
        rows.append([int(x) for x in stdin.readline().split()])
        rows.append([int(x) for x in stdin.readline().split()])
        pairs1 = [(rows[0][0], rows[0][2], rows[0][1]), (rows[0][0], rows[2][0], rows[1][0])]
        pairs1 += [(rows[2][0], rows[2][2], rows[2][1]), (rows[0][2], rows[2][2],rows[1][1])]
        pairs2 = [(rows[0][0], rows[2][2]), (rows[2][0], rows[0][2])]
        pairs2 += [(rows[0][1], rows[2][1]), (rows[1][0], rows[1][1])]
        ts = TestCase(idx, pairs1, pairs2)
        ts.print_result()
