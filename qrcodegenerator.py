import qrcode
import image
import os
import time

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5,
)

input1 = input("Enter the Link: ")
date = input1
qr.add_data(date)

qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')
time.sleep(1)
print("50%")
time.sleep(0.7)
print("75%")
time.sleep(0.5)
print("100%")
print("QR Code Generated Successfully")
os.system('qrcode.png')
#Source code by Orel Mizrahi Adani @oremizrahii