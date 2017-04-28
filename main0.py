# first test for astrohack

# 3th party libraries
import csv

folder_name = 'Astrohack-master/Data/Sample/'

filename = folder_name + 'sample.csv'

with open(filename, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    print(spamreader)
    
    n_spam = len(spamreader)
    print(n_spam)
    
    # skip first line since overhead
    for row_i in range(1, n_spam):
        row = spamreader[row_i]
    # for row in spamreader:
        print(row)
        
        print(row[0])
        
        ind_image = row[0]
        
        # print(', '.join(row))
