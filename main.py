# Student ID: 011837192

from package import Package
from truck import Truck
from hash_table import HashTable
from file_loaders import *


def main():
    # Create and populate HashTable for packages
    packages = HashTable()
    populate_packages_table('packages.csv', packages)

    # Create and populate List for addresses
    addresses = []
    populate_addresses_list('addresses.txt', addresses)

    # Create and populate 2D List for distances
    distances = []
    populate_distances_table('distances.csv', distances)


if __name__ == '__main__':
    main()
