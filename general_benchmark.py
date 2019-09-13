import math
import sys

name = sys.argv[1]

enablekeycharlimit = False #change to true when predictor is FUEL-mLoc
keycharlimit=10

predicted = dict()

correct = dict()


correctread = open("ITS.30.30.fasta.target", "r")
clines = correctread.readlines()
#errs = open("./" + sys.argv[1] + "/errors.txt", "r+")
#eread = errs.read()
#print(eread)
for x in range(1,int(len(clines)/4+1)):
    if enablekeycharlimit:
        n= clines[(x*4-1)-3][:10]
        if '\n' in n:
            n = n[:len(n)-1]
    else:
        n= clines[(x*4-1)-3][:len(clines[(x*4-1)-3])-1]
    s = int(clines[x*4-1])
    #print(clines[(x*4-1)-3][:len(clines[(x*4-1)-3])-1])
    
##    if clines[(x*4-1)-3][:len(clines[(x*4-1)-3])-1] in eread:
##        print(clines[(x*4-1)-3][:len(clines[(x*4-1)-3])-1])
##        continue
    correct[n]=s

print(len(correct))
print(correct)

read = open(sys.argv[1], 'r') #processed txt file from awk

rlines = read.readlines()

for x in range(int(len(rlines)/2)):
    n = rlines[x*2][:len(rlines[x*2])-1]
    s = rlines[x*2+1]
    if(sys.argv[2] in s and "mito" not in s and "nucl" not in s):
        predicted[n]=1
    else:
        predicted[n]=0

fp = 0.0
tp = 0.0
fn = 0.0
tn = 0.0
count = 0
for key in predicted.keys(): #change number to total protein processed (NOT MINUS ONE)
    if(correct[key] == 0):
        if(predicted[key] == 0):
            #print(key + " both 0\n")
            tn += 1
            count += 1
        else:
            #print(key + " cor 0 pre 1\n")
            fp += 1
            count += 1
    else:
        if(predicted[key] == 0):
            #print(key + " cor 1 pre 0\n")
            fn += 1
            count += 1
        else:
            #print(key + " both 1\n")
            tp += 1
            count += 1
print(predicted)
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
print(name + "\nfp:"+str(fp) +" tp:"+str(tp)+ " fn:"+str(fn)+ " tn:"+str(tn) +  "\nMCC: " + str(mcc) + "\nSpec:" + str(spec) + "\nSen: " + str(sen) + "\nFPR: " + str(fpr) +'\n\n')
out.write(name + "\nfp:"+str(fp) +"tp:"+str(tp)+ "fn:"+str(fn)+ "tn:"+str(tn) +  "\nMCC: " + str(mcc) + "\nSpec:" + str(spec) + "\nSen: " + str(sen) + "\nFPR: " + str(fpr) +'\n\n')
#out.write(name + str(mcc) + "\n")

read.close()
out.close()
