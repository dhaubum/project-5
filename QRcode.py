import qrcode
  
def qr_code(info):
    qr = qrcode.QRCode(version=10, box_size=10)
    qr.add_data(info)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    print("generated!")
  
info = 'https://github.com/dhaubum'
qr_code(info)