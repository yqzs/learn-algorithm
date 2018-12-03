def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		if costs[node] < lowest_cost and node not in processed:
			lowest_cost = costs[node]
			lowest_cost_node = node
	return lowest_cost_node
		
graph = dict()
graph["start"] = dict()
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = dict()
graph["a"]["final"] = 1
graph["b"] = dict()
graph["b"]["a"] = 3
graph["b"]["final"] = 5
graph["final"] = dict()
infinity = float("inf")
costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["final"] = infinity
parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["final"] = None
processed = []  #建立三个字典
node = find_lowest_cost_node(costs)  #最小开销节点
while node is not None:
	cost = costs[node]  
	for n in graph[node].keys():  #遍历节点的邻居
		new_cost = cost + graph[node][n]   #邻居的新开销
		if new_cost < costs[n]:
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)
for m in parents.keys():
	print(m +"->" + parents[m])