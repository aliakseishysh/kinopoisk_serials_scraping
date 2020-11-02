from csv import writer


def write_headers(file_path, first_header, second_header):
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = writer(csvfile) 
        csv_writer.writerow([first_header, second_header])

def save_to_csv(file_path, dictionary):
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = writer(csvfile) 
        for key, value in dictionary.items():
            csv_writer.writerow([key, value])
        
