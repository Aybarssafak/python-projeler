to_do_list = []

def görev_ekle(to_do_list):
    görev = input("Yapılacak Görevi Girin:")
    to_do_list.append(görev)
    print("Görev başarıyla eklendi")

def görev_göster(to_do_list):
    print("Yapılacak Görevler: ")
    for görev in to_do_list:
        print("- " + görev)
        
def görev_sil(to_do_list):
    görev = input("Silmek istediğiniz görevi girin: ")
    if görev in to_do_list:
        to_do_list.remove(görev)
        print("Görev başarıyla silindi.")
    else:
        print("Görev bulunmadı")
        
while True:
    print("\nTo_Do List Uygulaması")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Görevleri Sil")
    print("4. Çıkış")
    seçenek = input("Seçiminiz (1/2/3/4) ")
    
    if seçenek == "1":
        görev_ekle(to_do_list)
    elif seçenek == "2":
        görev_göster(to_do_list)
    elif seçenek == "3":
        görev_sil(to_do_list)
    elif seçenek == "4":
        print("Uygulamadan Çıkılıyor")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin")