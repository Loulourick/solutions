def pasture_area(wire, w):
    l = (wire - 2 * w) / 3
    return l * w
def best_pasture(wire):
    w = wire / 4
    l = (wire - 2 * w) / 3
    area = pasture_area(wire,w)
    return (w, l, area)
# def best_pasture(wire):
#     best_w = 0.0
#     best_area = 0.0
#     step = 0.1
#     w = 0.0
#     while w <= wire / 2:
#         area = pasture_area(wire,w)
#         if area > best_area:
#             best_area = area
#             best_w = w
#         w += step
#     best_l = (wire - 2 * best_w) / 3
#     return (best_w, best_l, best_area)
if __name__ == "__main__":
    pasture_area(100, 25)     # 416.666...
    pasture_area(100, 10)     # 266.666...
    pasture_area(100, 50)    # 0.0    вся проволока ушла на ширину
    best_pasture(100)        # (25.0, 16.666..., 416.666...)
    best_pasture(60)          # (15.0, 10.0, 150.0)
    best_pasture(12)          # (3.0, 2.0, 6.0)