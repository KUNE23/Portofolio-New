import json
import sqlite3
from pathlib import Path
from uuid import uuid4


DB_PATH = Path(__file__).with_name("portfolio.db")


skills = [
    ("Vue", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg", 10),
    ("Tailwind", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg", 20),
    ("Node.js", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg", 30),
    ("Laravel", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/laravel/laravel-original.svg", 40),
    ("Express", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg", 50),
    ("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", 60),
    ("PostgreSQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg", 70),
    ("MySQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg", 80),
    ("MongoDB", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg", 90),
    ("Redis", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg", 100),
    ("Figma", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg", 110),
    ("Git", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg", 120),
    ("GitHub", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg", 130),
    ("Postman", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postman/postman-original.svg", 140),
    ("Docker", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg", 150),
    (
        "AWS",
        "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg",
        160,
    ),
]

projects = [
    (
        "Proclub Learning Hub (LMS)",
        "Education Tech",
        "A learning platform designed to organize courses, materials, and student progress.",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuB1bN0wC_39r_PgpkdUa3Xqg8Jd7_1_8fXtWhIIyHAlxZvAtRzp9Z_KddaZNO31eJknhDyxuI2i3-1pmSYh99QH61JP8duiRt54OCnhOe8uPfz09erHBV1q_BnTF7AHSXpB5nVId2XfERPS7bG7zgO8hQDffTOJuOrv3lIh3hSACGXIYE_S3RBQdfD_J586rwG1q0KgwwcKSzPRd8JFFHO4tMbGwaq_j0pfVO3rdkNvcApDlvF_bXJX-PRaeBgt_rYo8x9gRBebZYU",
        ["Vue.js", "Node.js", "Tailwind CSS"],
        10,
    ),
    (
        "Website Portofolio Himpunan",
        "Branding",
        "A digital showcase for the student association to highlight achievements and programs.",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuAUkitKPUqiB4nCXd7cjdqgHv8rJbp7dgk1DJx-uGjazoIyRPik9rJxg7rnzyffmh9k8czXmgVg93TB2SOgntsDLKfMly-BzIniWAlZCyZum-c2Ds8bwO-BnV-tZRiBoyK4dpcQM1p2ryXbwV6PjdwBLfLIKorS6qaM4qpns-OmDYGAtzj14NRHXJiV4TU7Mdi2IlnitrlkRePFL-J5kctQR6-QX4qC3cTiRRl9_zxpSONtLsJTGUT6F3ExptPehJURv_kTD0neiPU",
        ["Figma", "Vue.js"],
        20,
    ),
    (
        "Sistem Manajemen PKL (Monitoring)",
        "Internal Tool",
        "Streamlining internship monitoring with tracking and reporting for students and supervisors.",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuBoJMDo_3IMD8WZ53aOTliElZz3LhbDNu1ZRy6LrifH9D8I_DcZykYDwiht3suluqdzwpQ23UsCb7pqUwd86GWVwRM4FcSss7oU-SZz2Rj-RE7lvtrYDSmooYgpi3urMgNQj8JU5ghS2-KCovbjSYqNjtAehWRxKyx8TAQWNinQ2dLMKFcl3dM1ELr_Ogx_Nhdqi-d2vWmBN2wAr5-XPM1eHaQ1s3mvOkbqnLi2SQmgLsxTBugbNxjDMHuAsVRChwcsUmrM5yFK5J4",
        ["Laravel", "PostgreSQL", "Vue.js"],
        30,
    ),
]


def create_tables(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        create table if not exists projects (
          id varchar(36) primary key,
          title varchar(140) not null,
          category varchar(80) not null,
          description text not null,
          image_url text not null,
          technologies json not null,
          case_study_url text,
          live_url text,
          sort_order integer not null default 0,
          is_featured boolean not null default 1,
          created_at datetime not null default current_timestamp,
          updated_at datetime not null default current_timestamp
        )
        """
    )
    conn.execute(
        """
        create table if not exists contact_messages (
          id varchar(36) primary key,
          name varchar(140) not null,
          email varchar(254) not null,
          message text not null,
          created_at datetime not null default current_timestamp,
          updated_at datetime not null default current_timestamp
        )
        """
    )
    conn.execute(
        """
        create table if not exists skills (
          id varchar(36) primary key,
          name varchar(80) not null unique,
          logo_url text not null,
          sort_order integer not null default 0,
          is_active boolean not null default 1,
          created_at datetime not null default current_timestamp,
          updated_at datetime not null default current_timestamp
        )
        """
    )


def main() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        create_tables(conn)

        for name, logo_url, sort_order in skills:
            conn.execute(
                """
                insert into skills (id, name, logo_url, sort_order, is_active)
                values (?, ?, ?, ?, 1)
                on conflict(name) do update set
                  logo_url = excluded.logo_url,
                  sort_order = excluded.sort_order,
                  is_active = 1,
                  updated_at = current_timestamp
                """,
                (str(uuid4()), name, logo_url, sort_order),
            )

        for title, category, description, image_url, technologies, sort_order in projects:
            existing = conn.execute("select id from projects where title = ?", (title,)).fetchone()
            if existing:
                conn.execute(
                    """
                    update projects
                    set category = ?, description = ?, image_url = ?, technologies = ?,
                        sort_order = ?, is_featured = 1, updated_at = current_timestamp
                    where title = ?
                    """,
                    (category, description, image_url, json.dumps(technologies), sort_order, title),
                )
            else:
                conn.execute(
                    """
                    insert into projects
                    (id, title, category, description, image_url, technologies, sort_order, is_featured)
                    values (?, ?, ?, ?, ?, ?, ?, 1)
                    """,
                    (str(uuid4()), title, category, description, image_url, json.dumps(technologies), sort_order),
                )

        conn.commit()

    print(f"Local database seeded: {DB_PATH}")


if __name__ == "__main__":
    main()
