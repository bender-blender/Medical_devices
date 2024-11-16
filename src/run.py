from factory import (
    NeurologyFactory,
    CardiologyFactory,
    OrthopedicsFactory
)
from interface import MedicalEquipmentFactory





def client_code(factory:MedicalEquipmentFactory):
    item_one = factory.create_device()
    item_two = factory.create_second_device()
    print(item_one.inspection())
    print(item_two.inspection())

client_code(NeurologyFactory())
client_code(CardiologyFactory())
client_code(OrthopedicsFactory())