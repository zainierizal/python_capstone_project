dataRentalMobil = [{'KODE' : 'TA20','BRAND' : 'TOYOTA', 'TIPE' : 'AVANZA','TAHUN' : 2020, 'STOK' : 3, 'HARGA SEWA' : 500000},
        {'KODE' : 'TA21','BRAND' : 'TOYOTA', 'TIPE' : 'AVANZA','TAHUN' : 2021, 'STOK' : 2, 'HARGA SEWA' : 550000},
        {'KODE' : 'TA22','BRAND' : 'TOYOTA', 'TIPE' : 'AVANZA','TAHUN' : 2022, 'STOK' : 1, 'HARGA SEWA' : 600000},
        {'KODE' : 'TA23','BRAND' : 'TOYOTA', 'TIPE' : 'AVANZA','TAHUN' : 2023, 'STOK' : 2, 'HARGA SEWA' : 650000},
        {'KODE' : 'TC20','BRAND' : 'TOYOTA', 'TIPE' : 'CALYA','TAHUN' : 2020, 'STOK' : 2, 'HARGA SEWA' : 400000},
        {'KODE' : 'TC21','BRAND' : 'TOYOTA', 'TIPE' : 'CALYA','TAHUN' : 2021, 'STOK' : 3, 'HARGA SEWA' : 450000},
        {'KODE' : 'TC22','BRAND' : 'TOYOTA', 'TIPE' : 'CALYA','TAHUN' : 2022, 'STOK' : 1, 'HARGA SEWA' : 500000},
        {'KODE' : 'TC23','BRAND' : 'TOYOTA', 'TIPE' : 'CALYA','TAHUN' : 2023, 'STOK' : 2, 'HARGA SEWA' : 550000},
        {'KODE' : 'DX20','BRAND' : 'DAIHATSU', 'TIPE' : 'XENIA','TAHUN' : 2020, 'STOK' : 3, 'HARGA SEWA' : 450000},
        {'KODE' : 'DX21','BRAND' : 'DAIHATSU', 'TIPE' : 'XENIA','TAHUN' : 2021, 'STOK' : 2, 'HARGA SEWA' : 500000},
        {'KODE' : 'DX22','BRAND' : 'DAIHATSU', 'TIPE' : 'XENIA','TAHUN' : 2022, 'STOK' : 1, 'HARGA SEWA' : 550000},
        {'KODE' : 'DX23','BRAND' : 'DAIHATSU', 'TIPE' : 'XENIA','TAHUN' : 2023, 'STOK' : 2, 'HARGA SEWA' : 600000},
        ]
hargaTotalRiwayatPenyewaan = 0
dataRiwayatRental = []

#1. MENAMPILKAN LIST DAFTAR MOBIL RENTAL
def menuTampilkanData () :
    while True :
        print('-'*75)
        print(f'{' MENU 1 : MENAMPILKAN DATA MOBIL RENTAL '.center(75,'-')}')
        print('-'*75)
        print('''
                1. TAMPILKAN SELURUH DATA MOBIL RENTAL
                2. TAMPILKAN DATA MOBIL BERDASARKAN FILTER
                3. TAMPILKAN HISTORY PENYEWAAN MOBIL
                4. KEMBALI KE MENU UTAMA
                ''')
        print('-'*75)
        pilihan = input(f'MASUKKAN PILIHAN ANDA ( 1 / 2 / 3 / 4 ) : ')
        if pilihan == '1' :
            tampilkanData ()
        elif pilihan == '2' :
            filterData()
        elif pilihan == '3' :
            riwayatSewa()
        elif pilihan == '4' :
            while True :
                pilihan = input(f'APAKAH ANDA INGIN KEMBALI KE MENU UTAMA? (Y/N) : ').upper()
                if pilihan == 'Y' :
                    return
                elif pilihan == 'N' :
                    break
                else :
                    print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')
        else :
            print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')

