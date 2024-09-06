import numpy as np
from myvasp import vasp_func as vf 
import os

def main():
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm

    # font = fm.FontProperties(family='Cambria', size=14)
    lcolor=['C0', 'C1', 'C2', 'C3', 'C4', 'y', 'k', 'w']
    lmarker=['o', '^', 'v', 's', 'p', 'D', '*']

    fig_wh = [3.27, 2.7]
    fig_subp = [1, 1]
    fig, ax = vf.my_plot(fig_wh, fig_subp)
    fig_pos  = np.array([0.20, 0.15, 0.75, 0.82])
    ax.set_position(fig_pos)

    dump = []
    elast = []
    PotEng = []
    
    with open('PotEng.dat', 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            data = line.split()
            dump.append(float(data[0]))
            elast.append(float(data[1]))
            PotEng.append(float(data[2]))
      
    ax.plot(dump, PotEng, linewidth=1, color='C0', label = r'Sample 1')
    # ax.plot(dump, elast, linewidth=1, color='C1', label = r'Sample 11')

    plt.xlabel(r'MC steps')    #, fontproperties=font
    plt.ylabel(r'Total potential energy (eV)')    #, fontproperties=font
    plt.grid(alpha=1, linewidth = 0.4, linestyle='--', dashes=(10, 10))

#     plt.xlim(0, 15000)
#     plt.ylim(0, 14)

    plt.legend(loc=(0.65, 0.70), fontsize = 7)
    plt.savefig('Energy evolvement.pdf')
#     plt.savefig('Element.png', dpi=300)
#     plt.show()
    plt.close('all')
main()
