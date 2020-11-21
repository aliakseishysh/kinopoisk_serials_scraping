from csv import writer


def write_headers(file_path, first_header, second_header):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow([first_header, second_header])


def save_to_csv(file_path, dictionary):
    with open(file_path, 'a', newline='') as csv_file:
        csv_writer = writer(csv_file)
        for key, value in dictionary.items():
            csv_writer.writerow([key, value])
