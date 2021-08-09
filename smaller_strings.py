MOD = 10**9 +7

def fast_pow(n,k):
    n = n % MOD
    res = 1
    while k > 0:
        if k % 2:
            res = res * n % MOD
        n *= n % MOD
        k = k // 2
    return res
        

def count(i,n,k,s):
    middle_2 = n //2
    middle_1 = middle_2 + n % 2
    pal_count = 1 if (s[middle_1:] > s[middle_2-1::-1]) else 0
    pal_count += sum(((ord(ss)-97) * fast_pow(k,enum)) %MOD for enum, ss in enumerate(s[middle_1-1::-1]))
    return f"Case #{i}: {pal_count % MOD}"


t = int(input())
for i in range(1, t+1):
    n, k = [int(x) for x in input().split()]
    s = input()
    print(count(i,n,k,s))