def touched_same_position(path: str = "") -> bool:
    x, y = 0, 0
    coordinates: set = {(0,0)}
    for direction in path:
        match direction:
            case "N": y += 1
            case "S": y -= 1
            case "E": x += 1
            case "W": x -= 1
        if not (x, y) in coordinates:
            coordinates.add((x, y))
        else: return True
    return False

print(touched_same_position('NNSWWEWSSESSWENNW'))