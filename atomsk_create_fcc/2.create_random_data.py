import random

# Main function to process the .lmp file
def main():
    input_filename = 'AuNi_111.lmp'
    output_filename = 'AuNi_111_random.lmp'
    
    # Read and shuffle atoms
    shuffled_atom_data = read_and_shuffle_atoms(input_filename)
    if shuffled_atom_data is not None:
        # Write the shuffled atoms to a new file with the first 17 lines from the original file
        write_shuffled_data(input_filename, shuffled_atom_data, output_filename)
        print(f"Shuffled atom data has been written to {output_filename}")

# Function to shuffle atom types
def shuffle_atom_types(atom_data):
    num_atoms = len(atom_data)
    num_type_1 = int(0.6 * num_atoms)  # 60% 的原子赋值为1
    num_type_2 = num_atoms - num_type_1  # 剩下的40% 的原子赋值为2

    # 创建新的 atom_types 列表，60% 的值为1，40% 的值为2
    atom_types = [1] * num_type_1 + [2] * num_type_2
    random.shuffle(atom_types)  # 随机打乱 atom_types 列表

    for i, atom in enumerate(atom_data):
        atom_data[i][1] = atom_types[i]  # 将随机打乱的类型赋予原子

    return atom_data

# Read the file and extract atom data
def read_and_shuffle_atoms(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Extracting atom data starting from line 17
            atom_data = [list(map(float, line.split())) for line in lines[16:]]
            # Shuffle atom types while keeping positions the same
            shuffled_atom_data = shuffle_atom_types(atom_data)
            return shuffled_atom_data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Write the shuffled atom data to a new file
def write_shuffled_data(input_filename, shuffled_atom_data, output_filename):
    try:
        with open(output_filename, 'w') as outfile:
            # Copy the first 17 lines from the input file to the output file
            with open(input_filename, 'r') as infile:
                for _ in range(17):
                    line = infile.readline()
                    outfile.write(line)
            
            # Write the shuffled atom data to the output file
            for atom in shuffled_atom_data:
                atom_line = '{:5d} {:5d} {:22.12f} {:22.12f} {:22.12f}\n'.format(
                    int(atom[0]), int(atom[1]), atom[2], atom[3], atom[4]
                )
                outfile.write(atom_line)
    except Exception as e:
        print(f"An error occurred while writing to {output_filename}: {e}")

if __name__ == "__main__":
    main()
