# Portofolio New

Portofolio New adalah website portofolio pribadi untuk menampilkan profil, pengalaman, skill, project, journey, dan informasi kontak dalam satu halaman yang rapi. Project ini dibuat sebagai showcase digital agar karya dan kemampuan teknis bisa dilihat dengan mudah melalui web publik.

Website ini memiliki tampilan frontend modern berbasis Vue, data default untuk konten portofolio, serta backend FastAPI opsional untuk kebutuhan pengelolaan konten dan endpoint admin.

## Fitur

- Landing page portofolio dengan section hero, about, skills, projects, journey, dan contact.
- Tampilan responsive untuk desktop dan mobile.
- Data default untuk project dan skill sehingga website tetap bisa berjalan tanpa backend.
- Admin view untuk pengelolaan konten melalui API.
- Backend lokal dengan SQLite untuk development.
- Dukungan konfigurasi API melalui environment variable `VITE_API_URL`.

## Tech Stack

### Frontend

- Vue 3 sebagai framework UI.
- Vue Router untuk routing halaman.
- Vite sebagai development server dan build tool.
- Tailwind CSS untuk styling utility-first.
- Lucide Vue untuk icon.
- JavaScript, HTML, dan CSS sebagai bahasa utama frontend.

### Backend

- FastAPI sebagai framework API.
- SQLAlchemy untuk ORM dan akses database.
- SQLite untuk database lokal development.
- Pydantic untuk validasi schema request dan response.
- Uvicorn sebagai ASGI server.

### Tooling

- npm untuk package management frontend.
- Python virtual environment untuk dependency backend.
- Git dan GitHub untuk version control.
- Vercel sebagai target deployment frontend.

## Struktur Project

```text
.
├── backend/              # FastAPI backend, schema, seed, dan konfigurasi database
├── public/               # Asset publik
├── src/                  # Source code frontend Vue
│   ├── components/       # Komponen layout, section, dan UI
│   ├── data/             # Data default portofolio
│   ├── router/           # Konfigurasi route
│   ├── services/         # Service API frontend
│   └── views/            # Halaman utama dan admin
├── index.html
├── package.json
└── vite.config.js
```

## Menjalankan Frontend

Install dependency:

```bash
npm install
```

Jalankan development server:

```bash
npm run dev
```

Build production:

```bash
npm run build
```

## Menjalankan Backend

Dokumentasi backend lebih lengkap tersedia di `backend/README.md`.

Ringkasnya:

```bash
cp backend/.env.example backend/.env
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Jika frontend ingin membaca backend lokal:

```bash
VITE_API_URL=http://127.0.0.1:8000 npm run dev
```

## Deployment

Project frontend dapat dideploy ke Vercel dengan konfigurasi Vite standar:

- Build command: `npm run build`
- Output directory: `dist`
- Install command: `npm install`

## Repository

Repository GitHub:

```text
https://github.com/KUNE23/Portofolio-New
```
