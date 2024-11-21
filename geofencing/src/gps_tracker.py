def is_within_boundary(current_location, authorized_boundary):
    """
    Checks if the current location is within the authorized boundary.
    :param current_location: Tuple (latitude, longitude).
    :param authorized_boundary: List of tuples defining the boundary [(lat, lon), ...].
    :return: True if within boundary, False otherwise.
    """
    lat, lon = current_location
    min_lat = min([point[0] for point in authorized_boundary])
    max_lat = max([point[0] for point in authorized_boundary])
    min_lon = min([point[1] for point in authorized_boundary])
    max_lon = max([point[1] for point in authorized_boundary])
    
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon
