import random

gramy = "tak"

podanie = []
wylosowane = []

while gramy == "tak":
      for i in range (6):
        podanie.append(int(input("Podaj liczbę numer"+str(i+1)+":")))
        wylosowane.append(random.randint(1,50))
trafione = 0
for z in podane:
      for j in wylosowane:
          if z == j:
             trafione = trafione + 1

             print("Twój wynik to: "+str(trafione))
             print("Wylosowane liczby:")
      for i in wylosowane:
        print(i)
        podanie.clear()
        wylosowane.clear()
        gramy = imput("Czy chcesz zagrać jeszcze raz? (tak/nie) ")
    
                  
                                 

