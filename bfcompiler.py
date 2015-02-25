import sys 
import numpy as np 
import time

class BrainFuck(object):

	def __init__(self):

		filename = str(sys.argv[1])

		if ".bf" not in filename or '.b' not in filename:
			print("You sure that's a brainfuck file?")
			sys.exit()
		self.bf_char = "+-><[].,"
		self.dummy = str()
		with open(filename,'r') as bf:
			for line in bf:
				self.dummy += line.strip('\n\t')

		self.master = str()
		for char in self.dummy:
			if char in self.bf_char:
				self.master += char
			else:
				continue

		self.ptrs = np.zeros(100,dtype=int)
		self.output = str()
		self.loc_ptr = 0

	def brace_map(self):
		opening = []
		loop = {}
		for index, char in enumerate(self.master):
			if char == '[':
				opening.append(index)
			elif char == ']':
				begin = opening.pop()
				loop[begin] = index
		self.loop = loop
		return loop	

	def while_loop(self,spot): #spot is the location in code. 
		code_chunk = self.master[spot+1:self.loop[spot]]
		time.sleep(1)
		print(code_chunk)
		while self.ptrs[self.loc_ptr] > 1:
			self.out(code_chunk,spot)
		# print(self.ptrs[0:7])
		# print(self.output)
		# while code[spot1] != ']':
		# 	if code[spot1] == '[':
		# 		self.while_loop(self.master, spot1)
		# 	code1 += code[spot1]
		# 	spot1 += 1
			# print(code1)

	def out(self,code=None,spot=0):
		if code == None:
			code = self.master

		for index, char in enumerate(code):
			# print(self.ptrs[0:5])
			# index is the location in the code. 
			# loc is the current position in the ptrs list. 
			if char == '+':
				self.ptrs[self.loc_ptr] += 1
			elif char == '-':
				self.ptrs[self.loc_ptr] -= 1
			elif char == '>':
				self.loc_ptr += 1
			elif char == '<':
				self.loc_ptr -= 1
			elif char == ',':
				self.ptrs[self.loc_ptr] = int(raw_input(">> "))
			elif char == '.':
				self.output += chr(self.ptrs[self.loc_ptr])
			elif char == '[':
				self.while_loop(index+spot)
			elif char == ']':
				continue


if __name__ == "__main__":
	foo = BrainFuck()
	print(foo.brace_map())
	print(foo.loop)
	foo.out()
	# print(foo.master)
	# foo.out()
	print(foo.output)
	# print(foo.output, foo.ptrs[0:10])

