#this file was created by Aditya Behal

#super useful video for calculating by hand one way anova test: https://www.youtube.com/watch?v=WUjsSB7E-ko

#importing tkinter to display results
import tkinter as tk

#defining global variables

#3 lists for three different categories of subjects
objectsOld = []	
objectsParkinson = []
objectsYoung = []

#3 lists for three different sample variances
oldVariance = []
parkinsonVariance = []
youngVariance = []

#defining 3 different classes for three different categories of subjects
class OldPatient():
	#initializing class with properties of time, stride, identity, and age
	def __init__(self, time, stride, identity, age):
		self.time = time
		self.stride = stride
		self.identity = identity 
		self.age = age
		
class ParkinsonPatient():
	#initializing class with properties of time, stride, identity, and age
	#age is an interval for Parkinson's patients ranged from 60 - 77 years old
	#average age of the interval (68.5 years) was used
	def __init__(self, time, stride, identity, age):
		self.time = time
		self.stride = stride
		self.identity = identity 
		self.age = age
			
class YoungPatient():
	#initializing class with properties of time, stride, identity, and age
	def __init__(self, time, stride, identity, age):
		self.time = time
		self.stride = stride
		self.identity = identity 
		self.age = age


#defining 3 different functions for 3 different categories of subjects
#reading data from 15 different text files (15 different subjects, 5 in each category)	
#used this resource to learn how to do this: http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#data from this resource: https://www.physionet.org/physiobank/database/gaitdb/	

def oldData():
	
	#using with loop to open up textfile
	with open("o1-76-si.txt") as file:
		#reading all the lines in the textfile and storing it in the variable data
		data = file.readlines()
		#using a for loop for each line in data
		for line in data:
			#splitting lines into two
			data_org = line.split()
			#defining objects with these properties
			obj = OldPatient(0, 0, 1, 76)
			#redefining some of the attributes of the objects
			#elements of data_org array in position 0 are time and position 1 for stride
			obj.time = data_org[0]
			obj.stride = data_org[1]
			#appending objects to objectsOld list
			objectsOld.append(obj)
			
	#same logic for the other 4 textfiles being read in the rest of the with loops	
	with open("o2-74-si.txt") as file:
		data2 = file.readlines()
		for line in data2:
			data_org2 = line.split()
			obj = OldPatient(0, 0, 2, 74)
			obj.time = data_org2[0]
			obj.stride = data_org2[1]
			objectsOld.append(obj)
			
	with open("o3-75-si.txt") as file:
		data3 = file.readlines()
		for line in data3:
			data_org3 = line.split()
			obj = OldPatient(0, 0, 3, 75)
			obj.time = data_org3[0]
			obj.stride = data_org3[1]
			objectsOld.append(obj)	
			
	with open("o4-77-si.txt") as file:
		data4 = file.readlines()
		for line in data4:
			data_org4 = line.split()
			obj = OldPatient(0, 0, 4, 77)
			obj.time = data_org4[0]
			obj.stride = data_org4[1]
			objectsOld.append(obj)
			
	with open("o5-71-si.txt") as file:
		data5 = file.readlines()
		for line in data5:
			data_org5 = line.split()
			obj = OldPatient(0, 0, 5, 71)
			obj.time = data_org5[0]
			obj.stride = data_org5[1]
			objectsOld.append(obj)

