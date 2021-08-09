from sys import stdin
import itertools


ROCK = 'R'
PAPER = 'P'
SCISSOR = 'S'
AV_CHOICES = [ROCK, PAPER, SCISSOR]
NUM_ROUNDS = 60


class TestCase:
    
    def __init__(self, idx, *args):
        self.idx = idx
        self.W = args[0]
        self.E = args[1]
        self._score = {}
        self._score[(1,0,0)] = 1/3 * (self.W + self.E)
        self._score[(0,1,0)] = 1/3 * (self.W + self.E)
        self._score[(0,0,1)] = 1/3 * (self.W + self.E)
        self.choices = {}
        self.choices[(1,0,0)] = ROCK
        self.choices[(0,1,0)] = PAPER
        self.choices[(0,0,1)] = SCISSOR

    def partitions(self):
        parts = itertools.combinations_with_replacement(range(61),3)
        for p in parts:
            if sum(p) == 60:
                yield p

    def print_result(self):
        agg, result = self.func()
        print(f'Case #{self.idx}: {result}')
        return agg


    def get_score(self,r,p,s):
        score = self._score.get((r,p,s)) 
        if not score: 
            return self.rec_func(r,p,s)
        return score

    def rec_func(self, r, p, s):
        if (r,p,s) in [(0,0,1),(0,1,0),(1,0,0)]: 
            return self.get_score(r,p,s)
        else:
            r_max = 0
            p_max = 0
            s_max = 0
            if r > 0:
                r_max = self.get_score(r-1,p,s) + self.W * p/(r-1+p+s) + self.E * s/(r-1+p+s)
            if p > 0:
                p_max = self.get_score(r,p-1,s) + self.W * s/(r+p-1+s) + self.E * r/(r+p-1+s)
            if s > 0:
                s_max = self.get_score(r,p,s-1) + self.W * r/(r+p+s-1) + self.E * p/(r+p+s-1)
            max_ = max(r_max, p_max, s_max)
            self._score[(r,p,s)] = max_
            if max_ == r_max:
                self.choices[(r,p,s)] = self.choices[(r-1,p,s)] + ROCK
            elif max_ == p_max:
                self.choices[(r,p,s)] = self.choices[(r,p-1,s)] + PAPER
            elif max_ == s_max:
                self.choices[(r,p,s)] = self.choices[(r,p,s-1)] + SCISSOR
            return max_

    def func(self):
        max_ = 0
        for r,p,s in self.partitions():
            ret = self.rec_func(r,p,s)
            if ret > max_:
                max_ = ret
                chosen = (r,p,s)
        choices = self.choices[chosen]
        return max_, choices


if __name__ == '__main__':
    num_days = int(stdin.readline())
    target_agg = int(stdin.readline())
    agg = 0
    total = target_agg * num_days
    for idx in range(1, num_days+1):
        parameters = [int(x) for x in stdin.readline().split()]
        if agg >= total:
            print(f'Case #{idx}: {ROCK*NUM_ROUNDS}')
        else:
            ts = TestCase(idx, *parameters)
            agg += ts.print_result()
