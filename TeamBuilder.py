with open("Chelsea.txt","r") as Chelsea:

    GK = list()
    DEF = list()
    MD = list()
    ATK = list()

    for row in Chelsea:
        row = row[:-1]
        row_el = row.split(",")

        if row_el[1] == "GK":
            GK.append(row + "\n")

        elif row_el[1] == "DEF":
            DEF.append(row + "\n")

        elif row_el[1] == "MD":
            MD.append((row + "\n"))

        else:
            ATK.append(row + "\n")

        with open("GK.txt","w") as gk:
            for i in GK:
                gk.write(i)

        with open("DEF.txt","w") as defe:
            for i in DEF:
                defe.write(i)

        with open("MD.txt","w") as md:
            for i in MD:
                md.write(i)

        with open("ATK.txt","w") as atk:
            for i in ATK:
                atk.write(i)






