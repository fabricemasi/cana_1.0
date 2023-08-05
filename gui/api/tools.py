import time


def pause(t: int, arg="Pause"):  # Fait une pause | arg1: temps de pause | arg2: element a printer
    print(arg, "("+str(t)+"sec)")
    time.sleep(t)
