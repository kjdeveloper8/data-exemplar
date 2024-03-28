from typing import List, Union
from trafilatura import fetch_url, extract
from pathlib import Path

DIR = "corpus" # default dir to store data
CORPUS = "data_corpus" # default file name to store data

url = 'https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/'

class GetData:
    """
    Fetch data from web url.

    :url: web url to get data from
    :store_dir: directory to store data
    :store_type: format type to store data (supported: txt, json, csv, xml)
    :language: language (default: en)
    """
    def __init__(self, 
                 url:Union[List[str],str], 
                 stored_dir:str, 
                 store_type:str='txt', 
                 language:str='en'):
        self.url = url
        self.stored_dir = stored_dir
        self.store_type = store_type
        self.language = language

    def get_web_data(self):
        try:
            get_data_from_url = fetch_url(self.url)
        except Exception as e:
            print(e)

        # extract data from url
        # return extract(get_data_from_url)
        return extract(get_data_from_url, 
                       output_format=self.store_type, 
                       target_language=self.language)
    
    def store_data(self):
        ''' Store data extracted from url in supported format'''
        extracted = self.get_web_data()
        print(extracted) # default: text

        # check dir exist if not create one
        Path(DIR).mkdir(parents=True, exist_ok=True) if True else None
        store_path = Path(DIR, CORPUS)
        print("Path to store ---> ",store_path)
        if self.store_type == 'txt':
            store_path = str(Path(store_path)) + '.' + self.store_type
            with open(store_path, 'w') as wfile:
                wfile.write(extracted)
        elif self.store_type == 'xml':
            store_path = str(Path(store_path)) + '.' + self.store_type
            with open(store_path, 'w') as wfile:
                wfile.write(extracted)
        elif self.store_type == 'json':
            store_path = str(Path(store_path)) + '.' + self.store_type
            import json
            with open(store_path, 'w') as wfile:
                json.dump(extracted, wfile, indent=4)
        elif self.store_type == 'csv':
            store_path = str(Path(store_path)) + '.' + self.store_type
            import csv
            with open(store_path, 'w', newline='') as wfile:
                writer = csv.writer(wfile)
                writer.writerow([extracted])
        else:
            print("Please check! File type maybe incorrect or not supported")
                
if __name__ == '__main__':
    ob = GetData(url, DIR, store_type='txt')
    ob.store_data()