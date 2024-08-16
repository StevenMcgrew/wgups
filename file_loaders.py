import csv
import datetime
from package import Package


def populate_packages_table(file_name, hash_table, addresses):
    time = datetime.datetime.strptime('00:00:01', '%H:%M:%S')
    with open(file_name) as packages_file:
        packages = csv.reader(packages_file, delimiter=',')
        next(packages)  # skip header
        for pkg in packages:
            id_ = int(pkg[0])
            address_id = addresses.index(pkg[1] + ' ' + pkg[4])
            address = pkg[1]
            city = pkg[2]
            state = pkg[3]
            zip_code = pkg[4]
            deadline = pkg[5]
            weight = pkg[6]
            status = "at hub"
            log_time = time
            if pkg[7] == "Delayed on flight---will not arrive to depot until 9:05 am":
                status = "Delayed"
                log_time = datetime.datetime.strptime('09:05:00', '%H:%M:%S')
            package = Package(id_, address_id, address, city, state, zip_code, deadline, weight, status,
                              {"at hub": log_time, "en route": None, "delivered": None})
            hash_table.insert(id_, package)


def populate_addresses_list(file_name, addresses_list):
    with open(file_name) as addresses_file:
        for line in addresses_file:
            addresses_list.append(line.strip())


def populate_distances_table(file_name, distances_table):
    with open(file_name) as distances_file:
        distances = csv.reader(distances_file, delimiter=',')
        for row in distances:
            intermediary_list = []
            for col_value in row:
                if col_value == '':
                    break
                intermediary_list.append(float(col_value))
            distances_table.append(intermediary_list)