#other functions parkinsonData() and youngData() have same structure/logic as the function oldData() above
def parkinsonData():
	with open("pd1-si.txt") as file:
		data = file.readlines()
		for line in data:
			data_org = line.split()
			obj = ParkinsonPatient(0, 0, 1, 68.5)
			obj.time = data_org[0]
			obj.stride = data_org[1]
			objectsParkinson.append(obj)	
			
	with open("pd2-si.txt") as file:
		data2 = file.readlines()
		for line in data2:
			data_org2 = line.split()
			obj = ParkinsonPatient(0, 0, 2, 68.5)
			obj.time = data_org2[0]
			obj.stride = data_org2[1]
			objectsParkinson.append(obj)
			
	with open("pd3-si.txt") as file:
		data3 = file.readlines()
		for line in data3:
			data_org3 = line.split()
			obj = ParkinsonPatient(0, 0, 3, 68.5)
			obj.time = data_org3[0]
			obj.stride = data_org3[1]
			objectsParkinson.append(obj)
				
	with open("pd4-si.txt") as file:
		data4 = file.readlines()
		for line in data4:
			data_org4 = line.split()
			obj = ParkinsonPatient(0, 0, 4, 68.5)
			obj.time = data_org4[0]
			obj.stride = data_org4[1]
			objectsParkinson.append(obj)
			
	with open("pd5-si.txt") as file:
		data5 = file.readlines()
		for line in data5:
			data_org5 = line.split()
			obj = ParkinsonPatient(0, 0, 5, 68.5)
			obj.time = data_org5[0]
			obj.stride = data_org5[1]
			objectsParkinson.append(obj)

#same logic for this function too		
def youngData():
	with open("y1-23-si.txt") as file:
		data = file.readlines()
		for line in data:
			data_org = line.split()
			obj = YoungPatient(0, 0, 1, 23)
			obj.time = data_org[0]
			obj.stride = data_org[1]
			objectsYoung.append(obj)
				
	with open("y2-29-si.txt") as file:
		data2 = file.readlines()
		for line in data2:
			data_org2 = line.split()
			obj = YoungPatient(0, 0, 2, 29)
			obj.time = data_org2[0]
			obj.stride = data_org2[1]
			objectsYoung.append(obj)
			
	with open("y3-23-si.txt") as file:
		data3 = file.readlines()
		for line in data3:
			data_org3 = line.split()
			obj = YoungPatient(0, 0, 3, 23)
			obj.time = data_org3[0]
			obj.stride = data_org3[1]
			objectsYoung.append(obj)
				
	with open("y4-21-si.txt") as file:
		data4 = file.readlines()
		for line in data4:
			data_org4 = line.split()
			obj = YoungPatient(0, 0, 4, 21)
			obj.time = data_org4[0]
			obj.stride = data_org4[1]
			objectsYoung.append(obj)
			
	with open("y5-26-si.txt") as file:
		data5 = file.readlines()
		for line in data5:
			data_org5 = line.split()
			obj = YoungPatient(0, 0, 5, 26)
			obj.time = data_org5[0]
			obj.stride = data_org5[1]
			objectsYoung.append(obj)
	
def statsOPY():
	#sample sizes
	countOld = len(objectsOld)
	countParkinson = len(objectsParkinson)
	countYoung = len(objectsYoung)
	countAll = countOld + countParkinson + countYoung
	
	#averages
	averageO = 0.0
	averageP = 0.0
	averageY = 0.0
	#~ #calculating average of stride interval times for Old 
	
	for x in objectsOld:
		#adding up all the stride interval times 
		averageO = averageO + float(x.stride)
		
	#dividing total by length of old list
	totalO = averageO
	averageO = averageO/len(objectsOld)
	
	#~ #calculating average of stride interval times for Parkinson's
	#~ #same logic for calculating average
	for x in objectsParkinson:
		averageP = averageP + float(x.stride)
	totalP = averageP
	averageP = averageP/len(objectsParkinson)
	
	#~ #calculating average of stride interval times for Young
	#~ #same logic for calculating average
	for x in objectsYoung:
		averageY = averageY + float(x.stride)
	totalY = averageY
	averageY = averageY/len(objectsYoung)
	
	#grand mean
	#Calculating grand mean
	averageG = (totalO + totalP + totalY)/countAll
	
	#k
	k = 3
	
	#SS within
	#Old
	for x in objectsOld:
		oldVariance.append((float(x.stride) - averageO)**2)
	totalOWI = sum(oldVariance)
	#Parkinson
	for x in objectsParkinson:
		parkinsonVariance.append((float(x.stride) - averageP)**2)
	totalPWI = sum(parkinsonVariance)
	#Young
	for x in objectsYoung:
		youngVariance.append((float(x.stride) - averageY)**2)
	totalYWI = sum(youngVariance)
	
	ssWI = totalOWI + totalPWI + totalYWI 
	
	#Mean of SS within
	#Divide of degree of freedom WI
	dFWI = countAll - k
	mssWI = ssWI/dFWI

	#Mean of SS between
	#Old
	mBWO = countOld*(averageO - averageG)**2
	#Parkinson
	mBWP = countParkinson*(averageP - averageG)**2
	#Young
	mBWY = countYoung*(averageY - averageG)**2
	#Total
	mBWT = mBWO + mBWP + mBWY
	#Divide by  degree of freedom BW
	dFBW = k - 1
	mssBW = mBWT/dFBW
	
	#F statistical value = MSSBW/MSSWI
	FS = mssBW/mssWI
	
	#F critical value (predetermined by table of values/Excel based on degrees of Freedom )
	FC = 2.9967142638104
	
	#Checking if null hypothesis (means of groups are the same) is T/F
	print("Conclusion from the One Way ANOVA Test")
	if FS > FC:
		print("The alternate hypothesis that the groups are statistically different is supported.")
		print("Therefore, there is a significant difference, statistically speaking, between the walk gaits of the three groups.")
	else:
		print("The null hypothesis that the groups are statistically the same is supported.")
		print("Therefore, there is not a significant difference, statistically speaking, between the walking gaits of the three groups.")


