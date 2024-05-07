import qrcode as qr
data = input("enter the link to make a qr code \n : ")
img = qr.make(data)
filesave = input("enter the file name you want to save without extension \n : ")
filesave = filesave +".png"
img.save(filesave)

