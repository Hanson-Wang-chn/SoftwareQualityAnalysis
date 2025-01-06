def calculate_T3(y1, y2, y3, y4, y5, y6, y7, epsilon, rho):
    # 关键属性权重
    alpha1, alpha2, alpha3, alpha4 = 0.3, 0.2, 0.35, 0.15
    # 非关键属性权重
    beta1, beta2, beta3 = 0.35, 0.40, 0.25
    # 计算最小关键属性的加权值
    min_y = min(y1, y2, y3, y4)
    weighted_min_y = (min_y / 10) ** epsilon * y1 ** alpha1 * y2 ** alpha2 * y3 ** alpha3 * y4 ** alpha4
    # 计算非关键属性的加权值
    non_critical_weighted = y5 ** beta1 * y6 ** beta2 * y7 ** beta3
    # 计算T3
    T3 = (alpha * weighted_min_y ** (-rho) + beta * non_critical_weighted ** (-rho)) ** (-1 / rho)
    return T3


# 定义常量
alpha, beta = 0.70, 0.30

# 数据集
data = [
    [8.3, 7.1, 8.1, 6.9, 9.1, 8.5, 8.6, 0.1, 0.10],
    [7.8, 8.7, 8.0, 6.2, 8.9, 8.0, 8.8, 0.05, 0.15],
    [5.8, 8.1, 6.8, 5.6, 7.9, 6.8, 8.1, 0.1, 0.10],
    [6.8, 7.8, 8.1, 6.9, 8.9, 7.8, 8.8, 0.05, 0.15],
    [3.8, 3.7, 4.8, 4.7, 3.9, 5.8, 6.8, 0.1, 0.10],
    [8.4, 7.2, 8.1, 7.7, 7.9, 8.8, 6.8, 0.05, 0.15],
    [9.0, 8.7, 8.9, 8.6, 9.1, 8.8, 8.9, 0.1, 0.10],
    [8.0, 7.8, 6.8, 8.7, 7.9, 8.1, 8.3, 0.05, 0.15]
]

# 计算每个软件的T3值
for i, d in enumerate(data, start=1):
    T3_value = calculate_T3(*d[:7], d[7], d[8])
    print(f"Software {i} T3: {T3_value:.4f}")
