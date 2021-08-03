import numpy as np
import pandas as pd

file="day6/input.txt"

if __name__=="__main__":

    with open(file,'r') as reader:
        line=reader.readline().strip()
        questions=0
        questions_b=0
        i=0
        while line!="":
            group_questions=set()
            group_questions_b=set()
            while line!="":
                s=set(line)
                group_questions_b=s if len(group_questions)==0 else group_questions_b.intersection(s)
                group_questions.update(s)
                line=reader.readline().strip()
            print
            questions+=len(group_questions)
            questions_b+=len(group_questions_b)
            line=reader.readline().strip()
            i+=1
            print("group {0} has {1} questions".format(i,len(group_questions_b)))
            

    print("Part A answer is:")
    print(questions)
    print("Part B answer is:")
    print(questions_b)
    print("Le Fin")