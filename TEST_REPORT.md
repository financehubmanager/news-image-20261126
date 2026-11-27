# TEST REPORT — news-image-20261126 (independent test)

Entry: "Sum up 26 November's world news in one image" — repo
`/home/hatch/workspace/makefun/news-image-20261126/`, tested at commit
`bf3b2ea`. Tester independent: tidak ada yang diperbaiki, hanya temuan.

## Verdict: BERSIH

**0 KRITIS, 0 SEDANG, 4 KECIL.** Entry layak submit apa adanya; keempat
temuan KECIL di bawah adalah polish opsional, bukan penghalang.

## Verifikasi yang dilakukan

### 1. Determinisme + format file (LULUS)
- `main.py` dijalankan 2x dengan `MAKEFUN_OUTPUT_DIR` berbeda
  (`/tmp/t1`, `/tmp/t2`): kedua output byte-identical satu sama lain dan
  dengan `entry.png` di repo — sha256
  `b9bfcdef7812c7eac2d6a15d75ab0b7769f12aaca3ff4cf227cb828c2ace72fc`
  (sama dengan klaim BUILD_REPORT.md).
- PNG walk: signature OK; chunk IHDR, IDAT, IDAT, IDAT, IEND — semua CRC
  OK, berakhir tepat di IEND, tidak ada data trailing.
- Dimensi 1024×1024, RGB, 8-bit; ukuran 132.418 byte (batas 1.048.576).
- `main.py` stdlib-only (`os`, `shutil`), hanya menyalin `entry.png`,
  tanpa network. `render.py` (PIL, build-time only) bukan bagian runtime.
- `.makefun/owner.json` berisi wallet
  `5XrS76uzjrhf9pyMBVQpfL1SpyxX7Dk8vyFUncED2o39`; LICENSE MIT
  (Copyright 2026 Budi Hertanto).

### 2. Visual — ukuran penuh (LULUS)
- Banner tanggal "THURSDAY, 26 NOVEMBER 2026" besar, kontras tinggi,
  tidak mungkin terlewat. 26 Nov 2026 memang hari Kamis — benar.
- 6 panel 2×3, ikon digambar sendiri, rapi. Tidak ada teks bertumpuk,
  terpotong, atau artefak. Perbaikan bug ikon timbangan dari build
  terverifikasi: badge Israel menampilkan timbangan utuh (dua piringan),
  tidak ada segitiga putih liar di panel Ukraine.
- Tidak ada teks acak-acakan (garbled). Semua teks dieja dengan benar.

### 3. Visual — downscale ~300px (LULUS dengan catatan, lihat K-4)
- Banner tanggal tetap jelas terbaca. Keenam headline masih bisa
  dibaca (kecil tapi terbaca). Ringkasan satu baris mengecil sampai
  ~7 px dan footer sumber (~6 px) — masih bisa dibaca dengan
  perhatian penuh, tapi tidak bisa dipindai cepat.

### 4. Fakta — dicek satu per satu ke sumber tepercaya (SEMUA BENAR)
1. **Tarif AS** — Reuters, "Five takeaways from Trump's new tariffs"
   (26 Nov 2026): 14 mitra; China 20% (40% bila gencatan dagang
   berakhir 10 Jan); Vietnam 20% dengan kesepakatan / 35% tanpa;
   India 17%/25%; EU/Jepang/Korsel/Taiwan/Swiss 15%; hearing publik
   25 Jan. Gambar: "China up to 20%; Vietnam 35%; EU 15%. Hearing
   Jan 25." — benar (lihat K-2 untuk kualifikasi Vietnam).
2. **Kebakaran tanker Kairo** — CNN/AP/Al Jazeera: tanker terguling
   dan terbakar di Ring Road, Warraq, Giza, Rabu malam; "at least 31"
   tewas, 21 luka, puluhan mobil hangus; jumlah korban masih
   preliminary. Gambar: "kills 31 … 21 hurt, dozens of cars charred."
   — benar (lihat K-3).
