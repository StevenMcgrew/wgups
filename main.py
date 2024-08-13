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

    # Prepare truck 1
    packages_1 = [packages.get(6),
                  packages.get(25),
                  packages.get(28),
                  packages.get(32),
                  packages.get(40),
                  packages.get(7),
                  packages.get(10),
                  packages.get(11),
                  packages.get(22),
                  packages.get(23),
                  packages.get(24),
                  packages.get(26),
                  packages.get(29),
                  packages.get(33),
                  packages.get(34),
                  packages.get(37)]
    route_1 = optimize_route(packages_1, distances)
    truck_1 = Truck(1, packages_1, route_1)

    # Prepare truck 2
    packages_2 = [packages.get(3),
                  packages.get(18),
                  packages.get(36),
                  packages.get(38),
                  packages.get(13),
                  packages.get(14),
                  packages.get(15),
                  packages.get(16),
                  packages.get(19),
                  packages.get(20),
                  packages.get(5),
                  packages.get(8),
                  packages.get(27),
                  packages.get(30),
                  packages.get(35),
                  packages.get(39)]
    route_2 = optimize_route(packages_2, distances)
    truck_2 = Truck(2, packages_2, route_2)

    # Prepare truck 3
    packages_3 = [packages.get(1),
                  packages.get(4),
                  packages.get(21),
                  packages.get(2),
                  packages.get(9),
                  packages.get(12),
                  packages.get(17),
                  packages.get(31)]
    route_3 = optimize_route(packages_3, distances)
    truck_3 = Truck(3, packages_3, route_3)

    cli = CLI(packages, [truck_1, truck_2, truck_3])
    cli.run()


if __name__ == '__main__':
    main()
