import OdometryCSVParser
import OdometryEntrySorter
import Plotter
import sys
import os


def main():
    print("This is Kilometer, the odometry parser")

    # Get odometry CSV file from arguments
    argc = len(sys.argv)
    if(2 != argc):
        print("[ERROR] Wrong number of arguments. Arg1 : <path/of/odometry_file>")
        exit(1)

    # Get entries from the CSV file
    entries = OdometryCSVParser.parse_csv(file, entries)

    # Print those entries
    print("[INFO ] Got the following entries from the CSV file")
    for entry in entries:
        entry.print()

    OdometryEntrySorter.sort_odometry_entries(entries)

    # Print the sorted entries
    print()  # Newline
    for entry in entries:
        entry.print()

    Plotter.plot_odometry(entries)
    Plotter.plot_cost(entries)

    Plotter.show()

    return 0


if __name__ == "__main__":
    # execute only if run as a script
    main()
