import sys

def read_input(filename):
    input = []
    for line in open(filename):
        input = [int(n) for n in line.split()]
    return input

def calculate_checksum(index, checksum, input):
    if index < len(input): 
        child_count = input[index]
        metadata_count = input[index + 1]

        if child_count == 0:
            return index + 2 + metadata_count, checksum + input[index + 2 : index + 2 + metadata_count]       
        else:
            new_index = index + 2
            while child_count > 0:
                new_index, checksum = calculate_checksum(new_index, checksum, input)
                child_count -=1
            return new_index + metadata_count, checksum + input[new_index : new_index + metadata_count]
    else:
        return index, checksum

def main():
    if len(sys.argv) < 2:
        print("Pass the input file as the argument")
    else: 
        input = read_input(sys.argv[1])
        index, checksum = calculate_checksum(0, [], input)
        print("Solution 1 :")
        print(sum(checksum))

if __name__ == '__main__':
    main()
