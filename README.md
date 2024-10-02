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

# Tugas 4 PBP

# 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
Fungsi HttpResponseRedirect() mengembalikan objek HttpResponse yang akan redirect ke URL tertentu, sesuai dengan parameter yang telah ditetapkan. Sedangkan redirect() merupakan fungsi yang lebih abstrak karena dapat menerima URL sebagai parameter, serta menerima nama dari view atau objek model yang akan otomatis ditangani URL-nya oleh Django.

# 2. Jelaskan cara kerja penghubungan model Product dengan User!
Dengan modul django.contrib.auth.models, kemudian potongan kode berikut pada class Product:
user = models.ForeignKey(User, on_delete=models.CASCADE)
Akan menghubungkan satu entry product dengan satu user, sehingga setiap product entry pasti terasosiasikan dengan seorang user.

Kemudian potongan kode product_entries = Product.objects.filter(user=request.user) berguna untuk hanya menampilkan product entry yang terasosiasi dengan user yang sedang login. Sistem akan mengetahui bahwa objek product entry tertentu milik user yang sedang login karena adanya kode 'name': request.user.username.

# 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication merupakan proses untuk mengenali identitas pengguna, biasanya melalui username dan password. Sedangkan authorization merupakan proses untuk menentukan hak akses pengguna terhadap fitur/data pada web, biasanya sesuai dengan peran pengguna (user atau admin). 

Saat pengguna login, mereka akan memasukkan username dan password mereka untuk diverifikasi oleh Django. Jika valid, maka pengguna diautentikasi dan sesi dimulai sesuai authorization yang diberikan kepada pengguna tersebut.

Django mengimplementasikan authentication ketika pengguna melakukan login, dimana kredensial pengguna akan diverifikasi dan dipastikan cocok dengan data yang ada di database. Hal ini dilakukan dengan modul django.contrib.auth, serta method authenticate() dan login() Kemudian, Django akan melakukan authorization dengan mengecek apakah pengguna memiliki izin untuk melakukan aksi/mengakses data tertentu. Hal ini dilakukan menggunakan sistem permissions oleh Django, dimana setiap model atau view dapat diatur dengan izin tertentu yang membatasi akses pengguna sesuai dengan perannya.

# 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Ketika pengguna berhasil login, Django menyimpan session data pada server dan menyimpan session ID pada cookie di browser pengguna. Setiap kali pengguna melakukan request baru, session ID tersebut akan dikirim kembali ke server untuk mengidentifikasi pengguna yang login.

Selain untuk login, cookies juga dapat digunakan untuk menyimpan preferensi setting pengguna, melacak aktivitas pengguna, dan sebagai token autentikasi dalam Single Sign-On (SSO).

