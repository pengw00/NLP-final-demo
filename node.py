
class Node:
	def __init__(self, root, left, right, end):
		self._root = root
		self._left = left
		self._right = right
		self._terminal = end
		self._status = True
		if end == None:
			self._status = False
	def root(self):
		return self._root
	def left(self):
		return self._left
	def right(self):
		return self._right
	def status(self):
		return self._status
	def terminal(self):
		return self._terminal