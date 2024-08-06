import spacy

nlp = spacy.blank("en")

with open("student.txt") as f:
    text = f.readlines()

text = " ".join(text)

doc = nlp(text)

emails = []
for token in doc:
    if token.like_email:
        emails.append(token.text)

print(emails)
