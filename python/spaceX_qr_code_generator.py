import qrcode as qr
from PIL import Image

qr_code = qr.QRCode(version=2,
                   error_correction=qr.constants.ERROR_CORRECT_H,
                   box_size=15,
                   border=4,)

qr_code.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=2")
qr_code.make(fit=True)
img = qr_code.make_image(fill_color="white", back_color="red").save("qr.png")

img = Image.open("qr.png")
img.show()
