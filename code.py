import  qrcode

qr = qrcode.QRCode(
    version= 2,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 1
)

qr.add_data('https://m.baidu.com/?from=1012852s')
qr.make(fit=True)
img = qr.make_image()
img.save('my_qrcode.png')

print('hahahaha')
print('ddd')