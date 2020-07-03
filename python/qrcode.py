from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import png 
from pyqrcode import QRCode
import pyqrcode 
from PIL import Image

s = Serializer('PATIENT_SECRET_KEY', 60*30) # 60 secs by 30 mins
token = s.dumps({'user_id': '00001'}).decode('utf-8') # encode user id 
a = "www.linked_health.dz/"+token
url=pyqrcode.create(a)
url.svg("myqr.svg", scale = 4)
url.png('myqr.png', scale = 2)

image1 = Image.open(r'myqr.png')
im1 = image1.convert('RGB')
im1.save(r'myqr.pdf')
