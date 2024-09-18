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

# Tugas 3 PBP

# 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery memastikan bahwa data bisa berjalan dengan baik antara client, server, dan database. Hal ini memungkinkan adanya pertukaran data secara real-time, memastikan bahwa data yang ditransfer tetap aman dengan adanya enkripsi, dan meningkatkan efisiensi pengiriman data.

# 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik karena sintaksnya lebih sederhana sehingga lebih mudah untuk dipahami, dan biasanya memiliki ukuran file yang kecil dibandingkan XML. JSON juga didukung oleh JavaScript, sehingga umum digunakan di web development. Maka dari itu, JSON juga lebih populer dibandingkan XML.

# 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
form.is_valid() digunakan pada fungsi create_product_entry di file views.py untuk memvalidasi input dari form dengan memastikan bahwa tipe data yang diinput sesuai dengan permintaan pengemabang. Hal ini digunakan untuk memastikan integritas data sehingga hanya data yang valid yang akan disimpan, dan untuk mengantisipasi kesalahan input data dari user sebelum mereka submit data tersebut.

# 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Cross-Site Request Forgery (csrf) token digunakan untuk mengenerasi token yang unik untuk memastikan bahwa request yang dipanggil berasal dari user yang membuka halaman web tersebut, sehingga memblokir unauthorized request. Hal ini dibutuhkan untuk menghindari CSRF attack, dimana seorang penyerang memanfaatkan user yang sedang logged in dengan meng-submit malicious request. Tanpa csrf token, penyerang dapat memanfaatkan user yang sedang logged-in karena server sudah 'trust' request dari user tersebut. 

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
     a. Membuat template dasar di file base.html agar halaman web yang lainnya dapat memuat data secara dinamis, kemudian mengatur variable TEMPLATES di file settings.py agar file base.html terdeteksi sebagai template.
     b. Mengaplikasikan template di file main.html dengan cara menambahkan baris kode  {% extends 'base.html' %}.
     c. Import Universally Unique Identifier (UUID) di file models.py untuk mengubah primary key agar tidak sekuensial, sehingga menjadi lebih aman karena lebih sulit untuk ditebak. Setelah import maka dilakukan migrasi model.
     d. Membuat file forms.py untuk membuat form input data name, price, description, size, dan color untuk input data product baru.
     e. Menambahkan 2 import di file views.py: fungsi render yang berfungsi untuk menampilkan data sesuai bentuk template pada suatu halaman web, dan fungsi redirect untuk membawa user ke URL yang ditentukan.
     f. Membuat fungsi create_product_entry yang menerima parameter request di file views.py. Fungsi ini akan menghasilkan form yang akan menambahkan data product saat user melakukan save. 
     g. Menambahkan product_entries pada fungsi show_main yang akan mengambil semua objek/data pada Products dengan Product.objects.all(). 
     h. Import fungsi create_product_entry di file urls.py, kemudian menambahkan path ke fungsi create_product_entry ke variabel urlpatterns.
     i. Membuat file HTML create_product_entry.html untuk menampilkan fields form pada forms.py sebagai tabel dan menampilkan tombol submit yang akan mengirimkan request ke view create_product_entry(request)
     j. Menambahkan tampilan data pada file main.html untuk menampilkan pesan "Belum ada data product pada bag shopper." jika belum ada input data, dan menampilkan data dalam bentuk tabel jika sudah ada input data. Menambahkan juga tampilan tombol "Add New Product Entry" yang akan redirect ke halaman form.
     k. Menambahkan 2 import di file views.py: HttpResponse dan Serializer untuk translate objek model menjadi format XML.  
     l. Menambahkan fungsi show_xml(request) yang akan menampilkan data dalam bentuk XML. Kemudian import fungsi tersebut di file urls.py, dan menambahkan path URL ke fungsi tersebut di urlpatterns.
     m. Melakukan hal yang sama dengan fungsi show_json(request), untuk menampilkan data dalam bentuk JSON.
     n. Menambahkan parameter id dan filter(pk=id) pada pengambilan data dengan Product.objects di keuda fungsi show_xml dan show_json agar kita bisa memilih objek (input data) yang ingin dilihat sesuai dengan IDnya.
     o. Melakukan git add, commit, dan push untuk menyimpan perubahan yang telah dibuat ke repository di github.
     p. Menjalankan server dengan command "python manage.py runserver", kemudian membuka aplikasi Postman.
     q. Membuat request baru menggunakan method GET dan memasukkan URL http://localhost:8000/xml/, http://localhost:8000/json/, http://localhost:8000/xml/[id], dan http://localhost:8000/json/[id] untuk menampilkan seluruh objek dalam bentuk XML dan JSON, serta objek dengan ID tertentu dalam bentuk XML dan JSON. 

# screenshot 
![alt text](<Screenshot 2024-09-18 at 08.42.39-1.png>)
![alt text](<Screenshot 2024-09-18 at 08.43.03.png>)
![alt text](<Screenshot 2024-09-18 at 08.43.25.png>)
![alt text](<Screenshot 2024-09-18 at 08.43.36.png>)