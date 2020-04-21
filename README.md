# Библиотека lib_optics
<p> lib_optics - это библиотека для визуализации физических процессов, происходящих в рамках геометрической оптики. С помощью данной библиотеки возможна визуализация процессов распространения света в различных средах, его отражения и преломления. С помощью lib_optics так же возможно производить построения изображений при прохождении света в тонких линзах в зависимости от положения объекта относительно фокусного расстояния линзы. Данная библиотека располагает обширной базой данных о коэффициентах преломления в разных средах, а также допускает настройку пользователем стилей построенных с ее помощью графиков и загрузку файлов с данными о коэффициентах преломления сред. 
</p>

## Преломление света

### 1 Нахождение угла преломления
<p>Углы указываются в граудсах</p>
<p>Информация о первой и второй среде указывается:</p>

* как строковое имя среды 
* либо числовой коэффициент преломления среды

```python
r = RefractionLightClass()
# пример строкового параметра среды
medium_one = "water"
medium_two = "air"
angle = 40 
print(r.get_angle_refraction(angle, medium_one, medium_two))

# 58.935271735411426
```

Другие доступные среды и их коэффициенты указаны в файле: https://github.com/Korgutlova/lib_optics/blob/master/files/list_of_refractive_indices.csv

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
  <img width="400" height="300" src="https://i.ibb.co/Vw71j4z/refraction.png">
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
<p>Пользовательский файл не должен содержать заголовков и должен содержать данные в следующем формате:</p>

* первый параметр - строковое название среды
* второй параметр - коэффициент преломления среды

<p>Пример возможного файла .csv</p>

|  |  |
|-------|-------|
| air | 1 |
| water | 1.3 |
| lens | 1.396 |


```python
# в качестве параметра указывается путь к файлу 'my_file.csv' с коэффциентами
# путь может быть относительным или абсолютынм
r.set_refractive_indexes("my_file.csv")
```
### 4 Настройка стиля для графика преломления
<p>График можно настраивать, указывая различные цвет для дуг, лучей, фона</p>

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

## Построение изображений в тонких линзах

<p>Библиотека предоставляет 2 класса линз:</p> 

* BiconvexLens — двояковыпуклая собирательная линза 
* BiconcaveLens(двояковогнутая рассеивающая линза

<p>Для создания объекта линзы нужно указать хотя бы 2 из трёх параметров:</p> 

* dist_subject — расстояние от линзы до объекта
* dist_image — расстояние от линзы до изображения
* focal_length — фокусное расстояние линзы

<p>Для проведения вычислений и построения графиков необходимо указать высоту объекта — height_subject.<br>Все остальные данные, а также график строятся на основании этих входных данных.</p>

### 1 Действительный объект находится дальше фокусного расстояния собирательной линзы
```python
x = BiconvexLens(dist_subject=15, focal_length=8, height_subject=5)
x.display_graphic()
```
<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/wYv3drt/1-case.png">
</p>

### 2 Действительный объект находится внутри фокусного расстояния собирательной линзы
```python
x = BiconvexLens(dist_subject=4, focal_length=5, height_subject=5)
x.display_graphic()
```
<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/JB0d3NP/2-case.png">
</p>

### 3 Действительный объект находится в фокусе собирательной линзы 
```python
x = BiconvexLens(dist_subject=10, focal_length=10, height_subject=5)
x.display_graphic()
```
<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/rtLkVWF/3-case.png">
</p>

### 4 Действительный объект находится дальше фокусного расстояния рассеивающей линзы
```python
lens = BiconcaveLens(dist_subject=8, focal_length=5, height_subject=3)
print(lens.get__dist_image())
# 3.076923076923077
lens.display_graphic()
```
<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/Km3wKDs/4-case.png">
</p>
  
### 5 Точка находится дальше фокусного расстояния рассеивающей линзы
```python
lens = BiconcaveLens(dist_subject=10, focal_length=5, height_subject=0)
lens.display_graphic()
```
<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/fYpm4n4/5-case.png">
</p>

### 6 Настройка стиля для отображения линзы и лучей
```python
x = BiconvexLens(dist_subject=7, focal_length=10, height_subject=5)
# указание цвета "blue" для отметки фокусного расстояния
x.graph.focus_color = "blue"
# указание цвета "magenta" сокращенно "m" для объекта
x.graph.subject_color = "m"
# указание цвета "red" для изображения объекта
x.graph.image_color = "red"
x.display_graphic()
```
<p align="center">
  <img width="400" height="300" src="https://i.ibb.co/hd22v2K/6-case.png">
</p>
