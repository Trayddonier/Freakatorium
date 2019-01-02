import RPi.GPIO as gp
gp.setmode(gp.BOARD)
gp.setup(7, gp.IN)
gp.setup(40, gp.OUT)


try:
        while True:
                if gp.input(7) == True:
                        print("Ein gedrückt")
                        import Freakatorium.py
                
                
except: gp.output(40, True), print("LED grün an")
