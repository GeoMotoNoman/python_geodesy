points = [
    {"name": "P1", "height": 152.3},
    {"name": "P2", "height": 149.8},
    {"name": "P3", "height": 151.2},
    {"name": "P4", "height": 150.6}
]

project_height = 151.0


def height_deviation():

    sum_height = 0
    for point in points:
        sum_height += point["height"]

    mean_height = sum_height / len(points)

    print("Mean height:", round(mean_height, 3))
    print()


    for point in points:
        height = point["height"]

        dev_project = height - project_height
        dev_mean = height - mean_height

        sign_proj = "+" if dev_project >= 0 else ""
        sign_mean = "+" if dev_mean >= 0 else ""

        print(f"{point['name']} -> project: {sign_proj}{round(dev_project, 3)} | mean: {sign_mean}{round(dev_mean, 3)}")


height_deviation()