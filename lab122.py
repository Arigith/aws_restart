# Calculating the Net Charge of Insulin by Using Python Lists and Loops

# Exercise 1: Assigning variables, lists, and dictionaries

# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin
pkr = {'y':10.07,
    'c':8.18,
    'k':10.53,
    'h':6.00,
    'r':12.48,
    'd':3.65,
    'e':4.25}

# Exercise 2: Using count() to count the numbers of each amino acid
# count = float(insulin.count('y'))
# print(count)
seqcount = ({x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']})
print(seqcount)

# Exercise 3: Writing the net charge formula
ph = 0
while ph <= 14:
    netcharge = (
        +(sum({x: ((seqcount[x]*(10**pkr[x]))/((10**ph)+(10**pkr[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqcount[x]*(10**ph))/((10**ph)+(10**pkr[x]))) \
        for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(ph), netcharge)
    ph += 1