#import connection function here.............
from connect import db_connect
import psycopg2
import qrcode
from io import BytesIO


connection = db_connect()

cur = connection.cursor()
# def generate_qr_code(data):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#     qr_img = qr.make_image(fill_color="black", back_color="white")
#     img_byte_array = BytesIO()
#     qr_img.save(img_byte_array)
#     return img_byte_array.getvalue()

# qr_data = generate_qr_code("hello wolrd")
def upload(qr_binary_image_form):
    '''
    this function accepts data in binary data of the QR code image
    '''
# Execute a command: create datacamp_courses table
    cur.execute("""
            CREATE TABLE IF NOT EXISTS qrcode(
            id BIGSERIAL PRIMARY KEY,
            code_data BYTEA)
            
            """)
    try:
        cur.execute(
            """
            INSERT INTO qrcode(code_data)
            VALUES (%s)
            """,
            (psycopg2.Binary(qr_binary_image_form),)
        )
        print("inserted succesfully")
        connection.commit()


    except (Exception, psycopg2.Error) as error:
        print("Error inserting QR code into database:", error)
# Make the changes to the database persistent
# Close cursor and communication with the database
    finally:

        cur.close()
        connection.close()


# pass in the binary dat of the qr image downloaded
upload()