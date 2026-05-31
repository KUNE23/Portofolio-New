<template>
  <section class="py-20" id="journey">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
      <div>
        <span class="font-label-sm text-primary tracking-widest uppercase">Journey</span>
        <h2 class="font-display text-headline-lg text-on-background">Learning by building.</h2>
      </div>
      <p class="text-on-surface-variant max-w-md">
        Beberapa titik penting dari proses belajar, organisasi, dan project yang membentuk cara saya membangun produk digital.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-bento-gap">
      <article
        v-for="item in timeline"
        :key="item.year"
        class="bg-surface-container-lowest border border-outline-variant/10 rounded-lg bento-shadow p-8"
      >
        <span class="font-label-sm text-primary">{{ item.year }}</span>
        <h3 class="font-display text-headline-md mt-3 mb-3">{{ item.title }}</h3>
        <p class="text-on-surface-variant">{{ item.description }}</p>
      </article>
    </div>
  </section>
</template>

<script setup>
const timeline = [
  {
    year: '2024',
    title: 'Started Web Development',
    description: 'Mendalami dasar frontend, backend, dan workflow pembuatan aplikasi web modern.',
  },
  {
    year: '2025',
    title: 'Built Real Projects',
    description: 'Mengembangkan website portofolio, sistem internal, dan dashboard yang fokus pada kebutuhan pengguna.',
  },
  {
    year: 'Now',
    title: 'Sharpening Product Craft',
    description: 'Memperkuat kemampuan UI, arsitektur aplikasi, dan problem solving lewat project yang lebih terarah.',
  },
]
</script>