#tkinter portion to display results in GUI in tabular format
#Code source (and then modified to show my results) courtesy of stack overflow. 
# http://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self, 15, 7)
        #makes cells and packs them against top of screen, and cells only occupy more space horizontally (set to fill only x)
        t.pack(side="top", fill="x")
        #writes text in cell (0,0) 
        t.set(0,0,"Anova: Single Factor")
        t.grid(row=0, column=2, columnspan=3)
        t.set(2,0,"Summary")
        t.set(3,0,"Groups")
        t.set(3,1,"Count")
        t.set(3,2,"Sum")
        t.set(3,3,"Average")
        t.set(3,4,"Variance")
        t.set(4,0,"Old")
        t.set(4,1,"4110")
        t.set(4,2,"4199.101")
        t.set(4,3,"1.02167907542579")
        t.set(4,4,"0.00697924548563806")
        t.set(5,0,"Parkinson")
        t.set(5,1,"1221")
        t.set(5,2,"1389.7859")
        t.set(5,3,"1.13823579033579")
        t.set(5,4,"0.0264168772343901")
        t.set(6,0,"Young")
        t.set(6,1,"3813")
        t.set(6,2,"4198.324")
        t.set(6,3,"1.10105533700498")
        t.set(6,4,"0.0041446598436233")
        t.set(9,0,"ANOVA")
        t.set(10,0,"Source of Variation")
        t.set(10,1,"SS")
        t.set(10,2,"df")
        t.set(10,3,"MS")
        t.set(10,4,"F")
        t.set(10,5,"P-value")
        t.set(10,6,"F crit")
        t.set(11,0,"Between Groups")
        t.set(11,1,"18.9579282414174")
        t.set(11,2,"2")
        t.set(11,3,"9.47896412070869")
        t.set(11,4,"1129.60511246935")
        t.set(11,5,"0")
        t.set(11,6,"2.9967142638104")
        t.set(12,0,"Within Groups")
        t.set(12,1,"76.7057532503411")
        t.set(12,2,"9141")
        t.set(12,3,"0.00839139626412221")
        t.set(14,0,"Total")
        t.set(14,1,"95.6636814917585")
        t.set(14,2,"9143")

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows, columns):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
				#width controls width of tkinter display screen
                label = tk.Label(self, text="", 
                                 borderwidth=0, width=20)
                #padx/y controls cell padding
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)
        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)
    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

#tkinter variable for running function 
#***when defined before class ExampleApp(), error message saying that ExampleApp() isn't defined***
#***therefore, can't put this with the other global variables      
app = ExampleApp()


#defining main function with the three functions being called in it	
def main():
	oldData()
	parkinsonData()
	youngData()
	statsOPY()
	app.mainloop()

#calling main to run program - output is printing of three different lists with different values in each object
main()
