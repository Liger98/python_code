import os

lattice_constant = 3.81
material = "Au Ni"
orientation = "[110] [1-12] [-111]"
# orientation = "[100] [010] [001]"
duplication = "14 8 6"
# duplication = "7 7 7"
filename = "{}_111".format(material.replace(" ", ""))
data = "lammps"

command = 'atomsk --create fcc {} {} orient {} -duplicate {} {} {} ' \
    .format(lattice_constant, material, orientation, duplication, filename, data)
# command = 'atomsk --create fcc {} {} orient {} -duplicate -sort  {} {} {}' \
#     .format(lattice_constant, material, orientation, duplication, filename, data)

os.system(command)

