import sys
import collections

input_lines = []
sum_dict = collections.defaultdict(int)

def calculate_frequency(input_lines):
	frequency = 0
	for ip in input_lines:
		frequency += int(ip)
	return frequency	

def read_input(filename):
	for line in open(filename):
		input_lines.append(int(line))

def find_frequency(input_lines):
	found_dict = { False: 0 }
	sum_dict[0] += 1
	while True not in found_dict:
		found_dict = find_repeated_frequency(found_dict.get(False), sum_dict, input_lines)
	print(found_dict.get(True))	

def find_repeated_frequency(sum, sum_dict, input_lines):
	value_dict = {}
	for line in input_lines:
		sum += line
		sum_dict[sum] +=1
		if sum_dict.get(sum) > 1:
			value_dict[True] = sum
			return value_dict

	value_dict[False] = sum
	return value_dict

def main():
	if len(sys.argv) < 2:
		print("Pass the input file as the argument")
	else: 
		read_input(sys.argv[1])
		frequency = calculate_frequency(input_lines)
		print("Solution 1 :")
		print(frequency)
		print("Solution 2 :")
		find_frequency(input_lines)

if __name__ == '__main__':
    main()

