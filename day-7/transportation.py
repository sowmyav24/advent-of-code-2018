import sys
import collections

graph = collections.defaultdict(list)
output = []

def read_input(filename):
	ip_list = []
	for line in open(filename):
		ip_list.append(line.replace(' must be finished before step ',' ').replace(' can begin.', '').replace('Step ','').split())
	
	for k, v in ip_list:
		graph[k].append(v)	

	for item in graph:
		graph[item] = sorted(graph[item])	

def find_values():
	values = set()
	for v in graph.values():
		for x in v:
			values.add(x)
	return values		

def generate_route(root_node):
	queue = []
	queue.extend(root_node)
	while graph:
		new_queue = []
		while len(queue) > 0:
			item = sorted(queue)[0]
			if item not in find_values():
				if item not in output:
					output.extend(item)
				item_values = graph[item]
				del graph[item]
				for i in item_values:
					if i not in find_values() and i not in queue:
						queue.extend(i)
			else:
				new_queue.append(item)
			queue.remove(item)	
		queue = new_queue
	print(''.join(output))		


def main():
	if len(sys.argv) < 2:
		print("Pass the input file as the argument")
	else: 
		read_input(sys.argv[1])
		values = find_values()
		root_node =  [key for key in graph.keys() if key not in values]
		print("Solution 1 :")
		generate_route(root_node)

if __name__ == '__main__':
    main()
