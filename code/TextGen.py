from textgenrnn import textgenrnn
textgen = textgenrnn()

#textgen.generate_samples(n=5)

#textgen.train_from_file('data/obamaspeechescorpus.txt', num_epochs=1)

#textgen.generate_samples()
#textgen.generate_to_file('generatefile.txt', n=5)
generated_texts = textgen.generate(n=5, prefix="America", temperature=0.2, return_as_list=True)

for text in generated_texts:
    print(text)
#Source: https://github.com/minimaxir/textgenrnn/blob/master/docs/textgenrnn-demo.ipynb
#Corpus: http://www.thegrammarlab.com/?nor-portfolio=corpus-of-presidential-speeches-cops-and-a-clintontrump-corpus
