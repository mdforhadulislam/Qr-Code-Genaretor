import qrcode
import random

url = input("Enter Url/Any Text :" )

qr = qrcode.QRCode(version=15,box_size=10,border=5)

data = url
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
input_file_name=input("Enter File Name: ")
file_name=input_file_name+str(random.randint(0,10))
img.save(f"{file_name}.png")