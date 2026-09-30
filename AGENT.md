# AGENT.md — Blogger/Blogspot SEO + PageSpeed Playbook

Skill & rule hasil riset. Dipakai saat optimizes `citzeyeblogspot.xml` (Blogger theme XML).

---

## 0. VALIDASI TEMPLATE (WAJIB tiap upload)

Blogger menolak upload kalau XML tidak valid atau setting widget ngawur. Cek lokal dulu sebelum upload — jangan sampai ditolak.

```bash
python3 - <<'PY'
import xml.dom.minidom
s=open('citzeyeblogspot.xml',encoding='utf-8').read()
xml.dom.minidom.parseString(s.replace('<HTML ','<HTML xmlns:b="urn:blogger" xmlns:data="urn:data" xmlns:expr="urn:expr" ',1))
print("XML OK")
PY
```

**RULE**
- Blogger memvalidasi **nama** setting **DAN nilainya**. Nama salah → upload ditolak, satu error per upload. Values salah juga bisa ditolak.
- **Sumber kebenaran = XML widget default Blogger sendiri**, bukan dokumentasi atau tebakan.
  Dokumentasi resmi Google ("Layouts Data Tags" & "Widget Tags for Layouts", support.google.com/blogger/answer/47270 & /46995) **tidak mendokumentasikan daftar setting widget sama sekali** — jangan andalkan itu.
- Contoh ground truth `PopularPosts` (dari XML default Blogger, repo `MoribundInstitute/mor-blogger-widget-blueprints`):
  ```xml
  <b:widget id='PopularPosts1' locked='false' title='Popular Posts' type='PopularPosts'>
    <b:widget-settings>
      <b:widget-setting name='numItemsToShow'>10</b:widget-setting>
      <b:widget-setting name='showThumbnails'>true</b:widget-setting>
      <b:widget-setting name='showSnippets'>true</b:widget-setting>
      <b:widget-setting name='timeRange'>LAST_YEAR</b:widget-setting>
    </b:widget-settings>
  ```
  → hanya **4 setting**, dan `timeRange` memakai **enum** (`LAST_DAY` / `LAST_WEEK` / `LAST_MONTH` / `LAST_YEAR` / `ALL_TIME`), **bukan** teks bebas seperti `"All time"`.

- **Daftar setting yang sudah diverifikasi:**

  | type | setting yang valid |
  |---|---|
  | `Blog` | `authorLabel`, `backlinksLabel`, `commentLabel`, `disableGooglePlusShare`, `postLabelsLabel`, `postsPerAd`, `reactionsLabel`, `showAuthor`, `showAuthorProfile`, `showBacklinks`, `showCommentLink`, `showDateHeader`, `showInlineAds`, `showLabels`, `showLocation`, `showReactions`, `showShareButtons`, `showTimestamp`, `timestampLabel`, `style.*` |
  | `HTML` | `content` |
  | `Label` | `display`, `selectedLabelsList`, `showFreqNumbers`, `showType`, `sorting` |
  | `PopularPosts` | `numItemsToShow`, `showThumbnails`, `showSnippets`, `timeRange` **only** |
  | `Navbar` | (tanpa setting) |
  | `AdSense` | `style.*` |

  ⚠️ **Dilarang** di `PopularPosts`: `showStyle`, `showNumComments`, `showFeaturedPost`, `dateFormat`. Sudah kena berulang kali.
- **Cara paling aman & anti-guessing:** kalau butuh setting dengan nilai enum yang tidak pasti, **biarkan Blogger yang menuliskannya** lewat UI **Layout → edit widget** di dashboard, lalu copy hasilnya ke template. Jangan menebak enum.
- Validasi lokal **wajib** sebelum upload (cek nama + nilai), jalankan tiap selesai edit widget.
- `b:section` dan `b:widget` id harus unik.
- Setiap widget wajib punya `<b:includable id='main'>`.
- Semua `b:include name='...'` harus menunjuk includable yang benar-benar ada di file.
- `&` di href/src harus `&amp;`.
- Hapus dead code: `data:blog.postImageUrl`, `data:post.hasJumpLink`/`jumpText` (jumpbreak dihapus), `data:top.showPlusOne` + `googlePlusBootstrap` (Google+ mati 2019), `data:post.addCommentOnclick`, `data:post.sharePostUrl`.

---

## 1. STRUKTUR KONTEN (ON-PAGE SEO)

