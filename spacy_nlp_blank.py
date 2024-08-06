import spacy

nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")

doc = nlp("Dr. Strange like pav bhaji of mumbai. Hulk loves chaat of delhi")

for sentence in doc.sents:
    print(sentence)
