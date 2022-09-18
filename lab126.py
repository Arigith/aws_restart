# Nubmer 14 in list
# Created 2 .py files (one for the lab 126 and one called jsonfilehandler.py)

# Exercise 1 Create a folder called files and add a insulin.json file and input data
# Exercise 2 Creating the JSON file handler module in the jsonfilehandler.py file
# Exercise 3: Creating the main program
import jsonfilehandler
data = jsonfilehandler.readjsonfile('files\insulin.json')
if data != "" :
    binsulin =data['molecules']['binsulin']
    ainsulin =data['molecules']['ainsulin']
    insulin = binsulin + ainsulin
    molecularweightinsulinactual = data['molecularweightinsulinactual']
    print('Binsulin: ' + binsulin)
    print('Ainsulin: ' + ainsulin)
    print('Molecular Weight Insulin Actual: ' + str(molecularweightinsulinactual))
else:
    print('Error, exiting program')