- **H1 = judul artikel saja.** H2–H6 untuk sub-heading. H1 dobel = sinyal degradasi, dan H1 = heading utama untuk snippet.
- Judul artikel harus `h1`/entry-title yang berisi keyword utama.
- **URL ringkas**: hanya keyword inti, tanpa stop-word ("and", "the", "yang", "dan").
- **Meta description**: ≤ 160 karakter, keyword + CTA, unik per artikel.
- **Title tag**: ~60 karakter, therapeutic, ada keyword.
- Sub-heading pakai H2 ke bawah, sertakan keyword di sebagian heading.
- Satu **kategori** per artikel (maks 1 label utama). Tambahkan beberapa tag spesifik.
- **Link internal**: artikel → artikel related. Artikel baru → artikel lama. Kurangi bounce rate.
- Internal link dengan `rel` benar, external `target='_blank' rel='noopener'`.
- Sitemap Blogger sudah otomatis; tetap submit ke Google Search Console.

---

## 2. GAMBAR (SEO + SPEED)

- `alt` deskriptif di SETIAP `<img>`. Google bot pakai alt untuk klasifikasi.
- **Compress sebelum upload** (Squoosh/TinyPNG, quality ~70). Gambar besar = LCP lambat.
- Format WebP/AVIF lebih baik; sertakan dimensi eksplisit.
- `loading='lazy'` untuk gambar di bawah fold, `fetchpriority='high'` untuk gambar LCP.
- Thumbnail widget: paksa HD (ganti `/s72-c/` → `/s0-c/`).
- Featured image = elemen LCP; pilih yang besar & relevan, bukan gambar kecil.

---

## 3. CORE WEB VITALS (TARGET)

Ambang Google (field data, mobile):
- **LCP** ≤ 2.5 s — kecepatan muat konten utama
- **INP** ≤ 200 ms — respons interaksi (ganti FID lama; INP mulai 2024)
- **CLS** ≤ 0.1 — kestabilan visual saat load

Diagnosis wajib per metrik: **identifikasi elemen penyebab → cek discovery/preload → cek render-blocking → cek apakah template-wide atau isolated.**

**LCP** — kompres & preconnect gambar, preload LCP image, kurangi TTFB, critical CSS inline, Jangan jadikan gambar besar sebagai LCP kalau bisa teks besar.

**INP** — potong long tasks, kurangi/hyperbolic JS pihak ketiga, `defer`/`async` script non-kritis, audit script pihak ketiga dulu sebelum kerja engineering.

**CLS** — WAJIB `width`/`height` atau `aspect-ratio` di setiap gambar/embed/iframe. reserves space untuk slot iklan & banner. `font-display: swap` supaya tidak ada FOIT. Jangan sisipkan konten dinamis di atas fold.

---

## 4. FON & RENDER-BLOCKING

- `font-display: swap` di link Google Fonts.
- `<link rel='preconnect'>` ke domain font & CDN.
- preload `as='font' type='font/woff2' crossorigin` untuk font kritikal.
- **Critical CSS** inline di `<head>`, non-kritis async. CSS besar = render-blocking.
- Gabung/minify stylesheet. Hapus CSS tak terpakai.
- **WAJIB sisipkan space untuk iklan** — container iklan dikasih tinggi minimum, else reel CLS saat Ads muat.

---

## 5. JAVASCRIPT & SCRIPT PIHAK KETIGA

- Minify + `defer`/`async` untuk JS non-kritis.
- Hapus JS tak terpakai (audit via DevTools → Network filter by domain).
- Script pihak ketiga (iklan, analytics, addthis) = pembunuh INP/LCP. Lazy-load setelah scroll/defer.
- Hapus widget & library berat yang tidak dipakai (mis. addthis bila tidak dipakai).

---

## 6. IKLAN (ADSENSE) & CLS

- Config: `enable_page_level_ads`, lazy-load adsbygoogle via IntersectionObserver/scroll (bukan blocking di head).
- Batasi **2 slot**: 1 sidebar, 1 dalam artikel. Setiap slot wajib punya dimensi/min-height → anti CLS.
- Density iklan rendah = lebih baik UX & Core Web Vitals.

---

## 7. PENGATURAN BLOGGER (DASHBOARD)

- Blog **public** & visible ke search engine.
- Deskripsi blog + judul jelas.
- **Custom robots.txt ON**. Archive, Search, dan halaman low-value diberi `noindex`.
- **Meta description** per artikel ON (tampil di snippet).
- **Comment form = Popup** (embedded memperlambat halaman).
- **Site feed = Short** (cegah content di-curry).
- Alt text untuk gambar = wajib saat upload.
- Hapus halaman yang tidak perlu diindeks (Archive, Search).

---

## 8. INTERNAL LINKING & STRUKTUR SITUS

