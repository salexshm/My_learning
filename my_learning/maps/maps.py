import folium
from flask import Flask, render_template

from geopy.distance import geodesic

app = Flask(__name__)


@app.route('/')
def index():
    # Создание карты
    map_object = folium.Map(location=[42.315521, 69.586942], zoom_start=12)  # Центр: Германия

    # Добавление метки
    folium.Marker([42.315521, 69.586942], tooltip="Шымкент").add_to(map_object)

    coordinates = [
        [42.320218, 69.591419],  # ЮКГУ
        [42.318915, 69.596761],  # Тауке-Хана - Байтурсынова
        [42.330684, 69.601671],  # Байтурсынова - Маделикожа
        [42.329212, 69.608599]  # Маделикожа
    ]

    for point in coordinates:
        folium.Marker(point).add_to(map_object)

    # Рисуем линию между точками
    folium.PolyLine(coordinates, color="blue", weight=2.5).add_to(map_object)

    # Добавление линии на карту
    folium.PolyLine(
        locations=coordinates,
        color='blue',
        weight=5,
        opacity=0.8
    ).add_to(map_object)

    # total_distance = 0  # В километрах
    # for i in range(len(coordinates) - 1):
    #     segment_distance = geodesic(coordinates[i], coordinates[i + 1]).kilometers
    #     total_distance += segment_distance
    #     print(f"Расстояние между {coordinates[i]} и {coordinates[i + 1]}: {segment_distance:.2f} км")


    # Сохранение карты во временный HTML-файл
    map_object.save("templates/index.html")

    return render_template("index.html")  # Возвращаем готовую страницу с картой


if __name__ == '__main__':
    app.run(debug=True)
# m = folium.Map(location=(42.315521, 69.586942), zoom_start=14, tiles="cartodb positron")

