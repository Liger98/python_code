import numpy as np
import matplotlib.pyplot as plt

def main():
    # 设置绘图属性
    lcolor = ['C0', 'C1', 'C2', 'C3', 'C4', 'y', 'k', 'w']
    lmarker = ['o', '^', 'v', 's', 'p', 'D', '*']
    
    fig_wh = [6, 4]
    fig, ax = plt.subplots(figsize=fig_wh)
    fig_pos = np.array([0.15, 0.15, 0.75, 0.75])
    ax.set_position(fig_pos)

    # 读取数据文件
    filename = 'alpha_data.txt'  # 修改为你的数据文件名
    with open(filename, 'r') as f:
        lines = f.readlines()
        headers = lines[0].strip().split()  # 获取列标题
        data = np.loadtxt(lines[1:])  # 跳过标题行，加载数据
    
    # 获取行和列数
    num_rows, num_cols = data.shape
    
    # 检查列数是否匹配标题
    if len(headers) != num_cols:
        raise ValueError("标题列数与数据列数不匹配！")

    # 绘制每一列
    x = np.arange(num_rows)  # 使用行号作为x轴
    for col in range(num_cols):
        ax.plot(x, data[:, col], label=f'{headers[col]}', 
                color=lcolor[col % len(lcolor)], 
                marker=lmarker[col % len(lmarker)], 
                markersize=3, linewidth=1)

    # 设置图形标签
    ax.set_xlabel('realization')
    ax.set_ylabel('alpha')
    ax.grid(alpha=0.7, linewidth=0.5, linestyle='--', dashes=(5, 5))
    plt.legend(loc='best', fontsize=8)

    # 保存图像
    # plt.savefig('Alpha_Values_Plot.pdf')
    plt.savefig('Alpha_Values_Plot.png', dpi=300)
    plt.close('all')

if __name__ == '__main__':
    main()
