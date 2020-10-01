import pathlib
import csv

def save_to_csv(dictionary):
    with open('films.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';') 
        writer.writerow(['Название', 'Рейтинг'])
        for key, value in dictionary.items():
            writer.writerow(['"'+str(key)+'"', '"'+str(value)+'"'])
        
