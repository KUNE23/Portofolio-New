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

    <div class="roadmap" aria-label="Developer journey roadmap">
      <article
        v-for="item in timeline"
        :key="item.year"
        class="roadmap-item"
      >
        <div class="roadmap-marker">
          <component :is="item.icon" class="roadmap-icon" aria-hidden="true" />
        </div>
        <div class="roadmap-card">
          <span class="roadmap-year font-label-sm text-primary">{{ item.year }}</span>
          <h3 class="font-display text-headline-md mt-3 mb-3">{{ item.title }}</h3>
          <p class="text-on-surface-variant">{{ item.description }}</p>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
import { Bot, Code2, Rocket } from '@lucide/vue'

const timeline = [
  {
    year: '2024',
    title: 'Started My Web Development Journey',
    description: 'Began learning the fundamentals of frontend, backend, databases, and how modern web applications are built.',
    icon: Code2,
  },
  {
    year: '2025',
    title: 'Built Real Digital Products',
    description: 'Developed portfolio websites, internal systems, dashboards, and learning platforms focused on real user needs.',
    icon: Rocket,
  },
  {
    year: 'Now',
    title: 'Exploring AI and Smarter Solutions',
    description: 'Currently improving my fullstack skills while learning Artificial Intelligence to build more intelligent, efficient, and impactful digital products.',
    icon: Bot,
  },
]
</script>

<style scoped>
.roadmap {
  position: relative;
  display: grid;
  gap: 1.5rem;
  padding-left: 1.75rem;
}

.roadmap::before {
  content: "";
  position: absolute;
  top: 1.5rem;
  bottom: 1.5rem;
  left: 0.75rem;
  width: 3px;
  border-radius: 999px;
  background: linear-gradient(180deg, #d92d20, #f7c948 55%, #7dd3fc);
}

.roadmap-item {
  position: relative;
  display: grid;
  grid-template-columns: 2.5rem minmax(0, 1fr);
  gap: 1rem;
  align-items: flex-start;
}

.roadmap-marker {
  position: relative;
  z-index: 1;
  display: grid;
  width: 2.5rem;
  height: 2.5rem;
  place-items: center;
  border-radius: 999px;
  color: #d92d20;
  background: #ffffff;
  border: 2px solid #d92d20;
  box-shadow: 0 12px 30px rgba(217, 45, 32, 0.16);
}

.roadmap-icon {
  width: 1.2rem;
  height: 1.2rem;
}

.roadmap-card {
  padding: 1.5rem;
  border-radius: 0.5rem;
  background: #ffffff;
  border: 1px solid rgba(207, 214, 221, 0.18);
  box-shadow: 0 18px 50px rgba(31, 31, 31, 0.08);
}

.roadmap-year {
  display: inline-flex;
  align-items: center;
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  background: #fff3c4;
}

@media (min-width: 768px) {
  .roadmap {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0;
    padding: 4.25rem 0 0;
  }

  .roadmap::before {
    top: 1.25rem;
    bottom: auto;
    left: 12%;
    right: 12%;
    width: auto;
    height: 3px;
    background: linear-gradient(90deg, #d92d20, #f7c948 55%, #7dd3fc);
  }

  .roadmap-item {
    grid-template-columns: minmax(0, 1fr);
    justify-items: center;
    gap: 1.25rem;
    padding: 0 0.75rem;
  }

  .roadmap-marker {
    position: absolute;
    top: -4.25rem;
  }

  .roadmap-card {
    min-height: 100%;
  }
}
</style>
