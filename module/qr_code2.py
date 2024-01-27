import qrcode

data = qrcode.QRCode()
data.add_data('''https://ray.so/''')
data.make(fit=True)
image = data.make_image(fill_color="yellow",back_color="black")
image.save("qr_code4.png")
print("Qr code Generated colorfully ")