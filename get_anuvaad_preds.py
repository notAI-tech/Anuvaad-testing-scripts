from anuvaad import Anuvaad

models = {
        #'tam': Anuvaad('english-tamil'),
        'tel': Anuvaad('english-telugu'),
        #'kan': Anuvaad('english-kannada'),
        #'mal': Anuvaad('english-malayalam'),
        #'mar': Anuvaad('english-marathi'),
        #'hin':  Anuvaad('english-hindi')
        }

from tqdm import tqdm

lines = open('english-telugu_tamil_hindi_kannada_malayalam_marathi.tatoeba-sentpairs.tsv').readlines()

of = open(list(models.keys())[0] + '-results.tsv', 'w')
of.write('SRC_ID\tTGT_ID\tSRC_LANG\tTGT_LANG\tSRC_SENT\tTGT_SENT\tPRED\n')

for line in tqdm(lines):
    try:
        if line.strip().split('\t')[3] not in models: continue
        pred = models[line.strip().split('\t')[3]].anuvaad(line.split('\t')[4].strip())
        of.write(line.strip() + '\t' + pred + '\n')
        of.flush()
    except Exception as ex:
        print('\n', ex, '\n')
        continue

