import spacy
from spacy import util
import random
'''
nlp = spacy.load('en')
print(nlp.pipe_names)

print(nlp.meta['lang'] + '_' + nlp.meta['name'] + '_' + nlp.meta['version'])
print(util.get_package_path('en_core_web_sm'))
'''
lang = 'en'
pipeline = ['tagger', 'parser', 'ner']
model_data_path = 'C:\\Users\\ARINDAM\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\en_core_web_sm\\en_core_web_sm-2.2.5'
lang_cls = spacy.util.get_lang_class(lang)
nlp = lang_cls()
for name in pipeline:
    component = nlp.create_pipe(name)
    nlp.add_pipe(component)
nlp.from_disk(model_data_path)
doc = nlp(u'I need a taxi to Festy.')
for ent in doc.ents:
  print(ent.text, ent.label_)

LABEL = 'DISTRICT'
TRAIN_DATA = [
('We need to deliver it to Festy.', {
    'entities': [(25, 30, 'DISTRICT')]
  }),
('I like red oranges', {
'entities': []
  })
]
ner = nlp.get_pipe('ner')
ner.add_label(LABEL)
nlp.disable_pipes('tagger')
nlp.disable_pipes('parser')
optimizer = nlp.entity.create_optimizer()

for i in range(25):
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        nlp.update([text], [annotations], sgd=optimizer)

doc = nlp(u'I need a taxi to Festy.')
for ent in doc.ents:
  print(ent.text, ent.label_)