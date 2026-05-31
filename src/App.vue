<template>
  <div id="app">
    <Transition name="welcome">
      <div v-if="showWelcome" class="welcome-screen" role="status" aria-live="polite">
        <p class="welcome-eyebrow">Welcome to Portofolio</p>
        <h1 class="welcome-title">Alfiansyah Sibyanurrizki</h1>
      </div>
    </Transition>

    <router-view />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const showWelcome = ref(false)

onMounted(() => {
  const hasSeenWelcome = sessionStorage.getItem('hasSeenWelcome')

  if (hasSeenWelcome) {
    return
  }

  showWelcome.value = true
  sessionStorage.setItem('hasSeenWelcome', 'true')

  window.setTimeout(() => {
    showWelcome.value = false
  }, 3200)
})
</script>

<style>
.welcome-screen {
  position: fixed;
  inset: 0;
  z-index: 999;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 1rem;
  padding: 2rem;
  background: #fafafa;
  color: #1f1f1f;
  overflow: hidden;
}

.welcome-screen::before {
  content: "";
  position: absolute;
  width: min(58vw, 520px);
  aspect-ratio: 1;
  border-radius: 999px;
  background: rgba(217, 45, 32, 0.1);
  filter: blur(42px);
  transform: translate(-32%, -18%);
}

.welcome-eyebrow,
.welcome-title {
  position: relative;
  margin: 0;
  text-align: center;
}

.welcome-eyebrow {
  color: #d92d20;
  font-size: clamp(1rem, 3vw, 1.35rem);
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  animation: welcomeSlideUp 0.8s ease both;
}

.welcome-title {
  max-width: 11ch;
  font-size: clamp(3rem, 12vw, 7rem);
  font-weight: 900;
  line-height: 0.95;
  animation: welcomeReveal 1.1s 0.35s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.welcome-enter-active,
.welcome-leave-active {
  transition: opacity 0.55s ease, transform 0.55s ease;
}

.welcome-enter-from,
.welcome-leave-to {
  opacity: 0;
  transform: scale(1.02);
}

@keyframes welcomeSlideUp {
  from {
    opacity: 0;
    transform: translateY(18px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes welcomeReveal {
  from {
    opacity: 0;
    clip-path: inset(0 0 100% 0);
    transform: translateY(26px);
  }

  to {
    opacity: 1;
    clip-path: inset(0 0 0 0);
    transform: translateY(0);
  }
}

@media (max-width: 767px) {
  .welcome-title {
    max-width: 9ch;
  }
}
</style>
