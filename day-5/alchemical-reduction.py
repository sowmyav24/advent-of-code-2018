import sys

def read_input(filename):
	polymer = '';
	for line in open(filename):
		polymer = line.strip();
	return polymer	

def check_if_reactive(char_one, char_two):
	return char_one != char_two and char_one.lower() == char_two.lower()  

def find_resultant_polymer_length(polymer):
	i = 1
	final_polymer = []
	final_polymer.append(polymer[0])
	while i < len(polymer):
		is_reactive = final_polymer and check_if_reactive(final_polymer[-1], polymer[i])
		if is_reactive:
			del final_polymer[-1]
		else:
			final_polymer.append(polymer[i])
		i += 1
	return len(final_polymer)

def reduced_min_units(polymer):
	min_length = len(polymer)
	units = set()
	for p in polymer:
		units.add(p.lower())
	for unit in units:
		reduced_polymer_length = find_resultant_polymer_length(list(polymer.replace(unit, '').replace(unit.upper(), '')))
		min_length = reduced_polymer_length if reduced_polymer_length < min_length else min_length
	return min_length	

def main():
	if len(sys.argv) < 2:
		print("Pass the input file as the argument")
	else: 
		polymer = read_input(sys.argv[1])
		print("Solution 1 :")
		print(find_resultant_polymer_length(list(polymer)))
		print("Solution 2 :")
		print(reduced_min_units(polymer))

if __name__ == '__main__':
    main()

