import numpy as np
from myvasp import vasp_func as vf 
import os
import glob



def readdat(filename):
    dump = []
    elast = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            data = line.split()
            dump.append(float(data[0]))
            elast.append(float(data[9]))
    return dump, elast

def main1():
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm

    # font = fm.FontProperties(family='Cambria', size=14)
    lcolor = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'magenta', 'brown', 'lime', 'orange', 'maroon']
    lmarker=['o', '^', 'v', 's', 'p', 'D', '*']

    fig_wh = [3, 2.7]
    fig_subp = [1, 1]
    fig, ax = vf.my_plot(fig_wh, fig_subp)
    fig_pos  = np.array([0.20, 0.15, 0.75, 0.82])
    ax.set_position(fig_pos)

    with open('Ef_random.dat', 'r') as file:
        Ef_random = float(file.read().strip())     # eV

#=========collect file PotEng.dat for different temperature=========#
    filenames = []
    for i in range(600, 1401, 100):
        filename = f"diff_temp/{i}/PotEng.dat"
        filenames.extend(glob.glob(filename))

    for i, filename in enumerate(filenames):
        dump, elast = readdat(filename)
        swap = [x/1440 for x in dump]  # MC step
        pote = [(x - Ef_random)/1440*1000  for x in elast]  # formation energy (meV/atom)
        ax.plot(swap[:288000], pote[:288000], linewidth=0.5, color=lcolor[i], label=f"{i*100+600}K")

#=========collect file PotEng.dat in 10e10=========#
    dump_10e10, elast_10e10 = readdat("diff_temp/10e10/PotEng.dat")
    swap_10e10 = [x/1440 for x in dump_10e10]  # MC step
    pote_10e10 = [(x - Ef_random)/1440*1000  for x in elast_10e10]  # formation energy (meV/atom)
    ax.plot(swap_10e10[:288000], pote_10e10[:288000], linewidth=0.5, color='black', label=f"$\infty$")
    ax.text(0.01, 0.99, f'$E_f^\mathrm{{rand}}={Ef_random/1440:.3f}$ eV/atom', transform=ax.transAxes, fontsize=5, fontweight='normal', va='top')


    plt.xlabel(r'MC step')    #, fontproperties=font
    plt.ylabel(r'$E_f - E_f^\mathrm{rand}$ (meV/atom)')    # $ 
    plt.grid(alpha=1, linewidth = 0.4, linestyle='--', dashes=(10, 10))

    #plt.xlim(-2, 102)
    # plt.ylim(-7100, -6960)

    plt.legend(fontsize = 5, loc='lower right', ncol=3)
    plt.savefig('Formation energy.pdf')
    plt.savefig('Formation energy.png', dpi=300)
    # plt.show()
    plt.close('all')

main1()