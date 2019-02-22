# Codingame-URO
Tugas programming sekuro 2019 (cakru 11).

### Anggota Kelompok:<br/>
16318111 - Kania Fatimah Saffanah <br/>
16518237 - Figo Agil Alunjati <br/>
16518259 - Muhamad Hudan Widzamil <br/>
16618228 - Brandon Louis Gunawan <br/>


### Strategi dalam memainkan game "Platinum Rift - Episode 2"
Strateginya adalah dengan mencari tempat berpindah bagi pod yaitu menggunakan `move` dan memilihnya menggunakan `random`.


Pertama kami mencari lokasi dari base pemain `p0base`dan base musuh `p1base`. Kemudian berdasarkan lokasi dari base pemain, dicari lokasi kosong untuk POD berpindah. Cara pindah didefinisikan sebagai `move` dan dengan melihat pada data yang ada terkumpulah kemungkinan tempat untuk berpindah yang kemudian dipilih secara acak oleh fungsi `random`. Kemudian hasil tersebut dimasukkan kedalam variabel `availablemove`. Dari jumlah POD di suatu tempat, Id dari tempat itu, dan hasil pilih `availablemove` dilakukan perpindahkan dengan cara mencetak ketiga hal diatas secara berurut.
