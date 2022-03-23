# -*- coding: utf-8 -*-
"""
A tool to make macrogen primer sheet. It takes a fasta file and produces an xls sheet 
"""

    
#dependancies     
import pandas as pd
from Bio import SeqIO
import warnings

#Gets rid of pandas xls warning
warnings.simplefilter(action='ignore', category=FutureWarning) 

#Needs to be in the same folder as the script
fasta_name = input('Please enter file name - including extension \n')

#Lists for data storage
record_list = []
data_list = []

#Parse fasta file and records the primer name and sequence 
for record in SeqIO.parse(str(fasta_name), 'fasta'):  
    record_list.append([str(record.id),str(record.seq)])

#Counts for calculating amount and total basepair
count = 0
total_len = 0

#Loops record list and extracts column properties
for item in record_list:
    count += 1
    no = count
    name = item[0]
    olgio = item [1]
    if len(olgio) >= 36:
        amount = 0.05
    else: 
        amount = 0.025
    if amount == 0.05:
        purification = 'MOPC'
    else:
        purification = 'Desalt'
    data_list.append([no, name, olgio, amount, purification])
    total_len +=(len(olgio))

#Sanity check
print (f'Processed {len(record_list)} samples')

#Build dataframe with column headings and populate from data_list
dataframe_name = input('Enter spreadsheet name - including xls extension \n')
data_frame = pd.DataFrame(data = data_list, \
columns='No., Oligo Name, 5` - Oligo Seq - 3`, \
Amount, Purification'.split(', '))
                          
#Export dataframe without an index column      
data_frame.to_excel(str(dataframe_name), index = False,)

#Let user know if successful and total basepairs
print (f'You have {total_len} base pairs')
print ('Excel spreadsheet made')
