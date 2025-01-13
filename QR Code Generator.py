import qrcode

def make_qr(data, name):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=10,
                       border=2)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(f"{name}.png")
    print(f"QR Code saved as '{name}.png'\n")

def generate_qr():
    data = input("Enter data to make a qr code: ")
    file_name = input("Enter file name to save the QR Code: ")
    make_qr(data, file_name)

print ("""--------------------
 QR CODE GENERATOR
--------------------""")

while True:
    generate_qr()
    generate_again = input("Do you want to generate again (y/n): ")
    if generate_again != 'y':
        print ("Thank You for using.")
        break
