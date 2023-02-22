# Untuk menyimpan data Buku dan Troli secara multidimensi
list_buku = []
troli = []

# Untuk menampilkan data Buku yang sudah diinput
def menampilkan_buku():
    print('Daftar Buku:')
    spasi()
    for i in range(len(list_buku)) :
        print('{}\t| {}\t| {}\t| {}\t| {}'.format(i,str(list_buku[i][0]),str(list_buku[i][1]),str(list_buku[i][2]),str(list_buku[i][3])))
    print('\n')

def spasi():
    a = 'Judul'
    if len(a)<20:
        b = ''
        for i in range(20-len(a)):b+=' '
        a = a+b
    c = 'Penulis'
    if len(c)<20:
        d = ''
        for i in range(20-len(c)):d+=' '
        c = c+d
        print('Index\t| {}\t| {}\t| Stock\t| Harga'.format(a,c))

def mengecek_buku(): #Menu cek
    print('Tekan 1 : Menampilkan Daftar Buku')
    print('Tekan 2 : Mencari Daftar Buku')
    print('Tekan 3 : Back to menu\n')
    plh_menu = int(input('Masukkan pilihan Anda: '))
    if(plh_menu == 1) :
        if (len(list_buku)) == 0 :
            print('Mohon maaf, tidak ada informasi\n')
        else:
            menampilkan_buku()
            mengecek_buku()
    elif(plh_menu == 2) :
        if (len(list_buku)) == 0 :
            print('Mohon maaf, tidak ada informasi\n')
            mengecek_buku()
        elif (len(list_buku)) != 0 :
            cek_index = int(input('Masukkan index buku yang ingin dilihat: '))
            if cek_index > (len(list_buku))-1:
                print('Informasi buku tidak ditemukan!\n')
                mengecek_buku()
            else:
                spasi()
                print('{}\t| {}\t| {}\t| {}\t| {}'.format(cek_index,(list_buku[cek_index][0]),(list_buku[cek_index][1]),(list_buku[cek_index][2]),(list_buku[cek_index][3])))
                print('\n')
                mengecek_buku()
    else:
        plh_menu = 3

# Untum memasukkan/menambah data Buku baru
def menambah_buku(): #Menu Tambah
    print('Tekan 1 : Menambah Daftar Buku')
    print('Tekan 2 : Back to menu\n')
    plh_menu = int(input('Masukkan pilihan Anda: '))
    if(plh_menu == 1) :
        isi()
    else:
        plh_menu = 2

def isi():
    if len(list_buku) > 30 :
            print('Data buku telah mencapai batas yang tersedia!!')
            return
    data = []
    judul_buku = input('Masukkan judul buku: ')
    if len(judul_buku)<20:
        a = ''
        for i in range(20-len(judul_buku)):a+=' '
        judul_buku = judul_buku+a
    penulis_buku = input('Masukkan penulis buku: ')
    if len(penulis_buku)<20:
        a = ''
        for i in range(20-len(penulis_buku)):a+=' '
        penulis_buku = penulis_buku+a
    stock_buku = input('Masukkan stock buku: ')
    harga_buku = input('Masukkan harga buku: ')
    for i in range(len(list_buku)):
        if list_buku[i][0] == judul_buku:
            print('Judul sudah ada, masukkan judul lainnya.\n')
            menambah_buku()
            break
    else:
        data.append(judul_buku)
        data.append(penulis_buku)
        data.append(int(stock_buku))
        data.append(int(harga_buku))
        list_buku.append(data)
        recheck = input('Apakah Anda ingin memasukkan data lain? (ya/tidak) = ')
        print('\n')
        if (recheck == 'ya'):
            isi()
        else:
            recheck == 'tidak'
            print('\n')
            print('-----------------------------------------')
            print('Data buku telah berhasil disimpan')
            print('-----------------------------------------')
            print('\n')
            menambah_buku()

# Untum mengupdate data Buku yang telah ada
def mengupdate_buku(): #Menu Update
    print('Tekan 1 : Lanjutkan mengupdate Daftar Buku')
    print('Tekan 2 : Back to menu\n')
    plh_menu = int(input('Masukkan pilihan Anda: '))
    if(plh_menu == 1) :
        baru()
    else:
        plh_menu = 2

