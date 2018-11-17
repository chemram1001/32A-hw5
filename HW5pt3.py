# Assignment 5
# Ramces Gonzalez
# Nov 15, 2018
# function that reads population file and builds dictionary
import csv
def makePopDictionary():
	# read data from file world_population_2017.tsv
	file = open('world_population_2017.tsv','r')
	popDictionary = {}
	for i in range(238):
		line = file.readline()
		line = line.strip()
		data = line.split("\t")
		rowNum = data[0]
		countryName = data[1]
		pop = data[2].replace(",","") # replace() removes "," from numbers
		pop = int(pop)
		popDictionary[countryName] = pop
		#print(countryName,pop)
	print(popDictionary)
	return {}

# function that reads drinking water file and prints out
# countries that have changed percentage of people with
# access, if population is big enough.
def readDWdata(D):
	csvfile = open('drinkingWater.csv','r')
	file = csv.reader(csvfile,delimiter=',')
	print("Country 1990 2010 Change")
	for key in D:
		print(D[key])
	for row in file:
		if row[1] == "" or row[21] == '':
			pass
		elif row[0]=='(home)':
			pass
		else:
			data1990 = row[1]
			data2010 = row[21]
			data1990 = int(data1990)
			data2010 = int(data2010)
			diff = data2010 - data1990
			print(row[0],row[1],row[21],diff)
	return

def main():
	#makePopDictionary()
	readDWdata(makePopDictionary())
	return
main()
