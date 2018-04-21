#defining 3 different classes for three different categories of subjects
class generalStore():
	#initializing class with properties of time, stride, identity, and age
	def __init__(self, Pname, Gname, cell, lifespan, development, unique):
		self.Pname = Pname
		self.Gname = Gname
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
			obj = generalStore(data_org[0], data_org[1], data_org[2], data_org[3], data_org[4], data_org[5])
			#appending objects to objectsOld list
			kingdoms.append(obj)


def userInput():
	ask = input("What do you want to know more about? ")
	i = 0
	while i != len(kingdoms):
		if ask in kingdoms[i].Pname:
			print("Phylogenetic name: " + kingdoms[i].Pname)
			print("General name: " + kingdoms[i].Gname)
			print("Cell type: " + kingdoms[i].cell)
			print("Lifespan: " + kingdoms[i].lifespan)
			print("Development: " + kingdoms[i].development)
			print("Unique characteristic: " + kingdoms[i].unique)
			break
		if ask in kingdoms[i].Gname:
			print("Phylogenetic name: " + kingdoms[i].Pname)
			print("General name: " + kingdoms[i].Gname)
			print("Cell type: " + kingdoms[i].cell)
			print("Lifespan: " + kingdoms[i].lifespan)
			print("Development: " + kingdoms[i].development)
			print("Unique characteristic: " + kingdoms[i].unique)
			break
		i = i + 1
					
def main():
	readData()
	userInput()
	
main()
