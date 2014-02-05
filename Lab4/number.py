class Integer(object):
	def __init__(self, number, p):	
		self.number=number
		self.p=p
	
	def display(self):
		if self.p:
			print self.number
		else: 
			print (self.number - self.number - self.number)

class NegativeInteger(Integer):
	def __init__(self, number):
         	super(NegativeInteger, self).__init__(number, False)
        def display(self):
		Integer.display(self)
		print "This is an object of the NegativeInteger class."

if __name__=="__main__":
	test = Integer(3, True)
	test.display()
	test2 = NegativeInteger(4)
	test2.display()
