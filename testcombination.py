from utils import combine
from PIL import Image

sun=Image.open("sun.png")
earth=Image.open("earth.png")

combine(sun,earth,1920,1080)