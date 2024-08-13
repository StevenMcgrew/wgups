def optimize_route(packages, distances):
    # Extract address id's to a set to eliminate duplicates
    address_ids = set()
    for pkg in packages:
        address_ids.add(pkg.address_id)

    # Optimize address order to reduce mileage
    # start at hub address_id 0
    current_address_id = 0
    route = [0]
    for _ in list(address_ids):
        nearest_address_id = get_nearest_address_id(current_address_id, address_ids, distances)
        route.append(nearest_address_id)
        current_address_id = nearest_address_id
        address_ids.remove(nearest_address_id)
    route.append(0)
    return route


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
