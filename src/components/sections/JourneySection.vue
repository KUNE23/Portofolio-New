<template>
  <section class="py-20" id="journey">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
      <div>
        <span class="font-label-sm text-primary tracking-widest uppercase">Journey</span>
        <h2 class="font-display text-headline-lg text-on-background">Learning, Building, and Growing as a Developer.</h2>
      </div>
      <p class="text-on-surface-variant max-w-md">
       A short overview of my growth as an Informatics Engineering student, from learning web development fundamentals to building real projects and exploring AI-powered solutions.
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
    title: 'Started My Web Development Journey',
    description: 'Began learning the fundamentals of frontend, backend, databases, and how modern web applications are built.',
  },
  {
    year: '2025',
    title: 'Built Real Digital Products',
    description: 'Developed portfolio websites, internal systems, dashboards, and learning platforms focused on real user needs.',
  },
  {
    year: 'Now',
    title: 'Exploring AI and Smarter Solutions',
    description: 'Currently improving my fullstack skills while learning Artificial Intelligence to build more intelligent, efficient, and impactful digital products.',
  },
]
</script>
