# Библиотека lib_optics

## Преломление света

### 1 Нахождение угла преломления
```python
r = RefractionLightClass()
medium_one = "water"
medium_two = "air"
angle = 40 
print(r.get_angle_refraction(angle, medium_one, medium_two))
```
### 2 Построение хода лучей на графике
```python
r.build_graph(angle, medium_one, medium_two)
```
![alt картинка](https://i.ibb.co/0Mj3ZQS/image.png)
### 3 Загрузка пользовательского файла с коэффициентами преломления сред
```python
r.set_refractive_indexes("my_files.csv")
```
### 4 Настройка стиля для графика преломления

##Построение графиков

### 1 Действительный объект находится дальше фокусного расстояния собирательной линзы
```python
x = BiconvexLens(dist_subject=15, focal_length=8, height_subject=5)
x.display_graphic()
```
![alt картинка](https://i.ibb.co/pxL1PKH/image.png)

### 2 Действительный объект находится внутри фокусного расстояния собирательной линзы
```python
x = BiconvexLens(dist_subject=4, focal_length=5, height_subject=5)
x.display_graphic()
```
![alt картинка](https://i.ibb.co/CBVzX0v/image.png)

### 3 Действительный объект находится на фокусном расстоянии от собирательной линзы 
```python
x = BiconvexLens(dist_subject=10, focal_length=10, height_subject=5)
x.display_graphic()
```

### 4 Действительный объект находится дальше фокусного расстояния рассеивающей линзы
```python
lens = BiconcaveLens(dist_subject=8, focal_length=5, height_subject=3)
print(lens.get__dist_image())
lens.display_graphic()
```
![alt картинка](https://i.ibb.co/fCqjSG7/image.png)
  
### 5 Точка находится дальше фокусного расстояния рассеивающей линзы
```python
lens = BiconcaveLens(dist_subject=10, focal_length=5, height_subject=0)
print(lens.get__dist_image())
lens.display_graphic()
```
![alt картинка](https://i.ibb.co/qNBcp9V/image.png)

### 6 Настройка стиля для отображения линзы и лучей
