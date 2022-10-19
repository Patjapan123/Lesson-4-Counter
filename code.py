class Counter:
	def __init__(self):
		self.Count=0
	def add_one(self):
		self.Count+=1
	def subtract_one(self):
		self.Count-=1
	def reset(self):
		self.Count-=self.Count
	def get(self):
		return self.Count
	