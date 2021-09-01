import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)
data = "https://www.instagram.com/stories/halfbloodpr/2653146097609052809/"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", bacl_color = "white")
img.save("test.png")