import sys 
import numpy as np 


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
	def while_loop(self,code,spot): #spot is the location in the main code. 
		code1 = str()
		spot1 = spot+1
		while code[spot1] != ']':
			# if code[spot1] == '[':
			# 	self.while_loop(self.master, spot1,self.loc_ptr)
			code1 += code[spot1]
			spot1 += 1
			# print(code1)

		while self.ptrs[self.loc_ptr] > 1:
			self.out(code1)

	def out(self,code=None,loc_ptr=0):
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
				self.while_loop(code, index)
			elif char == ']':
				continue

if __name__ == "__main__":
	foo = BrainFuck()
	# print(foo.master)
	foo.out()
	print(foo.output)
	print(foo.output, foo.ptrs[0:6])

