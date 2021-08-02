import numpy as np
import pandas as pd
import re

file = "day4/input.txt"

pattern="\w+:[#\w]+"

valid_fields = set([
                'byr',
                'iyr',
                'eyr',
                'hgt',
                'hcl',
                'ecl',
                'pid'
                #,'cid'
                ])

field_pattern_dict = {
    'byr': lambda x: 1920 <= int(x) <= 2002,#"19[2-9][0-9]|200[012]",
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hcl': lambda x: re.match("^#[a-f\d]{6}$", x) != None,
    'hgt': lambda x: len(x[:-2]) > 0 and ((59 <= int(x[:-2]) <= 76 and x[-2:] == "in") or (150 <= int(x[:-2]) <= 193 and x[-2:] == "cm")),
    'ecl': lambda x: re.match(r"amb|blu|brn|gry|grn|hzl|oth", x) != None, 
    'pid': lambda x:re.match(r"^\d{9}$",x)!=None
}

if __name__=="__main__":

    with open(file,'r') as reader:
        line = reader.readline()
        valid_a = 0
        valid_b = 0
        while line!="":
            line=line.strip()

            passport = {}
            while line not in ['\n','']:
                line=line.strip()
                if line!='':
                    split=re.findall(pattern,line)
                    line_dict = {x.split(':')[0] : x.split(':')[1] for x in split}
                    passport.update(line_dict)
               
                line=reader.readline()
            
            intersect= set(passport.keys()) & valid_fields
            if len(intersect)==len(valid_fields):
                field_validation = [field_pattern_dict[k](passport[k]) for k in valid_fields]
                valid_a+=1
                xxx = sum(field_validation)
                if sum(field_validation)==len(valid_fields):
                    valid_b+=1
                    #print("-----------")
                    #print(passport)


            line=reader.readline()
        print("Part 1 Answer:")
        print(valid_a)
        print("Part Two")
        print(valid_b)
    print("Le Fin")
