import numpy as np
import cv2 as cv

def sepImages(tipo,folder):
    if tipo == "LC08":
        #Seleccionar 2-3-4-5-6-7-8-10
        imagen2= open("ImageProc/data/"+folder+"/"+folder+"_B2.TIF", 'r')
        imagen3= open("ImageProc/data/"+folder+"/"+folder+"_B3.TIF", 'r')
        imagen4= open("ImageProc/data/"+folder+"/"+folder+"_B4.TIF", 'r')
        imagen5= open("ImageProc/data/"+folder+"/"+folder+"_B5.TIF", 'r')
        imagen6= open("ImageProc/data/"+folder+"/"+folder+"_B6.TIF", 'r')
        imagen7= open("ImageProc/data/"+folder+"/"+folder+"_B7.TIF", 'r')
        imagen8= open("ImageProc/data/"+folder+"/"+folder+"_B8.TIF", 'r')
        imagen10= open("ImageProc/data/"+folder+"/"+folder+"_B10.TIF", 'r')
        coleccion = [imagen2,imagen3,imagen4,imagen5,imagen6,imagen7,imagen8,imagen10]
        return coleccion
    elif tipo == "LC05":
        #Seleccionar 1-2-3-4-5-6-7
        imagen1= open("ImageProc/data/"+folder+"/"+folder+"_B1.TIF", 'r')
        imagen2= open("ImageProc/data/"+folder+"/"+folder+"_B2.TIF", 'r')
        imagen3= open("ImageProc/data/"+folder+"/"+folder+"_B3.TIF", 'r')
        imagen4= open("ImageProc/data/"+folder+"/"+folder+"_B4.TIF", 'r')
        imagen5= open("ImageProc/data/"+folder+"/"+folder+"_B5.TIF", 'r')
        imagen6= open("ImageProc/data/"+folder+"/"+folder+"_B6.TIF", 'r')
        imagen7= open("ImageProc/data/"+folder+"/"+folder+"_B7.TIF", 'r')
        coleccion = [imagen1,imagen2,imagen3,imagen4,imagen5,imagen6,imagen7]
        return coleccion
    elif tipo =="LC07":
        #Seleccionar 1-2-3-4-5-61-62-7
        imagen1= open("ImageProc/data/"+folder+"/"+folder+"_B1.TIF", 'r')
        imagen2= open("ImageProc/data/"+folder+"/"+folder+"_B2.TIF", 'r')
        imagen3= open("ImageProc/data/"+folder+"/"+folder+"_B3.TIF", 'r')
        imagen4= open("ImageProc/data/"+folder+"/"+folder+"_B4.TIF", 'r')
        imagen5= open("ImageProc/data/"+folder+"/"+folder+"_B5.TIF", 'r')
        imagen61= open("ImageProc/data/"+folder+"/"+folder+"_B6_VCID_1.TIF", 'r')
        imagen62= open("ImageProc/data/"+folder+"/"+folder+"_B6_VCID_2.TIF", 'r')
        imagen7= open("ImageProc/data/"+folder+"/"+folder+"_B7.TIF", 'r')
        coleccion = [imagen1,imagen2,imagen3,imagen4,imagen5,imagen61,imagen62,imagen7]
        return coleccion

def tiff2Jpeg(imagen):
    imgTiff = cv.imread(imagen, 0)
    cv.imwrite(imagen[:-4]+".JPEG",imgTiff)


def roi(imagen):
    im = cv.imread(imagen)
    fromCenter = False
    r = cv.selectROI("Imagen",im, fromCenter)
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv.imwrite(imagen[:-5]+"-Recorte.JPEG", imCrop)
    cv.waitKey(0)
    return r

#Testing
area = roi("LC08_L1TP_233076_20180120_20180206_01_T1_B1.JPEG")
print(area)
