import nltk

from nltk.tokenize import sent_tokenize

nltk.download("punkt")  # Download the punkt tokenizer data


sentences = sent_tokenize(
    "Dr. Strange like pav bhaji of mumbai. Hulk loves chaat of delhi"
)

print(sentences)

for s in sentences:
    print(s)
