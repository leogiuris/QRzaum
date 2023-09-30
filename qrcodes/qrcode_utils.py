import segno


def make_qr(qr_obj):
    qrcode = segno.make(qr_obj.data)
    qrcode.save("files/qrcode_images/"+ str(qr_obj.id) +".png")
    return