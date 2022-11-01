from datetime import datetime as dt
from time import time


def spravochnik_loger(info):
    time  = dt.now().strftime('%H:%M')
    with open('spravochnik.csv', 'a') as file:
        file.write(f'{time}  {info}')