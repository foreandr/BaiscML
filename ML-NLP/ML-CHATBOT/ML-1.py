import spacy #comment rasa
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
doc = nlp(u'I am going to London next week for a meeting.')
#for token in doc:
# print(token.text, token.pos_)


example_doc = nlp(u"car truck google")
for t1 in example_doc:
 for t2 in example_doc:
    similarity_perc = int(t1.similarity(t2) * 100)
    print("Word {} is {}% similar to word {}".format(t1.text, similarity_perc, t2.text))
