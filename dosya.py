# -*- coding: utf-8 -*-

#f= open("musteriler.txt")
##print(f.read())
#print("**//**//++--*****")
##print(f.readline())
##print(f.readline())
##print(f.readline())
##print(f.readline())
#for l in f:
#    print(l)
#f.close()    

#f= open("musteriler.txt","r") Read,dosya okuma
#f= open("musteriler.txt","a") Append,dosyaya okuma ve ekleme yapma
#f= open("musteriler.txt","w") Write,dosya oluşturma ve okuma yoksa oluşturma 
#f= open("musteriler.txt","x") Create,direkt dosya oluşturma

fileToAppend=open("ogrenciler.txt")
fileToAppend.write("Şaban")

fileToAppend.write("\n")

fileToAppend.close()