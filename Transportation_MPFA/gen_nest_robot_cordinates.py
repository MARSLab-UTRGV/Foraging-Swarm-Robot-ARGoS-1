import pdb
import matplotlib.pyplot as plt
import glob
import os.path
import numpy as np
from pylab import *

def sub_gen_coord(max_x,min_x, k, b):

    x1 = max_x - k/2.0
    y1 = max_y - k/2.0
    coordinates =[]
    for i in range(int(max_x - min_x)/k):
        for j in range(int(max_x - min_x)/k):
            x = x1 -k*i
            y = y1 -k*j
            coordinates.append([x, y])
    #prints coordinates
    return coordinates

arena_width =64

max_x, max_y = arena_width/2.0,  arena_width/2.0;
min_x, min_y = -max_x, -max_y;

#parameters
############################################################
#gaps = [32, 16, 8]
#gaps = [4,2]
gaps = [32, 16, 8,4]
#gaps = [8, 4]
#gaps = [2]
varyCapacity = 0 #0:constant capacity; 1:vary capacity
capacity = 2
varySpeed = 1
quad = 1

if quad:
    shift =arena_width/4.0
else:
    shift =0


if varySpeed:
    speed = 0.16 * pow(arena_width, 0.333)
else:
    speed = 0.16
print('speed=', speed)##############################################################
branch =4
results=[]
for k in gaps:
  print(k)  results.append(sub_gen_coord(max_x, min_x, k, branch))


coord_info =open("coord_for_worldFile.xml", "w")
coord_info_text = open("coord.xml", "w")

#shift = arena_width/4.0

count =1;

for coords in results:
    for xy in coords:
        coord_info.write("NestPosition_" + str(count) +"=\"" + str(xy[0]-shift) + ", " + str(xy[1]-shift)+"\"\n")
        coord_info_text.write(str(xy[0]-shift) + " " + str(xy[1]-shift)+"\n")
        count += 1

coord_info_text.close()


# there is only delivering robots
count = 0

total_robot=0

num_Drobot = 1
forageRate = 110/1800.0
print("forageRate=", forageRate)
delierying_robot =0
foraging_robot =0



if(varyCapacity):
    quantity = 4
else:
    #prints "nest location =[",xy[0],", ",xy[1], "]"
    distance = np.sqrt(2*(gaps[-1]/2.0)**2)
    print("distance=", distance)    #prints "unit=", unit
    print((forageRate*2*distance)/speed)    #quantity = math.ceil((forageRate*2*distance)/speed)
    quantity = round((forageRate*2*distance)/(speed*capacity))
    #quantity = (forageRate*2*distance)/speed
    #prints "2. delivery quantity", quantity
    if quantity == 0:
        quantity = 1
print("# of region delivery robot", quantity)
idx =1
level = len(gaps)
print("quantity=", quantity)print("level=", level)for coords in results[:-1]:
    print("idx=", idx)    for xy in coords:
	print(" nest location =[",xy[0],", ",xy[1], "]")	if(varyCapacity):
	    quantity2 = 4
	else:
            #distance = np.sqrt(2*(gaps[idx]/2.0)**2)
            #prints "distance=", distance
            #quantity = math.ceil((forageRate*2*distance*branch**(level-idx-1))/speed)
            #quantity = (forageRate*2*distance*branch**(level-idx-1))/speed
            quantity2 = quantity*((2*branch)**(level-idx))
            print("measured quantity=", quantity2)            #maxQuantity = round(distance/1.01)
            #prints "maxQuantity=", maxQuantity
            #if quantity > maxQuantity:
            #    quantity = maxQuantity

        print("1. delivery quantity", quantity2)        delierying_robot += quantity2
        total_robot += quantity2
	coord_info.write("<distribute>\n")
        #coord_info.write("<position max=\"" + str(xy[0]+gaps[-1]/6.0)+ ", " + str(xy[1]+gaps[-1]/6.0) + ", 0.0\" method=\"uniform\" min=\"" + str(xy[0]-gaps[-1]/6.0)+ ", " + str(xy[1]-gaps[-1]/6.0) + ", 0.0\"/>\n")
        coord_info.write("<position max=\"" + str(xy[0]-shift+gaps[-1]/6.0)+ ", " + str(xy[1]-shift+gaps[-1]/6.0) + ", 0.0\" method=\"uniform\" min=\"" + str(xy[0]-shift-gaps[-1]/6.0)+ ", " + str(xy[1]-shift-gaps[-1]/6.0) + ", 0.0\"/>\n")
        coord_info.write("<orientation mean=\"0, 0, 0\" method=\"gaussian\" std_dev=\"360, 0, 0\"/>\n")
        coord_info.write("<entity max_trials=\"100\" quantity=\"" +str(int(quantity2)) +"\">\n")
        coord_info.write("<foot-bot id=\"D" + str(count)+ "-" + "\"><controller config=\"MPFA\"/></foot-bot>\n")
        coord_info.write("</entity>\n")
        coord_info.write("</distribute>\n\n")
        count += 1
    idx += 1

