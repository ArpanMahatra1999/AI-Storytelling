# basic libraries
import pandas as pd

# nlp libraries
import spacy
nlp = spacy.load("en_core_web_sm")

# opening text file
with open("story.txt", "r") as f:
    text = f.read()

# create dataframes
df_characters = pd.DataFrame(columns=["name", "frequency", "features"])
df_paragraphs = pd.DataFrame(columns=["name", "dialogue", "narration"])

# finding personal entities from text
entities = nlp(text).ents
personal_entities = []
for entity in entities:
    if entity.label_ == 'PERSON':
        personal_entities.append(entity.text)
personal_entities = list(set(personal_entities))

# adding persons and counts to df_characters
for person in personal_entities:
    df_characters = df_characters._append({
        'name': person, 'frequency': text.count(person), 'features': None}, ignore_index=True)

# converting text to paragraphs
paragraphs = text.split("\n")
non_empty_paragraphs = list(filter(lambda x: x != '', paragraphs))
for paragraph in non_empty_paragraphs:
    pass

print(df_characters)