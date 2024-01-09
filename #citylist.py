#citylist
        # if("A" <= line[0] and (line[0] <= "Z")):  #these 3 are always in the same line so can stay inside if
        #     i = 0
        #     while(line[i] != ","):
        #         i = i+1
        #     cityName = line[:i]
        #     stateName = line[i+2:i+4]
        #     cityList.append(cityName + " " + stateName)
        #     #population
        #     j = 0 
        #     while(line[j] != "]"):
        #         j = j+1
        #     popList.append(line[j+1:])
        #     #coords
        #     match = re.search(r'\[(\d+),(\d+)\]',line)
        #     x =[]
        #     if match:
        #         x.append(int(match.group(1)))
        #         x.append(int(match.group(2)))
        #         coordList.append(x)
        # else:
        #     pass


# total = line.split(",")
#             cityList = total[0] + total[1].split("[")[0]
            
#             coordList = [int(total[1].split("[")[1]), int(total[2].split("]")[0])]

#             popList = int(total[2].split("]")[1])





# count = 0
#     add = 0
#     f = open("miles.dat")
#     for line in f:
#         #citylist
#         if("A" <= line[0] and (line[0] <= "Z")):  #these 3 are always in the same line so can stay inside if
#             i = 0
#             count = count +1
#             while(line[i] != ","):
#                 i = i+1
#             cityName = line[:i]
#             stateName = line[i+2:i+4]
#             cityList.append(cityName + " " + stateName)
#             #population
#             j = 0 
#             while(line[j] != "]"):
#                 j = j+1
#             popList.append(line[j+1:])
#             #coords
#             match = re.search(r'\[(\d+),(\d+)\]',line)
#             x =[]
#             if match:
#                 x.append(int(match.group(1)))
#                 x.append(int(match.group(2)))
#                 coordList.append(x)
#         else:
#             while(add < count):
#                 spl = line.split(" ")
#                 distanceList.append(spl[add])
#                 add = add + 1




# add = 0
#             tempList = []
#             spl = line.split()
#             while(add < count and add < len(spl)):
#                 if not distanceList:
#                     distanceList.append([])
#                 tempList.append(int(spl[add]))
#                 add = add + 1
#             distanceList.append(tempList)
            

#         for sublist in distanceList:
#             sublist.reverse()

# CHECKs

# cityList = []
# coordList = []
# popList = []
# distanceList = []
# name1 = "Salinas CA"
# name2 = "Yankton SD"
# r = 1000

# loadData(cityList,coordList,popList,distanceList)
# print(cityList)
# print(distanceList[3][0])
# print(cityList[0])
# print(getDistance(cityList,distanceList,name1,name2))
# print(nearbyCities(cityList,distanceList,name2,r))
# print(getPopulation(cityList,popList, name1))
# print(getCoordinates(cityList,coordList,name1))
# if tempList:
#                 if not distanceList:
#                     distanceList.append([])
#                 distanceList.append(tempList)
#                 tempList = []

# elif line[0].isdigit():
#             add = 0
#             spl = line.split()
#             while add < count and add < len(spl):
#                 tempList.append(int(spl[add]))
#                 add += 1

# # append the last tempList to distanceList
#     if tempList:
#         if not distanceList:
#             distanceList.append([])
#         distanceList.append(tempList)

#     for sublist in distanceList:
#         sublist.reverse()