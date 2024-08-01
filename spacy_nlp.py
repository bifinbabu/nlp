import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Dr. Strange like pav bhaji of mumbai. Hulk loves chaat of delhi")

for sentence in doc.sents:
    print(sentence)

for sentence in doc.sents:
    for word in sentence:
        print(word)