#1.1 TAMPILKAN SELURUH DATA MOBIL RENTAL
def tampilkanData () :
    if len(dataRentalMobil) > 0 :
        print('-'*75)
        print(f'{'NO'.center(7)}|{'KODE'.center(8)}|{'BRAND'.center(13)}|{'TIPE'.center(13)}|{'TAHUN'.center(8)}|{'STOK'.center(6)}|{'HARGA SEWA'.center(14)}')
        print('-'*75)
        for i in range(len(dataRentalMobil)) :
            print(f'{str(i+1).center(7)}|{dataRentalMobil[i]['KODE'].center(8)}|{dataRentalMobil[i]['BRAND'].center(13)}|{dataRentalMobil[i]['TIPE'].center(13)}|{str(dataRentalMobil[i]['TAHUN']).center(8)}|{str(dataRentalMobil[i]['STOK']).center(6)}|{str(dataRentalMobil[i]['HARGA SEWA']).center(14)}')
        print('-'*75)
    else :
        print('-'*75)
        print('TIDAK ADA DATA MOBIL RENTAL YANG BISA DITAMPILKAN'.center(75))

#1.2. TAMPILKAN DATA MOBIL BERDASARKAN FILTER
def filterData () :
    dataFilter = []
    print('-'*75)
    print(f'{' FUNGSI FILTER '.center(75,'-')}')
    print('-'*75)

    filterBrand = input('MASUKKAN BRAND (ATAU TEKAN "ENTER" JIKA TIDAK INGIN FILTER): ').upper()
    if filterBrand == '' :
        actionFilterBrand = 0
    else :
        actionFilterBrand = 1

    filterTipe = input('MASUKKAN TIPE (ATAU TEKAN "ENTER" JIKA TIDAK INGIN FILTER): ').upper()
    if filterTipe == '' :
        actionFilterTipe = 0
    else :
        actionFilterTipe = 1

    while True :
        filterTahun = input('MASUKKAN TAHUN (ATAU TEKAN "ENTER" JIKA TIDAK INGIN FILTER): ')
        if filterTahun.isnumeric() :
            filterTahun = int(filterTahun)
            actionFilterTahun = 1
            break
        else  :
            if filterTahun == '' :
                actionFilterTahun = 0
                break
            else :
                print(f'{filterTahun} BUKAN ANGKA! \nATAU TEKAN TOMBOL "ENTER" JIKA TIDAK INGIN FILTER DATA')
    match = 0
    if actionFilterBrand == 1 and actionFilterTipe == 1 and actionFilterTahun == 1 :
        print('-'*75)
        print(f'HASIL FILTER BERDASARKAN BRAND = {filterBrand}, TIPE = {filterTipe} DAN TAHUN = {filterTahun}')
        for i in range(len(dataRentalMobil)) :
            if dataRentalMobil[i]['TIPE'] == filterTipe and dataRentalMobil[i]['TAHUN'] == filterTahun and dataRentalMobil[i]['BRAND'] == filterBrand :
                dataFilter.append(dataRentalMobil[i])
                match = 1
            else :
                continue
    elif actionFilterBrand == 1 and actionFilterTipe == 1 and actionFilterTahun == 0 :
        print('-'*75)
        print(f'HASIL FILTER BERDASARKAN BRAND = {filterBrand} DAN TIPE = {filterTipe}')
        for i in range(len(dataRentalMobil)) :
            if dataRentalMobil[i]['TIPE'] == filterTipe and dataRentalMobil[i]['BRAND'] == filterBrand :
                dataFilter.append(dataRentalMobil[i])
                match = 1
            else :
                continue
    elif actionFilterBrand == 1 and actionFilterTipe == 0 and actionFilterTahun == 1 :
        print('-'*75)
        print(f'HASIL FILTER BERDASARKAN BRAND = {filterBrand} DAN TAHUN = {filterTahun}')
        for i in range(len(dataRentalMobil)) :
            if dataRentalMobil[i]['TAHUN'] == filterTahun and dataRentalMobil[i]['BRAND'] == filterBrand :
                dataFilter.append(dataRentalMobil[i])
                match = 1
            else :
                continue
    elif actionFilterBrand == 0 and actionFilterTipe == 1 and actionFilterTahun == 1 :
        print('-'*75)
        print(f'HASIL FILTER BERDASARKAN TIPE = {filterTipe} DAN TAHUN = {filterTahun}')
        for i in range(len(dataRentalMobil)) :
            if dataRentalMobil[i]['TIPE'] == filterTipe and dataRentalMobil[i]['TAHUN'] == filterTahun :
                dataFilter.append(dataRentalMobil[i])
                match = 1
            else :
                continue
    elif actionFilterBrand == 0 and actionFilterTipe == 0 and actionFilterTahun == 1 :
        print('-'*75)
        print(f'HASIL FILTER BERDASARKAN TAHUN = {filterTahun}')
        for i in range(len(dataRentalMobil)) :
            if dataRentalMobil[i]['TAHUN'] == filterTahun:
                dataFilter.append(dataRentalMobil[i])
                match = 1
            else :
                continue
    elif actionFilterBrand == 0 and actionFilterTipe == 1 and actionFilterTahun == 0 :
        print('-'*75)
        print(f'HASIL FILTER BERDASARKAN TIPE = {filterTipe}')
        for i in range(len(dataRentalMobil)) :
            if dataRentalMobil[i]['TIPE'] == filterTipe :
                dataFilter.append(dataRentalMobil[i])
                match = 1
            else :
                continue
    elif actionFilterBrand == 1 and actionFilterTipe == 0 and actionFilterTahun == 0 :
        print('-'*75)
        print(f'HASIL FILTER BERDASARKAN BRAND = {filterBrand}')
        for i in range(len(dataRentalMobil)) :
            if dataRentalMobil[i]['BRAND'] == filterBrand :
                dataFilter.append(dataRentalMobil[i])
                match = 1
            else :
                continue
    else :
        print('-'*75)
        print('ANDA TIDAK MEMASUKKAN KEYWORD UNTUK FILTER'.center(75))
        return

    if match == 1 :
        print('-'*75)
        print(f'{'NO'.center(7)}|{'KODE'.center(8)}|{'BRAND'.center(13)}|{'TIPE'.center(13)}|{'TAHUN'.center(8)}|{'STOK'.center(6)}|{'HARGA SEWA'.center(14)}')
        print('-'*75)
        for i in range(len(dataFilter)) :
            print(f'{str(i+1).center(7)}|{dataFilter[i]['KODE'].center(8)}|{dataFilter[i]['BRAND'].center(13)}|{dataFilter[i]['TIPE'].center(13)}|{str(dataFilter[i]['TAHUN']).center(8)}|{str(dataFilter[i]['STOK']).center(6)}|{str(dataFilter[i]['HARGA SEWA']).center(14)}')
        print('-'*75)
    else :
        print('-'*75)
        print(' TIDAK ADA DATA YANG TERSEDIA ! '.center(75,'-'))

