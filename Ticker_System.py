import sys
category_name2 = [] # Only names
category = [] # Names,rows,columns,all seats that can be purchase,purchased seats(full),purchased seats(student),purchased seats(season) dictionary
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
outputs = []

def CREATECATEGORY():
    a = line.split()
    row, column = a[2].split("x")
    b = int(row) * int(column)
    if a[1] in category_name2:
        print(f"Warning: Cannot create the category for the second time. The stadium has already {a[1]}.")
        outputs.append(f"Warning: Cannot create the category for the second time. The stadium has already {a[1]}.")
    elif a[1] not in category_name2:
        print(f"The category {a[1]} having {b} seats has been created.")
        outputs.append(f"The category {a[1]} having {b} seats has been created.")
        all_seats = []
        for i in alphabet[:int(row)]:
            for j in range(0, int(column)):
                i = i + str(j)
                all_seats.append(i)
                i = i[0]
        category_name1 = {"ct_name": a[1], "row": int(row), "column": int(column), "allseats": all_seats, "full": [], "student": [], "season": []}
        category_name2.append(a[1])
        category.append(category_name1)


def SELLTICKET():
    a = line.split()
    ticket1 = {"name": a[1], "ticket_type": a[2], "category_name": a[3], "seats": a[4:]}
    for i in ticket1["seats"]:
        if "-" not in i: # It only looks for like C2, B3 , D10
            for j in category: # It opens category list and look every dictionary in it
                if j["ct_name"] == ticket1["category_name"]:
                    if int(i[1:]) > j["column"] and alphabet.index(i[0]) + 1 > j["row"]:
                        b = j["ct_name"]
                        print(f"Warning: The category {b} has less row and column than the specified index {i}!")
                        outputs.append(f"Warning: The category {b} has less row and column than the specified index {i}!")
                    elif alphabet.index(i[0]) + 1 > j["row"]:
                        b = j["ct_name"]
                        print(f"Warning: The category {b} has less row than the specified index {i}!")
                        outputs.append(f"Warning: The category {b} has less row than the specified index {i}!")
                    elif int(i[1:]) > j["column"]:
                        b = j["ct_name"]
                        print(f"Warning: The category {b} has less column than the specified index {i}!")
                        outputs.append(f"Warning: The category {b} has less column than the specified index {i}!")
                    elif int(i[1:]) <= j["column"] and alphabet.index(i[0]) + 1 <= j["row"]:
                        if i in j["allseats"]:
                            print("Success: {} has bought {} at {}".format(a[1], i, a[3]))
                            outputs.append("Success: {} has bought {} at {}".format(a[1], i, a[3]))
                            if ticket1["ticket_type"] == "full":
                                j["full"].append(i)
                            elif ticket1["ticket_type"] == "student":
                                j["student"].append(i)
                            elif ticket1["ticket_type"] == "season":
                                j["season"].append(i)
                            j["allseats"].remove(i)
                        elif i not in j["allseats"]:
                            print("Warning: The seat {} cannot be sold to {} since it was already sold!".format(i, a[1]))
                            outputs.append("Warning: The seat {} cannot be sold to {} since it was already sold!".format(i, a[1]))

        if "-" in i: # It only looks like C2-10, D3-15
            for j in category: # It opens category list and look every dictionary in it
                if j["ct_name"] == ticket1["category_name"]:
                    c = i.split("-")  # c = ["C2", "4"]
                    d = c[0]
                    if int(c[1]) > j["column"] and alphabet.index(d[0]) + 1 > j["row"]:
                        b = j["ct_name"]
                        print(f"Warning: The category {b} has less row and column than the specified index {i}!")
                        outputs.append(f"Warning: The category {b} has less row and column than the specified index {i}!")
                    elif alphabet.index(d[0]) + 1 > j["row"]:
                        b = j["ct_name"]
                        print(f"Warning: The category {b} has less row than the specified index {i}!")
                        outputs.append(f"Warning: The category {b} has less row than the specified index {i}!")
                    elif int(c[1]) > j["column"]:
                        b = j["ct_name"]
                        print(f"Warning: The category {b} has less column than the specified index {i}!")
                        outputs.append(f"Warning: The category {b} has less column than the specified index {i}!")
                    elif int(c[1]) <= j["column"] and alphabet.index(d[0]) + 1 <= j["row"]:
                        for k in range(int(d[1:]), int(c[1]) + 1):
                            e = d[0] + str(k)  # k = C2 C3 C4
                            if e in j["allseats"]:
                                if k == int(c[1]):
                                    for h in range(int(d[1:]), int(c[1]) + 1):
                                        h = d[0] + str(h)
                                        if ticket1["ticket_type"] == "full":
                                            j["full"].append(h)
                                        elif ticket1["ticket_type"] == "student":
                                            j["student"].append(h)
                                        elif ticket1["ticket_type"] == "season":
                                            j["season"].append(h)
                                        j["allseats"].remove(h)
                                    print("Success: {} has bought {} at {}".format(a[1], i, a[3]))
                                    outputs.append("Success: {} has bought {} at {}".format(a[1], i, a[3]))
                            elif e not in j["allseats"]:
                                print("Warning: The seats {} cannot be sold to {} due some of them have already been sold!".format(i, a[1]))
                                outputs.append("Warning: The seats {} cannot be sold to {} due some of them have already been sold!".format(i, a[1]))
                                break


