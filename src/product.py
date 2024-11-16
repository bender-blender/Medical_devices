from interface import (
    SurgicalInstrument,
    RehabilitationDevice,
    DiagnosticDevice
    )
from random import randint
import time

class ECGMachine(DiagnosticDevice):
    """Экг машина 

    Args:
        DiagnosticDevice (_type_): _description_
    """
    def inspection(self) -> str:
        print("Подождите, идет обследование сердца...")
        

        sec = 0
        blows = 0
        while sec != 60:
            print(sec)
            time.sleep(1)
            sec += 1
            blows += randint(0,2)


        return f"Сердцебиение {blows} ударов в минуту!"
    


class Stethoscope(DiagnosticDevice):
    """Стетоскоп

    Args:
        DiagnosticDevice (_type_): _description_
    """
    def inspection(self) -> str:
        return f"измерении артериального давления для прослушивания тонов от пульсирующей пережатой артерии"
    

class Scalpel(SurgicalInstrument):
    """Скальпель

    Args:
        SurgicalInstrument (_type_): _description_
    """
    def inspection(self) -> str:
        return "Выполнен надрез"


class Forceps(SurgicalInstrument):
    """Щипцы

    Args:
        SurgicalInstrument (_type_): _description_
    """

    def inspection(self) -> str:
        return "Оттянуть ткань"
    

class ExerciseBike(RehabilitationDevice):
    """Велосипед

    Args:
        RehabilitationDevice (_type_): _description_
    """
    def __init__(self):
        self.speed = 0

    def inspection(self) -> str:
        self.speed += 10
        return f"Разогнали велосипед до {self.speed}км/год"
    

class TherapyBall(RehabilitationDevice):
    """Мяч
    """

    def inspection(self):
        
        return f"Пациент с мячом"
    