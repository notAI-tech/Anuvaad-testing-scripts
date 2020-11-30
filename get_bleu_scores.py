import sacrebleu
import sys
lines = open(sys.argv[1]).readlines()[1:]
lines = [line.strip().split('\t') for line in lines if line.strip()]
refs = [[line[-3] for line in lines]]
pred = [line[-2] for line in lines]

bleu = sacrebleu.corpus_bleu(pred, refs)
print('anuvaad', bleu.score)

lines = open(sys.argv[1]).readlines()[1:]
lines = [line.strip().split('\t') for line in lines if line.strip()]
refs = [[line[-3] for line in lines]]
pred = [line[-1] for line in lines]

bleu = sacrebleu.corpus_bleu(pred, refs)
print('google', bleu.score)


