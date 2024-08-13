import csv
from package import Package


def populate_packages_table(file_name, hash_table):
    with open(file_name) as packages_file:
        packages = csv.reader(packages_file, delimiter=',')
        next(packages)  # skip header
        for pkg in packages:
            id_ = int(pkg[0])
            address = pkg[1]
            city = pkg[2]
            state = pkg[3]
            zip_code = pkg[4]
            deadline = pkg[5]
            weight = pkg[6]
            status = "at hub"
            package = Package(id_, address, city, state, zip_code, deadline, weight, status)
            hash_table.insert(id_, package)
