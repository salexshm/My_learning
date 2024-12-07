from geopy.distance import distance
# from geopy import distance
from geopy.point import Point
import folium

coordinates = [
    [42.320218, 69.591419],  # ЮКГУ
    [42.318915, 69.596761],  # Тауке-Хана - Байтурсынова
    [42.330684, 69.601671],  # Байтурсынова - Маделикожа
    [42.329212, 69.608599]  # Маделикожа
]

# print(distance.distance(coordinates[0], coordinates[1]).km)

# Начальная точка
start_point = coordinates[0]

# Задаём расстояние в километрах и направление (азимут в градусах)
distance_km = 0.46354303489580473  # Расстояние в километрах
bearing = 110      # Направление: 90° (восток)

# Нахождение новой точки
new_point = distance(kilometers=distance_km).destination(start_point, bearing)

# Распечатываем новую точку
print(f"Координаты новой точки: {new_point.latitude}, {new_point.longitude}")


