
genişlik = int(input("Çizeceğiniz baklavanın genişliğini belirtiniz:"))
bosluk = genişlik-1

###baklavanın üst kısmı için
for i in range(1,genişlik+1):
    for j in range(bosluk):##yıldızdan once gelecek boslukları ayarlamak için
        print(end=" ")
    bosluk -= 1 #yıldızları ortalanması için
    for j in range(i):#yıldızların yerini ayarlamak için
        print(end="* ")
    print() #yıldızları alt alta yazdırması için bunu yazmazsak yan yana olucak
###baklavanın alt kısmı için
bosluk+=2 #alt kısmı yaparken boslugu ayarlamak için
for i in range(genişlik-1,0,-1):
    for j in range(bosluk):##yıldızdan once gelecek boslukları ayarlamak için
        print(end=" ")
    bosluk +=1  #yıldızları ortalanması için
    for j in range(i):#yıldızların yerini ayarlamak için
        print(end="* ")
    print()  # yıldızları alt alta yazdırması için




