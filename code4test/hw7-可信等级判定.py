import math
import matplotlib.pyplot as plt
import numpy as np

# 权重
weight = [0.05, 0.17, 0.20, 0.15, 0.09, 0.09, 0.11, 0.05, 0.09]

# 子权重
childWeight = [
    0.31, 0.36, 0.33,  # 指标1子权重
    0.33, 0.33, 0.34,  # 指标2子权重
    0.16, 0.17, 0.17, 0.17, 0.17, 0.16,  # 指标3子权重
    0.33, 0.34, 0.33,  # 指标4子权重
    0.34, 0.33, 0.33,  # 指标5子权重
    0.5, 0.5,          # 指标6子权重
    0.33, 0.34, 0.33,  # 指标7子权重
    0.5, 0.5,         # 指标8子权重
    0.33, 0.33, 0.34   # 指标9子权重
]

# 将等级转换为对应数值
def grade_to_value(grade):
    if grade == 'A':
        return 10.0
    elif grade == 'B':
        return 9.0
    elif grade == 'C':
        return 7.0
    elif grade == 'D':
        return 2.0
    else:
        return 0.0

# 计算信任值
def calculate_trust(values, weights):
    trust_value = 1.0
    for i in range(len(values)):
        trust_value *= math.pow(values[i], weights[i])
    return trust_value

# 判断信任等级
def judge_trust_level_07(component_trust_values, key_component_count, overall_trust):
    total_components = len(component_trust_values)
    key_threshold = 3
    low_key_count9_5 = 0
    low_key_count8_5 = 0
    low_key_count7_0 = 0
    low_key_count4_5 = 0
    has_low85 = False
    has_low70 = False
    has_low45 = False

    # 统计关键组件低于对应阈值的数量
    for i in range(key_component_count):
        if component_trust_values[i] < 9.5:
            low_key_count9_5 += 1
        if component_trust_values[i] < 8.5:
            low_key_count8_5 += 1
        if component_trust_values[i] < 7.0:
            low_key_count7_0 += 1
        if component_trust_values[i] < 4.5:
            low_key_count4_5 += 1

    # 统计所有组件低于对应阈值的情况
    for i in range(total_components):
        if component_trust_values[i] < 8.5:
            has_low85 = True
        if component_trust_values[i] < 7.0:
            has_low70 = True
        if component_trust_values[i] < 4.5:
            has_low45 = True

    # 判断信任等级
    if overall_trust >= 9.5 and low_key_count9_5 <= key_threshold and not has_low85:
        return "V"
    elif overall_trust >= 8.5 and not has_low70 and low_key_count8_5 <= key_threshold:
        return "IV"
    elif overall_trust >= 7.0 and not has_low45 and low_key_count7_0 <= key_threshold:
        return "III"
    elif overall_trust >= 4.5 and low_key_count4_5 <= key_threshold:
        return "II"
    else:
        return "I"

# 绘制折线图
def plot_line_chart(title, x_label, y_label, data, labels):
    plt.figure(figsize=(10, 6))
    for i, series in enumerate(data):
        plt.plot(series, label=labels[i])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.show()

# 绘制条形图
def plot_bar_chart(software_numbers, trust_values, trust_levels):
    # 定义等级对应的颜色
    level_colors = {
        "V": "green",
        "IV": "blue",
        "III": "orange",
        "II": "purple",
        "I": "red"
    }

    # 获取每个软件对应的颜色
    colors = [level_colors[level] for level in trust_levels]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(software_numbers, trust_values, color=colors)

    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.2f}", ha='center', va='bottom')

    plt.title("Software Trust Values and Trust Levels")
    plt.xlabel("Software Number")
    plt.ylabel("Trust Value")
    plt.xticks(software_numbers)
    plt.grid(True, axis='y')

    # 添加图例
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='green', label='Level V'),
        Patch(facecolor='blue', label='Level IV'),
        Patch(facecolor='orange', label='Level III'),
        Patch(facecolor='purple', label='Level II'),
        Patch(facecolor='red', label='Level I')
    ]
    plt.legend(handles=legend_elements, title="Trust Levels")

    plt.show()

