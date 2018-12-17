import numpy as np
import sys

cloth_rect = np.zeros((1000, 1000))
rect_details = []

def read_input(line):
	ip = line.replace(',',' ').replace('x',' ').replace(':','').replace('#','').split()
	id = int(ip[0])
	x = int(ip[2])
	y = int(ip[3])
	w = int(ip[4])
	h = int(ip[5])
	return id, x, y, w, h

def assign_values(filename):
	for line in open(filename):
		id, x, y, w, h = read_input(line)
		rect_details.append((id, x, y, w, h))
		cloth_rect[y:y+h,x:x+w] += 1

def print_unique_id():
	for id, x, y, w, h in rect_details:
		if(cloth_rect[y:y+h,x:x+w] == 1).all():
			print(id)

def print_overlapping_grid_count():
	print(np.sum(np.where(cloth_rect > 1, 1, 0)))


def main():
	if len(sys.argv) < 2:
		print("Pass the input file as the argument")
	else: 
		assign_values(sys.argv[1])
		print("Solution 1")
		print_overlapping_grid_count()
		print("Solution 2")
		print_unique_id()

if __name__ == '__main__':
    main()
