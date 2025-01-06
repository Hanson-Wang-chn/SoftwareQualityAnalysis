import numpy as np


# 定义正互反判断矩阵A
A = np.array([
    [1, 1/2, 3, 2, 1/2],
    [2, 1 , 2 , 3, 2],
    [1 / 3, 1/ 2, 1, 2, 1/3],
    [1 / 2, 1/3, 1/2, 1, 2],
    [2, 1/2, 3, 1 / 2, 1]
])

n = len(A)

# EV方法
def ev_method(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    max_eigenvalue_index = np.argmax(eigenvalues.real)
    principal_eigenvector = eigenvectors[:, max_eigenvalue_index].real
    normalized_weights = principal_eigenvector / np.sum(principal_eigenvector)
    return normalized_weights

# LLSM方法
def lls_method(A):
    n = len(A)
    product_list = []
    for i in range(n):
        product = 1
        for j in range(n):
            if A[i][j] == 0:
                raise ValueError("Matrix element is zero.")
            product *= A[i][j]
        product_list.append(product**(1/n))
    sum_product = sum(product_list)
    weights = [product / sum_product for product in product_list]
    return list(map(float, weights))


def csm_method(A, epsilon=1e-10, max_iter=1000):
    n = len(A)
    w = np.ones(n) / n  # Initial weight vector

    for iteration in range(max_iter):
        max_val, m = None, None

        # Step 1: Find the index `m` with the largest discrepancy
        for i in range(n):
            discrepancy = 0
            for j in range(n):
                discrepancy += ((1 + A[j, i] ** 2) * (w[i] / w[j]) - (1 + A[i, j] ** 2) * (w[j] / w[i]))
            discrepancy = abs(discrepancy)
            if max_val is None or discrepancy > max_val:
                max_val = discrepancy
                m = i

        # Step 2: Check for convergence
        if max_val <= epsilon:
            break

        # Step 3: Update the weight w[m]
        up, bottom = 0, 0
        for j in range(n):
            if j != m:
                up += (1 + A[m, j] ** 2) * (w[j] / w[m])
                bottom += (1 + A[j, m] ** 2) * (w[m] / w[j])

        # Update weight vector
        T = np.sqrt(up / bottom)
        w[m] *= T
        w /= np.sum(w)  # Normalize weights

    return w


# 计算每种方法的权重向量
W_EV = ev_method(A)
W_LLSM = lls_method(A)
W_CSM = csm_method(A)

# 打印权重向量
print("Weight vector using EV method:", [f"{w:.4f}" for w in W_EV])
print("Weight vector using LLSM method:", [f"{w:.4f}" for w in W_LLSM])
print("Weight vector using CSM method:", [f"{w:.4f}" for w in W_CSM])

# 计算TD（Total Deviation）
def total_deviation(W, A):
    n = len(A)
    TD = 0
    for i in range(n):
        for j in range(n):
            TD += abs(A[i][j] - W[i] / W[j])
    return TD


TD_EV = total_deviation(W_EV, A)
TD_LLSM = total_deviation(W_LLSM, A)
TD_CSM = total_deviation(W_CSM, A)

# 打印总偏差（TD）
print("TD of EV method: {:.4f}".format(TD_EV))
print("TD of LLSM method: {:.4f}".format(TD_LLSM))
print("TD of CSM method: {:.4f}".format(TD_CSM))

# 最终应当选择TD值最小的方法
