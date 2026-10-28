"""Indonesian."""
from . import blocks

MONTHS = ("Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September",
          "Oktober", "November", "Desember")


def date(day, month, year):
    return f"{day} {MONTHS[month - 1]} {year}"


WORDS = {
    "windows": "Unduh Panorun {version} untuk Windows",
    "android": "Unduh Panorun {version} untuk Android",
    "small": "mengunduh Panorun sambil memasangnya",
    "full": 'Atau <a href="{url}">penginstal lengkap</a> ({size}), berisi semuanya: memasang tanpa koneksi.',
    "locale": "id-ID",
}

BLOCKS = blocks([
    "Panorun - seluruh level terlihat | TIE-Games",
    "Seluruh level terlihat, teman-teman berlari di samping Anda.",
    "Panorun adalah emulator untuk game konsol 8-bit klasik yang menjaga seluruh level tetap terlihat: semua yang sudah Anda lewati tetap ada di layar di sekitar game. Main bersama secara online, dan teman-teman Anda berlari di samping Anda di dalam game Anda sendiri. Panorun dibuat oleh TIE-Games, studio independen di Dresden, Jerman.",
    'Punya ponsel Android? <a href="#test">Bantu uji Panorun di Google Play</a>.',
    "Unduh",
    "WINDOWS 10 DAN 11, 64-BIT",
    "Penginstal menanyakan lokasi pemasangan dan apakah perlu pintasan di desktop. Tidak perlu hak administrator.",
    "Penginstal belum ditandatangani kodenya: jika Windows menampilkan <em>Windows protected your PC</em>, klik <em>More info</em>, lalu <em>Run anyway</em>.",
    "Setelah itu Panorun memperbarui dirinya sendiri: klik <em>Update</em> saat ada versi baru.",
    "Untuk menghapus Panorun: Pengaturan Windows &rarr; Aplikasi &rarr; Aplikasi yang diinstal &rarr; Panorun &rarr; Copot instalan. Game dan rekaman Anda tetap ada di <em>Documents\\Panorun</em>.",
    "ANDROID 7 ATAU LEBIH BARU, 64-BIT",
    "<strong>Buka halaman ini di Chrome dulu.</strong> Halaman ini terbuka di dalam aplikasi lain (Telegram, WhatsApp, Gmail…) yang tidak bisa mengunduh file: di sana tombol di bawah tidak melakukan apa-apa.",
    '<a class="button" id="open-in-chrome" href="https://tie-games.com/panorun/">Buka di Chrome</a>',
    "Jika tidak terjadi apa-apa: ketuk <strong>&#8942;</strong> atau <strong>&#8943;</strong> di atas, lalu <em>Buka di Chrome</em> atau <em>Buka di browser</em>.",
    "<strong>Akses awal: Panorun sedang diuji di Google Play</strong> sebelum dibuka untuk semua orang, dan siapa pun bisa ikut pengujian:",
    'Gabung ke grup <a href="https://groups.google.com/g/panorun-testers">Panorun testers</a> dengan akun Google Anda: <em>Gabung ke grup</em>.',
    'Buka <a href="https://play.google.com/apps/testing/com.tiegames.panorun">pengujian Panorun di Google Play</a> lalu ketuk <em>Menjadi penguji</em>.',
    "Pasang Panorun dengan tombol Google Play di atas.",
    'Simpan selama dua minggu dan mainkan sesekali - <em>COBA DEMO</em>, game milik Anda, ruang bersama orang lain - lalu beri tahu kami apa yang berjalan dan apa yang tidak, di grup atau ke <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>. Google Play membuka Panorun untuk semua orang setelah cukup penguji memainkannya selama dua minggu.',
    "Atau unduh di sini:",
    '<strong>Mengunduh <span id="android-file">Panorun</span>&hellip;</strong> Tunggu sebentar.',
    "Setelah selesai, ketuk <em>Buka</em> pada pesan di bagian bawah Chrome.",
    "Tidak ada <em>Buka</em>, atau pesannya hilang? Ketuk <strong>&#8942;</strong> di kanan atas Chrome, lalu <em>Download</em>, dan ketuk file-nya. Atau buka aplikasi <em>Files</em> (di ponsel Xiaomi <em>File Manager</em>), lalu <em>Download</em>, dan ketuk file-nya.",
    "Ketuk <em>Instal</em>.",
    "Buka halaman ini di browser ponsel Anda (Chrome - bukan di dalam aplikasi lain) dan ketuk tombolnya. Setelah unduhan selesai, ketuk <em>Buka</em> pada pesan di bawah, lalu <em>Instal</em>. Terlewat? Di Chrome, <strong>&#8942;</strong> &rarr; <em>Download</em> ada file-nya: ketuk di sana.",
    "Pertama kali, Android menanyakan apakah browser Anda boleh memasang aplikasi: izinkan, kembali, lalu ketuk <em>Instal</em> lagi.",
    "Karena diunduh dari sini, Panorun tidak berasal dari Play Store, jadi Google Play Protect mungkin tidak mengenalnya: ketuk <em>Detail lainnya</em>, lalu <em>Tetap instal</em>.",
    "Panorun dari Google Play dan Panorun dari halaman ini tidak bisa dipasang saling menimpa: untuk berganti, copot dulu yang Anda punya - game yang tersimpan di dalamnya ikut terhapus.",
    "Versi baru dipasang dengan cara yang sama, menimpa yang Anda punya: game Anda tetap ada.",
    "Apa yang dilakukannya",
    "<strong>Menjaga level tetap terlihat.</strong> Konsol menggambar satu layar sekaligus dan melupakan sisanya. Panorun menyimpan setiap layar yang digambar dan melukis level di sekitar game di tempat seharusnya, jadi tanah yang sudah Anda lewati tetap di layar di kiri, atas, dan bawah.",
    "<strong>Menggambar peta saat Anda bermain.</strong> Sebuah strip di bawah game menampilkan level sejauh ini, dengan Anda di dalamnya.",
    "<strong>Membuat Anda bisa main bersama.</strong> Buka ruang dan kirim kodenya, atau gabung ke salah satu ruang yang terdaftar di server ruang; siapa pun yang bergabung memainkan salinan game yang sama miliknya sendiri, dan karakter setiap orang berlari di game semua orang lain, masing-masing dengan warnanya, dengan garisnya di peta. Game yang jauh di depan menunggu yang lain, agar semua tetap bersama. Hingga dua belas pemain per ruang.",
    "<strong>Mengobrol sambil bermain.</strong> Di dalam ruang, tahan tombol mikrofon (V di komputer) untuk bicara, atau ketuk agar tetap menyala. Suara game Anda dan kebisingan di sekitar disaring, jadi yang lain mendengar suara Anda, bukan game atau ruangan Anda.",
    "<strong>Server ruang, atau tanpa server.</strong> MAIN ONLINE membuka ruang di server ruang Panorun di web, terdaftar di sana agar teman-teman Anda bisa bergabung. Atau main LOKAL: ruang berjalan di jendela orang yang membukanya, dan teman-teman bergabung langsung. Panorun untuk Windows dilengkapi server ruang yang bisa dijalankan siapa saja.",
    "<strong>Pertarungan sungguhan.</strong> Begitu Panorun tahu di mana game menyimpan nyawa Anda, pemain lain bisa memukul karakter Anda, dan rasanya sakit seperti musuh dalam game: Anda terpental dan nyawa berkurang. Nyawa setiap orang tampil di atas namanya.",
    "<strong>Mempelajari setiap game sendiri.</strong> Saat Anda bermain, Panorun mempelajari rupa karakter Anda dan tombol mana yang melompat atau memukul, dan pemain dalam satu ruang berbagi apa yang diketahui Panorun mereka tentang sebuah game.",
    "<strong>Merekam permainan Anda.</strong> REKAM menyimpan setiap tombol yang Anda tekan, dan PUTAR ULANG memainkan lagi permainan itu dari awal.",
    "<strong>Main dengan yang Anda punya.</strong> Keyboard atau gamepad, setiap tombol bisa Anda atur. Di ponsel, tombol arah di kiri dan A, B, TURBO A, dan TURBO B di kanan.",
    "<strong>Lancar di ponsel.</strong> Prosesor serta chip gambar dan suara konsol berjalan sebagai kode native, jadi Panorun lancar di ponsel, bahkan dengan teman-teman di ruang.",
    "<strong>Tidak ada game yang disertakan.</strong> Panorun memainkan game yang dibuat untuk konsol 8-bit klasik. Pengembang independen masih membuat game baru untuk konsol ini, dan banyak yang membagikannya gratis - cari <em>8-bit homebrew games</em> di web. Atau gunakan salinan game milik Anda. Tambahkan dengan <em>TAMBAH GAME</em>, atau taruh di jendela; Panorun menyimpannya di <em>Documents\\Panorun</em>. Di ponsel, <em>TAMBAH GAME</em> dan <em>PILIH FOLDER</em> membuka pemilih file ponsel Anda. Atau <em>COBA DEMO</em>: game kecil milik Panorun sendiri.",
    "Privasi Anda",
    'Panorun tidak punya akun, analitik, maupun iklan. Game, pengaturan, dan rekaman Anda tetap di komputer atau ponsel Anda. Panorun hanya menghubungi GitHub, untuk mencari versi yang lebih baru (di Windows); server ruang kami dan situs ini, untuk daftar game yang file game-nya sudah kami terbitkan, dan file game dalam daftar saat Anda memulainya; dan, saat Anda main online, server ruang atau komputer yang ruangnya Anda masuki: saat itu ia membagikan nama Anda, karakter Anda, nyawanya, dan level tempat Anda berada kepada pemain di ruang itu, dan server ruang atau komputer ruang melihat alamat internet Anda. Saat Anda menahan atau menyalakan tombol mikrofon di ruang, suara Anda dikirim langsung ke pemain di ruang itu; suara itu tidak direkam dan tidak disimpan di mana pun. Detailnya ada di <a href="/panorun/privacy">Kebijakan Privasi</a> (dalam bahasa Inggris).',
    "Lisensi sumber terbuka",
    'Panorun dibuat dengan perangkat lunak sumber terbuka: antara lain Python, pygame dan SDL, NumPy, serta Opus, RNNoise, dan speexdsp dari Xiph.Org untuk suara. Masing-masing digunakan di bawah lisensinya sendiri. Daftar lengkap, dengan teks setiap lisensi, ada di dalam Panorun (PENGATURAN &rarr; LISENSI), di samping program di Windows, dan di sini: <a href="/panorun/third-party-notices.txt">pemberitahuan pihak ketiga</a>.',
    "Tautan",
    '<a href="/panorun/privacy">Kebijakan Privasi</a>',
    '<a href="/panorun/terms">Ketentuan Penggunaan</a>',
    '<a href="/panorun/third-party-notices.txt">Lisensi sumber terbuka</a>',
    'Kontak: <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>',
    "&copy; 2026 TIE-Games. Hak cipta dilindungi.",
    'Panorun tidak menyertakan game. Judul game adalah merek dagang pemiliknya; Panorun tidak berafiliasi dengan maupun didukung oleh mereka. Yang kami terbitkan tentang sebuah game hanyalah apa yang diketahui Panorun tentangnya - di mana game menyimpan nyawa karakter, tombol mana yang memukul - tidak pernah bagian apa pun dari game itu sendiri. Untuk meminta sesuatu dihapus, tulis ke <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>.',
    "Panorun adalah emulator untuk game konsol 8-bit klasik yang menjaga seluruh level tetap terlihat, dan membuat Anda bisa main online bersama teman-teman yang berlari di samping Anda.",
    "Panorun - seluruh level terlihat",
    "Ikon Panorun",
    "Dapatkan Panorun di Google Play",
    "Dapatkan di",
])
