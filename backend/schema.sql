create extension if not exists pgcrypto;

create table if not exists projects (
  id uuid primary key default gen_random_uuid(),
  title text not null check (char_length(title) <= 140),
  category text not null check (char_length(category) <= 80),
  description text not null check (char_length(description) <= 600),
  image_url text not null check (char_length(image_url) <= 1000),
  technologies jsonb not null default '[]'::jsonb,
  case_study_url text,
  live_url text,
  sort_order integer not null default 0,
  is_featured boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists skills (
  id uuid primary key default gen_random_uuid(),
  name text not null unique check (char_length(name) <= 80),
  logo_url text not null check (char_length(logo_url) <= 1000),
  sort_order integer not null default 0,
  is_active boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists contact_messages (
  id uuid primary key default gen_random_uuid(),
  name text not null check (char_length(name) <= 140),
  email text not null check (char_length(email) <= 254),
  message text not null check (char_length(message) <= 2000),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_projects_sort_order on projects (sort_order asc, created_at desc);
create index if not exists idx_skills_sort_order on skills (sort_order asc, created_at desc);
create index if not exists idx_contact_messages_created_at on contact_messages (created_at desc);

create or replace function set_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists projects_set_updated_at on projects;
create trigger projects_set_updated_at
before update on projects
for each row execute function set_updated_at();

drop trigger if exists skills_set_updated_at on skills;
create trigger skills_set_updated_at
before update on skills
for each row execute function set_updated_at();

drop trigger if exists contact_messages_set_updated_at on contact_messages;
create trigger contact_messages_set_updated_at
before update on contact_messages
for each row execute function set_updated_at();
