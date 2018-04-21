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
	with open("domains.txt") as file:
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
			domains.append(obj)
	#using with loop to open up textfile
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
	'''
	#using with loop to open up textfile
	with open("phylum.txt") as file:
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
			phylums.append(obj)
	#using with loop to open up textfile
	with open("order.txt") as file:
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
			orders.append(obj)
	#using with loop to open up textfile
	with open("class.txt") as file:
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
			classes.append(obj)
			'''
			
def userInput():
	ask = input("What do you want to know more about? ")
	a = 0
	while a != len(domains):
		if ask in domains[a].Pname:
			print("Phylogenetic name: " + domains[a].Pname)
			print("General name: " + domains[a].Gname)
			print("Cell type: " + domains[a].cell)
			print("Lifespan: " + domains[a].lifespan)
			print("Development: " + domains[a].development)
			print("Unique characteristic: " + domains[a].unique)
			break
		if ask in domains[a].Gname:
			print("Phylogenetic name: " + domains[a].Pname)
			print("General name: " + domains[a].Gname)
			print("Cell type: " + domains[a].cell)
			print("Lifespan: " + domains[a].lifespan)
			print("Development: " + domains[a].development)
			print("Unique characteristic: " + domains[a].unique)
			break
		a = a + 1
	
	b = 0
	while b != len(kingdoms):
		if ask in kingdoms[b].Pname:
			print("Phylogenetic name: " + kingdoms[b].Pname)
			print("General name: " + kingdoms[b].Gname)
			print("Cell type: " + kingdoms[b].cell)
			print("Lifespan: " + kingdoms[b].lifespan)
			print("Development: " + kingdoms[b].development)
			print("Unique characteristic: " + kingdoms[b].unique)
			break
		if ask in kingdoms[b].Gname:
			print("Phylogenetic name: " + kingdoms[b].Pname)
			print("General name: " + kingdoms[b].Gname)
			print("Cell type: " + kingdoms[b].cell)
			print("Lifespan: " + kingdoms[b].lifespan)
			print("Development: " + kingdoms[b].development)
			print("Unique characteristic: " + kingdoms[b].unique)
			break
		b = b + 1
	'''
	while c != len(phylums):
		if ask in phylums[i].Pname:
			print("Phylogenetic name: " + phylums[i].Pname)
			print("General name: " + phylums[i].Gname)
			print("Cell type: " + phylums[i].cell)
			print("Lifespan: " + phylums[i].lifespan)
			print("Development: " + phylums[i].development)
			print("Unique characteristic: " + phylums[i].unique)
		if ask in phylums[i].Gname:
			print("Phylogenetic name: " + phylums[i].Pname)
			print("General name: " + phylums[i].Gname)
			print("Cell type: " + phylums[i].cell)
			print("Lifespan: " + phylums[i].lifespan)
			print("Development: " + phylums[i].development)
			print("Unique characteristic: " + phylums[i].unique)	
			break
		c = c + 1
		
	while d != len(classes):
		if ask in classes[i].Pname:
			print("Phylogenetic name: " + classes[i].Pname)
			print("General name: " + classes[i].Gname)
			print("Cell type: " + classes[i].cell)
			print("Lifespan: " + classes[i].lifespan)
			print("Development: " + classes[i].development)
			print("Unique characteristic: " + classes[i].unique)
		if ask in classes[i].Gname:
			print("Phylogenetic name: " + classes[i].Pname)
			print("General name: " + classes[i].Gname)
			print("Cell type: " + classes[i].cell)
			print("Lifespan: " + classes[i].lifespan)
			print("Development: " + classes[i].development)
			print("Unique characteristic: " + classes[i].unique)
			
	while i != len(orders):
		if ask in orders[i].Pname:
			print("Phylogenetic name: " + orders[i].Pname)
			print("General name: " + orders[i].Gname)
			print("Cell type: " + orders[i].cell)
			print("Lifespan: " + orders[i].lifespan)
			print("Development: " + orders[i].development)
			print("Unique characteristic: " + orders[i].unique)
			break
		if ask in orders[i].Gname:
			print("Phylogenetic name: " + orders[i].Pname)
			print("General name: " + orders[i].Gname)
			print("Cell type: " + orders[i].cell)
			print("Lifespan: " + orders[i].lifespan)
			print("Development: " + orders[i].development)
			print("Unique characteristic: " + orders[i].unique)
			break
		i = i + 1
		
	while i != len(families):
		if ask in families[i].Pname:
			print("Phylogenetic name: " + families[i].Pname)
			print("General name: " + families[i].Gname)
			print("Cell type: " + families[i].cell)
			print("Lifespan: " + families[i].lifespan)
			print("Development: " + families[i].development)
			print("Unique characteristic: " + families[i].unique)
			break
		if ask in families[i].Gname:
			print("Phylogenetic name: " + families[i].Pname)
			print("General name: " + families[i].Gname)
			print("Cell type: " + families[i].cell)
			print("Lifespan: " + families[i].lifespan)
			print("Development: " + families[i].development)
			print("Unique characteristic: " + families[i].unique)
			break
		i = i + 1
	
	while i != len(genera):
		if ask in genera[i].Pname:
			print("Phylogenetic name: " + genera[i].Pname)
			print("General name: " + genera[i].Gname)
			print("Cell type: " + genera[i].cell)
			print("Lifespan: " + genera[i].lifespan)
			print("Development: " + genera[i].development)
			print("Unique characteristic: " + genera[i].unique)
			break
		if ask in genera[i].Gname:
			print("Phylogenetic name: " + genera[i].Pname)
			print("General name: " + genera[i].Gname)
			print("Cell type: " + genera[i].cell)
			print("Lifespan: " + genera[i].lifespan)
			print("Development: " + genera[i].development)
			print("Unique characteristic: " + genera[i].unique)
			break
		i = i + 1
		
	while i != len(species):
		if ask in species[i].Pname:
			print("Phylogenetic name: " + species[i].Pname)
			print("General name: " + species[i].Gname)
			print("Cell type: " + species[i].cell)
			print("Lifespan: " + species[i].lifespan)
			print("Development: " + species[i].development)
			print("Unique characteristic: " + species[i].unique)
			break
		if ask in species[i].Gname:
			print("Phylogenetic name: " + species[i].Pname)
			print("General name: " + species[i].Gname)
			print("Cell type: " + species[i].cell)
			print("Lifespan: " + species[i].lifespan)
			print("Development: " + species[i].development)
			print("Unique characteristic: " + species[i].unique)
			break
		i = i + 1
	'''
	
def main():
	userInput()
	readData()
	
main()
