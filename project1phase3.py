#braden miller (bmiller38)
#CS1 Fundamentals
#Project 1 Phase 3
#Date: 4/12/2023

import random
# ===PHASE 1 ======#
def extractCityStateNames(line):
    pieces = line.split(",")
    return pieces[0] + pieces[1][:3]


def extractCoordinates(line):
    pieces = line.split(",")
    return [int(pieces[1].split("[")[1]), int(pieces[2].split("]")[0])]

def extractPopulation(line):
    pieces = line.split(",")
    return int(pieces[2].split("]")[1])


def loadData(cityList, coordList, popList, distanceList):
    f = open("miles.dat")
    cityIndex = 0
    distances = []
    distanceList.append([])
    for line in f:
        if line[0].isalpha():
            if distances != []:
                distanceList.append(distances[::-1])
                distances = []
            
            cityList.append(extractCityStateNames(line))
            coordList.append(extractCoordinates(line))
            popList.append(extractPopulation(line))
            cityIndex = cityIndex + 1       
        elif line[0].isdigit():
            distances.extend([int(x) for x in line.split()])
        
    if distances != []:
        distanceList.append(distances[::-1])
            
def getCoordinates(cityList, coordList, name):
    return coordList[cityList.index(name)]


def getPopulation(cityList, popList, name):
    return popList[cityList.index(name)]

def getDistance(cityList, distanceList, name1, name2):
    index1 = cityList.index(name1)

    index2 = cityList.index(name2)

    if index1 == index2:
          return 0
    elif index1 < index2:

        return distanceList[index2][index1]
    else:

        return distanceList[index1][index2]
    

def nearbyCities(cityList, distanceList, name, r):
    result = []
    i = cityList.index(name)  
    j = 0
    for d in distanceList[i]:      # For every other previous city
        if d <= r :      # If within r of named city
            result = result + [cityList[j]]  # Add to result
        j = j + 1   
    j = i + 1
    while (j < len(distanceList)): # For every other previous city
        if distanceList[j][i] <= r: # If within r of named city
            result = result + [cityList[j]] # Add to result
        j = j + 1     
    return result

# PHASE 2 ####_____######

def locateFacilities(cityList, distanceList, r):
    served = [False] * len(cityList)
    facilities = []
    while not all(served):
        bestFacilityI = possibleFacilities(cityList, distanceList, r, served, facilities)
        facilities += [cityList[bestFacilityI]]
        served[bestFacilityI] = True
        nearServingCities = nearbyCities(cityList, distanceList, cityList[bestFacilityI], r)
        for city in nearServingCities:
            served[cityList.index(city)] = True
    return facilities

def possibleFacilities(cityList, distanceList, r, served, facilities):
    nearbyCity = []
    inRange = [0] * len(cityList)
    for i in range(len(cityList)):
        if cityList[i] not in facilities:
            nearbyCity = nearbyCities(cityList, distanceList, cityList[i], r)
        if served[i] == False:
            counter = 1
        else:
            counter = 0
        for city in nearbyCity:
            if served[cityList.index(city)] == False:
                counter += 1
        inRange[i] = counter
        i += 1
    best = max(inRange) 
    bestFacilityIndex = inRange.index(best)
    return bestFacilityIndex

# =PHASE 3 ####++++#######

#random lines
def createLineStyle(name, width, color): 
    r =  "<Style id=\"" + name+ "\">\n"
    r += "  <LineStyle>\n"
    r += "    <color>"+ color +"</color>\n"
    r += "    <width>"+ width + "</width>\n"
    r += "  </LineStyle>\n"
    r += "</Style>"
    return r

#create the lines between city and facility
def createEdges(name, desc, style, coordCity1, coordcity2): 
    r =  ""
    r += "<Placemark>\n"
    r += "   <name>" + name + "</name>\n"
    r += "   <description>" + desc + "</description>\n"
    if (len(style) > 0):
        r += "   <styleUrl>#" + style + "</styleUrl>\n"
    r += "   <LineString>\n"
    r += "     <coordinates>" + coordCity1 + "," + coordcity2 + "</coordinates>\n"
    r += "   </LineString>\n"
    r += "</Placemark>"
    return r

#create facility point using star image from google earth
def createFacilityPoint(name, desc, coords): 
    long = float(coords[1]/100)*-1
    lat = float(coords[0]/100)
    r = ""
    r += "<Placemark>\n"
    r += " <name>"+name+"</name>\n"
    r += " <Style>\n"
    r += "    <IconStyle>\n"
    r += "        <color>ff0080ff</color>\n"
    r += "        <scale>1.2</scale>\n"
    r += "        <Icon>\n"
    r += "           <href>https://www.gstatic.com/earth/images/stockicons/190201-2006-shape_star_4x.png</href>\n"
    r += "        </Icon>\n"
    r += "   </IconStyle>\n"
    r += "   <LabelStyle>\n"
    r += "       <color>ff0080ff</color>\n"
    r += "   </LabelStyle>\n"
    r += " </Style>"
    r += " <description>"+desc+"</description>\n"
    r += " <Point>\n"
    r += "  <coordinates>"+ str(long) + ","+ str(lat) + ",0" +"</coordinates>\n"
    r += " </Point>\n"
    r += "</Placemark>"
    return r

