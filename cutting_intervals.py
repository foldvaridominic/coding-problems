from sys import stdin
from collections import defaultdict


class TestCase:

    def __init__(self, idx, *args):
        self.idx = idx
        self.n = args[0]
        self.c = args[1]
        self.cuts = defaultdict(int)
        self.intervals = []

    def add_interval(self, l, r):
        if not self.intervals:
            self.intervals = [(l,r,1)]
            return
        intervals = []
        l1 = l
        r1 = r
        multi1 = 1
        for idx, (l2, r2, multi2) in enumerate(self.intervals):
            min_l = min(l1,l2)
            max_l = max(l1,l2)
            min_r = min(r1,r2)
            max_r = max(r1,r2)
            if max_l > min_r:
                if l2 > r1:
                    intervals.append((l1, r1, multi1))
                    intervals.append((l2,r2,multi2))
                    break
                else: # if l1 > r2
                    intervals.append((l2,r2,multi2))
                    if not self.intervals[idx+1:]:
                        intervals.append((l1, r1, multi1))
                        break
                    continue
            if max_l - 1 >= min_l:
                intervals.append((min_l, max_l-1, multi2))
            intervals.append((max_l, min_r, multi1 + multi2))
            if max_r >= min_r+ 1:
                l1 = min_r+1
                r1 = max_r
                if max_r == r2:
                    multi1 = multi2
                #elif max_r == multi1 --> multi1 = multi1
                if not self.intervals[idx+1:]:
                    intervals.append((l1, r1, multi1))
                    # break
            else:
                break
        self.intervals = intervals + self.intervals[idx+1:]
        #print(self.intervals)

    def calculate_cuts(self):
        for idx, (l, r, multi) in enumerate(self.intervals):
            self.cuts[multi] += r-l+1
        #print(self.cuts)

    def get_result(self):
        self.calculate_cuts()
        intervals = 0
        available_cuts = self.c
        cuts = list(sorted(self.cuts.items(), key=lambda x: -x[0]))
        for multiplier, num_cuts in cuts:
            temp = available_cuts - num_cuts
            if temp <= 0:
                intervals += available_cuts * multiplier
                break
            intervals += num_cuts * multiplier
            available_cuts = temp
        self.result = intervals + self.n

    def print_result(self):
        self.get_result()
        print(f'Case #{self.idx}: {self.result}')


if __name__ == '__main__':
    num_test_cases = int(stdin.readline())
    for idx in range(1, num_test_cases+1):
        n, c = [int(x) for x in stdin.readline().split()]
        #add = n
        #if n>4 and n<10:
        #    print(idx)
        #    print((n,c))
        ts = TestCase(idx, n, c)
        for xx in range(n):
            l, r = [int(x) for x in stdin.readline().split()]
            if l+1 > r-1: 
                continue
            #add += (r-1)-(l+1) + 1
            ts.add_interval(l+1,r-1)
            #print(add)
        ts.print_result()
