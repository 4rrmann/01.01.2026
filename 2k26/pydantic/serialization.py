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

# print(patient1)

# print('\n',patient1.name)
# print(patient1.address.city)
# print(patient1.address.pin)

#Dictionary:
# temp = patient1.model_dump(include=['name', 'gender'])
# temp = patient1.model_dump(exclude=['name', 'gender'])
temp = patient1.model_dump(exclude={'address':['state']})
print(temp)
print(type(temp))

#Json:
temp = patient1.model_dump_json()
print(temp)
print(type(temp))