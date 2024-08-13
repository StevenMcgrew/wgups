# Student ID: 011837192

from package import Package
from truck import Truck
from hash_table import HashTable
from csv_file_loaders import *


def main():
    # Create and populate HashTable for packages
    packages_table = HashTable()
    populate_packages_table('packages.csv', packages_table)

    print(packages_table)


if __name__ == '__main__':
    main()
