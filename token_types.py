import spacy

nlp = spacy.blank("en")

doc = nlp("Tony gave two $ to peter")

token0 = doc[0]
token1 = doc[1]
token2 = doc[2]
token3 = doc[3]

# print(dir(token0))

print(token2)
print(token2.like_num)
print(token3)
print(token3.is_currency)

for token in doc:
    print(
        token,
        "==>",
        "index: ",
        token.i,
        "is_alpha",
        token.is_alpha,
        "is_punct: ",
        token.is_punct,
        "like_num: ",
        token.like_num,
        "is_currency: ",
        token.is_currency,
    )