# there are foraging and delivering robots in each region
for xy in results[-1]:
    coord_info.write("<distribute>\n")
    #coord_info.write("<position max=\"" + str(xy[0]-shift+0.5)+ ", " + str(xy[1]-shift+0.5) + ", 0.0\" method=\"uniform\" min=\"" + str(xy[0]-shift)+ ", " + str(xy[1]-shift) + ", 0.0\"/>\n")
    coord_info.write("<position max=\"" + str(xy[0]-shift+gaps[-1]/6.0)+ ", " + str(xy[1]-shift+gaps[-1]/6.0) + ", 0.0\" method=\"uniform\" min=\"" + str(xy[0]-shift-gaps[-1]/6.0)+ ", " + str(xy[1]-shift-gaps[-1]/6.0) + ", 0.0\"/>\n")
    coord_info.write("<orientation mean=\"0, 0, 0\" method=\"gaussian\" std_dev=\"360, 0, 0\"/>\n")
    coord_info.write("<entity max_trials=\"100\" quantity=\"4\">\n")
    coord_info.write("<foot-bot id=\"F" + str(count)+ "-" + "\"><controller config=\"MPFA\"/></foot-bot>\n")
    coord_info.write("</entity>\n")
    coord_info.write("</distribute>\n\n")

    coord_info.write("<distribute>\n")
    #coord_info.write("<position max=\"" + str(xy[0]-shift+gaps[-1]/6.0)+ ", " + str(xy[1]-shift+gaps[-1]/6.0) + ", 0.0\" method=\"uniform\" min=\"" + str(xy[0]-shift-gaps[-1]/6.0)+ ", " + str(xy[1]-shift-gaps[-1]/6.0) + ", 0.0\"/>\n")
    coord_info.write("<position max=\"" + str(xy[0]-shift+gaps[-1]/6.0)+ ", " + str(xy[1]-shift+gaps[-1]/6.0) + ", 0.0\" method=\"uniform\" min=\"" + str(xy[0]-shift-gaps[-1]/6.0)+ ", " + str(xy[1]-shift-gaps[-1]/6.0) + ", 0.0\"/>\n")
    coord_info.write("<orientation mean=\"0, 0, 0\" method=\"gaussian\" std_dev=\"360, 0, 0\"/>\n")
    coord_info.write("<entity max_trials=\"100\" quantity=\""  + str(int(quantity))  +  "\">\n")
    coord_info.write("<foot-bot id=\"D" + str(count)+ "-" + "\"><controller config=\"MPFA\"/></foot-bot>\n")
    coord_info.write("</entity>\n")
    coord_info.write("</distribute>\n\n")
    count += 1

    delierying_robot += quantity
    foraging_robot += 4
    total_robot += 4+quantity

print("foraging_robot=", foraging_robot)print("deliverying_robot=", delierying_robot)print("total robot =", total_robot)print(total_robot == delierying_robot+foraging_robot)coord_info.close()



#for coords in results[:-1]:
#    for xy in coords:

#	coord_info.write("<distribute>\n")
#	coord_info.write("<position method=\"grid\"\n")
#	coord_info.write("center=\"" + str(xy[0])+ ", " + str(xy[1])+ ", 0.0\"\n")
#	coord_info.write("distances=\"0.3, 0.3, 0.0\"\n")
#	coord_info.write("layout=\"2, 1, 1\" />\n")
#	coord_info.write("<orientation method=\"constant\" values=\"0.0, 0.0, 0.0\"/>\n")
#	coord_info.write("<entity quantity=\"2\" max_trials=\"100\">\n")
#	coord_info.write("<foot-bot id=\"D" + str(count) + "\">\n")
#	coord_info.write("<controller config=\"MPFA\"/>\n")
#	coord_info.write("</foot-bot>\n")
#	coord_info.write("</entity>\n")
#	coord_info.write("</distribute>\n\n")
#	count += 1

## there are foraging and delivering robots in each region
#for xy in results[-1]:
#	coord_info.write("<distribute>\n")
#	coord_info.write("<position method=\"grid\"\n")
#	coord_info.write("center=\"" + str(xy[0])+ ", " + str(xy[1])+ ", 0.0\"\n")
#	coord_info.write("distances=\"0.3, 0.3, 0.0\"\n")
#	coord_info.write("layout=\"2, 2, 1\" />\n")
#	coord_info.write("<orientation method=\"constant\" values=\"0.0, 0.0, 0.0\"/>\n")
#	coord_info.write("<entity quantity=\"4\" max_trials=\"100\">\n")
#	coord_info.write("<foot-bot id=\"F" + str(count) + "\">\n")
#	coord_info.write("<controller config=\"MPFA\"/>\n")
#	coord_info.write("</foot-bot>\n")
#	coord_info.write("</entity>\n")
#	coord_info.write("</distribute>\n\n")


#	coord_info.write("<distribute>\n")
#	coord_info.write("<position method=\"grid\"\n")
#	coord_info.write("center=\"" + str(xy[0])+ ", " + str(xy[1]+0.5)+ ", 0.0\"\n")
#	coord_info.write("distances=\"0.3, 0.3, 0.0\"\n")
#	coord_info.write("layout=\"2, 1, 1\" />\n")
#	coord_info.write("<orientation method=\"constant\" values=\"0.0, 0.0, 0.0\"/>\n")
#	coord_info.write("<entity quantity=\"2\" max_trials=\"100\">\n")
#	coord_info.write("<foot-bot id=\"D" + str(count) + "\">\n")
#	coord_info.write("<controller config=\"MPFA\"/>\n")
#	coord_info.write("</foot-bot>\n")
#	coord_info.write("</entity>\n")
#	coord_info.write("</distribute>\n\n")
#	count += 1
