import pydload
from tqdm import tqdm

all_lines = open('sentences_detailed.csv').readlines()

open('eng_tel_hin_mal_mar_tam_kan_sentences_detailed.csv', 'w').write('\n'.join([i.strip() for i in tqdm(all_lines) if i.strip().split('\t')[1] in {"eng", "tel", "hin", "mal", "mar", "tam", "kan"}]))

import pandas as pd
sent_details = pd.read_csv('eng_tel_hin_mal_mar_tam_kan_sentences_detailed.csv',
                           sep='\t', header=None, error_bad_lines=False)
sent_details = sent_details.rename(columns={0:'Sentence id', 1:'Lang',  2:'Text',
                                            3:'Username', 4:'Date added',
                                            5:'Date last modified'})
sent_details.head()

links = pd.read_csv('links.csv', sep='\t', header=None, error_bad_lines=False)
links = links.rename(columns={0:'Sentence id',1:'Translation id'})
links.head()

from tqdm import tqdm
of = open("tatoeba-sentpairs.tsv", "w")

for idx, row in tqdm(links.iterrows()):
    src_idx, trg_idx = row['Sentence id'], row['Translation id']
    try:
        src = sent_details[sent_details['Sentence id']==src_idx][['Text', 'Lang']].iloc[0]
        trg = sent_details[sent_details['Sentence id']==trg_idx][['Text', 'Lang']].iloc[0]
    except:
        continue
    of.write('\t'.join([str(src_idx), str(trg_idx), src['Lang'], trg['Lang'], src['Text'], trg['Text']]) + '\n')






