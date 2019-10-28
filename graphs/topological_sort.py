def top_sort_DFS(root, node, graph, res=[], visited={}):
	'''
	A recursive depth-first search version of topological sort, which is an algorithm used
	to find a hierarchical ordering of a directed graph.

	The graph is assumed to be a dictionary such that each key is a vertex in the graph, and 
	the value associated with each key is an iterable containing the children of that vertex.

	If the graph is not acyclic, a topological sort is not possible/valid, in which case this function 
	will return True. So the boolean returns are True if cycle detected, False if acyclic. 

	Time Complexity: O(V+E)
	Space Complexity: O(V+E)
	'''
	if node not in visited:
		visited[node] = root
		for child in graph[node]:
			if top_sort_DFS(root, child, graph, res, visited):
				return True
		res.append(node)
	elif visited[node] == root:
		return True
	return False

