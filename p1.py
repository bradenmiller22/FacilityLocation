import re

def loadData(cityList, coordList, popList, distanceList):
    count = 0
    f = open("miles.dat")
    tempList =[]
    for line in f:
        #citylist
        if("A" <= line[0] and (line[0] <= "Z")):  #these 3 are always in the same line so can stay inside if
            i = 0
            count = count +1
            while(line[i] != ","):
                i = i+1
            cityName = line[:i]
            stateName = line[i+2:i+4]
            cityList.append(cityName + " " + stateName)
            #population
            j = 0 
            while(line[j] != "]"):
                j = j+1
            popList.append(int(line[j+1:]))
            #coords
            match = re.search(r'\[(\d+),(\d+)\]',line)
            x =[]
            if match:
                x.append(int(match.group(1)))
                x.append(int(match.group(2)))
                coordList.append(x)
        # update distanceList with concatenated distance values
            if tempList:
                if not distanceList:
                    distanceList.append([])
                distanceList.append(tempList)
                tempList = []

        elif line[0].isdigit():
            add = 0
            spl = line.split()
            while add < count and add < len(spl):
                tempList.append(int(spl[add]))
                add += 1

# append the last tempList to distanceList
    if tempList:
        if not distanceList:
            distanceList.append([])
        distanceList.append(tempList)

    for sublist in distanceList:
        sublist.reverse()
            
    
       


def getCoordinates(cityList, coordList, name):
    index = cityList.index(name)

    coord = coordList[index]

    return coord   


def getPopulation(cityList, popList, name):
    index = cityList.index(name)
    pop = popList[index]
    return pop

def getDistance(cityList, distanceList, name1, name2):
    index1 = cityList.index(name1)
    index2 = cityList.index(name2)
    
    # print(index2)
    if(index1 == index2):
        distance =  0
    elif(index2 > index1):
        distance = distanceList[index2][index1]
    else:
        distance = distanceList[index1][index2]
    return distance

def nearbyCities(cityList, distanceList, name, r):
    index = cityList.index(name)

    result = []

    for i in range(index):
        if i >= len(distanceList[index]):
            continue
        if distanceList[index][i] <= r:
            result.append(cityList[i])
    
    # Check cities after named city
    for i in range(index + 1, len(cityList)):
        if index >= len(distanceList[i]):
            continue
        if distanceList[i][index] <= r:
            result.append(cityList[i])
    
    return result

