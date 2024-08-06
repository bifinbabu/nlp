import spacy

nlp = spacy.blank("hi")

doc = nlp("अरे भाई, मुझे वो 500 ₹ वापस दे दो")

for token in doc:
    print(token, token.is_currency, token.like_num)
