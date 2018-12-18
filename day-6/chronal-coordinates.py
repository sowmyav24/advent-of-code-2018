import sys
import numpy as np

coordinates = []

def read_input(filename):
	for line in open(filename):
		x,y = line.replace('\n','').split(', ')
		coordinates.append((int(x),int(y)))
	return coordinates	

def form_initial_grid(coordinates):
	gridX = max(coordinates, key=lambda item:item[1])[1] + 1
	gridY = max(coordinates, key=lambda item:item[0])[0] + 1
	grid = np.zeros((gridX, gridY))

	for count, item in enumerate(coordinates):
		grid[item[1]][item[0]] = count+1
	return grid, gridX, gridY	

def calculate_distance(coordinates, grid):
	for ix,iy in np.ndindex(grid.shape):
		if grid[ix,iy] == 0:
			grid[ix,iy] = find_distance(coordinates, ix, iy, grid)
	return grid		

def find_distance(coordinates, ix, iy, grid):
	min_distance = 1000
	count = 0
	value = 1
	for c in coordinates:
		distance = abs(ix-c[1]) + abs(iy-c[0])
		if distance < min_distance:
			min_distance = distance
			count = 1
			value = grid[c[1], c[0]]
		elif distance == min_distance:
			count += 1
	return int(value) if count == 1 else 0			 

def find_region_count(coordinates, grid):
	count = 0
	for ix,iy in np.ndindex(grid.shape):
		distance = 0
		for c in coordinates:
			distance += abs(ix-c[1]) + abs(iy-c[0])
		if distance < 10000:
			count += 1
	print(count)				

def find_frequent(grid, x_axis, y_axis):
		unique, counts = np.unique(grid, return_counts=True)
		frequency = np.asarray((unique, counts)).T	
		ordered_frequency = sorted(frequency, key=lambda x: x[1],  reverse=True)
		for freq in ordered_frequency:
			if freq[0] not in (grid[x_axis - 1, 0:y_axis-1]) and freq[0] not in (grid[0, 0:y_axis - 1]) and freq[0] not in (grid[0:x_axis - 1, y_axis-1]) and freq[0] not in (grid[0:x_axis - 1, 0]) :
				print(int(freq[1]))
				break		

def main():
	if len(sys.argv) < 2:
		print("Pass the input file as the argument")
	else: 
		coordinates = read_input(sys.argv[1])
		grid, x_axis, y_axis = form_initial_grid(coordinates)
		grid = calculate_distance(coordinates, grid)
		print("Solution 1 : ")
		find_frequent(grid, grid.shape[0], grid.shape[1])
		find_region_count(coordinates, grid)

if __name__ == '__main__':
    main()