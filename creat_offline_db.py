from tkintermapview.offline_loading import OfflineLoader
import tkintermapview

database_path = 'file.db'
# position_a = (59.7721, 29.4038)
# position_b = (60.0627, 31.403)
position_a = (69.75, 15.45)
position_b = (55.35, 53.5)
zoom_min = 0
zoom_max = 14

loader = tkintermapview.OfflineLoader(path=database_path, tile_server="https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
loader.save_offline_tiles(position_a, position_b, zoom_min, zoom_max)