- Tambah **related posts** di akhir artikel (widget Related Posts native Blogger) → turunkan bounce.
- Clustering: artikel dalam satu topik saling link, bangun topical authority.
- Sitemap ke Search Console.
- Pantau URL 404, perbaiki link rusak.

---

## 9. KONTEN (PRIORITAS #1)

- Riset keyword dulu sebelum menulis judul.
- Struktur konten: pendahuluan → H2/H3 → detail → kesimpulan.
- Keyword di: title tag, H1, 100 kata pertama, heading, meta description, URL, alt gambar. **Hindari** keyword stuffing.
- Konten lengkap & menjawab intent, bukan padding.
- Perbarui artikel lama (stale screenshot, fakta usang) — sinyal kesegaran.
- Plain language, mudah dibaca, short paragraph.

---

## 10. CHECKLIST PASCA-UPLOAD

1. Upload XML → valid? (kalau "not valid", cek §0).
2. Refresh paksa (Ctrl+Shift+R) + Incognito.
3. PageSpeed Insights (mobile & desktop) → LCP/INP/CLS.
4. Search Console → Inspection per URL utama → rich result & index.
5. Rich Snippet test → Article, BreadcrumbList.
6.robots.txt & sitemap OK.
7. Tidak ada layout shift saat halaman load.

---

## 11. RESPONSIVE (BLOGGER-SPECIFIC)

### 11.1 WAJIB: flag `b:responsive='true'`
Template responsive Blogger **wajib** punya flag ini di tag `<html>`:

```xml
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' b:templateVersion='1.0.0' ...>
```

**Tanpa `b:responsive='true'`, Blogger menganggap template ini legacy** → dia akan menyajikan template mobile lawas (includable `mobile-main`, `mobile-post`, `mobile-index-post`, `mobile-nextprev`) ke HP, dan seluruh `@media` query di stylesheet utama **tidak pernah dipakai** di mobile.

> Jebakan: `class='ltr no-js rwd index'` itu cuma string CSS, **tidak fungsional**. Yang menentukan adalah `b:responsive='true'`.

**CHECKLIST**
- `b:responsive='true'` ada di tag `<html>`.
- `b:css='false'` → matikan CSS default Blogger, pakai CSS sendiri sepenuhnya.
- Dashboard: Theme → ⚙ → Mobile → **"Choose mobile theme: Custom"** → Save. Tanpa ini, perubahan tema tidak ikut ke mobile.
- Verifikasi: buka blog di HP, cek `View Source` — kalau masih ada markup `mobile-index-*`, Blogger masih pakai template mobile lawas.
- Alternatif cepat: `?m=1` di akhir URL untuk paksa versi mobile; `?m=0` untuk desktop.

### 11.2 CSS responsive
- `<meta content='width=device-width, initial-scale=1' name='viewport'/>` — **wajib**, satu saja (jangan dobel).
- **Mobile-first**: tulis style untuk layar kecil dulu, baru tambah `@media (min-width: …)`.
- Hindari `user-scalable=no, maximum-scale=1` — merusak aksesibilitas & bisa kena penalti.
- Breakpoint lazim: `480px`, `768px`, `992px`, `1200px`.
- Unit: pakai `rem`/`%`/`max-width`, hindari pixel absolut untuk container.
- Grid wajib pakai `float` + `calc()` (Blogger masih men-support cara lama) ATAU `flex`/`grid` modern.
- Target sentuh ≥ 44×44 px (Google: "clickable elements too close together").
- Maks lebar teks artikel 65–75 karakter per baris (`max-width: 70ch`) untuk keterbacaan.
- Overflow: cek `overflow-x` — horizontal scroll = sinyal mobile-unfriendly.
- Test di 320px, 375px, 414px, 768px, 1280px.

### 11.3 Data tag modern (Layouts v3)
Lebih baik dari `data:blog.pageType`:
- `data:view.isHomepage`, `data:view.isPost`, `data:view.isSearch`, `data:view.isArchive`, `data:view.isError`
- `data:view.title.escaped`, `data:blog.blogspotFaviconUrl`
- Legacy (`data:blog.pageType != "item"`) masih jalan, tapi `data:view.*` lebih bersih & cepat.

---

## 12. ARTIKEL LONGLASTING (EVERGREEN)

Blog teknologi cepat basi. Aturan di bawah supaya artikel lama **tetap terbaca dan masih bernilai 2–5 tahun** setelah ditulis.

