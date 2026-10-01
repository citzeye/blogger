# posts/ — workflow

Satu folder per post. **Nama folder = judul post persis.**
Tool `.py` di sini dipakai lintas post, jadi tetap di root.

```
posts/
├── <Judul Post>/           ← nama folder = judul post PERSIS
│   ├── index.html          ← SATU-SATUNYA file yang di-paste ke Blogger
│   ├── NOTES.md            ← catatan internal (tidak dipublish)
│   └── images/             ← 1 file gambar untuk post ini
├── _legacy/                ← file jaman awal, jangan dipakai lagi
└── *.py                    ← tool (validator + generator gambar)
```

## Struktur index.html

Tiga baris info di paling atas, dalam komentar yang **dihapus sebelum paste**.
Tiga baris ini persis sama dengan tiga kolom yang ada di editor Blogger:

```
<!--
TITLE:  3 AI Apps That Make Your Work Easier
TAGS:   AI
DESC:   Satu kalimat, 70-160 karakter, untuk kolom Search Description.
Paste the body below into Blogger's HTML view, then copy TITLE into the Title
field, TAGS into Labels and DESC into Search Description. Delete this comment.
-->
```

| Baris | Ke kolom Blogger mana |
|---|---|
| `TITLE:` | **Title** |
| `TAGS:` | **Labels** |
| `DESC:` | **Search Description** |

Lalu langsung isi artikel. Tidak ada `<h1>` di body. Tidak ada catatan
panjang — semua itu pindah ke `NOTES.md`.

**Tidak ada `SLUG:` lagi.** Blogger membuat permalink sendiri dari kolom Title,
jadi tidak ada yang perlu dideklarasikan. `§12.2` (tanpa tahun) tetap terjaga
karena `TITLE:`-nya sendiri sudah diperiksa validator.

**`KEYWORDS:` pindah ke `NOTES.md`.** Keyword bukan kolom Blogger dan
`<meta name='keywords'>` diabaikan mesin pencari sejak 2009. Yang benar-benar
berpengaruh adalah kata kunci itu **muncul di teks artikel**, dan
`validate-post.py` sekarang memeriksanya:

```
Every keyword appears in the article text
```

Jadi kalau sebuah kata kunci tidak ada di artikel, yang diperbaiki artikelnya —
bukan daftarnya.

## Kenapa gambar harus di-upload ke Blogger, bukan GitHub

Blogger **hanya** membuat thumbnail post dari gambar yang di-host di
`blogger.googleusercontent.com`. Kalau `src` menunjuk ke GitHub atau host lain,
`data:post.thumbnailUrl` **kosong** — card homepage tampil tanpa gambar, dan
`og:image` / `twitter:image` ikut hilang.

Jadi upload manual ke media Blogger. Catatan lengkap ada di `NOTES.md` tiap post.

## Bikin post baru

1. **Buat folder** dengan nama = title persis:
   ```bash
   mkdir -p "posts/<Judul Post>/images/refs"
   ```
2. **`index.html`** — simpan body artikel di sana. Yang wajib:
   - **Tanpa `<h1>`.** Judul Goes ke kolom *Title* Blogger; Blogger yang
     merender satu-satunya H1 dari situ.
   - Tanpa tahun di title maupun slug.
   - Tanpa wrapper `<div>`, tanpa `<a>` melingkupi `<img>`, tanpa `style=`,
     tanpa `border=` — itu yang ditulis ulang Blogger kalau sisip lewat dialog.
   - Harga **range** + "checked on <Bulan> <Tahun>".
   - Maksimal **3 picks** per artikel list.
   - Ejaan **US** (`color`, `behavior`, `center`) — bukan UK.
   - Mata uang **USD**, dan produknya harus benar-benar dijual di US **dan** UK.
3. **Simpan blok editor notes** di awal `index.html`, ditutup dengan
   ```html
   -->
   <!-- END EDITOR NOTES -->
   ```
   Isi notes: `TITLE`, `SLUG`, `KEYWORDS`, `META DESCRIPTION`, `LABEL`,
   `PRICE CHECKED ON`, `SOURCES`, `POST FOLDER`, `IMAGES`.
   Isi notes tidak pernah tayang.
4. **Foto produk** → `images/refs/`
5. **Buat komposit:**
   ```bash
   python3 posts/make-laptop-images.py "<Judul Post>"   # schema laptop
   python3 posts/make-real-images.py  "<Judul Post>"   # schema device/HP
   ```
   Script menolak jalan (dan tidak menghasilkan file apa pun) kalau foto
   produk belum ada. Tidak pernah membuat placeholder.
6. **Validasi:**
   ```bash
   python3 posts/validate-post.py "posts/<Judul Post>/index.html"
   python3 posts/slop-check.py  "posts/<Judul Post>/index.html"
   ```
   Target: `ALL RULES PASS` dan `CLEAN no flagged patterns`.

   Dua cek ini beda tugasnya. `validate-post.py` memeriksa struktur: urutan
   heading, target link, dimensi gambar, heading level. `slop-check.py` membaca
   kalimatnya: filler, jargon, dan pola tulisan yang sering muncul di teks
   mesin. Keduanya harus bersih sebelum commit.

## Upload ke Blogger

1. Blogger → **Edit post** → tab **HTML view** (bukan Compose)
2. Ctrl+A, paste isi `index.html`, Publish
3. Kolom **Title** diisi persis dengan `TITLE` dari editor notes
4. Upload komposit **urutan**: gambar pertama lebih dulu, karena yang pertama
   menentukan `data:post.thumbnailUrl`

> Nonaktifkan blocker (Brave Shields) untuk `blogger.com` dulu. Tanpa itu
> upload gambar gagal **tanpa报错**.

## Tool

| File | Guna |
|---|---|
| `validate-post.py` | Cek SEO, evergreen, heading, gambar, link internal |
| `slop-check.py` | Cek prosa: filler, jargon, pola tulisan AI. Pasang `anti-slop` |
| `make-real-images.py` | Komposit device/HP (1080px potret) |
| `make-laptop-images.py` | Komposit laptop (1080px potret) |
| `make-images.py` | Generator lama era grafik abstrak — **deprecated** |
| `build-fixed-post.py` | Bikin body pengganti untuk post yang sudah live |
| `post-body-FIXED.html` | Body pengganti artikel HP (sudah dipakai) |
| `images-paste.html` | Instruksi sisip gambar era lama |
| `phones-data.json` | Data pasar HP IDR era lama |

## Aturan isi yang tidak bisa dinegosiasi

Lihat `.opencode/skills/blogger-posts/SKILL.md` dan `AGENT.md`. Yang paling
sering dilanggar: **judul bukan `<h1>`**, **maksimal 3 picks**, **USD bukan
IDR**, dan **ejaan US**.
