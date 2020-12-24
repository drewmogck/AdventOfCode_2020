# -*- coding: utf-8 -*-
"""
Advent of Code 2020
Day 24
"""

#import data        
Lines = [line.rstrip() for line in open('Day24.txt')]

tiles={}

#e or w alone = +/-2 in E/W direction, 0 in N/S
#ne/se or nw/sw= +/-1 in E/W direction, 1 in N/S based on hex pattern

#line='nwwswee'

start_position = [0,0]

def direction(heading, posx, posy):
    if heading=='e':
        posx+=2
    elif heading=='w':
        posx-=2
    elif heading=='ne':
        posx+=1
        posy+=1
    elif heading=='nw':
        posx-=1
        posy+=1
    elif heading=='se':
        posx+=1
        posy-=1
    elif heading=='sw':
        posx-=1
        posy-=1
    return(posx, posy)


def get_map(line):
    posx= start_position[0]
    posy= start_position[1]
    
    map_dir={}
    dir_count=0
    skip_next=False
    
    for dir in line: 
        if dir=='n' or dir=='s':
            skip_next=True
            map_dir[dir_count]=dir
            
        elif dir=='e' or dir=='w':
            if skip_next==True:
                map_dir[dir_count]=map_dir[dir_count]+dir
                skip_next=False
            else:
                map_dir[dir_count]=dir
                
            dir_count+=1
            
    for d in map_dir:
        posx, posy = direction(map_dir[d], posx, posy)
        
    return(posx, posy)

#print(get_map(line))
    
def flip(posx,posy): #1 is black, 0 is white
    if (posx, posy) in tiles:
        if tiles[(posx, posy)]==1:
           tiles[(posx, posy)]=0
        elif tiles[(posx, posy)]==0:
            tiles[(posx,posy)]=1
    else:
        tiles[(posx, posy)]=1

for line in Lines:
    flip(get_map(line)[0], get_map(line)[1])
    
print(sum(tiles.values()))#part 1 answer

#part2:
def count(x,y): #counts black tiles in surrounding
    ne = tiles[(x+1, y+1)] if (x+1, y+1) in tiles else 0
    nw = tiles[(x-1, y+1)] if (x-1, y+1) in tiles else 0
    se = tiles[(x+1, y-1)] if (x+1, y-1) in tiles else 0
    sw = tiles[(x-1, y-1)] if (x-1, y-1) in tiles else 0
    e  = tiles[(x+2, y)] if (x+2, y) in tiles else 0
    w  = tiles[(x-2, y)] if (x-2, y) in tiles else 0
    return(ne+nw+se+sw+e+w)


#loop through tiles and add surrounding tiles as white if they don't exist yet
for tile in tiles.items():
    x=tile[0][0]; y=tile[0][1]
    if (x+1, y+1) not in tiles: tiles[(x+1, y+1)]=0 #ne
    if (x-1, y+1) not in tiles: tiles[(x-1, y+1)]=0#nw
    if (x+1, y-1) not in tiles: tiles[(x+1, y-1)]=0 #se
    if (x-1, y-1) not in tiles: tiles[(x-1, y-1)]=0 #sw
    if (x+2, y) not in tiles: tiles[(x+2, y)]=0 #e
    if (x-2, y) not in tiles: tiles[(x-2, y)]=0 #w



for tile in tiles:
    tiles[tile]==1:
        if count(tile[0], tile[1])==     