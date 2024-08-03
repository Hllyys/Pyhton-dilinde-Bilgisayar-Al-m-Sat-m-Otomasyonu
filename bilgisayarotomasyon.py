
# def bilgisayarekle():
#     bilgisayar_marka=input("->bilgisayarin modelini giriniz: ")
#     bilgisayar_hafiza=input("->bilgisayarin hafizasi ne kadar: ")
#     bilgisayar_ram =input("->bilgisayarin ram i ne kadar: ")
#     bilgisayar_fiyat =input("->bilgisayarin fiyati ne kadar: ")
#     with open("bilgiler.txt","a") as file:
#         file.write('bilgisayar modeli: '+bilgisayar_marka+' ''bilgisayar hafizasi: '+bilgisayar_hafiza+' ''bilgisayar ram i: '+bilgisayar_ram+' ''bilgisayar fiyati: '+bilgisayar_fiyat+'\n ')


# def bilgisayarlistele():                                                                           
#     with open("bilgiler.txt","r") as file:
#         for i in file:
#             print(i)


# def bilgisayarara():
#     bilgisayar_marka=input("aranacak bilgisayar markasini giriniz: ")
#     with open("bilgiler.txt","r") as file:
#         print("bulunan bilgiler-->")
#         for i in file:
#             if bilgisayar_marka in i:
#                     print(i)

# def bilgisayarguncelle():
#     bilgisayar_marka=input("guncellemek istediginiz bilgisayar modeli giriniz: ")
#     indis=0
#     with open("bilgiler.txt","r+") as file:
#         dosya = file.readlines()
#         for i in dosya:
#             if bilgisayar_marka in i:
#                 dosya.pop(indis)
#                 break
#         bilgisayar_marka=input("->bilgisayarin modelini giriniz: ")
#         bilgisayar_hafiza=input("->bilgisayarin hafizasi ne kadar: ")
#         bilgisayar_ram =input("->bilgisayarin ram i ne kadar: ")
#         bilgisayar_fiyat =input("->bilgisayarin fiyati ne kadar: ")
            
#     with open("bilgiler.txt","w",encoding="utf-8") as file: 
#         for i in dosya:
#             file.write(i)                
#     indis+=1
#     print("basariyla guncellestirildi ")
# # bilm_list=[]

# # def bilgisayarguncelle():
# #     bilgisayar_marka=input("guncellenecek bilgisayar markasi giriniz ")
# #     with open("bilgiler.txt","r") as file:
# #         bilm_list = file.readlines()
# #         for i in  range(len(bilm_list)):
# #             if bilgisayar_marka in bilm_list[i]:
# #                 bilgisayar_markayeni=input("->guncellemek istediginiz bilgisayar markasi giriniz ")
# #                 bilgisayar_hafizayeni=input("->guncel bilgisayar hafizasi giriniz ")
# #                 bilgisayar_ramyeni=input("->guncel bilgisayar ram i giriniz ")
# #                 bilgisayar_fiyatyeni=input("->guncel bilgisayar fiyati giriniz ")
# #                 bilm_list[i]=[bilgisayar_markayeni,bilgisayar_hafizayeni,bilgisayar_ramyeni,bilgisayar_fiyatyeni]
# #                 break
# #     with open("bilgiler.txt","a",encoding="utf-8") as file: 
# #         for i in  bilm_list[i]:            
# #             file.writelines(i)
# #         print("basarili bir sekilde guncellestirildi: ")
# # bilm_list=[]

# # def bilgisayarguncelle():
# #     bilgisayar_marka=input("guncellenecek bilgisayar markasi giriniz ")
   
