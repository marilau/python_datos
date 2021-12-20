import numpy as np

l = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([6, 7, 8, 9, 10])

#Saber el tipo de array
print(type(a1))

# Array de una dimensión
a4 = np.array([1, 2, 3])
print(a4.ndim)
print(a4.shape)

# Array de dos dimensiones
a5 = np.array([[1, 2, 3], [4, 5, 6]])
print(a5.ndim)
print(a5.shape)

# Array de tres dimensiones
a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a3.ndim)
print(a3.shape)
print(a3.size)
print(a3)

suma = a1 + a2 
print(suma)

#Mostrar el tipo de los datos que contiene el array
print(suma.dtype)

#Acceder al 2do elemento del array
print(suma[1])

#Saltarme los primeros elementos y sacar el último
print(suma[2:4])
#Cuando no sé cuántos elementos me traerá el archivo
print(suma[2:-2])

#Asignar un valor
a4[2] = 1000
print(a4)

#Broadcasting
r = a1 * 10
print(r)

a = np.array([[i for i in range(10)],
				 [i for i in range(10, 20)],
				 [i for i in range(20, 30)],
				 [i for i in range(30, 40)]], dtype=np.float64)
print(a)

#Seleccionar de 2 en 2 para filas y columnas
#print(a[::2,::2])

#Otras formas de seleccionar
#Seleccionar solo la fila 1 y de la columna hasta el elemento 3
print(a[1,:3])

#ALEATORIOS
b = np.arange(1, 10, 3)
print(b)

#linspace, para que sea x distante, se usa mucho para graficar los ejes x e y
c = np.linspace(-10, 10, 10)
print(c)

d = np.random.rand(3, 3)
print(d)

#Con distribución normal
e = np.random.randn(3, 3)
print(e)

#Matriz identidad
i = np.eye(3)
print(i)

j = np.identity(3)
print(j)


f = np.array([1, 3, 4])
g = np.repeat(f, 5)
print(g)

#Matriz de unos
unos = np.ones((4, 3), dtype=np.int64)
print(unos)

#Matriz de ceros
ceros = np.zeros((3, 2), dtype=np.int64)
print(ceros)

#Copias
co = np.arange(1, 10)
cop = np.copy(co)
cop[1] = 100
print(co)
print(cop)

#Promedio
prom = co.mean()
print(prom)

#Máximo y mínimo
maximo = co.max()
minimo = co.min()
print(maximo)
print(minimo)

#Desvío estándar
desvio = co.std()
print(desvio)

#O bien
desvio = np.std(co)
print(desvio)

#Lectura de achivos con numpy
filedata = np.loadtxt('data.txt', delimiter=',')
print(filedata)

filedata1 = np.genfromtxt('data.txt', delimiter=',')
print(filedata1)

#Filtros
x = np.linspace(1, 200, 10)
print(x)
print(x>100)
print(x[x>100])