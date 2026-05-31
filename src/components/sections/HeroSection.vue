<template>
  <section class="py-16 md:py-24 grid grid-cols-1 lg:grid-cols-12 gap-bento-gap relative" id="home">
    <!-- Decorative Blobs -->
    <div class="blob absolute -top-20 -left-20 w-64 h-64 bg-soft-pink opacity-50 rounded-full"></div>
    <div class="blob absolute top-40 -right-20 w-80 h-80 bg-soft-blue opacity-40 rounded-full"></div>
    <div class="lg:col-span-7 flex flex-col justify-center gap-6">
      <div class="inline-flex">
        <span class="bg-soft-yellow text-on-secondary-fixed-variant px-4 py-1.5 rounded-full font-label-sm border border-outline-variant/20 sticker-badge">
                  Informatics Student • Web Developer • AI Enthusiast
                </span>
      </div>
      <h1 class="hero-title font-display text-headline-lg-mobile md:text-display text-on-background leading-tight">
        Building useful web experiences while exploring
        <span class="text-primary typewriter-text" aria-label="large-language-model intelligence.">
          {{ typedText }}<span class="typewriter-cursor" aria-hidden="true"></span>
        </span>
      </h1>
      <p class="font-body-lg text-body-lg text-on-surface-variant max-w-xl">
                    <b>Hi, I’m Alfiansyah </b> – a Computer‑Science student and full‑stack developer who builds web experiences, information systems, and clean interfaces to solve real‑world problems.
 I’m currently deepening my expertise in AI, especially large‑language‑model integration, to make my applications smarter and more useful.
      </p>
      <div class="flex flex-wrap gap-4 mt-4">
        <a
          class="resume-button inline-flex items-center gap-2 bg-primary text-on-primary border border-primary px-8 py-4 rounded-full font-headline-md bento-shadow transition-all hover:bg-white hover:text-primary hover:scale-105 active:scale-95"
          href="/resume.pdf"
          download
        >
          <Download class="w-5 h-5" aria-hidden="true" />
          <span>Download Resume</span>
        </a>
      </div>
    </div>
    <div class="lg:col-span-5 relative flex items-center justify-center">
      <!-- Profile Bento Stack -->
      <div class="profile-frame relative w-full md:aspect-auto md:h-[500px]">
        <div class="absolute inset-0 bg-surface-container-lowest rounded-lg bento-shadow rotate-3 border border-outline-variant/10"></div>
        <div class="absolute inset-0 bg-white rounded-lg bento-shadow -rotate-2 border border-outline-variant/20 overflow-hidden group">
          <img
            alt="Alfiansyah Profile"
            class="w-full h-full object-cover profile-photo grayscale group-hover:grayscale-0 transition-all duration-700"
            :src="profilePhoto"
            width="1024"
            height="1536"
            loading="eager"
            decoding="async"
            fetchpriority="high"
          />
        </div>
        <!-- Floating Stickers -->
        <div class="absolute -top-6 -right-6 animate-float bg-soft-blue p-4 rounded-lg bento-shadow border border-white/50">
          <Code class="text-primary text-headline-md" />
        </div>
        <div class="absolute bottom-10 -left-10 animate-float [animation-delay:1s] bg-white p-4 rounded-lg bento-shadow border border-white/50 flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-soft-pink flex items-center justify-center">
            <Draw class="text-primary" />
          </div>
          <div>
            <p class="font-label-sm text-on-background">Code & Intelligence</p>
            <div class="h-1.5 w-16 bg-surface-container rounded-full overflow-hidden">
              <div class="h-full bg-primary w-4/5"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { Code, Download, PenTool as Draw } from '@lucide/vue'
import { onBeforeUnmount, onMounted, ref } from 'vue'
import profilePhoto from '@/assets/profile-home.webp'

const targetText = 'large-language-\nmodel intelligence.'
const typedText = ref('')
let typingTimer
let deletingTimer

const typeText = (index = 0) => {
  typedText.value = targetText.slice(0, index)

  if (index <= targetText.length) {
    typingTimer = window.setTimeout(() => typeText(index + 1), 70)
    return
  }

  deletingTimer = window.setTimeout(() => deleteText(targetText.length), 1800)
}

const deleteText = (index) => {
  typedText.value = targetText.slice(0, index)

  if (index > 0) {
    deletingTimer = window.setTimeout(() => deleteText(index - 1), 35)
    return
  }

  typingTimer = window.setTimeout(() => typeText(0), 450)
}

onMounted(() => {
  typeText()
})

onBeforeUnmount(() => {
  window.clearTimeout(typingTimer)
  window.clearTimeout(deletingTimer)
})
</script>

<style scoped>
.blob {
  filter: blur(60px);
  z-index: -1
}
.animate-float {
  animation: float 6s ease-in-out infinite
}
@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(0);
  } 50% {
    transform: translateY(-10px) rotate(2deg);
  }
}
.sticker-badge {
  transform: rotate(-3deg);
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
}
.sticker-badge:hover {
  transform: rotate(2deg) scale(1.1)
}
.typewriter-text {
  display: inline-block;
  min-width: min(100%, 15ch);
  white-space: pre-line;
}
.profile-frame {
  aspect-ratio: 3 / 4;
}
.typewriter-cursor {
  display: inline-block;
  width: 0.08em;
  height: 0.9em;
  margin-left: 0.08em;
  background: currentColor;
  transform: translateY(0.08em);
  animation: blink 0.85s steps(1) infinite;
}
@keyframes blink {
  50% {
    opacity: 0;
  }
}
.profile-photo {
  object-position: center 42%;
}
@media (max-width: 767px) {
  .hero-title {
    max-width: 100%;
    overflow-wrap: anywhere;
  }

  .typewriter-text {
    display: block;
    margin-top: 0.2em;
    min-width: 0;
    max-width: 100%;
    line-height: 1.08;
  }

  .profile-frame {
    aspect-ratio: 2 / 3;
    max-width: min(100%, 22rem);
    margin-inline: auto;
  }

  .profile-frame > div {
    transform: none;
  }

  .profile-photo {
    object-position: center center;
  }
}
</style>
