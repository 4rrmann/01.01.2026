from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float #kg
    height: float #meter
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

#now we have to add the 'bmi' section by our own:
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted!')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI:',patient.bmi)
    print('updated!')

patient_info = {'name': 'arman',
                'email':'kunzairen@hdfc.com',
                'age': '20', 'weight': 57, 'height': 1.778,
                'married':False,
                'allergies': ['college', 'past'],
                'linkedin_url':'https://www.linkedin.com/in/armanahmad16/',
                 'contact_details':{'phone':'6394214600'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)