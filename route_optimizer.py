def optimize_route(packages, distances):

    # Separate priority packages and EOD packages
    priority, EOD = separate_priority_and_EOD(packages)
    
    # Extract unique address ids for the packages
    priority_ids = extract_unique_address_ids(priority)
    EOD_ids = extract_unique_address_ids(EOD)

    # Remove EOD_ids that are also in priority_ids,
    # since those EOD packages will be delivered at time of priority drop off
    remove_redundant_EOD_ids(EOD_ids, priority_ids)

    # Route starts at the hub, which is id 0
    priority_route = [0] + priority_ids

    # Order the priority_ids by nearest address
    priority_route = order_by_nearest(priority_route, 0, distances)

    # Add EOD_ids to the end of the ordered priority_route
    total_route = priority_route + EOD_ids

    # Order the EOD_ids in the total_route by nearest address
    start_index = len(priority_route) - 1
    total_route = order_by_nearest(total_route, start_index, distances)

    # Route ends at the hub, which has an id of 0
    total_route.append(0)

    return total_route


def separate_priority_and_EOD(packages):
    priority = []
    EOD = []
    for pkg in packages:
        if pkg.deadline == 'EOD':
            EOD.append(pkg)
            continue
        priority.append(pkg)
    return priority, EOD


def extract_unique_address_ids(packages):
    address_ids = set()
    for pkg in packages:
        address_ids.add(pkg.address_id)
    return list(address_ids)


def remove_redundant_EOD_ids(EOD_ids, priority_ids):
    for id in EOD_ids:
        if id in priority_ids:
            EOD_ids.remove(id)


def order_by_nearest(ids, start_index, distances):
    current_id = ids[start_index]
    to_be_ordered = ids[(start_index + 1):]  # slice of list to be ordered
    ordered = ids[0:(start_index + 1)]       # slice of list already ordered
    for _ in range(len(to_be_ordered)):
        nearest_address_id = get_nearest_address_id(current_id, to_be_ordered, distances)
        ordered.append(nearest_address_id)
        current_id = nearest_address_id
        to_be_ordered.remove(nearest_address_id)
    return ordered


def get_nearest_address_id(from_address_id, address_ids, distances):
    nearest_address_id = None
    shortest_distance = 9999
    for address_id in address_ids:

        primary_index = from_address_id
        secondary_index = address_id

        if primary_index < secondary_index:
            primary_index = address_id
            secondary_index = from_address_id

        distance = distances[primary_index][secondary_index]
        if distance < shortest_distance:
            shortest_distance = distance
            nearest_address_id = address_id

    return nearest_address_id
