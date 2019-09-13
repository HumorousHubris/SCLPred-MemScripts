import math
import sys

name = sys.argv[1]

predicted = []

correct = [] 


correctread = open("ITS.30.30.fasta.target", "r")
clines = correctread.readlines()
errs = open("./" + sys.argv[1] + "/errors.txt", "r+")
eread = errs.read()
#print(eread)
for x in range(1,int(len(clines)/4+1)):
    s = int(clines[x*4-1])
    #print(clines[(x*4-1)-3][:len(clines[(x*4-1)-3])-1])
    
    if clines[(x*4-1)-3][:len(clines[(x*4-1)-3])-1] in eread:
        print(clines[(x*4-1)-3][:len(clines[(x*4-1)-3])-1])
        continue
    correct.append(s)

print(correct)

read = open(sys.argv[1], 'r') #processed txt file from awk

rlines = read.readlines()

for x in rlines:
    if(sys.argv[2] in x and "mito" not in x and "nucl" not in x):#change string to one indicating membrane
        #add a 1 to the predicted list and a -1 otherwise
        predicted.append(1)
    else:
        predicted.append(0)

fp = 0.0
tp = 0.0
fn = 0.0
tn = 0.0
count = 0
def printdums():
    print("fp:"+str(fp))
    print("tp:"+str(tp))
    print("fn:"+str(fn))
    print("tn:"+str(tn))

for x in range(len(correct)): #change number to total protein processed (NOT MINUS ONE)
    if(correct[x] == 0):
        if(predicted[x] == 0):
            tn += 1
            count += 1
        else:
            fp += 1
            count += 1
    else:
        if(predicted[x] == 0):
            fn += 1
            count += 1
        else:
            tp += 1
            count += 1
print(predicted)
printdums()
mcc = (tp*tn - fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))

#also calculate spec, sen and FDR
spec = 100*(tp/(tp+fp))
sen = 100*(tp/(tp+fn))
fpr = 100*(fp/(fp+tn))
acc = 100*((tp+tn)/(tp+tn+fn+fp))            
    
print(len(predicted))
#print(len(predicted))
print(len(correct))

print(acc)
out = open("output.txt", 'a+')
#print(mcc)
out.write(name + "\nfp:"+str(fp) +"tp:"+str(tp)+ "fn:"+str(fn)+ "tn:"+str(tn) +  "\nMCC: " + str(mcc) + "\nSpec:" + str(spec) + "\nSen: " + str(sen) + "\nFPR: " + str(fpr) +'\n\n')
#out.write(name + str(mcc) + "\n")

read.close()
out.close()
