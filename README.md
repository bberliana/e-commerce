# Tugas 2 PBP
**Rania Berliana** 
**2306165875**
**PBP B**

# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
    a. Buat folder baru di lokal bernama 'e-commerce', kemudian membuat repositori baru di git hub dengan nama yang sama, lalu melakukan set up untuk menghubungkan folder lokal dengan repositori di git.
    b. Aktifkan virtual environment, kemudian tambahkan dan install dependencies yang dibutuhkan untuk membuat website (termasuk Django).
    c. Buat proyek Django bernama 'e_commerce' untuk mendapatkan semua files yang dibutuhkan untuk membuat website.
    d. Konfigurasi proyek dan menjalankan server dengan menambahkan 'localhost' pada ALLOWED_HOSTS di file settings.py dan menjalankan perintah python3 manage.py runserver, untuk memastikan bahwa website sudah bisa berjalan dengan benar.
    e. Melakukan git add, commit, dan push untuk mengunggah proyek 'e-commerce' ke repository github saya.
    f. Mulai membuat aplikasi baru 'main' dan mendaftarkannya ke INSTALLED_APPS di file settings.py.
    g. Membuat file baru bernama 'main.html', dan mengisi file tersebut dengan data yang ingin ditampilkan (name, price, description, size, dan color).
    h. Mengatur definisi pada file 'models.py' untuk menetapkan name, size, dan color sebagai CharField, price sebagai IntegerField, dan description sebagai TextField, kemudian melakukan migrasi untuk menyesuaikan dengan perubahan model.
    i. Import render pada file views.py, yang akan digunakan untuk membuat fungsi view show_main, kemudian membuat fungsi show_main sesuai dengan tampilan informasi yang diinginkan (name, price, description, size, dan color).  
    j. Konfigurasi routing URL pada aplikasi main untuk menggunakan fungsi show_main yang telah dibuat sebelumnya, dan routing URL pada proyek untuk include main.urls pada urlpatterns.
    k. Login ke website PWS dan membuat proyek baru bernama 'ecommerce', yang nantinya akan digunakan untuk deploy website saya agar dapat diakses oleh orang lain melalui internet.
    l. Menambahkan link url deployment PWS saya pada ALLOWED_HOSTS di file settings.py.
    m. Melakukan git add, commit, dan push untuk menyimpan semua perubahan yang telah dibuat pada repository github saya.
    n. Menjalankan perintah project command dari PWS untuk mendeploy website saya, dan website sudah bisa diakses oleh orang lain melalui internet.

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.  
     Client (User) 
        | mengirim request
        v
-------------------------------
     urls.py 
-------------------------------
        | interaksi dengan model
        v
-------------------------------
     views.py
-------------------------------
        | return data kepada view
        v
-------------------------------
     models.py 
-------------------------------
        | render response
        v
-------------------------------
     HTML template 
-------------------------------
        | mengirim response
        v
     Client Response 

# 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!  
Git membantu pengembang untuk melacak semua perubahan-perubahan yang telah dibuat, karena setiap aksi git add, commit, dan push akan menyimpan perubahannya pada repositori git. Git juga dapat membantu beberapa pengembang untuk bekerjasama pada satu proyek dengan menggunakan branching, dimana masing-masing pengembang dapat mengerjakan bagiannya masing-masing tanpa mengganggu pengerjaan pengembang yang lainnya.

# 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?  
Django menyediakan banyak fitur, sehingga memudahkan pengembang karena mereka tidak perlu mengonfigurasi semuanya dari awal. Django juga menggunakan bahasa Python yang relatif lebih sederhana dan mudah untuk dipahami dibandingkan bahasa pemrograman yang lainnya. Di dunia nyata juga, Django banyak digunakan oleh perusahaan-perusahaan besar seperti Instagram dan Pinterest, yang membuktikan bahwa framework ini tepat untuk dipelajari karena akan bermanfaat di dunia pekerjaan.

# 5. Mengapa model pada Django disebut sebagai ORM?  
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena membantu kita untuk menghubungkan objek di dalam kode Python dengan tabel dalam database, sehingga tidak membutuhkan  SQL secara langsung. Django juga memungkinkan aplikasi untuk berinteraksi dengan berbagai jenis database tanpa harus menulis ulang kode saat mengganti database yang digunakan. Maka dari itu, ORM sangat mempercepat pengembangan aplikasi, karena mengurangi kompleksitas berinteraksi langsung dengan database.