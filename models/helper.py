import uuid0
import qrcode
from pydantic import BaseModel
# """Generates a UUID for an employee and creates a QR code encoding their name, 
# employee ID, and generated UUID.

# The generate_uuid function generates a random UUID for the given employee name and ID.
# The generate_qr_code function takes a dict with employee name, ID, and UUID, and creates a QR code 
# encoding that data. The QR code is saved to a PNG file named after the employee. The filename is returned.
# """


class User(BaseModel):
    user_name:str
    personal_website : str = None
    phone_number : int
    email_address: str
    employee_id: str
    employee_uuid: str = None
    

#TODO add encryption for sensitive data
def generate_uuid(input_data:dict) -> str:
    user_details = input_data
    uuid = str(uuid0.generate())
    return uuid


def generate_qr_code(**data:dict) -> str:
    "This function creates and save our qrcode information"
    #TODO check what data type is data
    employee_information = User(**data)
    employee_uuid = generate_uuid(employee_information)
    employee_information.employee_uuid = employee_uuid
    img = qrcode.make(employee_information)
    filename = "{}_{}.png".format( employee_information.user_name, employee_information.employee_uuid) 
    img.save(filename)
    return filename

info = {
    "user_name": "Fred",
    "personal_website" : "Fred_x.io",
    "phone_number" : "07042802954",
    "email_address": "jlsdjnpsoiq",
    "employee_id": "123444"
    
}

# generate_qr_code(**info)
