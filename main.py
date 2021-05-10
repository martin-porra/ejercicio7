from clase import FechaHora
from clase import Hora

def __add__(self, fecha):
  print('hola')
  a = self.int + int(fecha.hora())

if __name__ == '__main__':
 d = int(input("Ingrese Dia: "))
 mes = int(input("Ingrese Mes: "))
 a = int(input("Ingrese Año: "))
 h = int(input("Ingrese Hora: "))
 m = int(input("Ingrese Minutos: "))
 s = int(input("Ingrese Segundos: "))
 f = FechaHora(d, mes, a, h, m, s)
 f.Mostrar()
 h1 = int(input("Ingrese Hora: "))
 m1 = int(input("Ingrese Minutos: "))
 s1 = int(input("Ingrese Segundos: "))
 r = Hora(h1, m1, s1)
 r.mostrar()
 f2 = f + r
 f2.Mostrar()
 f3 = r + f
 f3.Mostrar()
 f4 = f3 - 1  # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de
    # días indicada por el número entero
 f4.Mostrar()
 #f4 = 1 + f2  # suma un día a un objeto FechaHora

