from urllib2 import * 
import csv
import random
import json


def getZipCode(lat, lon):
	return random.randrange(10)
	


random.seed()
#code to handle burglary..
data={}

with open('original/Burglary_Map.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar="\"")
	i=0
	for row in reader:
		
		lat = row["Latitude"]	
		log = row["Longitude"]
		
		zipCode=getZipCode(lat,log)
		
		isFalse = True
		
		if row["Event Clearance Group"] == "BURGLARY":
			isFalse = False
		
		#each tuple will have (false alarms, burglaries)
		if zipCode in data:
			tup = data[zipCode]
			
			if isFalse:
				data[zipCode] = (tup[0]+1, tup[1])
			else:
				data[zipCode] = (tup[0], tup[1]+1)
		else:
			if isFalse:
				data[zipCode] = (1,0)
			else:
				data[zipCode] = (0,1)
				
	f2 = open("pruned/burglery.csv","w")			
	f2.write('"zip", "False Alarms", "Burglary"\n')
	for key in data:
		tup=data[key]
		f2.write(str(key)+","+str(tup[0])+","+str(tup[1])+"\n")
	
	f2.close()


#code for crimes..
data={}
with open('original/Crime_Map.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar="\"")
	i=0
	for row in reader:
		
		lat = row["Latitude"]	
		log = row["Longitude"]
		
		zipCode=getZipCode(lat,log)
		
		#each item will have count of crimes for a zip code..
		if zipCode in data:
			data[zipCode] = data[zipCode]+1
			
		else:
			data[zipCode] = 1
	
	f2 = open("pruned/crime.csv","w")
	f2.write('"zip", "Crime"\n')			
	for key in data:
		tup=data[key]
		f2.write(str(key)+","+str(tup)+"\n")
	
	f2.close()


#code for public and private schools
data={}
with open('original/public_and_private_schools.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar="\"")
	i=0
	for row in reader:
			
		zipCode=row["ZIP"]
		
		#each item will have count of crimes for a zip code..
		if zipCode in data:
			data[zipCode] = data[zipCode]+1
			
		else:
			data[zipCode] = 1
	
	f2 = open("pruned/schools.csv","w")			
	f2.write('"zip", "Schools"\n')
	for key in data:
		tup=data[key]
		f2.write(str(key)+","+str(tup)+"\n")
	
	f2.close()

#code for neighborhood
data={}
with open('original/neighbor.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar="\"")
	i=0
	
	cols = ["Landmarks", "Parks", "Libraries", "High Schools", "Traffic Cameras", "Picnic Sites", "Childrens Play Areas", "Hospitals"]
	
	for row in reader:
			
		feature=row["City Feature"]
		
		if feature in cols:
			zipCode = getZipCode(row["Latitude"] , row["Longitude"])
			index = cols.index(feature)
			
			if zipCode in data:
				r = data[zipCode]
				r[index] = r[index]+1
				data[zipCode] = r
			else:
				r = [0 for i in range(len(cols))]
				r[index] = 1
				data[zipCode] = r
	
	f2 = open("pruned/general.csv","w")
	
	cols = [ "\""+s+"\"" for s in cols]	
	f2.write("\"zip\""+",".join(cols)+"\n")			
	for key in data:
		tup=data[key]
		tup = [str(x) for x in tup]
		f2.write(str(key)+","+ ",".join(tup)+"\n")
	
	f2.close()


#code for prostituition.
data={}
with open('original/Prostitution_Map.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar="\"")
	i=0
	for row in reader:
			
		zipCode=getZipCode(row["Latitude"], row["Longitude"])
		
		#each item will have count of crimes for a zip code..
		if zipCode in data:
			data[zipCode] = data[zipCode]+1		
		else:
			data[zipCode] = 1
	
	f2 = open("pruned/prost.csv","w")	
	f2.write('"zip", "Prost"')
			
	for key in data:
		tup=data[key]
		f2.write(str(key)+","+str(tup)+"\n")
	
	f2.close()


#code for Business.
data={}
with open('original/Business.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar="\"")
	i=0
	li =['Corporation', 'LLC*Limited Liability Co', 'Sole Proprietor', 'Partnership', 'LLP*Limited Liability Partners', 'Other', 'Corporation/Nonprofit', 'PLLC*Prof Limited Liability Co', 'Municipal', 'Partnership/Nonprofit']
	
	for row in reader:
			
		zipCode=row["City, State and ZIP"].split()
		zipCode = zipCode[len(zipCode)-1]
		
		#print zipCode
		owner = row["Ownership"]
		index = li.index(owner)
		
		#print zipCode, owner
		
		if "-" in zipCode:
			print zipCode
			zipCode = zipCode.split("-")[0]
			print zipCode	
		
		if len(zipCode) > 5:
			zipCode = zipCode[:5]
				
		#each item will have count of crimes for a zip code..
		if zipCode in data:
			r = data[zipCode]
			r[index] = r[index]+1			
			data[zipCode] = r		
		else:
			data[zipCode] = [0 for i in range(len(li))]
			data[zipCode][index] = 1
	
	f2 = open("pruned/business.csv","w")
	li = [ "\""+s+"\"" for s in li]			
	f2.write("\"zip\""+","+",".join(li)+"\n")
	for key in data:
		tup=data[key]
		tup = [str(x) for x in tup]
		f2.write(str(key)+","+",".join(tup)+"\n")
	
	f2.close()

			
'''
f = open("original/","r")
lines = f.readlines()
f.close()
'''
