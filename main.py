import OdometryCSVParser
import OdometryEntrySorter
import Plotter


def main():
    print("Hello world, this is Kilometer, the Kilometer parser")

    entries = []
    file = "odometry-data.csv"

    # Get entries from the CSV file
    OdometryCSVParser.parse_csv(file, entries)

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
