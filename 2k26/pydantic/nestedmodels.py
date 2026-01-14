from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Paient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city':'Shaheenbagh', 'state':'Delhi', 'pin':'110025'}
address1 = Address(**address_dict)

patient_dict = {'name':'Arman', 'gender':'male', 'age':20, 'address': address1}
patient1 = Paient(**patient_dict)

print(patient1)

print('\n',patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

#better Organisation of related data (e.g., vitals, address, insurance)
#Reusability: use vitals in multiple models (e.g., Patient, MedicalRecord)
#Readability: easier for developers and API consumers to understand
#Validation: nested models are validated automatically -no extra work needed