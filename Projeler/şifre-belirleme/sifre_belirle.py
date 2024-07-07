from pathlib import Path
from tkinter import *
from tkcalendar import DateEntry

m = Tk()
m.title("Hatırlatıcı")

canvas = Canvas(m, height=450, width=750)
canvas.pack()
# pack
# place
# grid

frame_ust = Frame(m, bg='#add8e6')
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt_sol = Frame(m, bg='#add8e6')
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

frame_alt_sag = Frame(m, bg='#add8e6')
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

hatirlatma_tipi_etiket = Label(frame_ust, bg='#add8e6', text='Hatırlatma Tipi:', font='Verdana 11 bold')
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsion = StringVar(frame_ust)
hatirlatma_tipi_opsion.set("\t")

hatirlatma_tipi_acilir_menu = OptionMenu(frame_ust, hatirlatma_tipi_opsion, "Özel Durum", "Normal Durum")
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)


hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background='orange', borderwidth=1, locale="de_De")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)


hatirlatma_tarihi_etiket = Label(frame_ust, bg='#add8e6', text='Hatırlatma Tarihi:', font='Verdana 11 bold')
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=LEFT)


Label(frame_alt_sol, text="Hatırlatma Yöntemi:", bg='#add8e6', font='Verdana 10 bold').pack(padx=10, pady=10, anchor=NW)

var = IntVar()

R1 = Radiobutton(frame_alt_sol, text="Sisteme Kaydet", variable= var, value=1, bg='#add8e6', font='Verdana 10')
R1.pack(anchor=NW, pady=5, padx=15)

R2 = Radiobutton(frame_alt_sol, text="E-posta Gönder", variable= var, value=2, bg='#add8e6', font='Verdana 10')
R2.pack(anchor=NW, pady=5, padx=15)

var1 = IntVar()
c1 = Checkbutton(frame_alt_sol, text="Bir hafta önce", variable=var1, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10')
c1.pack(anchor=NW, pady=2, padx=25)

var2 = IntVar()
c1 = Checkbutton(frame_alt_sol, text="Bir gün önce", variable=var2, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10')
c1.pack(anchor=NW, pady=2, padx=25)

var3 = IntVar()
c1 = Checkbutton(frame_alt_sol, text="Aynı gün", variable=var3, onvalue=1, offvalue=0, bg='#add8e6', font='Verdana 10')
c1.pack(anchor=NW, pady=2, padx=25)

from tkinter import messagebox


def gonder():
    son_mesaj = ""
    try:
        if var.get():
            if var.get() == 1:
                son_mesaj += "Veriniz başarıyla sisteme kaydedilmiştir."
                
                tip = hatirlatma_tipi_opsion.get()
                tarih = hatirlatma_tarih_secici.get()
                mesaj = metin_alani.get("1.0", "end")
                
                with open("hatirlatmalar.txt", "w") as dosya:
                    dosya.write(
                        '{} kategorisinde, {} tarihine ve "{}" notuyla hatirlatma'.format(
                        tip,
                        tarih,
                        mesaj
                        ))
                    dosya.close()
                     
            elif var.get() == 2:
                son_mesaj += "Veriniz E-posta yoluyla size ulaşacaktır."
                messagebox.showinfo("Başarili İşlem", son_mesaj)
                
        else:
            son_mesaj += "Tüm alanları doldurulduğunuzdan emin olun!"
            messagebox.showwarning("Başarısız İşlem", son_mesaj)
            
    except:
        son_mesaj += "İşlem Başarısız Oldu!"
        messagebox.showerror(son_mesaj)   
        
    finally:
        m.destroy()                 

Label(frame_alt_sag, text="Hatırlatma Mesajı:", bg='#add8e6', font='Verdana 10 bold').pack(padx=10, pady=10, anchor=NW)

metin_alani = Text(frame_alt_sag, height=9, width=50)
metin_alani.tag_configure('style', foreground='#bfbfbf', font=('Verdana', 7, 'bold'))
metin_alani.pack()

karsilama_metni = 'Mesajini buraya gir...'
metin_alani.insert(END, karsilama_metni, 'style')

gonderi_buttonu = Button(frame_alt_sag, text="Gönder", command=gonder)
gonderi_buttonu.pack(anchor=S)



m.mainloop()