# #     with open("bilgiler.txt","r") as file:
# #         bilm_list = file.readlines()
# #         for i in bilm_list:
# #             if bilgisayar_marka in i:
# #                 bilgisayar_markayeni=input("->guncellemek istediginiz bilgisayar markasi giriniz ")
# #                 bilgisayar_hafizayeni=int(input("->guncel bilgisayar hafizasi giriniz "))
# #                 bilgisayar_ramyeni=int(input("->guncel bilgisayar ram i giriniz "))
# #                 bilgisayar_fiyatyeni=int(input("->guncel bilgisayar fiyati giriniz "))
# #             #    bilm_list[i]=["bilgisayar_markayeni",bilgisayar_hafizayeni,bilgisayar_ramyeni,bilgisayar_fiyatyeni]
# #                 break
# #     bilm_list.writlenss()
# #   print("basarili bir sekilde guncellestirildi: ")
# # def bilgisayarguncelle():
# #     bilgisayar_marka=input("guncellenecek bilgisayar markasi giriniz ")
# #     indis=0
# #     with open("bilgiler.txt","r+") as file:
# #         dosya=file.readlines()
# #         for i in dosya:
# #             if bilgisayar_marka in i:
# #                 bilgisayar_marka=input("->guncellemek istediginiz bilgisayar modelini giriniz ")
# #                 bilgisayar_hafiza=input("->guncel bilgisayar hafizasi giriniz ")
# #                 bilgisayar_ram=input("->guncel bilgisayar ram i giriniz ")
# #                 bilgisayarfiyat=input("->guncel bilgisayar fiyati giriniz ")

# #                 break
# #             indis+=1
# #     with open("bilgiler.txt","r+",encoding="utf-8") as file: 
# #         for i in dosya:
# #             file.write(i)  
# #     print("bilgisayar basariyla guncellendi ")  


# def bilgisayarsil():
#     bilgisayar_marka=input("silmek istediginiz bilgisayar modeli giriniz: ")
#     indis=0
#     with open("bilgiler.txt","r+") as file:
#         dosya = file.readlines()
#         for i in dosya:
#             if bilgisayar_marka in i:
#                 dosya.pop(indis)
#                 break
#             indis+=1

#     with open("bilgiler.txt","w",encoding="utf-8") as file: 
#         for i in dosya:
#             file.write(i)                
#     print("basariyla bilgisayar silindi ")



# def bilgisayaradedi():
#     bilgisayar_marka=input(" hangi model bilgisayardan kac adet adet var ")
#     d={}
#     d[bilgisayar_marka]=0
#     with open("bilgiler.txt","r") as file:
#         dosya = file.readlines()
#         for i in dosya:
#             if bilgisayar_marka in i:
#                 d[bilgisayar_marka]+=1

#         print(d)
#     with open("bilgiler.txt","r+",encoding="utf-8") as file: 
#         for i in dosya:
#             file.write(i) 



# def menu():
#     print("--------------------------------------------------------")
#     print("1-> bilgisayar ekle ")
#     print("2-> bilgisayar listele ")
#     print("3-> bilgisayar ara ")
#     print("4-> bilgisayar guncelle ")
#     print("5-> bilgisayar sil ")
#     print("6-> bilgisayar adedi ")
#     print("0-> cikis yapmak icin ")
#     print("--------------------------------------------------------")
#     secim=int(input("secim yapiniz: "))
#     print("--------------------------------------------------------")
#     while True:
#         if secim== 1 :
#             bilgisayarekle()
#             menu()
#         elif secim== 2 :
#             bilgisayarlistele()
#             menu()
#         elif secim== 3 :
#             bilgisayarara()
#             menu()
#         elif secim== 4 :
#             bilgisayarguncelle()
#             menu()
#         elif secim== 5 :
#             bilgisayarsil()
#             menu()
#         elif secim== 6 :
#             bilgisayaradedi()
#             menu()
#         elif secim== 0 :
#             print("cikis yapiliyor " )
#             exit()
#         else:
#             print("hatali secim yaptiniz tekrar secim yapiniz!!!")
#             menu()
# menu()



from http.cookiejar import FileCookieJar


def bilgisayarekle():
    bilgisayar_marka=input("->bilgisayarin modelini giriniz: ")
    bilgisayar_hafiza=input("->bilgisayarin hafizasi ne kadar: ")
    bilgisayar_ram =input("->bilgisayarin ram i ne kadar: ")
    bilgisayar_fiyat =input("->bilgisayarin fiyati ne kadar: ")
    with open("bilgiler.txt","a") as file:
        file.write('bilgisayar modeli: '+bilgisayar_marka+' ''bilgisayar hafizasi: '+bilgisayar_hafiza+' ''bilgisayar ram i: '+bilgisayar_ram+' ''bilgisayar fiyati: '+bilgisayar_fiyat+'\n ')
    print("girdiginiz bilgiler kaydedildi...")