### 13.1 Pilih topik yang tidak cepat basi
- **Pakai**: how-to, tutorial, troubleshooting, penjelasan konsep, panduan beli yang bersifat umum, referensi spec.
- **Hindari**: berita rilis, "terbaru 2026", event, harga sesaat.
- Kalau memang berita: tetap tulis dengan tanggal jelas + konteks, dan tandai sebagai kandidat review.

### 13.2 JANGAN kunci waktu di judul & URL
- ❌ Judul `10 Laptop SSD 2026`, URL `/best-ssd-2026`
- ✅ Judul `How to Choose an SSD for Your Laptop`, URL `/how-to-choose-ssd`
- Tahun di URL/title = artikel mati di mata Google setelah 12 bulan dan tidak pernah direfresh di SERP.

### 13.3 Tulis fundamental, bukan gejala
- Jelaskan **mengapa** + prinsipnya, bukan hanya langkah-langkahnya.
- Prinsip (arsitektur, protokol, cara kerja) bertahan bertahun-tahun; nama model hanya bertahan satu tahun.

### 13.4 Version-agnostic, atau nyatakan versinya
- Kalau memang harus menyebut versi: `Chrome 120+` (bukan "versi terbaru").
- Tambah baris `Tested on Chrome 120, March 2026` — jadi kredibel **dan** punya titik jelas kapan harus di-review.
- Hindari kata "sekarang", "saat ini", "terbaru" tanpa acuan waktu.

### 13.5 Harga & angka: beri rentang + tanggal
- ❌ `Harga SSD 1TB cuma $60`
- ✅ `Around $60 (checked March 2026) — prices change often, check current listings`
- Angka hardware cepat berubah; **caranya**, bukan angkanya, yang bikin artikel tidak basi.

### 13.6 Screenshot bukan longa-lasting
- Tampilan UI rusak tiap update. Utamakan instruksi **berbasis teks**: `Settings > About`.
- Kalau perlu gambar, tetap tulis langkahnya dalam teks — jangan andalkan gambar saja.
- `alt` deskriptif di setiap gambar.

### 13.7 Link ke sumber yang stabil
- Dokumentasi resmi > artikel pihak ketiga.
- Hindari embed pihak ketiga (bisa mati / berubah kebijakan).
- Tulis nama menu secara literal supaya tetap bisa dicari walau URL-nya mati.

### 13.8 Scaffolding untuk keterbacaan jangka panjang
- Heading hierarkis (H1 → H2 → H3), **tidak melompat level**.
- Tambah daftar isi / anchor untuk artikel panjang.
- TL;DR di awal, tabel spesifikasi, paragraf pendek.
- **Satu artikel = satu topik.** Jangan gabung 5 topik dalam satu halaman.

### 13.9 Link internal = strategi terbaik
- Setiap artikel lama harus punya minimal 1–2 link internal ke artikel yang masih hidup.
- Artikel baru **link ke artikel lama** → menghidupkan kembali traffic-nya.
- Momentum: artikel lama dapat klik +FRESHNESS signal tanpa harus menulis baru.

### 13.10 Maintenance berkala
- Tandai artikel traffic tinggi untuk review tiap 6–12 bulan.
- Review = cek tahun/angka/screenshot, tambah `Last updated: <tanggal>`.
- Artikel yang benar-benar usang: **update atau gabungkan** — jangan dibiarkan diam-diam.
- Jangan menghapus artikel yang masih ter-index (mengganggu link & ranking-nya).

### 13.11 Anti-pattern konten
- ❌ Tahun di URL/judul
- ❌ "Terbaik 2026" tanpa qualify
- ❌ Harga absolut tanpa tanggal
- ❌ Instruksi yang hanya ada di screenshot
- ❌ Bergantung pada tool/embed pihak ketiga
- ❌ Banyak topik digabung dalam satu artikel
- ❌ Copy-paste tanpa verifikasi — artikel hardware yang salah lebih berbahaya daripada tidak ada.

## 13. ANTI-PATTERN (JANGAN)

- ❌ H1 lebih dari satu per halaman.
- ❌ Gambar tanpa `alt` / tanpa dimensi.
- ❌ Script pihak ketiga blocking di `<head>`.
- ❌ CSS besar tanpa critical-CSS inline.
- ❌ Slot iklan tanpa reserved space (bunuh CLS).
- ❌ `<head>`/`</head>` ter-escape (`&lt;head&gt;`) → head kosong & teks mengotak (BUG, bukan trik).
- ❌ Mematikan kode data-tag yang sudah dihapus Blogger.
- ❌ `b:widget-setting` yang tidak valid.
- ❌ Mengganti layout/tampilan hanya warna — selalu ada perubahan struktural yang terlihat.
