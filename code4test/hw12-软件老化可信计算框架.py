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

formatted_Hs = [f"{x:.5f}" for x in Hs]
print("各类别的熵：", formatted_Hs)

formatted_Us = [f"{x:.5f}" for x in Us]
print("各类别的可信值：", formatted_Us)

T = 1
for i in range(n):
    T *= math.pow(Us[i], theta[i])
print("可信值：{0:.3f}".format(T))

