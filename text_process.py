import spacy

nlp = spacy.load('en')

#doc = nlp(u'this product integrates both libraries for downloading and applying patches')
doc = nlp('I am flying to Frisco')
print([(w.text,w.lemma_) for w in doc])

special_case = [{'ORTH':u'Frisco', 'LEMMA': u'San Francisco'}]
nlp.tokenizer.add_special_case(u'Frisco', special_case)
print([(w.head.text, w.text,w.lemma_, w.pos_, w.dep_) for w in doc])

doc = nlp(u'I want a green apple.')
print([w for w in doc[4].lefts])