import csv
from OdometryEntry import OdometryEntry
from datetime import datetime


def check_string_to_float(s):
    try:
        float(s)
        return True
    except:
        return False


def parse_csv(p_file_path, p_entry_array):
    with open(p_file_path, newline='') as csv_file:
        csv_file_reader = csv.reader(csv_file, delimiter=";", quotechar='|')
        i = 0
        for row in csv_file_reader:
            if 0 == i or 3 > len(row):
                # The fist line is a comment for the column names
                i += 1
                continue
            print(', '.join(row))
            # print(str(row) + " (" + str(i) + ", size = " + str(len(row)) + ")" )

            # Check error cases, empty data, etc.
            if not row[2]:
                row[2] = .0

            entry = OdometryEntry(datetime.strptime(row[0], "%d/%m/%Y").date(), float(row[1]), float(row[2]), row[3])
            # entry.print()
            # print("\n\r")

            p_entry_array.append(entry)

            i += 1
