# SCLPred-MemScripts
Scripts used when working on SCLPred-Mem in Dublin Summer 2019
My role in this project was training our network, tuning its hyperparameters, and benchmarking it against other predictors with a similar task.
I wrote all of these scripts to automate some of the more repetitive tasks.
Below is a description of the usage of each script. Some require MatPlotLib.

*general_benchmark.py*
is the main script to used for benchmarking, except for WoLF PSORT(see below)
calling it uses a command like this:
$python general_benchmark.py ./BUSCAparsed.txt membrane

The first argument is the path to the parsed results file, the second argument is the string that the predictor uses as a positive.
In the case of BUSCA, "organelle membrane" is either replaced with its gene ontology term (from the original output file) or is just removed.
The structure of the parsed output file the script expects is like this:

ABLB2_PHYIT
MIT

Every odd numbered line is the name of a protein, and the next line is the prediction. Each predictor has a different string that belongs in the second argument.
In the above example (which is subcons) it is MEM. Below is a list of what I used when I ran the benchmarks:
BUSCA: "membrane"
DeepLoc: "membrane"
FUEL-mLoc: "Membrane"
LocTree3: "membrane"
Subcons: "MEM"
WoLF PSORT: "plas"

Those are submitted without quotes.

*general_benchmarkold.py*
The next script is general_benchmarkold.py, which is used only for benchmarking WoLF PSORT. The script for breaking the output down into its predictions only
outputs in the format of the old benchmarking procedure I used before removing dependency on the results being in their submission order, and it was really
complicated to change it. WoLF PSORT does output its results in the order that they are submitted, so I figured it would be easier just to use the old script.
The command format is the same, but since it is only used with wolf psort, the second argument should always be "plas" without the quotes.

$python general_benchmarkold.py ./WoLF_PSORTparsed.txt plas

*wolfpsortparser.py*
WoLF PSORT outputs its results in one massive line of text, so this script goes through it all and takes out the predictions.
It has no command line arguments, just run it in a folder with the raw output from WoLF PSORT. (Note: wolf psort doesnt offer a download of its results, i just
pressed CTRL+A with the overview open, then pasted it into a text file.) The script expects the results to be in "res.txt" and will output the predictions to
"parsed_out.txt". These can be renamed after if you so desire. Just paste it into a folder with the results and double click and you will have the predictions.


*SCLpred_parser.py*
This script was used before we modified predict_wholeset to output spec, sen and FPR. It takes a predictions file from predict or predict_wholeset and outputs
the MCC, spec, sen and FPR to a file called SCLPred_out.txt. it looks for a file called allpred.predictions, but this can be changed by editing the string
on line 70. This script just included because I found it useful if sonic was inaccessible and I could not run a new prediction but had the predictions file.
It doesnt use any command line arguments.

*makeplot.py*
this is the script used to make the charts I showed during hyperparameter testing. i usually ran it using a bash for loop to iterate over all of the log files
and make a chart for all of them. the command structure is:

$python makeplot.py nameoffile.log

the charts title will also be the name of the file, so name the files what you want before running the for loop. This also generates maxes.txt, which is a list
of the best MCCs on train test and validation for each log file. The log files come from the trainings. All of the outputs go to a folder in the same folder as the
script called charts

*getBest.py*
this script can be used in the charts directory mentioned above to get the best run on test and validation. all it needs to work is the maxes.txt file
from makeplot.py, and outputs to best.txt.

