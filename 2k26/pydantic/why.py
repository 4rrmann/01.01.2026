from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50chars', examples=['Arman Ahmad','Md. Awaiz','Sohan Sarkar'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)] #greater than 0, Strictly only in float data-type
    married: Optional[bool] = False
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_details: Dict[str, str]

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
                'email':'kunzairen@gmail.com',
                'age': 20, 'weight': 57,
                # 'married':True,
                'allergies': ['college', 'past'],
                'linkedin_url':'https://www.linkedin.com/in/armanahmad16/',
                 'contact_details':{'phone':'6394214600'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)