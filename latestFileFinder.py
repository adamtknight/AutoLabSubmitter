import os
import glob

def findLatestFile():
    list_of_files = glob.glob('/Users/adamk/Documents/Chem269/submitLab/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    file = latest_file.split("/Users/adamk/Documents/Chem269/submitLab\\")[1]
    file = file[0:len(file) - 4] 
    return file