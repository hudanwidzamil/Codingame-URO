import sys
import math
import random
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
link1=[]
link2=[]
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    link1.append(zone_1)
    link2.append(zone_2)

p0base=-1
p1base=-1

def move(p):
    movable=[]
    for i in range (len(link1)):
        if p==link1[i]:
            movable.append(link2[i])
    for i in range (len(link1)):
        if p==link2[i]:
            movable.append(link1[i])
    return movable
# game loop
while True:
    visiblezone=[]
    pods=[]
    my_platinum = int(input())  # your available Platinum
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        if visible==1:
            visiblezone.append(z_id)
            if p1base == -1 and owner_id ==1:
                p1base = z_id
        if pods_p0>0:
            pods.append([z_id,pods_p0])
            if p0base == -1:
                p0base=z_id
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    #print(link1,file=sys.stderr)
    #print(link2,file=sys.stderr)
    #print(pods,file=sys.stderr)
    print(pods_p0,file=sys.stderr)
    print(pods_p1,file=sys.stderr)
    
  
    
    #print("10"+" "+str(pods[0])+" "+str(max(availablemove)))
    for i in range(len(pods)):
        availablemove=random.choice(move(pods[i][0]))
        print(str(pods[i][1])+" "+str(pods[i][0])+" "+str(availablemove))
               
           
    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    print("WAIT")
    #print("WAIT")
