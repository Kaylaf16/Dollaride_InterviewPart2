#!/usr/bin/env python3
List = [1,2,3,5,10,9,8,9,10,11,7]

def findConsecutiveRuns(List):
   runs =[]
   order = 0 # keeping track of Ascending or Descending
   for index in range(len(List)):
        if(index < len(List)-2):
           current,next,nextnext = index,index+1,index+2
           if(List[current]+1 == List[next]):
               order =1
           if(List[current]-1== List[next]):
               order =-1
           if((order == 1) and (List[next]+1 == List[nextnext])):
               runs.append(current)
           elif((order == -1 )and (List[next]-1 == List[nextnext])):
               runs.append(current)

   return runs

print(findConsecutiveRuns(List))
