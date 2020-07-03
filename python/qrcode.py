import random
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from simplecrypt import encrypt, decrypt
import png
from pyqrcode import QRCode
import pyqrcode 
from PIL import Image

class qrcode:
	def __init__(self, id):
			self.id = id
			a = "https://rocky-harbor-71969.herokuapp.com/dossier?id="+self.id
			url=pyqrcode.create(a)
			
			url.png(''+id+'.png', scale = 10)
			
			image1 = Image.open(r''+id+'.png')
			im1 = image1.convert('RGB')
			im1.save(r''+id+'myqr.pdf')

