def euclideanDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

points = [(1,2),(2,5),(0,5),(2,8),(2,3)]
distances = []
i=0
while i < len(points):
    j= i +1
    while j<len(points):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        j=j+1
    i=i+1
print(f"Minimum distance between the points is : {min(distances)}")