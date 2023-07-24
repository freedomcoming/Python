# 拆解Python字节码

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')

import dis
res = dis.dis(countdown)

print(res)