def bilgisayarlistele():
    print("---LİSTE---")                                                                           
    with open("bilgiler.txt","r") as file:
        for i in file:
            print(i)
    

def bilgisayarara():
    bilgisayar_marka=input("aranacak bilgisayar modelini giriniz: ")
    with open("bilgiler.txt","r") as file:
        print("bulunan bilgiler-->")
        for i in file:
            if bilgisayar_marka in i:
                    print(i)



def bilgisayarguncelle():
    
    #bilgisayar_marka=input("guncellenecek bilgisayar markasi giriniz ")
    with open("bilgiler.txt","r") as file:

        bilm_list = file.readlines()
        for i,j in enumerate(bilm_list):
            print(i,j)
        for i in  range(len(bilm_list)):
            i=int(input("i....."))
            bilgisayar_markayeni=input("->guncellemek istediginiz bilgisayar markasi giriniz ")
            bilgisayar_hafizayeni=input("->guncel bilgisayar hafizasi giriniz ")
            bilgisayar_ramyeni=input("->guncel bilgisayar ram i giriniz ")
            bilgisayar_fiyatyeni=input("->guncel bilgisayar fiyati giriniz ")
            a="bilgisayar modeli : "+bilgisayar_markayeni+' ''bilgisayar hafizasi: '+bilgisayar_hafizayeni+' ''bilgisayar ram i: '+bilgisayar_ramyeni+' ''bilgisayar fiyati: '+bilgisayar_fiyatyeni+"\n"
            bilm_list[i]=a
            break
        print(bilm_list)
      
    with open("bilgiler.txt","w") as file2:         
        file2.writelines(bilm_list)
    print("basarili bir sekilde guncellestirildi: ")
    
 


def bilgisayarsil():
    bilgisayar_marka=input("silmek istediginiz bilgisayar modeli giriniz: ")
    indis=0
    with open("bilgiler.txt","r+") as file:
        dosya = file.readlines()
        for i in dosya:
            if bilgisayar_marka in i:
                dosya.pop(indis)
                break
            indis+=1

    with open("bilgiler.txt","w",encoding="utf-8") as file: 
        for i in dosya:
            file.write(i)                
    print("basariyla bilgisayar silindi ")



def bilgisayaradedi():
    bilgisayar_marka=input(" hangi model bilgisayardan kac adet adet var ")
    print("kayitli olan ayni marka bilgisayar bilgisi ")
    d={}
    d[bilgisayar_marka]=0
    with open("bilgiler.txt","r") as file:
        dosya = file.readlines()
        for i in dosya:
            if bilgisayar_marka in i:
                d[bilgisayar_marka]+=1

        print(d)
    with open("bilgiler.txt","r+",encoding="utf-8") as file: 
        for i in dosya:
            file.write(i) 



def menu():
    print("--------------------------------------------------------")
    print("1-> bilgisayar ekle ")
    print("2-> bilgisayar listele ")
    print("3-> bilgisayar ara ")
    print("4-> bilgisayar guncelle ")
    print("5-> bilgisayar sil ")
    print("6-> bilgisayar adedi ")
    print("0-> cikis yapmak icin ")
    print("--------------------------------------------------------")
    secim=int(input("secim yapiniz: "))
    print("--------------------------------------------------------")
    while True:
        if secim== 1 :
            bilgisayarekle()
            menu()
        elif secim== 2 :
            bilgisayarlistele()
            menu()
        elif secim== 3 :
            bilgisayarara()
            menu()
        elif secim== 4 :
            bilgisayarguncelle()
            menu()
        elif secim== 5 :
            bilgisayarsil()
            menu()
        elif secim== 6 :
            bilgisayaradedi()
            menu()
        elif secim== 0 :
            print("cikis yapiliyor " )
            exit()
        else:
            print("hatali secim yaptiniz tekrar secim yapiniz!!!")
            menu()
menu()