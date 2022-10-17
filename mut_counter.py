'''This script takes an aligned fasta file that contains a reference sequence and returns a csv file that contains simple statistics and list of mutations. 
It will work on nucleotide sequences and amino acid sequences'''

#dependences
try:
    from Bio import SeqIO # For reading sequences 
    import csv #For writing output file 
    import pandas as pd # for graphing
    import matplotlib.pyplot as plt #for graphing 
    import seaborn as sns #for graphing
    import statistics #for calculating statistics 
    import sys
except:
    print ('Module not found')



def mut_collector(seq_file, ref_seq_name, outputfilename):
    seq_dict = {}
    
    #extracting out sequences 
    try:
        for record in SeqIO.parse(str(seq_file), 'fasta'): 
            seq_dict[str(record.id)] = str(record.seq)
    except:
        print ('fasta file not found')

    #pulling out ref_seq
    try:
        ref_seq = (seq_dict[str(ref_seq_name)]) 
    except:
        print ('ref seq not found')

    #looping through to pull out mutations
    dif_dict = {}
    count_dict = {}
    for name, value in seq_dict.items():
        mut_list = []
        count = 0 
        for i in range(0, len(value)):
            count +=1
            if value[i] == ref_seq[i]:
                continue
            else: 
                diff = (str(ref_seq[i]) + str(count) + str(value[i]))
                mut_list.append(diff)            
                if (count in count_dict):
                    count_dict[count] += 1
                else:
                    count_dict[count] = 1
            dif_dict[name] = mut_list 

    #writing output file 
    with open(str(outputfilename), 'w', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(['Sequence', 'Mutations'])
        for item, value in dif_dict.items():
            writer.writerow([item,value])

    #counting the length of each value from the input dict to determine how many mutations.
    mutation_counter_list = [] 
    for value in dif_dict.values():
        mutation_counter_list.append(len(value))
    average_seq = round(statistics.mean(mutation_counter_list),2)
    quant_seq = statistics.quantiles(mutation_counter_list,)

    #graph the location of the mutations 
    seq_df = pd.DataFrame.from_dict(count_dict, orient='index')
    seq_df.reset_index(inplace=True)
    seq_df.rename(columns={'index':'location', 0:'numbers'}, inplace=True)
    plt.figure(figsize=(20,10))
    graph = sns.barplot(data= seq_df, x = 'location', y= 'numbers')
    plt.xticks(rotation=90, fontsize='x-small')
    plt.xlabel('# position')
    plt.ylabel('# number of mutations')
    save_graph = plt.savefig(f'{sys.argv[2]}_output.png')

    return (print (f'There are {len(dif_dict)} sequences and the average number of mutations is {average_seq} and the quantiles are {quant_seq}'), save_graph)

mut_collector(seq_file = str(sys.argv[1]) , ref_seq_name = str(sys.argv[2]), outputfilename= str(sys.argv[3]))

    
    









    



    
    

