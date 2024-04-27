# Converting Harry Potter csv data to txt 

def to_txt(file_from:str, file_to:str):
    with open(file_from, 'r') as rfile, open(file_to, 'a') as wfile:
        text = rfile.readlines()
        text = ' '.join([i for i in text]).replace(";", ": ")
        return wfile.writelines(text)
        
if __name__ == "__main__":
    csv = "Harry Potter 1.csv"
    txt = "harry_potter.txt"
    to_txt(csv, txt)