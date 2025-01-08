# Rembg is a tool to remove images background. It is based on u2net.
from rembg import remove
from PIL import Image
data_repo = '../../data_repo/'

input_img = f'{data_repo}pexels-pixabay-326900.jpg'
output_img = f'{data_repo}pexels-pixabay-326900_rmbg.png'

inp = Image.open(input_img)
output = remove(inp)

output.save(output_img)
