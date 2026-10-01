def shortest_distance(kilometers, meters):
    kilometers = kilometers * 1000
    return min(kilometers, meters)
if __name__ == "__main__":
    shortest_distance(1, 500)
    shortest_distance(0.2, 900)
    shortest_distance(1, 1000)
