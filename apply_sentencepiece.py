import sentencepiece as spm
import codecs
import sys
sentencepiece_model = sys.argv[1]
infile = sys.argv[2]
outfile = sys.argv[3]

s = spm.SentencePieceProcessor(model_file=sentencepiece_model)

target = codecs.open(outfile,'w',encoding='utf-8')
data = []
with codecs.open(infile,'r',encoding='utf-8') as f:
	for line in f:
		tokens = s.encode(line, out_type=str, enable_sampling=False, alpha=0.1, nbest_size=1)
		spm_line = " ".join(_ for _ in tokens)
		target.write(spm_line+"\n")
target.close()