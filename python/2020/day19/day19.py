import re
import itertools

file = "day19/input2.txt"

rules = {}

rule_pattern = "(\d+): ((([\d\s]+)(\|)?([\d\s]+)?)|(\"\w+\"))"

def parse_rule(match: re.Match) -> None:
    groups = match.groups()

    rule = int(groups[0])

    rule_groups = list()
    if groups[6]:
        rule_groups.append(groups[6].replace("\"",""))
    else:
        if groups[3] and (group1 := groups[3].strip().split(" ")):
            rule_groups.append(group1)
        if groups[5] and (group2 := groups[5].strip().split(" ") if groups[2] else None):
            rule_groups.append(group2)

    rules[rule] = rule_groups

rules_strings = {}

def rule_string(i: int) -> str:
    
    if rules_strings.get(i,None):
        return rules_strings.get(i)

    groups = rules[i]
    
    str_lists = list()

    for group in groups:
        grp_list = list()
        for x in group:
            if x.isnumeric():
                grp_list.append(rule_string(int(x)))
            else:
                grp_list.append(x)
        str_lists.append(grp_list)

    if len(str_lists) == 1:
        strng = "".join(str_lists[0])
    else:
        part_a = "".join(str_lists[0])
        part_b = "".join(str_lists[1])
        strng = f"({part_a}|{part_b})"

    rules_strings[i] = strng

    return strng

max_depth = 10

new_rules_dict = {}

def rule_string_b(i: int, depth: int, max_depth: int) -> list:
    if  depth > max_depth:
        return []

    if rules_strings.get(i, None):
        return rules_strings.get(i)

    groups = rules[i]

    str_lists = list()

    for group in groups:
        grp_list = list()
        for x in group:
            if x.isnumeric():
                grp_list.append(rule_string(int(x)))
            else:
                grp_list.append(x)
        str_lists.append(grp_list)

    if len(str_lists) == 1:
        strng = "".join(str_lists[0])
    else:
        part_a = "".join(str_lists[0])
        part_b = "".join(str_lists[1])
        strng = f"({part_a}|{part_b})"

    rules_strings[i] = strng

    return strng

if __name__ == "__main__":
    with open(file, 'r') as reader:
        line = reader.readline().strip()

        while line != "":
            match = re.match(rule_pattern, line)
            parse_rule(match)
            line = reader.readline().strip()
        
        pattern_0 = "^" + rule_string(0) + "$"

        line = reader.readline()

        i = 0
        
        lines = list()

        while line != "":
            flag = 0
            if re.match(pattern_0, line):
                i += 1
                flag = 1
            lines.append(line)            
            line = reader.readline()

        new_lines = ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]
        
        max_depth = max(list(map(len,lines)))

        for line in new_lines:
            match = re.match(rule_pattern, line)
            parse_rule(match)

        patterns_0_b = rule_string_b(0,0,max_depth)

        print("Answer to part A:")
        print(i)
        print("Le Fin")