#1.3. TAMPILKAN HISTORY PENYEWAAN MOBIL
def riwayatSewa () :
    print('-'*75)
    print(f'{' RIWAYAT PEMESANAN MOBIL RENTAL '.center(75,'-')}')
    print('-'*75)
    if len(dataRiwayatRental) >= 1 :
        print(f'{'BRAND'.center(13)}|{'TIPE'.center(13)}|{'TAHUN'.center(9)}|{'QUANTITY'.center(10)}|{'DURASI(HARI)'.center(14)}|{'SUBTOTAL'.center(10)}')
        print('-'*75)
        for i in range(len(dataRiwayatRental)) :
            print(f'{dataRiwayatRental[i]['nama'].center(13)}|{dataRiwayatRental[i]['TIPE'].center(13)}|{str(dataRiwayatRental[i]['TAHUN']).center(9)}|{str(dataRiwayatRental[i]['jumlah']).center(10)}|{str(dataRiwayatRental[i]['durasi']).center(14)}|{str(dataRiwayatRental[i]['subtotal']).center(10)}')
        print('-'*75)
        print(f'{'TOTAL AKUMULASI'.rjust(59)}{str(hargaTotalRiwayatPenyewaan).center(20)}')
        print('-'*75)
    else :
        print('TIDAK ADA DATA DI RIWAYAT PENYEWAAN'.center(75))

