# Student ID: 011837192

from cli import CLI
from truck import Truck
from hash_table import HashTable
from file_loaders import *
from route_optimizer import optimize_route


def main():
    # Load data from csv files
    addresses = []
    populate_addresses_list('addresses.txt', addresses)

    distances = []
    populate_distances_table('distances.csv', distances)

    packages = HashTable()
    populate_packages_table('packages.csv', packages, addresses)

    # Prepare trucks
    truck_1 = Truck(1)
    truck_1.load_packages(packages, [6, 25, 28, 32, 40, 7, 10, 11, 22, 23, 24, 26, 29, 33, 34, 37])
    truck_1.route = optimize_route(truck_1.packages, distances)

    truck_2 = Truck(2)
    truck_2.load_packages(packages, [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 5, 8, 27, 30, 35, 39])
    truck_2.route = optimize_route(truck_2.packages, distances)

    truck_3 = Truck(3)
    truck_3.load_packages(packages, [1, 4, 21, 2, 9, 12, 17, 31])
    truck_3.route = optimize_route(truck_3.packages, distances)

    # Run CLI
    cli = CLI(packages, distances, [truck_1, truck_2, truck_3])
    cli.run()


if __name__ == '__main__':
    main()