def baru():
    menampilkan_buku()
    cek_index = int(input('Masukkan index buku yang ingin diupdate: '))
    if (cek_index > len(list_buku)-1):
        print('Informasi buku tidak ditemukan!!\n')
        mengupdate_buku()
    else:
        print('Tekan 1 : Mengupdate Judul Buku')
        print('Tekan 2 : Mengupdate Penulis Buku')
        print('Tekan 3 : Mengupdate Stock Buku')
        print('Tekan 4 : Mengupdate Harga Buku\n')
        plh_menu = int(input('Masukan pilihan Anda: '))
        if(plh_menu == 1):
            new_judul_buku = input('Update judul buku: ')
            if len(new_judul_buku)<20:
                a = ''
                for i in range(20-len(new_judul_buku)):a+=' '
                new_judul_buku = new_judul_buku+a
            recheck = input('Apakah Anda yakin ingin mengupdatenya? (ya/tidak) = ')
            print('\n')
            if(recheck == 'tidak'):
                mengupdate_buku()
            else:
                recheck == 'ya'
                list_buku[cek_index][0] = new_judul_buku
                kata()
                mengupdate_buku()
        elif(plh_menu == 2):
            new_penulis_buku = input('Update penulis buku: ')
            if len(new_penulis_buku)<20:
                a = ''
                for i in range(20-len(new_penulis_buku)):a+=' '
                new_penulis_buku = new_penulis_buku+a
            recheck = input('Apakah Anda yakin ingin mengupdatenya? (ya/tidak) = ')
            print('\n')
            if(recheck == 'tidak'):
                mengupdate_buku()
            else:
                recheck == 'ya'
                list_buku[cek_index][1] = new_penulis_buku
                kata()
                mengupdate_buku()    
        elif(plh_menu == 3):
            new_stock_buku = int(input('Update stock buku: '))
            recheck = input('Apakah Anda yakin ingin mengupdatenya? (ya/tidak) = ')
            print('\n')
            if(recheck == 'tidak'):
                mengupdate_buku()
            else:
                recheck == 'ya'
                list_buku[cek_index][2] = int(new_stock_buku)
                kata()
                mengupdate_buku()
        elif(plh_menu == 4):
            new_harga_buku = int(input('Update harga buku: '))            
            recheck = input('Apakah Anda yakin ingin mengupdatenya? (ya/tidak) = ')
            print('\n')
            if(recheck == 'tidak'):
                mengupdate_buku()
            else:
                recheck == 'ya'
                list_buku[cek_index][3] = int(new_harga_buku)
                kata()
                mengupdate_buku()
def kata():
    print('\n')                                   
    print('-----------------------------------------')
    print('Data buku telah berhasil diupdate')
    print('-----------------------------------------')
    print('\n')

# Untum menghapus data Buku yang telah ada
def menghapus_buku() : #Menu Hapus
    print('Tekan 1 : Lanjutkan menghapus Daftar Buku')
    print('Tekan 2 : Back to menu\n')
    plh_menu = int(input('Masukkan pilihan Anda: '))
    if(plh_menu == 1) :
        hapus()
    else:
        plh_menu = 2

def hapus():
    menampilkan_buku()
    cek_index = int(input('Masukkan index buku yang ingin dihapus: '))
    if (cek_index > len(list_buku)-1):
        print('Informasi buku tidak ditemukan!!\n')
        menghapus_buku()
    else:
        recheck = input('Apakah Anda yakin ingin menghapusnya? (ya/tidak) = ')
        print('\n')
        if (recheck == 'ya'):
            del list_buku[cek_index]
            print('\n') 
            print('-----------------------------------------')
            print('Data buku telah berhasil dihapus')
            print('-----------------------------------------')
            print('\n')
            menghapus_buku()
        else:
            recheck = 'tidak'
            menghapus_buku()

