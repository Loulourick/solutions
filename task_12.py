def shortest_distance(kilometers, meters):
    kilometers = kilometers * 1000
    if kilometers < meters: return kilometers
    elif kilometers > meters: return meters
    if kilometers == meters: return max(kilometers, meters)
print (shortest_distance(1, 500))
print (shortest_distance(0.2, 900))
print (shortest_distance(1, 1000))