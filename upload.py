#!/usr/bin/env python
#!/usr/bin/env python

from database import connect
import psycopg2
from io import BytesIO


connection = connect()

cur = connection.cursor()

def upload(filename, employee_information):
    '''
    this function accepts data in binary data of the QR code image
    '''
    # Execute a command: create datacamp_courses table
    try: 
        employee_name = employee_information["employee_name"]
        personal_website = employee_information["personal_website"]
        phone_number = employee_information["phone_number"]
        email_address = employee_information["email_address"]
        qr_image = filename

        query = """INSERT INTO qrcode (employee_name, personal_website,
            phone_number,
            email_address,
            qr_image)
            VALUES (%s, %s, %s, %s, %s)
            (employee_name, personal_website, phone_number, email_address, qr_image)
            """
        # cur.execute(
        #     """
        #     INSERT INTO qrcode(code_data)
        #     VALUES (%s)
        #     """,
        #     (psycopg2.Binary(employee_information),)
        # )
        print("inserted succesfully")
        connection.commit()


    except (Exception, psycopg2.Error) as error:
        print("Error inserting QR code into database:", error)
        # Make the changes to the database persistent
        # Close cursor and communication with the database
    finally:
        cur.close()
