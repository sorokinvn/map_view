import tkinter as tk
from PIL import Image, ImageTk
import geopandas as gpd
import matplotlib.pyplot as plt
import io

# 1. Чтение SHP-файла
shp_file_path = "leningrad_01.shp"
try:
    gdf = gpd.read_file(shp_file_path)
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")
    exit()

# 2. Создание окна Tkinter и Canvas
root = tk.Tk()
root.geometry('1024x768')

canvas = tk.Canvas(root, width=1000, height=700, bg="white")
canvas.pack()

# 3. Отображение данных на Matplotlib-графике
fig, ax = plt.subplots()
gdf.plot(ax=ax, edgecolor='black')
plt.title("SHP-файл")
# plt.axis('off') # Отключаем оси

# 4. Сохранение графика в буфер памяти
buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
buf.seek(0)

# 5. Перенос изображения на Canvas
img = Image.open(buf)
photo = ImageTk.PhotoImage(img)

canvas.create_image(0, 0, anchor=tk.NW, image=photo)

root.mainloop()