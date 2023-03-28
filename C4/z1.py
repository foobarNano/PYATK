from math import ceil

def tile_calc(floor_length, floor_width, tile_length, tile_width, tiles_per_box) -> int:
    tiles_num = (floor_length / tile_length) * (floor_width / tile_width) * 1.1
    return ceil(tiles_num / tiles_per_box)

print("Potrzeba : " + str(tile_calc(4, 4, 0.20, 1, 10)))
