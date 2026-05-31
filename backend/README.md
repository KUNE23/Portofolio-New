# Portfolio Backend

Backend ini memakai FastAPI. Default sekarang memakai SQLite lokal supaya bisa dipakai tanpa Supabase dulu.

## Setup

1. Copy env:

```bash
cp backend/.env.example backend/.env
```

2. Isi `ADMIN_TOKEN`. Untuk lokal sekarang tokennya:

```env
ADMIN_TOKEN=PianPian1
```

Untuk lokal, `DATABASE_URL` biarkan:

```env
DATABASE_URL=sqlite+aiosqlite:///./portfolio.db
```

3. Install dan jalankan:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
set -a
source .env
set +a
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

File database lokal akan otomatis dibuat di `backend/portfolio.db` saat backend pertama kali jalan.

Untuk mengisi data awal ke database lokal:

```bash
cd backend
source .venv/bin/activate
python seed_local.py
```

## Pindah ke Supabase Nanti

Kalau nanti ingin kembali memakai Supabase PostgreSQL:

1. Ganti `DATABASE_URL` di `backend/.env` ke connection string Supabase.
2. Jalankan `backend/schema.sql` di Supabase SQL Editor.
3. Opsional jalankan `backend/seed.sql` untuk data awal.

Frontend membaca API dari `VITE_API_URL`. Jika backend jalan lokal:

```bash
VITE_API_URL=http://127.0.0.1:8000 npm run dev
```

## Security

- CORS dibatasi oleh `ALLOWED_ORIGINS`.
- Admin endpoint wajib header `X-Admin-Token`.
- Rate limit per IP dan path.
- Validasi input menggunakan Pydantic.
- Database memakai SQLAlchemy ORM dengan parameter binding, bukan string SQL mentah.
- Security headers dasar aktif di semua response.
