import qrcode

# Ask user to enter a URL
url = input("Enter a URL to generate QR code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qr_code.png")

print("✅ QR Code generated and saved as 'qr_code.png'")