#2. MENAMBAHKAN DATA LIST MOBIL RENTAL
def menuTambahkanData () :
    while True :
        print('-'*75)
        print(f'{' MENU 2 : MENAMBAHKAN DATA LIST MOBIL RENTAL '.center(75,'-')}')
        print('-'*75)
        tampilkanData()
        print('''
                1. MENAMBAHKAN DATA MOBIL RENTAL KE DATABASE
                2. KEMBALI KE MENU UTAMA 
                ''')
        print('-'*75)
        pilihan = input('MASUKKAN PILIHAN ANDA ( 1 / 2 ): ')
        print('-'*75)
        if pilihan == '1' :
            print(f'''INPUT DATA MOBIL YANG AKAN DITAMBAHKAN KE DATABASE :''')
            newKode = input('1. MASUKKAN KODE MOBIL : ').upper()
            newBrand = input('2. MASUKKAN BRAND MOBIL : ').upper()
            newTipe = input('3. MASUKKAN TIPE MOBIL : ').upper()
            while True :
                newTahun = input('4. MASUKKAN TAHUN PRODUKSI MOBIL : ')
                if newTahun.isnumeric() :
                    newTahun = int(newTahun)
                    break
                else :
                    print(f'INPUT {newTahun} TIDAK VALID, SILAHKAN INPUT TAHUN')
            
            addData = 1
            for item in dataRentalMobil :
                if item['KODE'] == newKode and item['BRAND'] == newBrand and item['TIPE'] == newTipe and item['TAHUN'] == newTahun :
                    addData = 0
                    break 

            if addData == 0 :
                print(f'JENIS MOBIL KODE {newKode} {newBrand} {newTipe} TAHUN {newTahun} SUDAH ADA !'.center(75,'-'))
                continue
            elif addData == 1 :
                while True :
                    newStok = input('5. MASUKKAN STOK MOBIL : ')
                    if newStok.isnumeric() :
                        newStok = int(newStok)
                        break
                    else :
                        print(f'INPUT {newStok} TIDAK VALID, SILAHKAN INPUT STOK')
                while True :
                    newHarga = input('6. MASUKKAN HARGA SEWA PER HARI : ')
                    if newHarga.isnumeric() :
                        newHarga = int(newHarga)
                        break
                    else :
                        print(f'INPUT {newHarga} TIDAK VALID, SILAHKAN INPUT HARGA SEWA PER HARI')                        
                print('-'*75)
                pilihan = input('SIMPAN DATA ? ( Y / N ) ').upper()
                if pilihan == 'Y' :
                    print('DATA BARU TELAH BERHASIL DITAMBAHKAN')
                    newData = {'KODE' : newKode,'BRAND' : newBrand, 'TIPE' : newTipe,'TAHUN' : newTahun, 'STOK' : newStok, 'HARGA SEWA' : newHarga}
                    dataRentalMobil.append(newData)
                elif pilihan == 'N' :
                    print('DATA TIDAK DISIMPAN')
                else :
                    print(f'INPUT {pilihan} TIDAK DIKENAL, DATA TIDAK DISIMPAN')
        elif pilihan == '2' :
            while True :
                pilihan = input(f'APAKAH ANDA INGIN KEMBALI KE MENU UTAMA? (Y/N) : ').upper()
                if pilihan == 'Y' :
                    return
                elif pilihan == 'N' :
                    break
                else :
                    print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')
        else :
            print(f'INPUT {pilihan} TIDAK DIKENALI, SILAHKAN COBA LAGI')

