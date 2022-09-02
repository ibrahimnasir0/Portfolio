import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=GlLRYml8mCY")
img.save('qr_code.png')
img.show()