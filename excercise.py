import spacy

nlp = spacy.blank("en")

doc = nlp("Tony gave two $ to peter, Bruce gave 500 ₹ to steve")

for token in doc:
    if token.like_num and doc[token.i + 1].is_currency:
        print(token, doc[token.i + 1])
