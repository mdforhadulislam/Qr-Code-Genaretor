import qrcode
import random

url = input("Enter Url/Any Text :" )

qr = qrcode.QRCode(version=15,box_size=10,border=5)

data = url
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
file_name="test"+str(random.randint(0,10000000))
img.save(file_name+".png")