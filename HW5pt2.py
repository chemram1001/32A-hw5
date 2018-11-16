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
	#print(popDictionary)
	return {}

# function that reads drinking water file and prints out
# countries that have changed percentage of people with
# access, if population is big enough.
def readDWdata():
	csvfile = open('drinkingWater.csv','r')
	file = csv.reader(csvfile,delimiter=',')
	for row in file:
		country = row[0]
		if row[1].isdigit() and row[21].isdigit():
			data1990 = int(row[1])
			data2010 = int(row[21])
			diff = data2010 - data1990
			print(country, data1990, data2010, diff)
	return

def main():
	makePopDictionary()
	readDWdata()
	return
main()