# Untuk membeli Buku dari data yang telah ada
def membeli_buku() : #Menu Beli
    print('Tekan 1 : Lanjutkan membeli Buku')
    print('Tekan 2 : Back to menu\n')
    plh_menu = int(input('Masukkan pilihan Anda: '))
    if(plh_menu == 1) :
        menampilkan_buku()
        cek_index = int(input('Masukkan index buku yang ingin dibeli: '))
        if (cek_index > len(list_buku)-1):
            print('Informasi buku tidak ditemukan!!\n')
            membeli_buku()
        else:
            beli()
    else:
        plh_menu = 2

def beli():
    menampilkan_buku()
    while True :
        index = input('Mohon masukkan kembali index buku yang ingin dibeli: ')
        qty_buku = input('Masukkan jumlah yang ingin dibeli: ')
        if (int(qty_buku) > list_buku[int(index)][2]) :
            print('Mohon maaf, stock tidak cukup, stock tinggal {}'.format(list_buku[int(index)][2]))
            print('\n')
        else :
            troli.append({
                'judul': list_buku[int(index)][0], 
                'qty': int(qty_buku), 
                'harga': list_buku[int(index)][3], 
                'index': int(index)
            })
        print('Isi Troli:')
        a = 'Judul'
        if len(a)<20:
            b = ''
            for i in range(20-len(a)):b+=' '
            a = a+b
            print('{}\t| Qty\t| Harga'.format(a))
        for item in troli :
            print('{}\t| {}\t| {}'.format(item['judul'], item['qty'], item['harga']))
        print('\n')
        checker = input('Mau beli buku yang lain? (ya/tidak): ')
        print('\n')
        if(checker == 'tidak'):
            break

    print('Daftar Belanja: ')
    a = 'Judul'
    if len(a)<20:
        b = ''
        for i in range(20-len(a)):b+=' '
        a = a+b
        print('{}\t| Qty\t| Harga\t| Total Harga'.format(a))
    total_harga = 0
    for item in troli :
        print('{}\t| {}\t| {}\t| {}'.format(item['judul'], item['qty'], item['harga'], item['qty'] * item['harga']))
        total_harga += item['qty'] * item['harga']
    print('\n')
    while True :
        print('Total yang harus dibayar = {}'.format(total_harga))
        jml_uang = int(input('Masukkan jumlah uang: '))
        print('\n')
        if(jml_uang > total_harga) :
            kembali = jml_uang - total_harga
            print('-----------------------------------------')
            print('Terima kasih :) \nUang kembali anda: {}'.format(kembali))
            print('-----------------------------------------\n')
            for item in troli :
                list_buku[item['index']][2] -= item['qty']
            troli.clear()
            break
        elif(jml_uang == total_harga) :
            print('-----------------------------------------')
            print('Terima kasih :)')
            print('-----------------------------------------\n')
            for item in troli :
                list_buku[item['index']][2] -= item['qty']
            troli.clear()
            break
        else :
            kekurangan = total_harga - jml_uang
            print('Mohon maaf, uang anda kurang sebesar: {}'.format(kekurangan))
            print('\n')
    membeli_buku()

while True :
    print('''
    -----------------------------------------
    ------ SELAMAT DATANG DI TOKO BUKU ------
    -----------------------------------------\n
    ''')

    print('List Menu: ')
    print('Tekan 1 : Menampilkan Daftar Buku')
    print('Tekan 2 : Menambah Daftar Buku')
    print('Tekan 3 : Mengupdate Daftar Buku')
    print('Tekan 4 : Menghapus Daftar Buku')
    print('Tekan 5 : Membeli Buku')
    print('Tekan 6 : Exit Program\n')
    pilihan_menu = int(input('Masukkan Menu yang Anda pilih: '))

    print('\n-----------------------------------------')

    if(pilihan_menu == 1) :
        mengecek_buku()
    elif(pilihan_menu == 2) :
        menambah_buku()
    elif(pilihan_menu == 3) :
        mengupdate_buku()
    elif(pilihan_menu == 4) :
        menghapus_buku()
    elif(pilihan_menu == 5) :
        membeli_buku()
    elif(pilihan_menu == 6) :
        break
    else:
        print('Masukkan pilihan sesuai Menu yang ada.')