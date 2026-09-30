# Taruh 3 foto produk laptop di sini

Folder: `posts/3 Cheap Laptops for School That Hold Up/images/refs/laptop/`

Folder ini tempat lu menyimpan foto produk asli. Setelah 3 file ada di sini,
jalankan satu perintah dan 2 grafik artikel langsung jadi.

```
python3 posts/make-laptop-images.py "3 Cheap Laptops for School That Hold Up"
```

## File yang dibutuhkan

| Laptop | Kata kunci yang harus ada di nama file | Contoh nama |
|---|---|---|
| Acer Chromebook Plus 514 | `acer` atau `chromebook` | `acer-chromebook-plus-514.png` |
| Lenovo IdeaPad Slim 3i | `lenovo`, `ideapad`, atau `slim 3i` | `lenovo-ideapad-slim-3i.jpg` |
| HP OmniBook 3 | `hp` atau `omnibook` | `hp-omnibook-3.webp` |

**Format bebas**: `.jpg`, `.jpeg`, `.png`, `.webp`.
**Nama bebas** selama salah satu kata kunci di tabel masih ada di dalamnya.
Jadi `Screenshot 2026-09-30 at 14.22.01.png` tetap jalan asal ada `hp` di
namanya. Kalau nama file-nya sama-sama tidak nyambung ke thrice kata kunci
sekaligus, script akan menugaskan sisa file secara berurutan.

## Cara dapat fotonya

1. Buka halaman produknya di browser biasa (bukan lewat script):
   - Acer Chromebook Plus 514 — cari model **CB514-3H** di store.acer.com atau acer.com/us-en
   - Lenovo IdeaPad Slim 3i — cari model **Core i3-N305 / 8GB / 128GB** di lenovo.com/us
   - HP OmniBook 3 — cari **Ryzen 3 / 8GB / 512GB / 17.3"** di hp.com/us-en/shop
2. Klik kanan foto produk utama → **Save image as**
3. Simpan ke folder ini

Pilih foto **frontal, laptop menghadap samping atau sedikit miring** — bukan
foto close-up detail dan bukan gambar logo. Foto produk dengan background putih
kelihatan paling bersih, tapi tidak wajib; script akan otomatis memotong
whitespace dan menempelkannya di atas background putih.

### WAJIB: cek produknya sebelum disimpan

Ini pernah salah dan bisa fatal. File `hp-omnibook-3.png` berisi foto
**HP Omen** — laptop gaming — bukan HP OmniBook 3. Nama file-nyaNIH benar,
isi fotonya produk berbeda. Memasang foto itu ke rekomendasi OmniBook 3 akan
menjadi kesalahan fakta, dan pembaca akan mengira mereka melihat unit yang
dibeli.

Jadi sebelum menyimpan, zoom foto dan cari logo di bodi:

| Laptop | Yang harus tertulis di机身机身 | Foto yang salah |
|---|---|---|
| Acer Chromebook Plus 514 | "acer" di bezel bawah layar,桌面 app drawer ChromeOS | Laptop generic tanpa logo |
| Lenovo IdeaPad Slim 3i | "Lenovo" di tepi bodi depan / engsel | Laptop HP/Acer/Dell |
| HP OmniBook 3 | "HP" atau "OmniBook" di-results lid atau deck | **HP Omen** (logo "OMEN" di deck) |

Kalau ragu, jangan simpan. Tanya dulu.

## Kenapa tidak diambil otomatis oleh script

Situs pabrikan dan retailer memblokir scraping dari environment ini:

- `hp.com`, `lenovo.com`, `acer.com` — SPA, HTML-nya cuma shell, foto produk
  dimuat lewat JavaScript
- `static.acer.com` — HTTP 503
- Walmart, Newegg, B&H, Adorama — HTTP 403 (bot block)
- Endpoint image search — diblokir

Yang **bisa** diakses cuma sebagian kecil CDN, dan hanya berisi gambar
promosi atau navigational — bukan foto produk.

Wikimedia Commons memang punya gambar HP OmniBook, tapi itu model **300** dan
**X** — bukan OmniBook 3. Memasang foto model lain di rekomendasi produk itu
kesalahan fakta, jadi script-nya menolak menukar sendiri.Script lebih baik gagal
dengan pesan jelas daripada menghasilkan gambar produk yang salah.

## Output

Setelah dijalankan, script membuat:

- `images/04-laptops-featured.webp` (1080 × 1722) — upload **lebih dulu**,
  karena gambar pertama di artikel menentukan thumbnail post
- `images/05-laptops-price.webp` (1080 × 1268)

Ukuran dan `width`/`height` di HTML artikel sudah disesuaikan dengan kedua
file ini.

## Kalau ada yang salah

Script mencetak daftar file yang kurang beserta kata kunci yang dibutuhkan,
lalu berhenti tanpa menghasilkan file apa pun. Jadi kalau gagal, tidak ada
grafik setengah jadi yang tertinggal.
