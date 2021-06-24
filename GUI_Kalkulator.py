from tkinter import *

#fungsi penjumlahan
def penjumlahan():
    try: #mencoba
        bil_1 = entry1.get() #memanggil value
        bil_2 = entry2.get() #memanggil value
        hasil = float(bil_1)+float(bil_2)
        lab_hsl.config(text=('Hasil : ' + str(hasil)))
        lab_5.config(text='')
    except:
        lab_5.config(text='Masukkan angka yang benar !!!!')
        lab_hsl.config(text='')

#fungsi pengurangan
def pengurangan():
    try:
        bil_1 = entry1.get()
        bil_2 = entry2.get()
        hasil = float(bil_1)-float(bil_2)
        lab_hsl.config(text=('Hasil : ' + str(hasil)))
        lab_5.config(text='')
    except:
        lab_5.config(text='Masukkan angka yang benar !!!!')
        lab_hsl.config(text='')

#fungsi perkalian
def perkalian():
    try:
        bil_1 = entry1.get()
        bil_2 = entry2.get()
        hasil = float(bil_1)*float(bil_2)
        lab_hsl.config(text=('Hasil : ' + str(hasil)))
        lab_5.config(text='')
    except:
        lab_5.config(text='Masukkan angka yang benar !!!!')
        lab_hsl.config(text='')

#fungsi pembagian
def pembagian():
    try:
        bil_1 = entry1.get()
        bil_2 = entry2.get()
        if float(bil_2) == 0:
            hasil = 'infinite'
        else:
            hasil = float(bil_1)/float(bil_2)

        lab_hsl.config(text=('Hasil : ' + str(hasil)))
        lab_5.config(text='')
    except:
        lab_5.config(text='Masukkan angka yang benar !!!!')
        lab_hsl.config(text='')

#membuat layout tkinter
root = Tk()
root.geometry('400x300') #ukuran layour
root.title('Kalkulator')

#membuat text judul 'Kalkulator' dengan font CMS 13
lab_1 = Label(root,text='Kalkulator',font=('Comic Sans ms',13))
lab_1.place(relx=.5,rely=.05,anchor='center')

#membuat text bertulis 'Bilangan ke-1'
lab_2 = Label(root,text='Bilangan ke-1 :')
lab_2.place(relx=.5,rely=.22,anchor='center')

#membuat widget entry 'Bilangan ke-1'
entry1 = Entry(root)
entry1.place(relx=.5,rely=.3,anchor="center")

#membuat text bertulis 'Bilangan ke-2'
lab_3 = Label(root,text='Bilangan ke-2 :')
lab_3.place(relx=.5,rely=.42,anchor='center')

#membuat widget entry 'Bilangan ke-2'
entry2 = Entry(root)
entry2.place(relx=.5,rely=.5,anchor='center')

#membuat text operator
lab_4 = Label(root,text='Operator')
lab_4.place(relx=.5,rely=.575,anchor='center')

#membuat button
btn_add = Button(root,text='+',command=penjumlahan)
btn_add.place(relx=.4,rely=.675,anchor='center')
btn_min = Button(root,text='-',command=pengurangan)
btn_min.place(relx=.475,rely=.675,anchor='center')
btn_mul = Button(root,text='x',command=perkalian)
btn_mul.place(relx=.55,rely=.675,anchor='center')
btn_div = Button(root,text=':',command=pembagian)
btn_div.place(relx=.625,rely=.675,anchor='center')

#membuat laber peringatan
lab_5 = Label(root,text='')
lab_5.place(relx=.5,rely=.15,anchor='center')

#membuat tempat hasil
lab_hsl = Label(root, text = '')
lab_hsl.place(relx=.5, rely=.8, anchor='center')

root.mainloop()