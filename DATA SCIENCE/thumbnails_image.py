from PIL import Image
   

image = Image.open(r"‪C:\Users\danish\Desktop\haloalkaine & haloarine\uni.jpg")
MAX_SIZE = (100, 100)
  
image.thumbnail(MAX_SIZE)
  

image.save('halo.png').show()
image.show()