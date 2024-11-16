from interface import MedicalEquipmentFactory


from product import (
    Scalpel,
    Stethoscope,
    Forceps,
    TherapyBall,
    ExerciseBike,
    ECGMachine,
    
)

class CardiologyFactory(MedicalEquipmentFactory):
    """Кардиолог

    Args:
        MedicalEquipmentFactory (_type_): _description_
    """

    def create_device(self) -> ECGMachine:
        return ECGMachine()
    
    def create_second_device(self) -> Stethoscope:
        return Stethoscope()


class OrthopedicsFactory(MedicalEquipmentFactory):
    """Ортопед

    Args:
        MedicalEquipmentFactory (_type_): _description_
    """

    def create_device(self) -> TherapyBall:
        return TherapyBall()
    
    def create_second_device(self) -> ExerciseBike:
        return ExerciseBike()
    
class NeurologyFactory(MedicalEquipmentFactory):
    """Нейрохирург

    Args:
        MedicalEquipmentFactory (_type_): _description_
    """

    def create_device(self) -> Scalpel:
        return Scalpel()
    
    def create_second_device(self) -> Forceps:
        return Forceps()

