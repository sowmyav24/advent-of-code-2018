import sys
import collections 

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

def calculate_root_checksum(input_iter, child_count, metadata_count):
    if child_count == 0:
        return sum(next(input_iter) for i in range(metadata_count))

    value = 0
    value_children = collections.defaultdict(int)

    for i in range(child_count):
        value_children[i] = calculate_root_checksum(input_iter, next(input_iter), next(input_iter))
    
    for i in range(metadata_count):
        value += value_children[next(input_iter) - 1]

    return value

def main():
    if len(sys.argv) < 2:
        print("Pass the input file as the argument")
    else: 
        input = read_input(sys.argv[1])
        index, checksum = calculate_checksum(0, [], input)
        print("Solution 1 :")
        print(sum(checksum))
        print("Solution 2 :")
        input_iter = iter(input)
        print(calculate_root_checksum(input_iter, next(input_iter), next(input_iter)))

if __name__ == '__main__':
    main()




