n = int(input("类别数："))
theta = list(map(float, input("各个类别的权重：").split()))
m = list(map(int, input("各个类别的度量元数量：").split()))
R = []
BETA = []
for i in range(n):
    beta = list(map(float, input("第{0}个类别-各个度量元的权重：".format(i + 1)).split()))
    r = list(map(float, input("第{0}个类别-各个度量元的该时刻最大风险值：".format(i + 1)).split()))
    BETA.append(beta)
    R.append(r)

import math
Hs = []
Us = []
for i in range(n):
    H = 0
    for j in range(m[i]):
        H += BETA[i][j] * math.log10(R[i][j])
    U = max(10 * math.exp(-H), 1)
    Hs.append(H)
    Us.append(U)

print("各类别的熵：{0}".format(Hs))
print("各类别的可信值：{0}".format(Us))
T = 1
for i in range(n):
    T *= math.pow(Us[i], theta[i])
print("可信值：{0}".format(T))


# 作业，t=10
# 5
# 0.539 0.125 0.238 0.049 0.049 1.000
# 15 4 7 2 2
# 0.0506 0.1845 0.0238 0.0238 0.0774 0.0774 0.0774 0.0238 0.0238 0.0506 0.0506 0.0238 0.0238 0.1042 0.1845
# 4 7 7 4 9 4 7 7 7 4 7 7 7 9 7
# 0.25 0.25 0.25 0.25
# 7 9 7 7
# 0.2340 0.1064 0.1064 0.2340 0.1064 0.1064 0.1064
# 7 10 7 4 7 10 9
# 0.2 0.8
# 7 4
# 0.10 0.90
# 7 7
