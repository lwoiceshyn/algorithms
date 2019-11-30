class MaxHeap:
	'''
	Max heap class implementation. Uses a dummy value in the zero-index location to make indexing
	into the child/parent nodes easier. 
	'''
	def __init__(self, keys):
		self.heap = [0]
		if self.keys:
			self.heap += keys
			for i in range(1, len(self.heap)):
				self.heapify_down(i)

	def left(self, x): return 2*x
	def right(self, x): return 2*x +1
	def parent(self, x): return x // 2

	def heapify_up(self, index):
		'''
		Check if parent exists and if parent has a smaller value than the current node. If so,
		swap them and assign index to parents index.
		'''
		while self.parent(index) > 0 and self.heap[self.parent(index)] < self.heap[index]:
			self.heap[index], self.heap[self.parent(index)], = self.heap[self.parent(index)], self.heap[index]
			self.index = self.parent(index)

	def heapify_down(self, index):
		'''
		First check that the current node has a left or right child, and that the left or right child has a key value greater than the 
		current nodes' value.

		Then, if either the right child doesn't exist or the value of the left child's is greater, swap the current node with the left child.
		Else, swap the node with the right child. After, change the index to that node.
		'''
		while (self.left(index) < len(self.heap) and self.heap[self.left(index)] > self.heap[index]) or \
		(self.right(index) < len(self.heap) and self.heap[self.right(index)] > self.heap[index]):

			if self.right(index) >= len(self.heap) or self.heap[self.left(index)] > self.heap[self.right(index)]:
				self.heap[index], self.heap[self.left(index)], = self.heap[self.left(index)], self.heap[index]
				index = self.left(index)
			else:
				self.heap[index], self.heap[self.right(index)], = self.heap[self.right(index)], self.heap[index]
				index = self.right(index)

	def get_max(self, index):
		assert len(self.heap) > 1
		return self.heap[1]

	def insert_key(self, key):
		self.heap.append(key)
		self.heapify_up(len(self.heap)-1)

	def increase_key(self, index, increment):
		'''
		If we increase the key, the only potential necessary change would be to
		percolate it up.
		'''
		self.heap[index] += increment
		self.heapify_up(index)

	def decrease_key(self, index, decrement):
		'''
		If we decrease the key, the only potential necessary change would be to
		percolate it down.
		'''
		self.heap[index] -= decrement
		self.heapify_down(index)

	def extract_max(self):
		'''
		Extract the max(root) by swapping it with the last node, popping it, then heapifying the swapped
		node down.
		'''
		assert len(self.heap) > 1
		self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
		res = self.heap.pop()
		self.heapify_down(1)
		return res

	def heap_sort(self):
		'''
		Simply keep extracting the max node and appending to a list to
		get the sorted version in decreasing order, the reverse it.
		'''
		res = []
		while len(self.heap) > 1:
			res.append(self.extract_max())
		res.reverse()
		return res

class MinHeap:
	'''
	Min heap class implementation. Uses a dummy value in the zero-index location to make indexing
	into the child/parent nodes easier. 
	'''
	def __init__(self, keys):
		self.heap = [0]
		if self.keys:
			self.heap += keys
			for i in range(1, len(self.heap)):
				self.heapify_down(i)

	def left(self, x): return 2*x
	def right(self, x): return 2*x +1
	def parent(self, x): return x // 2

	def heapify_up(self, index):
		'''
		Check if parent exists and if parent has a greater value than the current node. If so,
		swap them and assign index to parents index.
		'''
		while self.parent(index) > 0 and self.heap[self.parent(index)] > self.heap[index]:
			self.heap[index], self.heap[self.parent(index)], = self.heap[self.parent(index)], self.heap[index]
			self.index = self.parent(index)

	def heapify_down(self, index):
		'''
		First check that the current node has a left or right child, and that the left or right child has a key value smaller than the 
		current nodes' value.

		Then, if either the right child doesn't exist or the value of the left child's is smaller, swap the current node with the left child.
		Else, swap the node with the right child. After, change the index to that node.
		'''
		while (self.left(index) < len(self.heap) and self.heap[self.left(index)] < self.heap[index]) or \
		(self.right(index) < len(self.heap) and self.heap[self.right(index)] < self.heap[index]):

			if self.right(index) >= len(self.heap) or self.heap[self.left(index)] < self.heap[self.right(index)]:
				self.heap[index], self.heap[self.left(index)], = self.heap[self.left(index)], self.heap[index]
				index = self.left(index)
			else:
				self.heap[index], self.heap[self.right(index)], = self.heap[self.right(index)], self.heap[index]
				index = self.right(index)

	def get_min(self, index):
		assert len(self.heap) > 1
		return self.heap[1]

	def insert_key(self, key):
		self.heap.append(key)
		self.heapify_up(len(self.heap)-1)

	def increase_key(self, index, increment):
		'''
		If we increase the key, the only potential necessary change would be to
		percolate it down.
		'''
		self.heap[index] += increment
		self.heapify_down(index)

	def decrease_key(self, index, decrement):
		'''
		If we decrease the key, the only potential necessary change would be to
		percolate it up.
		'''
		self.heap[index] -= decrement
		self.heapify_up(index)

	def extract_min(self):
		'''
		Extract the min(root) by swapping it with the last node, popping it, then heapifying the swapped
		node down.
		'''
		assert len(self.heap) > 1
		self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
		res = self.heap.pop()
		self.heapify_down(1)
		return res

	def heap_sort(self):
		'''
		Simply keep extracting the min node and appending to a list to
		get the sorted version in increasing order.
		'''
		res = []
		while len(self.heap) > 1:
			res.append(self.extract_min())
		return res