def CANCELTICKET():
    a = line.split()
    ticket2 = {"ct_name": a[1], "seats": a[2:]}
    for i in ticket2["seats"]:
        for j in category: # It opens category list and look every dictionary in it
            if j["ct_name"] == ticket2["ct_name"]:
                if int(i[1:]) > j["column"] and alphabet.index(i[0]) + 1 > j["row"]:
                    b = j["ct_name"]
                    print(f"Warning: The category {b} has less row and column than the specified index {i}!")
                    outputs.append(f"Warning: The category {b} has less row and column than the specified index {i}!")
                elif alphabet.index(i[0]) + 1 > j["row"]:
                    b = j["ct_name"]
                    print(f"Warning: The category {b} has less row than the specified index {i}!")
                    outputs.append(f"Warning: The category {b} has less row than the specified index {i}!")
                elif int(i[1:]) > j["column"]:
                    b = j["ct_name"]
                    print(f"Warning: The category {b} has less column than the specified index {i}!")
                    outputs.append(f"Warning: The category {b} has less column than the specified index {i}!")
                elif int(i[1:]) <= j["column"] and alphabet.index(i[0]) + 1 <= j["row"]:
                    if i in j["allseats"]:
                        print("Warning: The seat {} at {} has already been free! Nothing to cancel".format(i, a[1]))
                        outputs.append("Warning: The seat {} at {} has already been free! Nothing to cancel".format(i, a[1]))
                    elif i not in j["allseats"]:
                        print("Success: The seats {} at {} have been canceled and now ready to sell again".format(i, a[1]))
                        outputs.append("Success: The seats {} at {} have been canceled and now ready to sell again".format(i, a[1]))
                        if i in j["full"]:
                            j["full"].remove(i)
                        elif i in j["student"]:
                            j["student"].remove(i)
                        elif i in j["season"]:
                            j["season"].remove(i)
                        j["allseats"].append(i)


def BALANCE():
    a = line.split()
    print("Category report of {}".format(a[1]))
    outputs.append("Category report of {}".format(a[1]))
    print("-" * 30)
    outputs.append("-" * 30)
    for j in category: # It opens category list and look every dictionary in it
        if a[1] == j["ct_name"]:
            full = len(j["full"]) * 20
            student = len(j["student"]) * 10
            season = len(j["season"]) * 250
            total = full + student + season
            print("Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars".format(len(j["student"]), len(j["full"]), len(j["season"]), total))
            outputs.append("Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars".format(len(j["student"]), len(j["full"]), len(j["season"]), total))

def SHOWCATEGORY():
    a = line.split()
    print("Printing category layout of {}".format(a[1]))
    outputs.append("Printing category layout of {}".format(a[1]))
    print()
    outputs.append("")
    for j in category: # It opens category list and look every dictionary in it
        if a[1] == j["ct_name"]:
            for i in reversed(alphabet[:j["row"]]): # j["student"] = ['B3', 'B4', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']
                b = []
                for h in range(0, j["column"]):
                    b.append("X")
                for k in j["full"]:
                    if i == k[0]:
                        b[int(k[1:])] = "F"
                for k in j["student"]:
                    if i == k[0]:
                        b[int(k[1:])] = "S"
                for k in j["season"]:
                    if i == k[0]:
                        b[int(k[1:])] = "T"
                b = "  ".join(map(str, b))
                print(i + " " + b)
                outputs.append(i + " " + b)
            if j["column"] < 10:
                b = "  ".join(map(str, range(0, j["column"])))
                print(b)
                outputs.append(b)
            elif j["column"] > 10:
                b = "  ".join(map(str, range(0, 10)))
                c = " ".join(map(str, range(10, j["column"])))
                print("  " + b + " " + c)
                outputs.append("  " + b + " " + c)

def output(): # It opens a new txt file and sets up to print all outputs
    outfile = open("output.txt", "w")
    for line in outputs:
        outfile.write(line + "\n")

def main():
    with open(sys.argv[1], "r") as file:
        global line
        for line in file: # It looks each line in input.txt
            if line.startswith("CREATECATEGORY"):
                CREATECATEGORY()
            elif line.startswith("SELLTICKET"):
                SELLTICKET()
            elif line.startswith("CANCELTICKET"):
                CANCELTICKET()
            elif line.startswith("BALANCE"):
                BALANCE()
            elif line.startswith("SHOWCATEGORY"):
                SHOWCATEGORY()
    output()

main()
