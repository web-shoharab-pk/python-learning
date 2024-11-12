import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename to save the QR code: ').strip()

qr = qrcode.QRCode(
    # version=None,  # Automatically determine the version
    # error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
# qr.make(fit=True)  # Ensure the QR code fits the data

img = qr.make_image(fill_color='black', back_color='white')

# Check if the PIL module is available
try:
    img.save(filename)
    print(f'QR code saved to {filename}')
except ModuleNotFoundError:
    print("Error: The 'PIL' module is not installed. Please install it using 'pip install Pillow'.")
