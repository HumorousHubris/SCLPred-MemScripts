import math

def SCLPred_parse(fname):

    predicted = []
    correct = []


    read = open(fname, 'r') #processed txt file from awk, must include memb and nonmemb, otherwise returns 0.

    rlines = read.readlines()

    #correct first, then predicted

    for x in range(0,len(rlines)):
        if((x-3) % 6 == 0):
            if('1' in rlines[x]):
                correct.append(1)
            else:
                correct.append(-1)
            if('1' in rlines[x+1]):
                predicted.append(1)
            else:
                predicted.append(-1)
                    
    fp = 0.0
    tp = 0.0
    fn = 0.0
    tn = 0.0
    count = 0
    def printdums():
        print(fp)
        print(tp)
        print(fn)
        print(tn)

    for x in range(0,len(predicted)):
        if(correct[x] == -1):
            if(predicted[x] == -1):
                tn += 1
                count += 1
            else:
                fp += 1
                count += 1
        else:
            if(predicted[x] == -1):
                fn += 1
                count += 1
            else:
                tp += 1
                count += 1

    printdums()
    mcc = (tp*tn - fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))

    #also calculate spec, sen and FDR
    spec = 100*(tp/(tp+fp))
    sen = 100*(tp/(tp+fn))
    fpr = 100*(fp/(fp+tn))
                
        
    print(len(predicted))
    print(len(correct))
    read.close()
    return [mcc, spec, sen, fpr]


out = open("SCLPred_ITSout.txt", 'a+')
#print(mcc)
output = SCLPred_parse("allpred.predictions")
out.write("SCLPredOut:\nMCC: " + str(output[0]) + "\nSpec: " + str(output[1]) + "\nSen: " + str(output[2]) + "\nFPR: " + str(output[3]) +'\n')
#out.write(name + str(mcc) + "\n")


out.close()
