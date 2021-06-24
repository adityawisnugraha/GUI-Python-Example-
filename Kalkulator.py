#definisikan cond = 'error'
cond = 'error'

#jika cond = 'error', lakukan:
while cond == 'error':
    # input angka1 tipe decimal
    angka1 = float(input('masukkan bilangan ke-1: '))
    # input angka2 tipe decimal
    angka2 = float(input('masukkan bilangan ke-2: '))
    # input operator
    oprtr = input('masukkan operator (+,-,*,/): ')

    # definisikan cond='normal'
    cond = 'normal'

    if oprtr == '+':
        # kondisi jika operator +
        hasil = angka1+angka2
    elif oprtr == '-':
        # kondisi jika operator -
        hasil = angka1-angka2
    elif oprtr == '*':
        # kondisi jika operator *
        hasil = angka1*angka2
    elif oprtr == '/':
        # kondisi jika operator /
        if angka2 == 0:
            # jika pembagi = 0
            hasil = 'Infinite'
        else:
            # jika pembagi tidak 0
            hasil = angka1/angka2
    else:
        # kondisi jika oprtr selain (+,-,*,/)
        cond = 'error'

#tampilkan hasilnya
print('hasil',angka1,oprtr,angka2,'=',hasil)