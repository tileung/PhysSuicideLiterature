## Tag each citation with THEME, based on tags.

import os
import sys
import csv
import time

## Start timer
start = time.time()

## Read a workbook of tags and of citations with uncategorized tags
path = 'C:\\Users\\Tiffany Leung\\Documents\\Compassion\\Suicide references\\PyThemes\\'

## Initiate file to save results, with Key|Title and all possible Themes.
fName = path + "CitThemes.txt"
try:
    os.remove(fName)
    print("old file removed")
except OSError:
    pass

results_file = "CitThemes.tab"
results = open(results_file,"w")

## Define a function to search text in a string
##def findtext(text,stringoftext):
##    i = 0
##    if stringoftext.find(text) == -1:
##        pass
##    else:
##        i = i+1

## Identify files for comparison
themeslist = path + "ThemesTagsFinal.txt"
citationslist = path + "CitationsTags.txt"

# for each row in citation list, ...
f = open(citationslist, 'r')
freader = csv.reader(f, dialect = csv.excel_tab)

for n in freader:
    # assign these...
    citkey = n[0]
    cittitle = n[1]
    cittags = str(n[2])

    # look for one tag at a time (loop through the rows of tags)...
    g = open(themeslist, 'r')
    greader = csv.reader(g, dialect = csv.excel_tab)

    for m in greader:
        tag = str(m[0])
        if cittags.find(tag) == -1:
            pass
        else:
            theme = str(m[1])
            line = citkey + '\t' + theme + '\n' # cittitle + '\t' + cittags + '\t' + tag + '\t' + theme + '\n'
            # print line
            results.write(line)
        
results.close()
        
end = time.time()
elapsed = end - start
print "Time elapsed (in seconds)"
print elapsed
sys.exit(0)   