#3. MENG-UPDATE DATA LIST MOBIL RENTAL
def menuUpdateData () :
    while True :
        updateData = {}
        print('-'*75)
        print(f'{' MENU 3 : MENGUPDATE DATA LIST MOBIL RENTAL '.center(75,'-')}')
        print('-'*75) 
        tampilkanData() 
        print('''
                    1. UPDATE DATA MOBIL RENTAL
                    2. KEMBALI KE MENU UTAMA
              ''') 
        pilihan = input('MASUKKAN PILIHAN ANDA : ')
        print('-'*75)
        if pilihan == '1' :
            if len(dataRentalMobil) > 0 :
                kodeUpdate = input('MASUKKAN KODE MOBIL DARI DATA YANG AKAN DIUPDATE: ').upper()
                for i in range(len(dataRentalMobil)) :
                    if dataRentalMobil[i]['KODE'] == kodeUpdate :
                        print('-'*75)
                        print(f'{'NO'.center(7)}|{'KODE'.center(8)}|{'BRAND'.center(13)}|{'TIPE'.center(13)}|{'TAHUN'.center(8)}|{'STOK'.center(6)}|{'HARGA SEWA'.center(14)}')
                        print('-'*75)
                        print(f'{str(i+1).center(7)}|{dataRentalMobil[i]['KODE'].center(8)}|{dataRentalMobil[i]['BRAND'].center(13)}|{dataRentalMobil[i]['TIPE'].center(13)}|{str(dataRentalMobil[i]['TAHUN']).center(8)}|{str(dataRentalMobil[i]['STOK']).center(6)}|{str(dataRentalMobil[i]['HARGA SEWA']).center(14)}')
                        print('-'*75)
                        match = 1
                        break
                    else :
                        match = 0
                if match == 1 : 
                    while True :
                        pilihan = input('APAKAH ANDA AKAN MELANJUTKAN UPDATE ? ( Y / N ) ').upper()
                        if pilihan == 'Y' :
                            kolomUpdate = input('MASUKKAN KOLOM YANG AKAN DIUPDATE : ').upper()
                            if kolomUpdate == 'BRAND' or kolomUpdate == 'TIPE' or kolomUpdate == 'KODE' :
                                valueUpdate = input(f'MASUKKAN VALUE BARU UNTUK KOLOM {kolomUpdate} : ').upper()
                                print('-'*75)
                                updateData.update({kolomUpdate : valueUpdate})
                            elif kolomUpdate == 'STOK' or kolomUpdate == 'TAHUN' or kolomUpdate == 'HARGA SEWA' :
                                while True :
                                    valueUpdate = input(f'MASUKKAN VALUE BARU UNTUK KOLOM {kolomUpdate} : ')
                                    if valueUpdate.isnumeric() :
                                        valueUpdate = int(valueUpdate)
                                        break
                                    else :
                                        print(f'INPUT {valueUpdate} TIDAK VALID, SILAHKAN COBA LAGI')
                                print('-'*75)
                                updateData.update({kolomUpdate : valueUpdate})
                            else :
                                print('DATA YANG DIINPUT TIDAK VALID')
                        elif pilihan == 'N' : 
                            print('ANDA MEMILIH UNTUK TIDAK MELANJUTKAN UPDATE DATA')
                            break
                        else :
                            print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')
                    pilihan = input('SIMPAN DATA? ( Y / N ) ').upper()
                    if pilihan == 'Y' :
                        for item in updateData.items() :
                            dataRentalMobil[i][item[0]] = item[1]
                        print('DATA TELAH BERHASIL DIPERBAHARUI')
                    elif pilihan == 'N' : 
                        print('DATA TIDAK DISIMPAN')
                    else :
                        print(f'INPUT {pilihan} TIDAK VALID, DATA TIDAK DISIMPAN')
                else : #elif match == 0
                    print(f'KODE MOBIL {kodeUpdate} TIDAK TERSEDIA')
            else :
                print('DATABASE KOSONG, TIDAK ADA DATA YANG BISA DIUPDATE'.center(75))

        elif pilihan == '2' :
            while True :
                pilihan = input(f'APAKAH ANDA INGIN KEMBALI KE MENU UTAMA? (Y/N) : ').upper()
                if pilihan == 'Y' :
                    return
                elif pilihan == 'N' :
                    break
                else :
                    print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')
        else :
            print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')  

#4. MENGHAPUS DATA LIST MOBIL RENTAL
def menuHapusData () :
    while True :
        print('-'*75)
        print(f'{' MENU 4 : MENGHAPUS DATA LIST MOBIL RENTAL '.center(75,'-')}')
        print('-'*75) 
        tampilkanData()   
        print('''
            1. HAPUS DATA MOBIL RENTAL
            2. KEMBALI KE MENU UTAMA
        ''') 
        pilihan = input('MASUKKAN PILIHAN ANDA : ')
        print('-'*75)
        if pilihan == '1' :
            if len(dataRentalMobil) > 0 :
                kodeHapus = input('MASUKKAN KODE MOBIL YANG AKAN DIHAPUS: ').upper()
                for i in range(len(dataRentalMobil)) :
                    if dataRentalMobil[i]['KODE'] == kodeHapus :
                        print('-'*75)
                        print(f'{'NO'.center(7)}|{'KODE'.center(8)}|{'BRAND'.center(13)}|{'TIPE'.center(13)}|{'TAHUN'.center(8)}|{'STOK'.center(6)}|{'HARGA SEWA'.center(14)}')
                        print('-'*75)
                        print(f'{str(i+1).center(7)}|{dataRentalMobil[i]['KODE'].center(8)}|{dataRentalMobil[i]['BRAND'].center(13)}|{dataRentalMobil[i]['TIPE'].center(13)}|{str(dataRentalMobil[i]['TAHUN']).center(8)}|{str(dataRentalMobil[i]['STOK']).center(6)}|{str(dataRentalMobil[i]['HARGA SEWA']).center(14)}')
                        print('-'*75)
                        match = 1
                        break
                    else :
                        match = 0
                if match == 1 :
                    pilihan = input('HAPUS DATA? ( Y / N ) ').upper()
                    if pilihan == 'Y' :
                        del dataRentalMobil[i]
                        print('DATA TELAH BERHASIL DIHAPUS')
                    elif pilihan == 'N' : 
                        print('DATA TIDAK DIHAPUS')
                    else :
                        print(f'INPUT {pilihan} TIDAK VALID, DATA TIDAK DIHAPUS')
                else : # elif match == 0
                    print(f'KODE MOBIL {kodeHapus} TIDAK TERSEDIA')
                    continue
            else :
                print('DATABASE KOSONG, TIDAK ADA DATA YANG BISA DIHAPUS'.center(75))

        elif pilihan == '2' :
            while True :
                pilihan = input(f'APAKAH ANDA INGIN KEMBALI KE MENU UTAMA? (Y/N) : ').upper()
                if pilihan == 'Y' :
                    return
                elif pilihan == 'N' :
                    break
                else :
                    print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')
        else :
            print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')

