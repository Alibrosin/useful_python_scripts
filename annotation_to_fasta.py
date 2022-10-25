import csv 
import sys

def annotation_to_fasta (csvfile, outputfilename):
    'takes a csv file from geneious and converts the annotations to a primer list'
    fasta_dict = {}
    with open(str(csvfile), 'r') as fh:
        reader = csv.reader(fh)
        next(reader)
        for line in reader:
            fasta_dict[line[0]] = line[4]
    
    with open(f'{outputfilename}.fasta', 'w') as fh:
        for key, value in fasta_dict.items():
            fh.write(f'>{key}\n{value}\n')

    return print (f'I have processed {len(fasta_dict)} files. Please use the macrogen tool to order')
        
annotation_to_fasta(str(sys.argv[1]), str(sys.argv[2]))