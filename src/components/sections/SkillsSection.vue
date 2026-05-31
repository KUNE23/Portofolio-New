<template>
  <section class="py-20 bg-surface-noise rounded-xl p-12 mb-20" id="skills">
    <div class="text-center mb-16">
      <h2 class="font-display text-headline-lg mb-4">Technical Arsenal</h2>
      <p class="text-on-surface-variant max-w-xl mx-auto">The tools and technologies I use to bring ideas to life across the full development stack.</p>
    </div>
    <div class="skills-marquee" aria-label="Technology skills carousel">
      <div class="skills-track">
        <article
          v-for="skill in scrollingSkills"
          :key="`${skill.name}-${skill.copy}`"
          class="skill-card"
        >
          <img class="skill-logo" :src="skill.logo" :alt="`${skill.name} logo`" loading="lazy" />
          <span class="skill-name">{{ skill.name }}</span>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { defaultSkills } from '@/data/defaultContent'
import { getSkills } from '@/services/api'

const skills = ref(defaultSkills)

const scrollingSkills = computed(() => [...skills.value, ...skills.value].map((skill, index) => ({
  ...skill,
  logo: skill.logo_url || skill.logo,
  copy: index,
})))

onMounted(async () => {
  try {
    const data = await getSkills()
    if (Array.isArray(data) && data.length) {
      skills.value = data
    }
  } catch {
    skills.value = defaultSkills
  }
})
</script>

<style scoped>
.skills-marquee {
  position: relative;
  overflow-x: auto;
  overflow-y: hidden;
  padding: 0.75rem 0 1.25rem;
  scrollbar-width: none;
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
  mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
}

.skills-marquee::-webkit-scrollbar {
  display: none;
}

.skills-track {
  display: flex;
  width: max-content;
  gap: 1rem;
  animation: scrollSkills 32s linear infinite;
}

.skills-marquee:hover .skills-track {
  animation-play-state: paused;
}

.skill-card {
  flex: 0 0 auto;
  width: 148px;
  min-height: 132px;
  display: grid;
  place-items: center;
  gap: 0.75rem;
  padding: 1.25rem 1rem;
  border-radius: 0.75rem;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(207, 214, 221, 0.22);
  box-shadow: 0 18px 50px rgba(31, 31, 31, 0.08);
}

.skill-logo {
  width: 54px;
  height: 54px;
  object-fit: contain;
}

.skill-name {
  color: #1f1f1f;
  font-size: 0.95rem;
  font-weight: 700;
  text-align: center;
}

@keyframes scrollSkills {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(calc(-50% - 0.5rem));
  }
}

@media (max-width: 767px) {
  .skills-marquee {
    margin-left: -1rem;
    margin-right: -1rem;
    padding-left: 1rem;
    padding-right: 1rem;
    -webkit-mask-image: none;
    mask-image: none;
  }

  .skills-track {
    animation-duration: 26s;
  }

  .skill-card {
    width: 122px;
    min-height: 116px;
  }

  .skill-logo {
    width: 46px;
    height: 46px;
  }
}
</style>
