import qrcode

# Data you want to encode in the QR code
data = "artifence.co.ke"

# Create a QR code instance
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=5,
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create a QR code image using the Pillow library
qr_code = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
qr_code.save("my_qr_code.png")
