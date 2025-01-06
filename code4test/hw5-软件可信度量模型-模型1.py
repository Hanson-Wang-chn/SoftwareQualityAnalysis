import numpy as np

def calculate_T(y_values, alphas, epsilon=None, rho=None):
    """  
    根据给定的属性值和权重计算 T 值。  

    参数:  
        y_values (np.array): 包含各个属性值的数组。  
        alphas (np.array): 包含对应属性权重的数组。  
        epsilon (float, optional): 控制最小关键属性影响的参数。默认为 None。  
        rho (float, optional): 替代性参数。默认为 None。  

    返回:  
        float: 计算得到的 T 值。  
    """  # 验证数据

    # 计算 T 值
    if epsilon is not None and rho is not None:
        y_min = np.min(y_values[:len(alphas)])
        T = (10 / 11) * ((y_min / 10) ** epsilon) * np.prod(y_values[:len(alphas)] ** alphas) + (10 / 11) * np.prod(
            y_values[len(alphas):] ** alphas)
    else:
        T = np.prod(y_values ** alphas)

    return T


# 定义权重
alphas = np.array([0.25, 0.15, 0.20, 0.23, 0.17])

# 定义属性值矩阵
y_values_matrix = np.array([
    [6.8, 8.2, 7.8, 6.8, 7.9],
    [8.8, 8.9, 9.2, 9.0, 9.3],
    [5.6, 5.9, 6.0, 9.0, 5.3],
    [4.6, 7.8, 3.8, 5.1, 4.5]
])

# 计算每个属性值组合的 T 值
Ts = [calculate_T(y_values, alphas) for y_values in y_values_matrix]

# 输出结果
for i, T in enumerate(Ts, start=1):
    print(f"第{i}组属性值的 T 值为: {T:.4f}")
