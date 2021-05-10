

class FechaHora:
    __año : ''
    __mes = ''
    __dia = ''
    __minuto = ''
    __hora = ''
    __segundos = ''

    def __init__(self,año = '2020', mes = '1', dia = '1', hora = '0', minuto = '0', segundo = '0'):
       if int(año) < 2022:
        self.__año = año
       else:
         self.__año = 2020
       if int(mes) <= 12:
         self.__mes = mes
       else:
        self.__mes = 1
       if int(dia) <= 31:
        self.__dia = dia
       else:
        self.__dia = 1
       if int(hora) <= 24:
        self.__hora = hora
       else:
         self.__hora = 0
       if int(minuto) <= 60:
        self.__minuto = minuto
       else:
        self.__minuto = 0
       if int(segundo) <= 60:
        self.__segundos = segundo
       else:
         self.__segundos = 0
       if mes == 2 and dia > 28:
         if not año % 4 and (año % 100 or  not año % 400):
           print('a')
           self.__dia = 29
         else:
             self.__dia = 28
       if mes == 4 and dia == 31:
         self.__dia = 30
       if mes == 6 and dia == 31:
         self.__dia = 30
       if mes == 9 and dia == 31:
         self.__dia = 30
       if mes == 11 and dia == 31:
         self.__dia = 30


    def Mostrar(self):
     print(  'fecha :' + str(self.__dia)  + '/' + str(self.__mes) + '/' + str(self.__año) + '  hora :' + str(self.__hora) + 'h '+ str(self.__minuto) + 'm ' + str(self.__segundos) + 's' )
    def PonerEnHora(self,hora = 25, minuto = 61, segundo = 61):
        if int(hora) <= 24:
            self.__hora = hora
        if int(minuto) <= 60:
           self.__minuto = minuto
        if int(segundo) <= 60:
           self.__segundos = segundo
    def AdelantarHora(self, hora = 0, minuto = 0):
        self.__hora = int(self.__hora) + int(hora)
        self.__minuto = int(self.__minuto) + int(minuto)
        if self.__minuto > 60:
          self.__minuto =  self.__minuto - 60
          self.__hora = self.__hora + 1
          if self.__hora > 24:
            self.__hora =   self.__hora - 24
            self.__hora = self.__hora - 1
            self.__dia = self.__dia +1
            if self.__mes == 12:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
                if self.__mes > 12:
                  self.__mes =  self.__mes  - 12
                  self.__año = self.__año + 1
            elif self.__mes == 1:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 3:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 5:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 7:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 8:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 10:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 4:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 6:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 9:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 11:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 2:
              if self.__dia > 28:
                if not self.__año % 4 and (self.__año % 100 or not self.__año % 400):
                   if self.__dia == 29:
                     self.__mes = 2
                     self.__dia = 29
                   else:
                     self.__mes = 3
                     self.__dia = 1
                else:
                  self.__dia = self.__dia - 28
                  self.__mes = self.__mes + 1


    def __add__(self, hora):
        dia = 0
        min = 0
        ho = 0
        seg = self.__segundos + hora.seg()
        if seg > 60:
          seg = seg - 60
          min =  1
        min = min + self.__minuto + hora.min()
        if min > 60:
          min = min - 60
          ho =  1
        ho = ho + self.__hora + hora.hora()
        if ho > 24:
          ho = ho - 25
          dia = 1
        return  FechaHora(0,0,dia,ho,min,seg)

    def seg(self):
        return self.__segundos
    def min(self):
        return  self.__minuto
    def hora(self):
        return  self.__hora

    def __sub__(self, num):
        dia = self.__dia
        año = self.__año
        mes = self.__mes
        if mes == 0 and año == 0 and dia == 0:
            print('no se puede restar por que dia, mes y año son 0')
        else:
         while num > dia or año == 0:
           dia = dia + 31
           mes = mes - 1
           if mes == 0:
            mes =  mes + 12
            año = año - 1
         dia = dia - num
        return FechaHora(año,mes,dia,self.__hora,self.__minuto,self.__segundos)


class Hora:
    __hora = 0
    __minuto = 0
    __segundo = 0

    def __init__(self,hora = 0,minu = 0,seg = 0):
        if int(hora) <= 24:
            self.__hora = hora
        else:
            self.__hora = 0
        if int(minu) <= 60:
            self.__minuto = minu
        else:
            self.__minuto = 0
        if int(seg) <= 60:
            self.__segundo = seg
        else:
            self.__segundo = 0

    def mostrar (self):
        print('hora :' + str(self.__hora) + 'h '+ str(self.__minuto) + 'm ' + str(self.__segundo) + 's' )
    def seg (self):
        return  self.__segundo
    def min(self):
        return  self.__minuto
    def hora(self):
        return self.__hora

    def __add__(self, fecha):
        dia = 0
        min = 0
        ho = 0
        seg = self.__segundo + fecha.seg()
        if seg > 60:
            seg = seg - 60
            min = 1
        min = min + self.__minuto + fecha.hora()
        if min > 60:
            min = min - 60
            ho = 1
        ho = ho + self.__hora + fecha.hora()
        if ho > 24:
            ho = ho - 25
            dia = 1
        return FechaHora(0, 0, dia, ho, min, seg)



