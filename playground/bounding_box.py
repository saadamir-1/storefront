def findBBox(coord1a, coord1b, coord2a, coord2b, coord3a, coord3b, coord4a, coord4b):
    lon = [coord1a, coord2a, coord3a, coord4a]
    lat = [coord1b, coord2b, coord3b, coord4b]
    bbox = [min(lon), min(lat), max(lon), max(lat)]
    return bbox