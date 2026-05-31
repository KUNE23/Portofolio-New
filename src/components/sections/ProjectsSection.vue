<template>
  <section class="py-20" id="projects">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
      <div>
        <span class="font-label-sm text-primary tracking-widest uppercase">Portfolio Highlights</span>
        <h2 class="font-display text-headline-lg text-on-background">Featured Works</h2>
      </div>
      <p class="text-on-surface-variant max-w-md">
        A selection of platforms I've designed and developed, from educational hubs to management systems.
      </p>
    </div>

    <div class="projects-grid">
      <article v-for="project in visibleProjects" :key="project.id" class="project-card group">
        <div class="project-media">
          <img
            :alt="project.title"
            class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
            :src="project.image_url"
            loading="lazy"
          />
        </div>
        <div class="project-content">
          <div class="flex justify-between items-start gap-4 mb-4">
            <div>
              <span class="bg-soft-blue text-on-secondary-fixed-variant px-3 py-1 rounded-full font-label-sm mb-2 inline-block">
                {{ project.category }}
              </span>
              <h3 class="font-display text-headline-md">{{ project.title }}</h3>
            </div>
            <a
              v-if="project.live_url || project.case_study_url"
              class="project-icon"
              :href="project.live_url || project.case_study_url"
              target="_blank"
              rel="noreferrer"
              aria-label="Open project"
            >
              <NorthEast class="text-white" />
            </a>
          </div>
          <p class="text-on-surface-variant mb-6">{{ project.description }}</p>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="tech in project.technologies"
              :key="tech"
              class="bg-surface-container px-3 py-1 rounded-full text-label-sm"
            >
              {{ tech }}
            </span>
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { ArrowUpRight as NorthEast } from '@lucide/vue'
import { defaultProjects } from '@/data/defaultContent'
import { getProjects } from '@/services/api'

const projects = ref(defaultProjects)

const visibleProjects = computed(() => (projects.value.length ? projects.value : defaultProjects))

onMounted(async () => {
  try {
    const data = await getProjects()
    if (Array.isArray(data) && data.length) {
      projects.value = data
    }
  } catch {
    projects.value = defaultProjects
  }
})
</script>

<style scoped>
.projects-grid {
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
  gap: 24px;
}

.project-card {
  overflow: hidden;
  border-radius: 0.5rem;
  background: #ffffff;
  border: 1px solid rgba(207, 214, 221, 0.1);
  box-shadow: 0 18px 50px rgba(31, 31, 31, 0.08);
}

.project-media {
  aspect-ratio: 16 / 9;
  overflow: hidden;
}

.project-content {
  padding: 2rem;
}

.project-icon {
  flex: 0 0 auto;
  width: 3rem;
  height: 3rem;
  border-radius: 999px;
  background: #d92d20;
  display: grid;
  place-items: center;
  transition: transform 0.25s ease;
}

.project-card:hover .project-icon {
  transform: rotate(45deg);
}

@media (min-width: 768px) {
  .projects-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .project-card:first-child {
    grid-column: span 2 / span 2;
  }
}
</style>
