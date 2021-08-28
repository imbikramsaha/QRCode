# pip install qrcode ( at first install qrcode in windows powershell or command prompt or your mac / linux Terminal )

import qrcode
img = qrcode.make("imbikramsaha@zohomail.in")
img.save("Zohomail.jpg")
