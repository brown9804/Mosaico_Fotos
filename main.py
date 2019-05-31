import cv2
import numpy as np
import glob
import sys
from funciones import mosaico100x100


filenames = [img1 for img1 in glob.glob(str(sys.argv[2]) + "/*.jpg")] #Se accede a todas los archivos del directorio con
filenames.sort()                                                      #con terminación .jpg
img = []
for img1 in filenames: #Se guardan todas las imagenes del directorio en un array
    n= cv2.imread(img1)
    imagen = cv2.resize(n, (15,15)) #Se redimensionan las imagenes del directorio a 15x15 pixeles
    img.append(imagen)

entrada = cv2.imread(str(sys.argv[1]))
entrada = cv2.resize(entrada, (800,800))
entrada_new = cv2.resize(entrada, (100,100))

mosaico = mosaico100x100(img, entrada_new)
cv2.imwrite("mosaico_creado.jpg",mosaico)
mosaico = cv2.resize(mosaico, (800,800))

out = np.hstack([entrada, mosaico])
cv2.imshow("Entrada     //     Mosaico", out)
cv2.waitKey(0)

