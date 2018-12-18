import sys
import collections

input_lines = []

def read_input(filename):
	for line in open(filename):
		input_lines.append(line)

def count_occurences(input_lines):
	two_count = 0
	three_count = 0
	
	for line in input_lines:
		char_dict = collections.defaultdict(int)
		for c in line:
			char_dict[c] += 1
		if 2 in char_dict.values():
			two_count += 1
		if 3 in char_dict.values():
			three_count += 1

	print(two_count * three_count)			

def min_edit_distance(input_lines):
	is_one = False
	for line in input_lines:
		for other_line in input_lines:
			if (line != other_line and len(line) == len(other_line)):
				is_one, index = is_edit_distance_one(line, other_line)
			if is_one:
				print(line[:index] + line[index+1:])
				break
		if is_one:
			break		

def is_edit_distance_one(line, other_line):
	differ_count = 0
	index = 0
	for i in range(len(line)):
		if line[i] != other_line[i]:
			differ_count += 1
			index = i
		if differ_count > 1:
			return False, index

	if differ_count == 1:
		return True, index		

	return False, index	


def main():
	if len(sys.argv) < 2:
		print("Pass the input file as the argument")
	else: 	
		read_input(sys.argv[1])
		print("Solution 1: ")
		count_occurences(input_lines)
		print("Solution 2: ")
		min_edit_distance(input_lines)

if __name__ == '__main__':
    main()
