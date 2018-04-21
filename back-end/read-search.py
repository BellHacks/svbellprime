#defining 3 different classes for three different categories of subjects
class generalStore():
	#initializing class with properties of time, stride, identity, and age
	def __init__(self, identity, cell, lifespan, development, unique):
		self.identity = identity
		self.cell = cell
		self.lifespan = lifespan
		self.development = development
		self.unique = unique
		
#3 lists for three different categories of subjects
domains = []	
kingdoms = []
phylums = []
classes = []
orders = []
families = []
genera = []
species = []
		
def readData():
	#using with loop to open up textfile
	with open("kingdom.txt") as file:
		#reading all the lines in the textfile and storing it in the variable data
		data = file.readlines()
		#using a for loop for each line in data
		for line in data:
			#debug 1 below
			#print(line)
			#splitting lines into two
			data_org = line.split(',')
			#eliminating spaces
			data_org = [elem.strip() for elem in data_org]
			#debug 2 below
			#print(data_org)
			#defining objects with these properties
			obj = generalStore(data_org[0], data_org[1], data_org[2], data_org[3], data_org[4])
			#appending objects to objectsOld list
			kingdoms.append(obj)
			
def main():
	readData()

main()
