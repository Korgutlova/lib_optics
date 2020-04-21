# Библиотека lib_optics

## Преломление света

### 1 Нахождение угла преломления
<p>Углы указываются в граудсах</p>
<p>Информация о первой и второй среде указывается:</p>

* как строковое имя среды 
* либо числовый коэффициент преломления среды

```python
r = RefractionLightClass()
medium_one = "water"
medium_two = "air"
angle = 40 
print(r.get_angle_refraction(angle, medium_one, medium_two))

# 58.935271735411426
```
### 2 Построение хода лучей на графике
<p>Случай, когда луч преломляется</p>

```python
r = RefractionLightClass()
medium_one = "water"
medium_two = "air"
angle = 40 
r.build_graph(angle, medium_one, medium_two)
```
<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/PZBnNYg/refraction.png">
</p>

<p>Случай, когда луч отражается</p>

```python
r = RefractionLightClass()
r.build_graph(50, 2, 1)
```
<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/vYRwPpM/reflection.png">
</p>

### 3 Загрузка пользовательского файла с коэффициентами преломления сред
```python
r.set_refractive_indexes("my_file.csv")
```
### 4 Настройка стиля для графика преломления
<p>График можно настраивать указывая различные цвет для дуг, лучей, фона</p>

```python
r = RefractionLightClass()
# указание цвета "black" для падающего луча
r.graph.first_ray_color = "black"
# указание цвета "pink" для заливки второй среды
r.graph.second_medium_color = "pink"
# указание цвета "teal" для преломляющегося луча
r.graph.second_ray_color = "teal"
r.build_graph(35, 1.5, 2)
```

<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/RStVmPK/refraction-style.png">
</p>

## Построение графиков

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
