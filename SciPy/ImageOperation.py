from imageio import imread, imsave
from PIL import Image

img = imread('cat.jpg')
print(img.shape)

# Using PIL.Image instead because of scipy.misc.imresize is deprecated
img_tinted = Image.fromarray(img).resize(size=(300, 300))

imsave('cat_tinted.jpg', img_tinted)
