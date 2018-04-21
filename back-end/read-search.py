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

	c = 0
	while c != len(phylums):
		if ask in phylums[c].Pname:
			print("Phylogenetic name: " + phylums[c].Pname)
			print("General name: " + phylums[c].Gname)
			print("Cell type: " + phylums[c].cell)
			print("Lifespan: " + phylums[c].lifespan)
			print("Development: " + phylums[c].development)
			print("Unique characteristic: " + phylums[c].unique)
		if ask in phylums[c].Gname:
			print("Phylogenetic name: " + phylums[c].Pname)
			print("General name: " + phylums[c].Gname)
			print("Cell type: " + phylums[c].cell)
			print("Lifespan: " + phylums[c].lifespan)
			print("Development: " + phylums[c].development)
			print("Unique characteristic: " + phylums[c].unique)	
			break
		c = c + 1
	
	d = 0	
	while d != len(classes):
		if ask in classes[d].Pname:
			print("Phylogenetic name: " + classes[d].Pname)
			print("General name: " + classes[d].Gname)
			print("Cell type: " + classes[d].cell)
			print("Lifespan: " + classes[d].lifespan)
			print("Development: " + classes[d].development)
			print("Unique characteristic: " + classes[d].unique)
		if ask in classes[d].Gname:
			print("Phylogenetic name: " + classes[d].Pname)
			print("General name: " + classes[d].Gname)
			print("Cell type: " + classes[d].cell)
			print("Lifespan: " + classes[d].lifespan)
			print("Development: " + classes[d].development)
			print("Unique characteristic: " + classes[d].unique)
		d = d + 1
	
	e = 0		
	while e != len(orders):
		if ask in orders[e].Pname:
			print("Phylogenetic name: " + orders[e].Pname)
			print("General name: " + orders[e].Gname)
			print("Cell type: " + orders[e].cell)
			print("Lifespan: " + orders[e].lifespan)
			print("Development: " + orders[e].development)
			print("Unique characteristic: " + orders[e].unique)
			break
		if ask in orders[e].Gname:
			print("Phylogenetic name: " + orders[e].Pname)
			print("General name: " + orders[e].Gname)
			print("Cell type: " + orders[e].cell)
			print("Lifespan: " + orders[e].lifespan)
			print("Development: " + orders[e].development)
			print("Unique characteristic: " + orders[e].unique)
			break
		e = e + 1
		
	f = 0	
	while f != len(families):
		if ask in families[f].Pname:
			print("Phylogenetic name: " + families[f].Pname)
			print("General name: " + families[f].Gname)
			print("Cell type: " + families[f].cell)
			print("Lifespan: " + families[f].lifespan)
			print("Development: " + families[f].development)
			print("Unique characteristic: " + families[f].unique)
			break
		if ask in families[f].Gname:
			print("Phylogenetic name: " + families[f].Pname)
			print("General name: " + families[f].Gname)
			print("Cell type: " + families[f].cell)
			print("Lifespan: " + families[f].lifespan)
			print("Development: " + families[f].development)
			print("Unique characteristic: " + families[f].unique)
			break
		f = f + 1
	
	g = 0
	while g != len(genera):
		if ask in genera[g].Pname:
			print("Phylogenetic name: " + genera[g].Pname)
			print("General name: " + genera[g].Gname)
			print("Cell type: " + genera[g].cell)
			print("Lifespan: " + genera[g].lifespan)
			print("Development: " + genera[g].development)
			print("Unique characteristic: " + genera[g].unique)
			break
		if ask in genera[g].Gname:
			print("Phylogenetic name: " + genera[g].Pname)
			print("General name: " + genera[g].Gname)
			print("Cell type: " + genera[g].cell)
			print("Lifespan: " + genera[g].lifespan)
			print("Development: " + genera[g].development)
			print("Unique characteristic: " + genera[g].unique)
			break
		g = g + 1
		
	h = 0	
	while h != len(species):
		if ask in species[h].Pname:
			print("Phylogenetic name: " + species[h].Pname)
			print("General name: " + species[h].Gname)
			print("Cell type: " + species[h].cell)
			print("Lifespan: " + species[h].lifespan)
			print("Development: " + species[h].development)
			print("Unique characteristic: " + species[h].unique)
			break
		if ask in species[h].Gname:
			print("Phylogenetic name: " + species[h].Pname)
			print("General name: " + species[h].Gname)
			print("Cell type: " + species[h].cell)
			print("Lifespan: " + species[h].lifespan)
			print("Development: " + species[h].development)
			print("Unique characteristic: " + species[h].unique)
			break
		h = h + 1
	
def main():
	readData()
	userInput()
	
main()