Tidak semua cookies aman digunakan, karena cookies juga dapat dieksploitasi melalui serangan Cross-Site Scripting (XSS) atau Session Hijacking. Cookies yang tidak diamankan juga dapat digunakan oleh penyerang untuk mencuri informasi sesi atau melakukan session fixation attacks.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
     a. Memastikan direktori sudah sesuai dengan yang ada di tutorial, dan mengubah nama file deploy.yml menjadi push.yaml
     b. Menyalakan virtual environment dan membuat fitur registrasi agar pengguna dapat membuat akun dengan username dan password
     c. Fitur registrasi dibuat dengan import UserCreationForm dan messages, kemudian membuat fungsi register di file views.py, kemudian membuat file register.html untuk mengatur tampilan halaman registrasi untuk pengguna. Kemudian import fungsi registrasi di file urls.py dan mengatur path url menuju fungsi tersebut di urlpatterns.
     d. Sama seperti langkah sebelumnya, saya membuat fitur login dengan import AuthenticationForm dan login di file views.py, kemudian membuat fungsi login di file views.py, beserta file login.html untuk mengatur tampilan halaman login untuk pengguna. Kemudian import fungsi login di file urls.py dan mengatur path url menuju fungsi tersebut di urlpatterns.
     e. Sama juga seperti kedua langkah sebelumnya, saya membuat fitur logout dengan import logout di file views.py, kemudian membuat fungsi logout di file views.py, dan menambahkan tombol logout di file main.html. Kemudian import fungsi logout di file urls.py dan mengatur path url menuju fungsi tersebut di urlpatterns.
     f. Saya juga menambahkan restriksi pada halaman main web saya agar hanya user yang sudah diautentikasi yang dapat mengaksesnya. Hal ini dilakukan dengan import login_required pada file views.py, kemudian menambahkan kode @login_required(login_url='/login') di atas fungsi show_main di file yang sama.
     g. Saya mencoba test fitur-fitur yang telah diimplementasi dengan cara membuat satu akun untuk test fitur registrasi, dan mencoba untuk login dan logout dengan akun tersebut.
     h. Setelah fitur sudah berhasil diimplementasikan, saya menambahkan fitur untuk menampilkan waktu terakhir akun tersebut login dengan menggunakan cookies. 
     i. Fitur tersebut ditambahkan dengan cara import HttpResponseRedirect, reverse, dan datetime di file views.py, kemudian menambahkan kedua baris kode berikut pada fungsi login, khususnya di blok if form.is_valid():
          response = HttpResponseRedirect(reverse("main:show_main"))
          response.set_cookie('last_login', str(datetime.datetime.now()))
     j. Pada fungsi show_main juga ditambahkan kode berikut: 
          'last_login': request.COOKIES['last_login'],
     k. Dan pada fungsi logout juga ditambahkan kode berikut:
          response = HttpResponseRedirect(reverse('main:login'))
          response.delete_cookie('last_login')
     l. Menambahkan kode di file main.html untuk menampilkan data waktu/sesi terakhir kali user login
     m. Menghubungkan Product dengan user agar tampilan produk di web untuk setiap user sesuai dengan produk yang ditambahkan oleh user tersebut
     n. Hal tersebut dilakukan dengan import User di file models.py kemudian menambahkan kode berikut di model Products:
          user = models.ForeignKey(User, on_delete=models.CASCADE)
     o. Kemudian menambahkan kode di fungsi create_product_entry di file views.py:
          product_entry = form.save(commit=False)
          product_entry.user = request.user
          product_entry.save()
     p. Mengubah juga potongan kode pada fungsi show_main menjadi sebagai berikut:
          product_entries = Product.objects.filter(user=request.user)

          context = {
               'name': request.user.username,
               ...
          }
     q. Kemudian save semua perubahan dan make migrations untuk migrasi model. Saat muncul error, saya menetapkan user yang telah diregistrasi sebelumnya sebagai default value dengan ID 1 untuk field user pada semua row database, kemudian dilakukan migrasi lagi.
     r. Terakhir, menambah import OS di file settings.py dan mengubah variabel DEBUG menjadi sebagai berikut:
          PRODUCTION = os.getenv("PRODUCTION", False)
          DEBUG = not PRODUCTION
     s. Menyimpan semua perubahan dan melakukan git add, commit, dan push untuk menyimpan perubahan juga di repository Github dan sekaligus push ke PWS.

# Tugas 5 PBP

# 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan pengambilan CSS selector dipengaruhi oleh spesifisitas selector dan aturan cascade, khususnya urutan prioritasnya adalah: Inline CSS (contoh: <div style="color: red;">), ID Selector (#id), Class Selector (.class), attribute selector, dan pseudo-class (:hover, :focus), kemudian Tag/Type Selector (div, p, h1) memiliki prioritas paling rendah. Pengecualian untuk rule yang memiliki deklarasi !important maka akan diprioritaskan di atas rule yang lain.

# 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design artinya desain dan layout web dapat menyesuaikan dengan berbagai ukuran device. Hal ini penting untuk pengalaman pengguna (UX) agar tampilan website tetap nyaman dilihat dan digunakan dari device apapun. Hal ini juga memudahkan pengembang agar hanya perlu mengembangkan satu versi web yang dapat otomatis menyesuaikan dengan tiap device.

