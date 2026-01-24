import csv
import os


def remove_duplicates_from_csv():
    folder_path = "."

    all_rows = []

    for file_name in ["file1.csv", "file2.csv"]:
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row not in all_rows:
                    all_rows.append(row)

    result_file = os.path.join(folder_path, "result_hridina.csv")

    with open(result_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(all_rows)


remove_duplicates_from_csv()
