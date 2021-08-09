from sys import stdin


class TestCase:

    def __init__(self, idx, *args):
        self.idx = idx
        self.G = args[0]
        self.result = None

    def get_result(self):
        count = 0
        i = 1
        r = self.G / float(i)
        while r - (i - (i-1)*0.5) + 1 > 0:
            if i % 2:
                count += int(r % 1.0 == 0.0)
            else:
                count += int((r / 0.5) % 2.0 == 1.0)
            i += 1
            r = self.G / float(i)
        self.result = count

    def print_result(self):
        self.get_result()
        print(f'Case #{self.idx}: {self.result}')


if __name__ == '__main__':
    num_test_cases = int(stdin.readline())
    for idx in range(1, num_test_cases+1):
        parameters = [int(x) for x in stdin.readline().split()]
        ts = TestCase(idx, *parameters)
        ts.print_result()

