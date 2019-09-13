
maxes = open("maxes.txt", "r")
maxlines = maxes.readlines()
tests = []
teps = []
valids = []
veps = []
names = []

for x in range(0,int(len(maxlines)/5)):
    nameline = x*5
    names.append(maxlines[nameline])
    tests.append(float(maxlines[nameline+2][10:maxlines[nameline+2].find(",")]))
    teps.append(int(maxlines[nameline+2][maxlines[nameline+2].find("p")+2:len(maxlines[nameline+2])]))

    valids.append(float(maxlines[nameline+3][16:maxlines[nameline+3].find(",")]))
    veps.append(int(maxlines[nameline+3][maxlines[nameline+3].find("p")+2:len(maxlines[nameline+3])]))
    
out = open("best.txt", "w+")
bestTest = tests.index(max(tests))
bestVali = valids.index(max(valids))
out.write("Best TEST mcc\n" + names[bestTest] + "\nMCC: " + str(tests[bestTest]) + " epoch: " + str(teps[bestTest]) + "\n")
print(names)
print(valids)
print(veps)
print(bestVali)
out.write("\nBest VALIDATION MCC\n" + names[bestVali] + "\nMCC: " + str(valids[bestVali]) + " epoch: " + str(veps[bestVali]))
                    
