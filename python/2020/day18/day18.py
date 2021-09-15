import re
import numpy as np
file = "day18/input.txt"


def calc_line_b(line: str) -> int:

    closures = re.findall("\([\d\-*\+\s]+\)", line)
    new_line = line

    if closures:
        for closure in closures:
            val = calc_line_b(closure.strip("()"))
            new_line = new_line.replace(closure,str(val))

        return calc_line_b(new_line)
    else:
        match = re.search("(\d+) [\+] (\d+)",new_line)
        
        while match:
            val = eval(match.group())
            new_line = new_line.replace(match.group(),str(val),1)
            match = re.search("(\d+) [\+] (\d+)", new_line)
            xxx= 1

        match = re.search("(\d+) [\*] (\d+)", new_line)

        while match:
            val = eval(match.group())
            new_line = new_line.replace(match.group(), str(val), 1)
            match = re.search("(\d+) [\*] (\d+)", new_line)
            xxx = 1
        return int(new_line)


def calc_line(line: str) -> int:

    closures = re.findall("\([\d\-*\+\s]+\)", line)
    new_line = line

    if closures:
        for closure in closures:
            val = calc_line(closure.strip("()"))
            new_line = new_line.replace(closure, str(val))

        return calc_line(new_line)
    else:
        match = re.match("(\d+) [\+\*] (\d+)", new_line)

        while match:
            val = eval(match.group())
            new_line = new_line.replace(match.group(), str(val), 1)
            match = re.match("(\d+) [\+\*] (\d+)", new_line)

        return int(new_line)

if __name__ == "__main__":
    with open(file, 'r') as reader:
        line = reader.readline().strip()
        part_a = list()
        part_b = list()
        i = 0
        while line != "":
            i+=1
            x = calc_line(line)
            y = calc_line_b(line)
            part_a.append(x)
            part_b.append(y)
            print(f"{line} value is: {y}")
            line = reader.readline().strip()

    print("Answer to part A:")
    print(sum(part_a))
    print("Answer to part B:")
    print(sum(part_b))
    print("Le Fin")
