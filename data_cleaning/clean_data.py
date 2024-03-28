import re

def clean_text(text_str):
  text_str = re.sub(r'^RT[\s]+', '', text_str) # Removes 'RT' tag from the tweet
  text_str = re.sub(r'https?:\/\/.*[\r\n]*', '', text_str) # Removes hyperlinkls, starting with https
  text_str = re.sub(r'#', '', text_str) # Removes the '#'
  text_str = re.sub(r'[0-9]', '', text_str) # Removes all numerics
  text_str = re.sub(r'[^A-Za-z0-9 ]+','',text_str) # Removes everything except alphabets and numerics
  return text_str