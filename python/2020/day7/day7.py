import pandas as pd
import numpy as np
import re

file="day7/input.txt"

pattern_a="(\w+) (\w+) bags?"
pattern_b="\d+"

bag_a=("shiny","gold")

colors = {}
colors_b = {}

bag_count_dict = {}

def trace_bag_ancestor(key:set) -> set:
    bags=set(colors.get(key,[]))
    child_bags=set()
    for bag in bags:
        bag_set = trace_bag_ancestor(bag)
        child_bags.update(bag_set)
    
    return bags.union(child_bags)

def count_bags(bag:set) -> int:
    if bag_count_dict.get(bag):
        return bag_count_dict[bag]
    if bag==('no','other'):
        return 0

    bags_counter=0

    for child_bag in colors_b[bag]:
        child_bags=count_bags(child_bag[0])
        bags_counter+=child_bags*child_bag[1]    

    bag_count_dict[bag]=bags_counter + 1

    return bag_count_dict[bag]

if __name__=="__main__":
    bag_a=("shiny","gold")

    with open(file,'r') as reader:
        line=reader.readline()
        gold_colors = []
        while line!="":

            split=re.findall(pattern_a,line)
            color=split.pop(0)
            bags= split if len(split) else []
            count=list(map(int,re.findall(pattern_b,line)))
            bags_counter= count if count else [0]
            for bag in bags:
                colors[bag]=colors.get(bag,[]) + [color]
            colors_b[color]=[(bags[i],bags_counter[i]) for i in range(len(bags))]
            line=reader.readline()
    colors_b[('no','other')]=[]
    part_a=trace_bag_ancestor(bag_a)
    part_b=count_bags(bag_a)-1
    print("Answer to part A:")
    print("colors:{0}".format(len(part_a)))
    print("Answer to Part B:")
    print(part_b)
    print("Le Fin")
