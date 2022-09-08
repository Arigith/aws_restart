#Open clean text and make a soft copy
readopen = open('preproinsulin-seq-clean.txt')
copyopen = readopen.readlines()
readopen.close()

#turn soft copy into a string
strcopyopen = str(copyopen)

#copy first 24 characters
lsinsulin = strcopyopen[2:26]
#print characters to check if running right
print(lsinsulin)
#print count to ensure right amount of characters are copied
print(len(lsinsulin))
#write result in first file
lsinsulin_write = open('lsinsulin-seq-clean.txt', 'w')
lsinsulin_write.writelines(lsinsulin)
lsinsulin_write.close

#copy next 30 characters
binsulin = strcopyopen[26:56]
#print characters to check if running right
print(binsulin)
#print count to ensure right amount of characters are copied
print(len(binsulin))
#write result in second file
binsulin_write = open('binsulin-seq-clean.txt', 'w')
binsulin_write.writelines(binsulin)
binsulin_write.close

#copy next 35 characters
cinsulin = strcopyopen[56:91]
#print characters to check if running right
print(cinsulin)
#print count to ensure right amount of characters are copied
print(len(cinsulin))
#write result in third file
cinsulin_write = open('cinsulin-seq-clean.txt', 'w')
cinsulin_write.writelines(cinsulin)
cinsulin_write.close

#copy next 21 characters
ainsulin = strcopyopen[91:112]
#print characters to check if running right
print(ainsulin)
#print count to ensure right amount of characters are copied
print(len(ainsulin))
#write result in fourth file
ainsulin_write = open('ainsulin-seq-clean.txt', 'w')
ainsulin_write.writelines(ainsulin)
ainsulin_write.close