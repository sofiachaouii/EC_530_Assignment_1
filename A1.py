import math

Radius = 6371  # Radius of Earth in Kilometers

geoloc_1 = [[33.6196, 7.1257]]  # Benslimane, Morocco
geoloc_2 = [[33.5731, 7.5898], [38.7223, 9.1393], [40.7128, 74.006], [35.2271, 80.8431]]  # Casablanca, Lisbon, NY, Charlotte

def Distance(A1, B1, A2, B2):
    A1, B1, A2, B2 = map(math.radians, [A1, B1, A2, B2])  # Convert degrees to radians
    AD = A2 - A1
    BD = B2 - B1
    k = math.sin(AD / 2)**2 + math.cos(A1) * math.cos(A2) * math.sin(BD / 2)**2
    dist = 2 * math.atan2(math.sqrt(k), math.sqrt(1 - k)) * Radius
    return dist

for PointA in geoloc_1:
    a1, b1 = PointA
    dist = 40075  # Earth's circumference
    m = -1  # Index of closest point

    for i in range(len(geoloc_2)):
        a2, b2 = geoloc_2[i]
        dist1 = Distance(a1, b1, a2, b2)
        if dist1 < dist:
            dist = dist1
            m = i

    print(f"The point closest to ({a1}, {b1}) is {geoloc_2[m]}, and the distance is {dist:.2f} kilometers.")
