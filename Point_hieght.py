points = [
    {"name": "P1", "height": 152.3},
    {"name": "P2", "height": 149.8},
    {"name": "P3", "height": 151.2}
]

project_high = 150.00

def point_height (*args):
    for point in points :
        for key,value  in point.items() :
            deviation = project_high - point ["height"]
        print(f"deviation from the mean:{point['name']} , {round (deviation ,3 )}")
                #print(f"deviation from the mean:{point["name"]}, = {deviation} ")





point_height(points)
