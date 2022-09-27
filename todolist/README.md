Link heroku tugas ini:
Home : https://tugas2-pbp-vinsen.herokuapp.com/todolist/ (wajib login)
Login : https://tugas2-pbp-vinsen.herokuapp.com/todolist/login
register : https://tugas2-pbp-vinsen.herokuapp.com/todolist/register
Membuat Task : https://tugas2-pbp-vinsen.herokuapp.com/todolist/create-task/ (wajib login)

Akun yang dibuat:
1. username : vinsen | password : AnakKuda123
2. username : sapi | password : AnakKuda123
Setiap akun memiliki 3 dummy data buku

Fungsi dari tag {% csrf_token %} merupakan sebuah implementasi untuk melindungi program yang dibuat terhadap serangan dari luar. Tag tersebut akan membuat token CSRF pada server pada saat melakukan rendering suatu laman. CRSF Token tersebut akan dicek secara terus menerus sebelum memproses request yang datang dari user. Dengan kata lain, akses laman tanpa adanya CSRF token akan membatalkan eksekusi code yang akan memproses laman sebagai respon pada user. (Sumber info: https://www.educative.io/answers/what-is-a-csrf-token-in-django dan django documentation)

Seperti yang kita tahu, tag {{ form.as_table }} akan melakukan rendering for yang kita buat ke dalam sebuah bentuk tabel yang diawali "<tr>" dan diakhiri "</tr>" pada template yang kita rancang. Akan tetapi, penggunaan tag {{ form.as_table }} DAPAT kita abaikan dan tidak gunakan apabila kita akan membuat sebuah form dan menyusun strukturnya secara mandiri. untuk menyusun struktur form secara manual adalah sebagai berikut:
1. Membuat komponen form secara manual misalnya, button, field, dan label. Setelah itu, kita akan menyusun komponen yang diinginkan untuk disusun ke dalam sebuah bentuk tabel dengan cara nomor2.
2. Memberikan tag <table> dan </table> pada awal dan akhir struktur form yang ingin kita susun seperti sebuah table. Hal ini dikarenakan bahwa, tanpa adanya tag {{ form.as_table }}, maka <table> dan </table> tidak akan otomatis terbentuk dan membuat struktur bagian form yang kita rancang menjadi berantakan. Selain itu, tanpa ada tag <table> dan </table>, browser tidak memiliki referensi untuk melakukan render aplikasi.

Pada saat user melakukan pengisian dan submit form, maka aplikasi pertama kali akan langsung melakukan pengecekan CSRF token terlebih dahulu. Submisi data form akan melakukan hit pada server yang men-trigger transfer data ke dalam database. Setelah itu, aplikasi akan melakukan pencocokan data yang dimasukan oleh user dengan models dan fields yang ada pada aplikasi. Setelah berhasil melakukan pencocokan, aplikasi akan memulai migration dan melakukan setup pada database tempat kita menyimpan data. Data base akana menyimpan data dengan mengatur user sebagai user yang logged in pada saat itu, dan date sebagai waktu pada saat itu. Setelah daya disimpan, untuk menampilkan pada template, views.py akan mengambil seluruh object yang ada pada models dan melakukkan passing data tersebut untuk di render dalam bentuk context. Setelah itu, pada template, aplikasi akan memanfaatkan iterasi for loop untuk menampilkan data-data yang ada kepada user dalam bentuk response yang telah dirender rapi. 

Alur dan cara menjalankan checklist tugas:
1. saya melakukan startapp todolist untuk membuat aplikasi todolist
2. Saya memasukan path path('todolist/', include('todolist.urls')), pada urls.py di project django sehingga apabila user hit path tersebut, user akan dialihkan ke urls.py di todolist
3. Saya menyusun model task dengan atribut User sebagai foreign key, date sebagai waktu aktual pada saat itu, title dengan charfield sebagai judul, description dengan textfield sebagai deskripsi.
4. Saya membuat template, menyusun views, dan memasukkan path untuk login, register, dan logout pada aplikasi todolist.
5. Saya menyusun routing pada todolist urls.py sesuai dengan permintaan pada soal.
6. Saya melakukan deployment ke heroku melalui perantara github
7. Saya menyusun 2 akun dan 3 dummy data pada heroku dengan melakukan register 2 kali dan memasukkan 3 data task pada masing-masing akun.