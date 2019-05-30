import numpy as np

def prom_rgb(image): #Esta funcion toma el promedio de rgb de una imagen (se define par una de 15x15 pixeles)
    r=0
    g=0
    b=0
    for n in range (0,15):
        for i in range (0, 15):
            r=r+image[n,i,0]
            g=g+image[n,i,1]
            b=b+image[n,i,2]
    r=r/225 #Cada imagen tiene una cantidad de 15x15=225 pixeles
    g=g/225
    b=b/225
    rgb=[r,g,b]
    return rgb

def comparacion (rgb, dir_rgb): #Esta función compara un valor de un pixel rgb con el de todos los
                                #valores promedio de cada una de las imagenes del directorio
    imagen_num=0
    cond0=False
    cond1=False
    cond2=False
    cond3=False
    cond4=False
    cond5=False
    cond6=False
    
    for n in range(0, len(dir_rgb)):
        if (cond0==False):
            if(abs(dir_rgb[n][0]-rgb[0])<=200 and abs(dir_rgb[n][1]-rgb[1])<=200 and abs(dir_rgb[n][2]-rgb[2])<=200 ):
                imagen_num = n      #Si encuentra un valor con una diferencia de los valores rgb menor a 200
                cond0=True          #guarda la posición de esa imagen en el directorio, lo mismo para los siguientes casos,
        if (cond1==False):			  #pero con valores de diferencia más pequeños
            if(abs(dir_rgb[n][0]-rgb[0])<=100 and abs(dir_rgb[n][1]-rgb[1])<=100 and abs(dir_rgb[n][2]-rgb[2])<=100 ):
                imagen_num = n
                cond1=True
        
        elif (cond2==False):
            if(abs(dir_rgb[n][0]-rgb[0])<=80 and abs(dir_rgb[n][1]-rgb[1])<=80 and abs(dir_rgb[n][2]-rgb[2])<=80 ):
                imagen_num = n
                cond2=True
        elif (cond3==False):
            if(abs(dir_rgb[n][0]-rgb[0])<=50 and abs(dir_rgb[n][1]-rgb[1])<=50 and abs(dir_rgb[n][2]-rgb[2])<=50 ):
                imagen_num = n
                cond3=True
        
        elif (cond4==False):
            if(abs(dir_rgb[n][0]-rgb[0])<=30 and abs(dir_rgb[n][1]-rgb[1])<=30 and abs(dir_rgb[n][2]-rgb[2])<=30 ):
                imagen_num = n
                cond4=True
        elif (cond5==False):
            if(abs(dir_rgb[n][0]-rgb[0])<=15 and abs(dir_rgb[n][1]-rgb[1])<=15 and abs(dir_rgb[n][2]-rgb[2])<=15 ):
                imagen_num = n
                cond5=True
        elif (cond6==False):
            if(abs(dir_rgb[n][0]-rgb[0])<=5 and abs(dir_rgb[n][1]-rgb[1])<=5 and abs(dir_rgb[n][2]-rgb[2])<=5 ):
                imagen_num = n
                cond6=True               
    return imagen_num #retorna la posición de la imagen en el directorio que tenga los valores más parecidos al pixel 
                      #que se esta analizando de la imagen de entrada

def mosaico100x100(imagenes, entrada ): #Crea un mosaico de una imagen con 100x100 imagenes de un directorio
    dir_rgb = []
    for n in range(0, len(imagenes)): #Se crea un array que contiene los valores promedios rgb de las imagenes en el directorio
        dir_rgb.append(prom_rgb(imagenes[n])) 
    
    colum = []
    o = []
    for n in range(0,100): #Se compara el valor rgb de cada pixel de la imagen con el de todos los valores rgb del directorio
        for k in range (0,100):
            imagen_num = comparacion (entrada[k,n], dir_rgb)
            colum.append(imagen_num)
        o.append(colum)
        colum = []

    vs1=[]
    vs2=[]
    vs3=[]
    vs4=[]
    hs1=[]
    hs2=[]
    hs3=[]
    for n in range(0,10): #Se crea el mosaico con las funciones np.vstack y np.hstack, que combinan los ndarray de 
        c1=10*n           #cada imagen del directorio en forma vertical y horizontal respectivamente
        for m in range(0,10):
            for i in range(0,10):
                c2=10*i
                for j in range(0,10):
                    vs1.append(imagenes[o[(c1+m)][(c2+j)]])
                vs2=np.vstack([vs1[0], vs1[1], vs1[2], vs1[3], vs1[4], vs1[5], vs1[6], vs1[7], vs1[8], vs1[9]])
                vs3.append(vs2)
                vs1=[]
                vs2=[]
            vs4=np.vstack([vs3[0], vs3[1], vs3[2], vs3[3], vs3[4], vs3[5], vs3[6], vs3[7], vs3[8], vs3[9]])
            hs1.append(vs4)
            vs3=[]
            vs4=[]  
        hs2=np.hstack([hs1[0], hs1[1], hs1[2], hs1[3], hs1[4], hs1[5], hs1[6], hs1[7], hs1[8], hs1[9]])
        hs3.append(hs2)
        hs1=[]
        hs2=[]
    mosaico=np.hstack([hs3[0], hs3[1], hs3[2], hs3[3], hs3[4], hs3[5], hs3[6], hs3[7], hs3[8], hs3[9]])
    return mosaico
