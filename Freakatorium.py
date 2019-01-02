

import time, threading, random, RPi.GPIO as gp

gp.setmode(gp.BOARD)

gp.setup((7, 11, 12,13), gp.IN)

gp.setup((16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38, 40, 15), gp.OUT)
RPWM = gp.PWM(32, 200)

random.seed()
EA = random.randint(1,5)
P = random.randint(1,100)

def Lämpchen():
  while True:
    if gp.input(13) == False:
      gp.output(15, True)
      print("LED rot an")
    else: break
      

def Venti():
  while True:
    if gp.input(13) == False:
      gp.output(16, True)
      print("Ventilator läuft")
    else: break

def Heizung():
  while True:
    if gp.input(13) == False:
      gp.output(18, True)
      #print("Heizung läuft")
    else: break
 
def Strasselicht():
  while True:
    if gp.input(13) == False:
      gp.output(29, True)
      #print("Strasenlicht läuft")
    else: break

def Defekt():
  while True:
    if gp.input(13) == False:
      time.sleep(EA)
      gp.output(31, True)
      #print("Defektes Strasenlicht läuft")
      time.sleep(EA)
      gp.output(31, False)
      #print("Defektes Strasenlicht läuft nicht")
    else: break
 
def Arbeitslicht():
  while True:
    if gp.input(13) == False:
      time.sleep(2)
      gp.output(33, True)
      #print("Arbeitslicht läuft")
      time.sleep(3)
      gp.output(33, False)
      #print("Ornamentlicht läuft")
    else: break

  
def Türlicht():
  while True:
    if gp.input(13) == False:
      gp.output(35, True)
      #print("Türlicht 1 läuft")
      time.sleep(2)
      gp.output(35, False)
      #print("Türlicht 1 läuft nicht")
      gp.output(36, True)
      #print("Türlicht 2 läuft")
      time.sleep(2)
      gp.output(36, False)
      #print("Türlicht 2 läuft nicht")
      gp.output(37, True)
      #print("Türlicht 3 läuft")
      time.sleep(2)
      gp.output(37, False)
      #print("Türlicht 3 läuft nicht")
      gp.output(38, True)
      #print("Türlicht 4 läuft")
      time.sleep(2)
      gp.output(38, False)
      #print("Türlicht 4 läuft nicht")
    else: break

def Pulsierend():
  while True:
    if gp.input(13) == False:
      gp.output(32, True)
      #print("Pulsierendes Strasenlicht läuft")
      RPWM.start(P), time.sleep(0.2)
    else: break
  
#def Manuell():
#  while True:
#    if gp.input(11) and gp.input(12) == True:
#      print("Dampf manuell ein")
#      gp.output(22, True), time.sleep(6)
#      gp.output(22, False)
#      print("Dampf manuell aus")
    
def Ready():
  try:
    while True:
      if gp.input(12):
        for count in range(0,1200,1):
          if gp.input(12):
            count = count+1
            time.sleep(1)
          if (count <= 1200):
            print("Dampf ready")
          if (count >=1200):
            print("Dampfprogramm EIN")
            gp.output(22, True), time.sleep(6)
            gp.output(22, False)
            print("Dampfprogramm AUS")
  except: print("Dampfmaschine nicht ready")
  
def Ende():
  while True:
    if gp.input(13) == True:
      gp.output((18, 22, 29, 31, 32, 33, 35, 36, 37, 38, 40, 15), False)
      gp.output(16, True), time.sleep(3)#1800
      gp.output(16, False)
      print("Programm Ende: Danke före iisatz!")
      time.sleep(2)
      gp.cleanup()
      exit()


Lämpchen = threading.Thread(target=Lämpchen)
Venti = threading.Thread(target=Venti)
Heizung = threading.Thread(target=Heizung)
Strasselicht = threading.Thread(target=Strasselicht)
Defekt = threading.Thread(target=Defekt)
Arbeitslicht = threading.Thread(target=Arbeitslicht)
Türlicht = threading.Thread(target=Türlicht)
Pulsierend = threading.Thread(target=Pulsierend)
#Manuell = threading.Thread(target=Manuell)
Ende = threading.Thread(target=Ende)
Ready = threading.Thread(target=Ready)

Lämpchen.start()
#time.sleep(0.1)
Venti.start()
#time.sleep(0.1)
Heizung.start()
#time.sleep(0.1)
Strasselicht.start()
#time.sleep(0.1)
Defekt.start()
#time.sleep(0.1)
Arbeitslicht.start()
#time.sleep(0.1)
Türlicht.start()
#time.sleep(0.1)
Pulsierend.start()
#time.sleep(0.1)
Ende.start()
#time.sleep(0.1)
#Manuell.start()
#time.sleep(0.1)
Ready.start()






