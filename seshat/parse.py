# TODO: handle inputs of 'books' (text file, epub) and output a spacy NLP parsed version of the text
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
