geo_data = [
    {"name": "P1", "x": 10000, "y": 10000},
    {"name": "P2", "x": 10100, "y": 10050},
    {"name": "P3", "x": 10250, "y": 10150},
]




def distance (points):
    results = {}
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i + 1]
        dx = p2["x"] - p1["x"]
        dy = p2["y"] - p1["y"]

        d = round((dx **2 + dy **2 )**0.5 , 3)

        key = f"{p1 ['name']} -> {p2 ['name']}"

        results [key] = d

    return results

print(distance(geo_data))











