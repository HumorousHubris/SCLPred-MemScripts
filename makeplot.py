import sys
import matplotlib.pyplot as plt

res = open(sys.argv[1], "r")
#res = open("results.log", "r")

reslines = res.readlines()

valids = []
trains = []
tests = []
epochs = []
count = 1

for x in reslines:
    if "train_MCC" in x:
        trains.append(float(x[10:]))
    if "test_MCC" in x:
        tests.append(float(x[9:]))
    if "validation_MCC" in x:
        valids.append(float(x[15:]))
        epochs.append(count*10)
        count += 1

#print(epochs)
#print(valids)


plt.title(sys.argv[1])
plt.axis([0, 2000, .2, 1])
plt.ylabel('MCC')
plt.xlabel('Epochs')
plt.plot(epochs, valids, 'r-', label = 'Validation')
plt.plot(epochs, trains, color = "green", label = 'Train')
plt.plot(epochs, tests, color = "blue", label = 'Test')
plt.legend()
s = ("Max Train: " + str(max(trains)) + " Max Test: " + str(max(tests)) + " Max Validation: " + str(max(valids)))
plt.figtext(0,0,s)
#plt.show()
plt.savefig("./charts/" + sys.argv[1] + ".png")

maxes = open("./charts/maxes.txt", "a+")
maxes.write(sys.argv[1] + "\n" + "Max Train: " + str(max(trains)) + ", ep:" + str(trains.index(max(trains))*10)+ "\nMax Test: " + str(max(tests)) + ", ep:" + str(tests.index(max(tests))*10) + "\nMax Validation: " + str(max(valids)) + ", ep:" + str(valids.index(max(valids))*10)+ "\n\n")
maxes.close()
res.close()
