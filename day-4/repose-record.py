import sys
import numpy as np
import collections

guard_dict = collections.defaultdict(lambda: np.zeros((60)))

def read_input(filename):
	ip_list = []
	for line in open(filename):
			ip_list.append(line.replace('[',' ').replace(']',' ').replace('#','').replace('up', '').replace('falls','').replace('begins','').replace('shift','').split())
	sorted_ip_list = sorted(ip_list, key=lambda x: (x[0], x[1]))
	return sorted_ip_list						

def calculate_sleep_time(sorted_ip_list):
	sleep_time = 0
	for guard in sorted_ip_list:
		if guard[2] == 'Guard':
			guard_id = int(guard[3])
		if guard[2] == 'asleep':
				sleep_time = int(guard[1].split(':')[1])
		if guard[2] == 'wakes':
				end_time = int(guard[1].split(':')[1])
				guard_dict[guard_id][sleep_time:end_time] += 1

def find_guard_checksum():
	sorted_dict = sorted(guard_dict.items(), key=lambda i: np.sum(i[1]), reverse=True)
	print(sorted_dict[0][0] * sorted_dict[0][1].argmax())

def find_guard_minute_checksum():
	sorted_dict = sorted(guard_dict.items(), key=lambda i: np.max(i[1]), reverse=True)
	print(sorted_dict[0][0] * sorted_dict[0][1].argmax())


def main():
	if len(sys.argv) < 2:
		print("Pass the input file as the argument")
	else: 
		sorted_ip_list = read_input(sys.argv[1])
		calculate_sleep_time(sorted_ip_list)
		print("Solution 1 :")
		find_guard_checksum()
		print("Solution 2 :")
		find_guard_minute_checksum()

if __name__ == '__main__':
    main()
