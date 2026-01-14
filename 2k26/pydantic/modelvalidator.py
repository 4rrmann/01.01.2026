from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

#if a paitent age>60 then they must have emergency phone no.
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Paitents older than 60 must have emergency contact')
        return model


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted!')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated!')

patient_info = {'name': 'arman',
                'email':'kunzairen@hdfc.com',
                'age': 69, 'weight': '57',
                'married':False,
                'allergies': ['college', 'past'],
                'linkedin_url':'https://www.linkedin.com/in/armanahmad16/',
                 'contact_details':{'phone':'6394214600', 'emergency':'64738492'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)