#create city points using placemark image from google earth
def createCityPoint(name, desc, coords): 
    long = float(coords[1]/100)*-1
    lat = float(coords[0]/100)
    r = ""
    r += "<Placemark>\n"
    r += " <name>"+name+"</name>\n"
    r += " <Style>\n"
    r += "    <IconStyle>\n"
    r += "        <color>ffff8888</color>\n"
    r += "        <scale>0.8</scale>\n"
    r += "        <Icon>\n"
    r += "           <href>https://www.gstatic.com/earth/images/stockicons/190201-2000-shape_default_4x.png</href>\n"
    r += "        </Icon>\n"
    r += "   </IconStyle>\n"
    r += "   <LabelStyle>\n"
    r += "       <color>ffB45A14</color>\n"
    r += "   </LabelStyle>\n"
    r += " </Style>"
    r += " <description>"+desc+"</description>"
    r += " <Point>\n"
    r += "  <coordinates>"+ str(long) + ","+ str(lat) + ",0" +"</coordinates>\n"
    r += " </Point>\n"
    r += "</Placemark>"
    return r

#choose a random style
def randomStyle(): 
    list = ["yellowLine", "redLine", "greenLine", "blueLine", "purpleLine"]
    style = random.choice(list)
    return style

#description for styles in kml
def style_desc(style):
    styleList = ["yellowLine", "redLine", "greenLine", "blueLine", "purpleLine"]
    dl = ["yellow line", "red line", "green line", "blue line", "purple line"]
    index = styleList.index(style)
    return dl[index]
    
def display(facilities, cityList, distanceList, coordList, r): 
    
    #open file accounting for either 300 or 800, renames correctly
    fileName = "visualization" + str(r) + ".kml"
    
    earth = open(fileName, "w") 

    #file header 
    earth.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    earth.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n")
    earth.write("<Document>\n\n")

    #creating styles y,r,g,b,p
    yellowLine = createLineStyle("yellowLine", "2.5", "7f00ffff")
    redLine = createLineStyle("redLine", "2.5", "7f1400FA")
    greenLine = createLineStyle("greenLine", "2.5", "7f14F01E")
    blueLine = createLineStyle("blueLine", "2.5", "7fF0E614")
    purpleLine = createLineStyle("purpleLine", "2.5", "7f782878")
    earth.write(yellowLine)
    earth.write("\n\n")
    earth.write(redLine)
    earth.write("\n\n")
    earth.write(greenLine)
    earth.write("\n\n")
    earth.write(blueLine)
    earth.write("\n\n")
    earth.write(purpleLine)

    #creating points for facilities 
    for facility in facilities:
        earth.write("\n\n")
        name = facility
        desc = facility
        cityIndex = cityList.index(facility)
        coords = coordList[cityIndex]
        cityKML = createFacilityPoint(name, desc, coords)
        earth.write(cityKML)
    #creating points for cities that get served
    for city in cityList:
        if (city not in facilities):
            earth.write("\n\n")
            name = city
            desc = city
            cityIndex = cityList.index(city)
            coords = coordList[cityIndex]
            cityKML = createCityPoint(name, desc, coords)
            earth.write(cityKML)

    
    #createEdges for the lines between facillities and cities
    list = [city for city in cityList if city not in facilities]
    count = 0
    for city in list:
        closestDistance = float('inf')
        for facility in facilities:
            newDist = getDistance(cityList, distanceList, city, facility)
            #check if its already been hit by another facility
            if (newDist < closestDistance):
                closestDistance = newDist
                bestFacility = facility
                count += 1
        closestFacility = bestFacility
        #do coords and send to functions
        rawCity = getCoordinates(cityList, coordList, city)
        rawFacility = getCoordinates(cityList, coordList, closestFacility)
        realCity = '-' + str(rawCity[1]/100) +',' + str(rawCity[0]/100) + ',0'
        realFacility = '-' + str(rawFacility[1]/100) +',' + str(rawFacility[0]/100) + ',0'
        name = city + " to " + closestFacility        
        style = randomStyle()
        desc = 'A ' + style_desc(style) + ' from ' + name
        createLine = createEdges(name, desc, style, realCity, realFacility)
        earth.write(createLine)
        earth.write("\n\n")

    #end of first file
    earth.write("\n</Document>\n")
    earth.write("</kml>")
    #
    earth.close()

# # # # # # # # # # # # # # #main program###
cityList = []
coordList = []
popList = []
distanceList = []
r1 = 300
r2 = 800
loadData(cityList, coordList, popList, distanceList)

facilities = locateFacilities(cityList, distanceList, r1)
display(facilities, cityList, distanceList, coordList, r1)

facilities = locateFacilities(cityList,distanceList,r2)
display(facilities,cityList,distanceList,coordList,r2)