# 主函数
def main():
    # 8组28个等级数据
    grades = [
        # ['C', 'B', 'C', 'D', 'B', 'B', 'C', 'A', 'C', 'D', 'C', 'A', 'C', 'C', 'C', 'C', 'C', 'A', 'D', 'C', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D'],
        "CBCDBBCACDCACCCCCADCAAABBCCD",
        ['C', 'B', 'B', 'B', 'D', 'D', 'B', 'C', 'C', 'C', 'B', 'C', 'B', 'C', 'C', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A'],
        ['A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A'],
        ['C', 'B', 'B', 'B', 'D', 'A', 'B', 'C', 'C', 'C', 'B', 'C', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A'],
        ['C', 'B', 'B', 'B', 'D', 'D', 'B', 'C', 'C', 'C', 'B', 'C', 'B', 'C', 'C', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A'],
        ['C', 'B', 'B', 'B', 'D', 'D', 'A', 'B', 'C', 'C', 'B', 'C', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A'],
        # ['C', 'B', 'B', 'B', 'D', 'D', 'B', 'C', 'C', 'C', 'B', 'C', 'B', 'C', 'C', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A'],
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAB",
        ['C', 'D', 'D', 'D', 'D', 'D', 'B', 'C', 'C', 'C', 'D', 'C', 'D', 'C', 'C', 'D', 'B', 'D', 'D', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'B']
    ]

    # 处理每一组数据
    attribute_trust_values_list = []
    software_trust_values = []
    trust_levels = []

    for i in range(len(grades)):
        child_trust_values = [grade_to_value(grade) for grade in grades[i]]

        # 计算各属性信任值
        attribute_trust_values = []
        index = 0
        for attr in range(len(weight)):
            sub_trusts = []
            sub_weights = []
            if attr == 0:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1], child_trust_values[index+2]]
                index += 3
            elif attr == 1:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1], child_trust_values[index+2]]
                index += 3
            elif attr == 2:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1], child_trust_values[index+2],
                              child_trust_values[index+3], child_trust_values[index+4], child_trust_values[index+5]]
                index += 6
            elif attr == 3:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1], child_trust_values[index+2]]
                index += 3
            elif attr == 4:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1], child_trust_values[index+2]]
                index += 3
            elif attr == 5:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1]]
                index += 2
            elif attr == 6:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1], child_trust_values[index+2]]
                index += 3
            elif attr == 7:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1]]
                index += 2
            elif attr == 8:
                sub_trusts = [child_trust_values[index], child_trust_values[index+1], child_trust_values[index+2]]
                index += 3

            sub_weights = childWeight[index-len(sub_trusts):index]
            attribute_trust_values.append(calculate_trust(sub_trusts, sub_weights))

        attribute_trust_values_list.append(attribute_trust_values)

        # 计算软件信任值
        software_trust_value = calculate_trust(attribute_trust_values, weight)
        software_trust_values.append(software_trust_value)

        # 判断信任等级
        trust_level = judge_trust_level_07(attribute_trust_values, len(attribute_trust_values), software_trust_value)
        trust_levels.append(trust_level)

        # 输出每组的各属性信任值
        print(f"第 {10 + i} 组", end=" ")
        for attr_trust in attribute_trust_values:
            print(f"{attr_trust:.3f}", end=" ")

        # 输出软件信任值及信任等级
        print(f" 软件信任值为 {software_trust_value:.3f}  信任等级为 {trust_level}")

    # 可视化属性信任值
    labels = [f"Software Number {10 + i}" for i in range(len(grades))]
    plot_line_chart("Software Reliability Attributes Line Chart", "Attributes", "Trust Value", attribute_trust_values_list, labels)

    # 可视化软件信任值（条形图）
    software_numbers = range(10, 10 + len(grades))
    plot_bar_chart(software_numbers, software_trust_values, trust_levels)

if __name__ == "__main__":
    main()
