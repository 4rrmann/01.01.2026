from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

#specific domain on email:
    @field_validator('email') #whom
    @classmethod              #on what

    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        #abc@'gmail'.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

#capital caps NAME of the paitent:
    @field_validator('name')
    @classmethod
    #ARMAN
    def transform_name(cls, value):
        return value.upper()
    
#we can operate @field_validator in two modes: (before & after)
    @field_validator('age', mode='after') #by default mode='after'
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


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
                'age': '20', 'weight': 57,
                'married':False,
                'allergies': ['college', 'past'],
                'linkedin_url':'https://www.linkedin.com/in/armanahmad16/',
                 'contact_details':{'phone':'6394214600'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)