3. **Kyiv** — Reuters via TBS News, 26 Nov 2026: rudal balistik
   menghantam pusat belanja + 2 gedung di distrik Desnianskyi;
   7 luka (2 serius); 113 drone Shahed diluncurkan semalam (76
   bermesin jet). Gambar: "7 wounded in overnight strikes; 113 drones
   launched at Ukraine." — benar penuh, dan satu-satunya cerita yang
   murni peristiwa 26 Nov (serangan semalam 25→26 Nov, dilaporkan
   pagi 26 Nov).
4. **Netanyahu Case 4000** — Reuters/CNN, 25 Nov 2026: hakim
   merekomendasikan jaksa mencabut dakwaan Case 4000 (conviction
   "unlikely"), mempertimbangkan ulang Case 2000, mencari deal di
   Case 1000; rekomendasi BUKAN putusan. Gambar: "Case 4000
   'unlikely' to convict, judges say. Not a ruling yet." — benar dan
   ditulis hati-hati. (Catatan: posisi yang sama pernah disampaikan
   hakim Juni 2023 dan Juni 2026; sidang 25 Nov adalah penegasan
   kembali — tidak mengubah kebenaran gambar.)
5. **Kepulauan Solomon–Australia** — AP/Al Jazeera/The News,
   25–26 Nov 2026: traktat ditandatangani di Canberra 25 Nov
   (Albanese + Wale); Australia "primary security partner"; tidak
   ada pangkalan militer/security asing; A$740m selama 10 tahun
   (A$670m hibah + A$70m pinjaman). Gambar: "Treaty bars foreign
   military bases; A$740m aid over 10 years." — benar penuh.
6. **Parade Macy's** — CNN/USA Today/NY Post, 25 Nov 2026: parade
   ke-100 dipindah dari Kamis 26 Nov ke Sabtu 28 Nov karena
   nor'easter; pertama kali ditunda karena cuaca dalam sejarah
   (ditangguhkan 1942–1944 karena WWII, tidak pernah dijadwal ulang
   karena cuaca). Gambar: "Nor'easter moves the 100th parade to
   Saturday, Nov 28." + headline "a first in 100 years" — benar.
- Tidak ada satu pun peristiwa sebelum 13 Nov 2026 di gambar
  (batas keras juri). Klaim Hormuz yang tak terverifikasi dan banjir
  Bogor dengan angka korban konflik sengaja tidak dipakai — keputusan
  yang tepat.

## Skor per kriteria juri (1–10)

1. **Satu hari berita + menyebut tanggal: 9/10.** Tanggal besar dan
   tak ambigu; 6 peristiwa spesifik hari itu. Minus 1: lima dari
   enam peristiwa diumumkan Rabu 25 Nov waktu setempat (lihat K-1);
   aturan "in any time zone" dan cutoff keras 13 Nov melindungi
   entry ini, tapi juri yang hafal tanggal persis bisa sedikit
   mengurangi nilai.
2. **Seleksi & keluasan: 9/10.** 6 cerita, 5+ wilayah (AS, Mesir,
   Ukraina, Israel, Pasifik) dan 6 bidang (perdagangan, bencana,
   perang, hukum, keamanan, budaya). Minus 1: dua dari enam panel
   adalah AS, dan cerita besar AS lain dari badai yang sama
   (900.000 pelanggan tanpa listrik) tidak mendapat panel sendiri.
3. **Keterbacaan dari gambar saja: 8/10.** Headline + ringkasan
   menceritakan tiap peristiwa tanpa perlu sumber luar. Minus 2:
   pada ~300px ringkasan menjadi kecil (lihat K-4); pembaca cepat
   hanya mendapat tanggal + headline.
