from urllib2 import * 
import csv
import random
import json
import math
import re

listOfCoords = []
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc

def readFromCSV():
	lat = []
	lng = []
	f = open( 'Seattle_Zip_Codes.csv', 'rU' ) #open the file in read universal mode
	for line in f:
	    cells = line.split( "," )
	    lats = re.findall('\d+.\d+',cells[1])
	    latVal = 0
	    longVal = 0
	    for l in lats:
	    	latVal = l
	    longs = re.findall('\d+.\d+',cells[2])
	    for l in longs:
	    	longVal = l
	    # print latVal,longVal
	    zipCode = cells[5]
	    listOfCoords.append((latVal,longVal,zipCode)) #since we want the first, second and third column
	f.close()
	listOfCoords.pop(0)
readFromCSV()

def getZipCode(lat,lng):
	i = 0
	minArc = 0
	lat = float(lat)
	lng = -float(lng)
	for cords in listOfCoords:
		latVal =  float(cords[0])
		longVal = float(cords[1])
		if(i == 0):
			minArc = distance_on_unit_sphere(lat,lng,latVal,longVal)
			i = 1
			zipCode = cords[2]
		else:
			arc = distance_on_unit_sphere(lat,lng,latVal,longVal)
			if(arc < minArc):
				minArc = arc
				zipCode = cords[2]
			
	return zipCode
	
random.seed()


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




#code for Business.
data={}
with open('original/Business.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar="\"")
	i=0
	li =['Corporation', 'LLC*Limited Liability Co', 'Sole Proprietor', 'Partnership', 'LLP*Limited Liability Partners', 'Other', 'Corporation/Nonprofit', 'PLLC*Prof Limited Liability Co', 'Municipal', 'Partnership/Nonprofit']
	
	for row in reader:
			
		zipCode=row["City, State and ZIP"].split()
		zipCode = zipCode[len(zipCode)-1]
		
		
		owner = row["Ownership"]
		index = li.index(owner)
		
		#print zipCode, owner
		
		if "-" in zipCode:
			#print zipCode
			zipCode = zipCode.split("-")[0]
			#print zipCode	
		
		if len(zipCode) > 5:
			zipCode = zipCode[:5]
		if zipCode[:2]!="98":
			continue
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
