# saliency
A saliency detection algorithm based on brightness  and contrast :
Method is based on obtaining salient parts of the images by brightness and
contrast values. The aim is to identify the pixels with high contrast, in a way with a high
standard deviation, and label them as salient pixels.
The logic depends on the following assumption:
If ǀf(i,j)-Jǀ ≥ α C
then f(i,j) is a salient pixel.
Where,
f(i,j) is pixel value
J is brightness
C is contrast
alpha is a constant between [0.8-3]
After converting the image to greyscale, the brightness and contrast values of the image
were calculated. Brightness is defined by average pixel level for each band in the image.
Contrast is defined by root mean square for each band in the image. After this process the salient
pixels were transformed into white (255) and the rest to black (0), which is basic global
thresholding.
