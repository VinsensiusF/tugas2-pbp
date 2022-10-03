Link heroku tugas ini:
Home : https://tugas2-pbp-vinsen.herokuapp.com/todolist/ (wajib login)

Inline CSS
Inline CSS merupakan penggunaan CSS dimana kode CSS dituliskan secara langsung pada atribut elemen yang ada di HTML.
Kelebihan Inline CSS adalah dapat dimanfaatkan saat live-coding sehingga perubahan elemen yang di-edit akan dapat langsung terlihat, dan pemrosesan request akan lebih cepat karena tidak perlu meng-import CSS dari file lain sehingga, load website lebih cepat dan responsif
Kelemahan inline CSS adalah kerapian kode yang ditulis menurun karena penulisan css yang bertumpuk, dan keefisienan yang rendah karena satu CSS hanya berlaku untuk satu elemen saja.

Internal CSS
Internal CSS merupakan penggunaan CSS dimana kode CSS dituliskan di dalam tag HTML dan kode HTML-nya berada pada header file HTML.
Kelebihan Internal CSS adalah keefektifan saat melakukan editing per halaman saja karena CSS tipe ini hanya berlaku untuk satu file HTML, dan penggunaan yang lebih mudah dengan memanfaatkan 'class' dan 'id'.
Kelemahan Internal CSS adalah Ketidak-efisienan saat akan melakukan editing dengan banyak file HTML mengacu pada satu CSS yang sama sehingga duplikasi CSS dapat terjadi, Kinerja kode yang ditulis menurun karena pemrosesan CSS yang berbeda untuk tiap file HTML.

External CSS
External CSS merupakan penggunaan CSS dimana kode CSS dituliskan di pada file terpisah (bertipe .css) yang biasanya dibedakan untuk setiap file HTML dan disimpan pada sebuah folder CSS.
Kelebihan External CSS adalah kerapian file HTML karena tidak ada tumpukan kode CSS, ukuran file HTML lebih kecil sehingga load aplikasi lebih cepat, dan mendukung penggunaan satu kode CSS untuk banyak file HTML.
Kekurangan External CSS adalah kinerja aplikasi berdasarkan pada internet, dengan internet yang lambat, tampilan aplikasi dapat menjadi kacau karena pemanggilan CSS oleh file HTML terhambat atau mungkin gagal.


Tag HTML5 yang sering saya pakai:
<b> untuk memberikan efek bold pada text
<body> untuk menunjukan body file/dokumen/kode
<button> untuk membuat button/tombol
<col> untuk membuat kolom pada tabel
<div> untuk menunjukan divisi atau bagian code pada file
<form> untuk mendefinisikan form HTML yang menerima user input
<head> untuk menunjukan head dari dokumen biasanya berisi link atau informasi krusial lain
<header> untuk menunjukan header dokumen
<h1> sampai <h6> untuk membuat HTML heading sesuai ukuran
<html> untuk menunjukan root file HTML
<i> untuk memberikan efek italic text
<link> untuk mendefinisikan hubungan elemen HTML dengan resources internal maupun eksternal
<span> untuk membuat dokumen tanpa style
<strong>untuk memberikan efek penekanan atau mirip bold
<table> untuk mendefiniskan tabel di file HTML
<th> untuk mendefinisikan header cell di tabel
<tr> untuk mendifinisikan row pada tabel
<u> untuk memberikan efek underline bagi text
<var> untuk mendefinisikan sebuah variabel
<mark> untuk menandai suatu elemen

Selector CSS yang sering saya gunakan:
.class = mengambil seluruh elemen yang memiliki class tersebut
.classA.classB = mengambil elemen dengan nama kedua class tersebut pada atribut classnya.
#id = Mengambil elemen dengan id tertentu(yang disebutkan)
* = mengambil seluruh elemen
:hover = mengambil elemen yang di hover
:root = mengambil root elemen dokumen
:active = mengambil link yang aktif
:lang(bahasa) = mengambil elemen dengan bahasa yang sama

Saya mengimplementasikan seluruh checklist tugas yang ada dengan metode yang serupa. Pertama, saya melakukan load dan link ke CSS dan penambahan script ke ajax dan bootstrap. Setelah itu, saya melakukan styling.

Pada todolist.html, saya melakukan align text di awal ke tengah dan saya membuat row yang akan berisi kolom-kolom card. Saya membuata card dalam setiap forloop agar setiap task memiliki card masing-masing. Lalu, saya membuat dua button memanjang dan full di bawah. Seluruh elemen tersebut saya warnai dengan sejalan agar tidak bertabrakan untuk dilihat mata.

Pada form.html, saya melakukan align text di awal ke tengah. Lalu, saya membuat tabel dengan justify di tengah dan kolomnya berukuran secara otomatis. pada tabel tersebut, saya membuat label judul dan deskripsi diikuti field inputnya. Lalu, saya akhiri dengan membuat button dan mewarnai seluruh elemen.

Pada login.html, Saya mewarnai text pembuka dan melakukan align ke tengah. Lalu, saya membuat tabel yang di-align ke tengah dan berisikan 2 label (nama dan username) dan 2 field untuk nama dan username. Lalu, saya membuat button unutk submitrequest. Setelah itu, saya memberikan tulisan diikuti dengan kata "Buat Akun" yang mengarah ke link register user. Terakhir, saya mewarnai semua elemen yang ada.

Pada register.html, tidak banyak yang dapat saya lakukan karena HTML ini memanfaatkan UserCreationForm yang sudah merupakan template. Oleh karena itu, saya hanya melakukan align text pembuka ke tengah, dan membuat button di bagian paling bawah. Terakhir, saya mewarnai elemen tersebut dengan warna yang selaras.