4. **Kesetiaan fakta: 9/10.** Semua angka terverifikasi ke
   Reuters/CNN/AP/Al Jazeera; hedging dijaga ("may be dropped",
   "Not a ruling yet"); tanpa hype dan tanpa spekulasi sebagai
   fakta. Minus 1: K-2 dan K-3 (kualifikasi yang hilang).
5. **Craft: 9/10.** Satu komposisi koran yang jelas, ikon bersih,
   tanpa smear/artefak/teks acak; terbaca di ~300px untuk tanggal
   dan headline. Minus 1: teks ringkasan/footer yang kecil di
   skala contact-sheet (K-4).

**Skor keseluruhan: 8,8/10.**

## Temuan

### KECIL

- **K-1 — Lima dari enam cerita diumumkan 25 Nov waktu setempat.**
  Tarif (Washington), kebakaran Kairo (Rabu malam), sidang Netanyahu
  (Yerusalem), traktat Solomon (Canberra), dan penundaan Macy's
  (New York) semuanya diumumkan/dilaporkan pertama kali pada Rabu
  25 Nov waktu setempat; hanya serangan Kyiv yang murni peristiwa
  26 Nov. Mitigasi: aturan bounty menghitung "first reported on
  26 November 2026 in any time zone" — pengumuman Rabu malam AS
  adalah Kamis pagi di Asia-Pasifik, dan artikel Reuters tentang
  tarif bertanggal 26 Nov; keenamnya adalah cerita utama liputan
  26 Nov. Risiko sisa kecil: juri yang hafal tanggal persis bisa
  menilai kriteria 1 sedikit lebih rendah. Lokasi: `render.py`
  (STORIES) + `BUILD_REPORT.md` (bagian Story selection — builder
  mengakui ini secara terbuka). Perbaikan opsional: tidak ada yang
  bisa diubah tanpa mengganti cerita; diterima apa adanya.
- **K-2 — "Vietnam 35%" tanpa kualifikasi.** 35% adalah tarif
  bila negosiasi gagal; dengan kesepakatan tarifnya 20%
  (Reuters). Gambar menulis "China up to 20%; Vietnam 35%; EU 15%"
  — "up to" hanya melekat pada China. Lokasi: `render.py`, STORIES
  butir 1 (summary). Perbaikan opsional (1 menit): "Vietnam up to
  35%".
- **K-3 — "kills 31" tanpa "at least".** Jumlah korban bersifat
  preliminary menurut Kementerian Kesehatan Mesir dan bisa naik;
  semua sumber menulis "at least 31". Lokasi: `render.py`, STORIES
  butir 2 (headline). Perbaikan opsional (1 menit): "kills at
  least 31" — atau biarkan, karena konvensi headline koran memang
  menghilangkan "at least".
- **K-4 — Ringkasan dan footer kecil pada ~300px.** Ringkasan
  24 pt dan footer 20 pt (`render.py`: `f_sum`, `f_foot`) menyusut
  menjadi ~7 px dan ~6 px pada lebar 300 px — masih terbaca
  dengan perhatian penuh, tapi tidak bisa dipindai cepat.
  Pengakuan builder soal ini terkonfirmasi, namun lebih ringan dari
  yang dikhawatirkan: tanggal dan keenam headline tetap terbaca
  jelas. Perbaikan opsional: naikkan ringkasan ke 26–27 pt dan
  footer ke 22 pt, atau persingkat ringkasan supaya tetap 1 baris
  dengan huruf lebih besar.

### SEDANG
- (Tidak ada.)

### KRITIS
- (Tidak ada.)

## Satu kalimat jujur

Entry ini layak submit apa adanya — tanggalnya tidak ambigu, keenam
ceritanya spesifik, akurat, dan lintas wilayah/bidang, dan tidak ada
cacat yang mengancam gate maupun penilaian juri; keempat temuan KECIL
hanya polish yang bisa dikerjakan fixer dalam hitungan menit bila
parent menginginkannya, dan menolaknya pun tidak merugikan.
