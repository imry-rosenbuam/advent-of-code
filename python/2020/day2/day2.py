import numpy as np
import pandas as pd
import re

file="input.txt"
pattern="(\d+)\-(\d+)\s([a-zA-Z]): ([a-zA-Z]+)\s?"


if __name__=="__main__":
    valid = 0
    valid_2=0

    with open("day2/input.txt",'r') as reader:
        line=reader.readline()
        while line !='':
            match=re.match(pattern,line)
            if match:
                s=match.groups()
                c=int(s[3].count(s[2]))
                if (int(s[0]) <= c )and (c<=int(s[1])):
                    valid+=1
            z=0
            z=z+1 if s[3][int(s[0])-1] == s[2] else z   
            z=z+1 if s[3][int(s[1])-1] == s[2] else z
            if z==1:
                valid_2+=1
                
            line=reader.readline()
    print("First Part") 
    print(valid)
    print("Second Part")
    print(valid_2)



    print("Le Fin")