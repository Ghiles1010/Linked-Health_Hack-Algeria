from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import png 
from pyqrcode import QRCode
import pyqrcode 
from PIL import Image

class qrcode: 
	
	def __init__(self, key, id): 
			self.key = key
			self.id = id
			
			s = Serializer(key, 60*30) # 60 secs by 30 mins
			token = s.dumps({'user_id': id}).decode('utf-8') # encode user id 
			a = "www.linked_health.dz/"+token
			url=pyqrcode.create(a)
			
			url.png(''+id+'.png', scale = 2)
			
			image1 = Image.open(r''+id+'.png')
			im1 = image1.convert('RGB')
			im1.save(r''+id+'myqr.pdf')



