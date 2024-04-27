import re
import string

def clean(sample_text):
    punctuations = string.punctuation # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    sample_text = re.sub(punctuations, " ") # removes punctuations
    sample_text = re.sub(r'\w*\d\w*', '', sample_text) # returns alphanumerics
    sample_text = re.sub(r'[#]+',' ', sample_text) # removes hash sign
    sample_text = re.sub(r'[|]+',' ', sample_text) # removes pipe sign
    sample_text = re.sub(r'\n+','', sample_text) # removes \n
    sample_text = re.sub(r'[^\x00-\x7F]+',' ', sample_text) # removes non eng words
    sample_text = re.sub(r"\bhttps\w+", "", sample_text) # removes word started with https
    sample_text = re.sub(r"\bhttp\w+", "", sample_text) # removes word started with http
    sample_text = re.sub(r'\s+', ' ', sample_text).strip() # removes spaces at beginning and ending
    return sample_text