import qrcode
img = qrcode.make('''https://getbootstrap.com/''')
img.save("qr_code2.png")
print("Qr code generated successfully ")