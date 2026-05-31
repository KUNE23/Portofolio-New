insert into skills (name, logo_url, sort_order, is_active) values
  ('Vue', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg', 10, true),
  ('Tailwind', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg', 20, true),
  ('Node.js', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg', 30, true),
  ('Laravel', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/laravel/laravel-original.svg', 40, true),
  ('Express', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg', 50, true),
  ('Python', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg', 60, true),
  ('PostgreSQL', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg', 70, true),
  ('MySQL', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg', 80, true),
  ('MongoDB', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg', 90, true),
  ('Redis', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg', 100, true),
  ('Figma', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg', 110, true),
  ('Git', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg', 120, true),
  ('GitHub', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg', 130, true),
  ('Postman', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postman/postman-original.svg', 140, true),
  ('Docker', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg', 150, true),
  ('AWS', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg', 160, true)
on conflict (name) do update set
  logo_url = excluded.logo_url,
  sort_order = excluded.sort_order,
  is_active = excluded.is_active;

insert into projects (title, category, description, image_url, technologies, case_study_url, live_url, sort_order, is_featured) values
  (
    'Proclub Learning Hub (LMS)',
    'Education Tech',
    'A learning platform designed to organize courses, materials, and student progress.',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuB1bN0wC_39r_PgpkdUa3Xqg8Jd7_1_8fXtWhIIyHAlxZvAtRzp9Z_KddaZNO31eJknhDyxuI2i3-1pmSYh99QH61JP8duiRt54OCnhOe8uPfz09erHBV1q_BnTF7AHSXpB5nVId2XfERPS7bG7zgO8hQDffTOJuOrv3lIh3hSACGXIYE_S3RBQdfD_J586rwG1q0KgwwcKSzPRd8JFFHO4tMbGwaq_j0pfVO3rdkNvcApDlvF_bXJX-PRaeBgt_rYo8x9gRBebZYU',
    '["Vue.js", "Node.js", "Tailwind CSS"]'::jsonb,
    null,
    null,
    10,
    true
  ),
  (
    'Website Portofolio Himpunan',
    'Branding',
    'A digital showcase for the student association to highlight achievements and programs.',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuAUkitKPUqiB4nCXd7cjdqgHv8rJbp7dgk1DJx-uGjazoIyRPik9rJxg7rnzyffmh9k8czXmgVg93TB2SOgntsDLKfMly-BzIniWAlZCyZum-c2Ds8bwO-BnV-tZRiBoyK4dpcQM1p2ryXbwV6PjdwBLfLIKorS6qaM4qpns-OmDYGAtzj14NRHXJiV4TU7Mdi2IlnitrlkRePFL-J5kctQR6-QX4qC3cTiRRl9_zxpSONtLsJTGUT6F3ExptPehJURv_kTD0neiPU',
    '["Figma", "Vue.js"]'::jsonb,
    null,
    null,
    20,
    true
  ),
  (
    'Sistem Manajemen PKL (Monitoring)',
    'Internal Tool',
    'Streamlining internship monitoring with tracking and reporting for students and supervisors.',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuBoJMDo_3IMD8WZ53aOTliElZz3LhbDNu1ZRy6LrifH9D8I_DcZykYDwiht3suluqdzwpQ23UsCb7pqUwd86GWVwRM4FcSss7oU-SZz2Rj-RE7lvtrYDSmooYgpi3urMgNQj8JU5ghS2-KCovbjSYqNjtAehWRxKyx8TAQWNinQ2dLMKFcl3dM1ELr_Ogx_Nhdqi-d2vWmBN2wAr5-XPM1eHaQ1s3mvOkbqnLi2SQmgLsxTBugbNxjDMHuAsVRChwcsUmrM5yFK5J4',
    '["Laravel", "PostgreSQL", "Vue.js"]'::jsonb,
    null,
    null,
    30,
    true
  );