#5. MEMESAN MOBIL RENTAL
def menuRentalMobil () :
    while True :
        cart = []
        hargaTotal = 0
        print('-'*75)
        print(f'{' MENU 5 : MEMESAN MOBIL RENTAL '.center(75,'-')}')
        print('-'*75) 
        print('''
                    1. ORDER MOBIL RENTAL
                    2. KEMBALI KE MENU UTAMA
        ''') 
        pilihan = input('MASUKKAN PILIHAN ANDA : ')
        print('-'*75)
        if pilihan == '1' :
            if len(dataRentalMobil) > 0 :
                tampilkanData()
                while True :
                    kodeMobil = input('MASUKKAN KODE MOBIL YANG AKAN DISEWA: ').upper()
                    match = 0
                    for i in range(len(dataRentalMobil)) :
                        if dataRentalMobil[i]['KODE'] == kodeMobil :
                            match = 1
                            break

                    if match == 0 :
                        print(f'KODE MOBIL {kodeMobil} TIDAK VALID')
                        continue
                    elif match == 1 :
                        print('-'*75)
                        print(f'{'NO'.center(7)}|{'KODE'.center(8)}|{'BRAND'.center(13)}|{'TIPE'.center(13)}|{'TAHUN'.center(8)}|{'STOK'.center(6)}|{'HARGA SEWA'.center(14)}')
                        print('-'*75)
                        print(f'{str(i+1).center(7)}|{dataRentalMobil[i]['KODE'].center(8)}|{dataRentalMobil[i]['BRAND'].center(13)}|{dataRentalMobil[i]['TIPE'].center(13)}|{str(dataRentalMobil[i]['TAHUN']).center(8)}|{str(dataRentalMobil[i]['STOK']).center(6)}|{str(dataRentalMobil[i]['HARGA SEWA']).center(14)}')
                        print('-'*75)
                        qtyOrder = input('MASUKKAN QUANTITY MOBIL RENTAL : ')
                        if qtyOrder.isnumeric() :
                            qtyOrder = int(qtyOrder)
                            if qtyOrder > dataRentalMobil[i]['STOK'] :
                                print(f'STOK TIDAK CUKUP, STOK SISA {dataRentalMobil[i]['STOK']}')
                                continue
                            else :
                                while True :
                                    dayOrder = input('MASUKKAN DURASI PENYEWAAN MOBIL (HARI) : ')
                                    if dayOrder.isnumeric() :
                                        dayOrder = int(dayOrder)
                                        break
                                    else :
                                        print(f'{dayOrder} BUKAN ANGKA, SILAHKAN INPUT ANGKA')
                                cart.append({'nama' : dataRentalMobil[i]['BRAND'], 'TIPE' : dataRentalMobil[i]['TIPE'], 'TAHUN' : dataRentalMobil[i]['TAHUN'], 'jumlah': qtyOrder, 'durasi': dayOrder,'subtotal': dataRentalMobil[i]['HARGA SEWA']*qtyOrder*dayOrder})
                                dataRiwayatRental.append({'nama' : dataRentalMobil[i]['BRAND'], 'TIPE' : dataRentalMobil[i]['TIPE'], 'TAHUN' : dataRentalMobil[i]['TAHUN'], 'jumlah': qtyOrder, 'durasi': dayOrder,'subtotal': dataRentalMobil[i]['HARGA SEWA']*qtyOrder*dayOrder})
                                dataRentalMobil[i]['STOK'] -= qtyOrder
                                hargaTotal += dataRentalMobil[i]['HARGA SEWA']*qtyOrder*dayOrder
                                global hargaTotalRiwayatPenyewaan
                                hargaTotalRiwayatPenyewaan += dataRentalMobil[i]['HARGA SEWA']*qtyOrder*dayOrder
                                while True :
                                    pilihan = input('APAKAH MAU ORDER MOBIL LAIN? ( Y / N ) ').upper()
                                    print('-'*75)
                                    if pilihan == 'Y' or pilihan == 'N':
                                        break
                                    else :
                                        print(f'INPUT {pilihan} TIDAK DIKENALI ')
                                if pilihan == 'Y' :
                                        continue
                                elif pilihan == 'N' :
                                        break
                        else :
                            print(f'{qtyOrder} BUKAN ANGKA!')
                if len(cart) > 0 :
                    print('-'*75)
                    print(f'{' BILL ORDER '.center(75,'-')}')
                    print('-'*75)
                    print(f'{'BRAND'.center(13)}|{'TIPE'.center(13)}|{'TAHUN'.center(9)}|{'QUANTITY'.center(10)}|{'DURASI(HARI)'.center(14)}|{'SUBTOTAL'.center(10)}')
                    print('-'*75)
                    for i in range(len(cart)) :
                        print(f'{cart[i]['nama'].center(13)}|{cart[i]['TIPE'].center(13)}|{str(cart[i]['TAHUN']).center(9)}|{str(cart[i]['jumlah']).center(10)}|{str(cart[i]['durasi']).center(14)}|{str(cart[i]['subtotal']).center(10)}')
                    print('-'*75)
                    print(f'{'TOTAL AKUMULASI'.rjust(59)}{str(hargaTotal).center(20)}')
                    print('-'*75)
                    while(True) :
                        uangBayar = input('MASUKKAN JUMLAH UANG : ')
                        if uangBayar.isnumeric() :
                            uangBayar = int(uangBayar)
                            if uangBayar < hargaTotal :
                                print(f' UANG ANDA KURANG SEBESAR  {hargaTotal - uangBayar} '.center(75,'-'))
                            elif uangBayar == hargaTotal :
                                print('-'*75)
                                print('TERIMAKASIH'.center(75))
                                print('-'*75)
                                break
                            else :
                                print('-'*75)
                                print(f' TERIMAKASIH '.center(75))
                                print(f' KEMBALIAN ANDA : {uangBayar-hargaTotal} '.center(75))
                                print('-'*75)
                                break  
                        else :
                            print(f'{qtyOrder} BUKAN ANGKA! SILAHKAN INPUT ANGKA')
                else : 
                    break   
            else :
                print('DATABASE KOSONG, TIDAK ADA YANG BISA DIORDER'.center(75))
        elif pilihan == '2' :
            while True :
                pilihan = input(f'APAKAH ANDA INGIN KEMBALI KE MENU UTAMA? (Y/N) : ').upper()
                if pilihan == 'Y' :
                    return
                elif pilihan == 'N' :
                    break
                else :
                    print(f'INPUT {pilihan} TIDAK VALID, SILAHKAN COBA LAGI')
        else :
            print(f'INPUT {pilihan} TIDAK VALID')

#MENU UTAMA APLIKASI RENTAL MOBIL
def mainmenu() :
    while True :
        print('-'*75)
        print(f' MENU UTAMA APLIKASI RENTAL MOBIL '.center(75,'-'))
        print('-'*75)
        print('''
                1. MENAMPILKAN LIST DAFTAR MOBIL RENTAL
                2. MENAMBAHKAN DATA LIST MOBIL RENTAL
                3. MENG-UPDATE DATA LIST MOBIL RENTAL
                4. MENGHAPUS DATA LIST MOBIL RENTAL
                5. MEMESAN MOBIL RENTAL
                6. KELUAR DARI APLIKASI
            ''')
        print('-'*75)
        pilihan = input('MASUKKAN PILIHAN ANDA : ')
        if pilihan == '1' :
            menuTampilkanData()
        elif pilihan == '2' :
            menuTambahkanData()
        elif pilihan == '3' :
            menuUpdateData()
        elif pilihan == '4' :
            menuHapusData()
        elif pilihan == '5' :
            menuRentalMobil ()
        elif pilihan == '6' :
            break
        else :
            print('-'*75)
            print(f'INPUT {pilihan} TIDAK VALID !')
    
mainmenu()