# 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin: spacing di luar elemen yang memisahkan suatu elemen dengan elemen lain.
Contoh: margin: 20px;

Border: garis pembatas di sekeliling konten elemen, terletak di antara padding dan margin. 
Contoh: border: 2px solid black;

Padding: spacing di dalam elemen, di antara konten elemen dan border elemen.
Contoh: padding: 10px;

# 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox berguna untuk layout satu dimensi (baris atau kolom). Kegunaannya adalah untuk mengatur item dalam satu baris atau kolom untuk alignment, spacing, dan pengaturan ukuran otomatis berdasarkan ruang yang tersedia. Contoh kegunaannya adalah untuk mengatur elemen dalam navigation bar.

Sedangkan grid layout adalah sistem layout dua dimensi (baris dan kolom). Kegunaannya adalah untuk memberikan kontrol lebih dalam membuat grid kompleks dengan banyak baris dan kolom yang bisa diatur secara eksplisit. Contoh kegunaannya adalah untuk mengatur layout halaman utama yang memiliki header, sidebar, dan konten utama.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
     a. Memastikan direktori sudah sesuai dengan yang ada di tutorial 
     b. Memastikan file base.html sudah memiliki tag <meta name="viewport"> agar halaman web dapat menyesuaikan dengan ukuran mobile
     c. Menghubungkan template Django dengan tailwind dengan menambahkan barisan kode <script src="https://cdn.tailwindcss.com"> </script> pada file base.html
     d. Menambahkan fungsi edit_product pada file views.py, kemudian menambah import reverse dan HttpResponseRedirect
     e. Membuat file edit_product.html di main/templates yang berisi tampilan dari page untuk edit detail product
     f. Import fungsi edit_product yang telah dibuat dan mengatur pathnya di file urls.py
     g. Menambahkan tombol edit product button di file main.html
     h. Menambahkan fungsi delete_product pada file views.py, kemudian import fungsi dan mengatur pathnya di file urls.py
     i. Menambahkan tombol delete product button di file main.html
     j. Menjalankan perintah python manage.py runserver untuk mengecek apakah tombol edit product dan delete product sudah berfungsi dengan baik
     k. Menambahkan navigation bar dengan membuat file navbar.html pada folder templates di root directory, yang akan mengatur tampilan dari navigation bar
     l. Menambah {% include 'navbar.html' %} di file main.html, create_product_entry.html, dan edit_product.html agar navigation bar tetap tertampil di semua halaman web
     m. Menambahkan konfigurasi static dengan barisan kode 'whitenoise.middleware.WhiteNoiseMiddleware' di variable MIDDLEWARE pada file settings.py agar file statis dapat diakses di deployment saya
     n. Mengubah variable static pada file settings.py sebagai berikut:
          STATIC_URL = '/static/'
          if DEBUG:
               STATICFILES_DIRS = [
                    BASE_DIR / 'static' # merujuk ke /static root project pada mode development
               ]
          else:
               STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
     o. Mulai mengatur design dari web dengan pertama membuat file global.css di direktori static/css
     p. Menambahkan barisan kode <link rel="stylesheet" href="{% static 'css/global.css' %}"/> pada file base.html untuk menghubungkan file global.css dengan template
     q. Mengatur design web sesuai kemauan saya di file global.css, login.html, register.html, create_product_entry.html, dan edit_product.html
     r. Membuat file card_info.html untuk menampilkan nama, npm, kelas, dan last log in untuk user yang sedang logged in
     s. Membuat file card_prouct.html untuk menampilkan setiap product entry
     t. Menambahkan foto no-product.png untuk ditampilkan di halaman utama saat belum ada product yang ditambahkan
     u. Menambahkan barisan include pada file main.html untuk menampilkan semua berkas yang sudah dibuat 
     v. Menambahkan image logo.png untuk di navigation bar, logo-full.png untuk di halaman utama, home.webp untuk background halaman utama
     w. Melakukan git add, commit, dan push untuk menyimpan semua perubahan ke repository github dan sekaligus push ke pws.