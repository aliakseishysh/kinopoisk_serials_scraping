from csv import writer


def save_to_csv(dictionary):
    with open('serials.csv', 'w', newline='') as csvfile:
        csv_writer = writer(csvfile) 
        csv_writer.writerow(['Название', 'Рейтинг'])
        for key, value in dictionary.items():
            csv_writer.writerow([key, value])
        
