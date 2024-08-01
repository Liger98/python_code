#\循环，将lammps的dump格式文件dump.MC.{10*i}文件，例：dump.MC.{10}转换成data格式文件sro_{i}.data，例：sro_1.data。
from ase.io import read, write
import re

# Loop through the range of files
for i in range(1, 1441):
    # Construct the filename for the current index i
    filename = f'dump.MC.{10*i}'
    dataname = f'sro_{i}.data'
    
    # Read the atoms from the LAMMPS dump file
    atoms_in = read(filename, index="-1", format="lammps-dump-text")
    
    # Write the atoms to a LAMMPS data file
    write(dataname, atoms_in, format="lammps-data")

print('Convert dump to data completed.')

# Loop through the range of files
for i in range(1, 1441):
    dataname = f'sro_{i}.data'
    
    # Read the entire content of the file
    with open(dataname, 'r') as file:
        lines = file.readlines()
    
    # Modify the sixth line by replacing 'ylo yhi' with 'zlo zhi'
    lines[5] = re.sub(r'ylo yhi$', 'zlo zhi', lines[5])
    
    # Modify the seventh line by replacing 'zlo zhi' with 'ylo yhi'
    lines[6] = re.sub(r'zlo zhi$', 'ylo yhi', lines[6])
    
    # Process the rest of the lines starting from line 12
    for j in range(11, len(lines)):
        # Split the line into separate values
        split_line = lines[j].split()
        
        # Check if the line has at least five elements to swap the fourth and fifth
        if len(split_line) >= 5:
            # Swap the fourth and fifth elements
            split_line[3], split_line[4] = split_line[4], split_line[3]
            
            # Join the line back together and assign it back to the list
            lines[j] = ' '.join(split_line) + '\n'
    
    # Write the modified content back to the file
    with open(dataname, 'w') as file:
        file.writelines(lines)

print('Transform position completed.')


