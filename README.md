1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Buat folder baru di lokal bernama 'e-commerce', kemudian membuat repositori baru di git hub dengan nama yang sama, lalu melakukan set up untuk menghubungkan folder lokal dengan repositori di git.
b. Aktifkan virtual environment, kemudian tambahkan dan install dependencies.
c. Buat proyek django bernama 'e_commerce' untuk mendapatkan semua files yang dibutuhkan untuk membuat website.
d. Konfigurasi proyek dan menjalankan server dengan mengatur ALLOWED_HOSTS dan menjalankan perintah python3 manage.py runserver, untuk memastikan bahwa website sudah bisa berjalan dengan benar.
e. Melakukan git add, commit, dan push untuk mengunggah proyek 'e-commerce' ke repository github saya.
f. Mulai membuat aplikasi baru 'main' dan mendaftarkannya ke INSTALLED_APPS.
g. Membuat file baru bernama 'main.html', dan mengisi file tersebut dengan data yang ingin ditampilkan (name, price, description, size, dan color).
h. Mengatur definisi pada file 'models.py' untuk menetapkan name, size, dan color sebagai CharField, price sebagai IntegerField, dan description sebagai TextField, kemudian melakukan migrasi.
i. Konfigurasi routing URL pada aplikasi main dan proyek dengan mengubah isi pada file 'urls.py' pada aplikasi dan file 'urls.py' pada proyek.
j. Deploy website saya ke PWS agar dapat diakses oleh orang lain di internet
k. Melakukan git add, commit, dan push untuk menyimpan semua perubahan yang telah dibuat pada repository github saya.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django menyediakan banyak fitur, sehingga memudahkan pengembang karena mereka tidak perlu mengonfigurasi semuanya dari awal. Django juga memiliki konvensi yang lebih sederhana, serta dokumentasi yang mudah untuk dipahami. Di dunia nyata juga, Django banyak digunakan oleh perusahaan-perusahaan besar seperti Instagram dan Pinterest, yang membuktikan bahwa framework ini tepat untuk dipelajari karena akan bermanfaat di dunia pekerjaan.

5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena membantu kita untuk menghubungkan objek di dalam kode Python dengan tabel dalam database, sehingga tidak membutuhkan  SQL secara langsung. Django juga dapat memetakan kelas Python ke tabel database dan atribut kelas ke kolom tabel secara otomatis, dan memungkinkan aplikasi berinteraksi dengan berbagai jenis database tanpa harus menulis ulang kode saat mengganti database yang digunakan.

Maka dari itu, ORM sangat membantu dalam mempercepat pengembangan aplikasi, karena mengurangi kompleksitas berinteraksi langsung dengan database.
a