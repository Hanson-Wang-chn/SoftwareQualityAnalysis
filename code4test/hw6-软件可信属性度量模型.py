import numpy as np

# 子属性的权重
weights = np.array([0.15, 0.20, 0.20, 0.25, 0.20])

# 参数 ρ_y
rho_y_values = [0.01, 0.55]

# 软件系统数据
software_data = [
    {'编号': '1', 'x1': 8.6, 'x2': 9.1, 'x3': 9.2, 'x4': 8.8, 'x5': 8.9},
    {'编号': '2', 'x1': 6.8, 'x2': 7.9, 'x3': 5.9, 'x4': 6.6, 'x5': 6.1},
    {'编号': '3', 'x1': 9.1, 'x2': 9.9, 'x3': 8.9, 'x4': 8.8, 'x5': 7.8},
    {'编号': '4', 'x1': 3.5, 'x2': 4.2, 'x3': 5.6, 'x4': 4.9, 'x5': 5.2}
]

# 计算 y1
def calculate_y1(system_data):
    values = list(system_data.values())[1:]  # 排除第一个元素（编号）
    return np.prod(np.power(values, weights))

# 计算 y2
def calculate_y2(system_data, rho_y):
    values = list(system_data.values())[1:]
    sum_term = np.sum(weights / np.power(values, rho_y))
    return pow(sum_term, -1/rho_y)

# 输出结果
for software in software_data:
    print(f"Software System {software['编号']}:")
    for rho_y in rho_y_values:
        y1 = calculate_y1(software)
        y2 = calculate_y2(software, rho_y)
        print(f"  Test Group with ρ_y={rho_y}: y1={y1:.4f}, y2={y2:.4f}")
