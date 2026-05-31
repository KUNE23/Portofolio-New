<template>
  <header class="sticky top-0 w-full bg-surface/80 backdrop-blur-md border-b border-outline-variant/10 shadow-sm z-50">
    <div class="navbar-shell px-margin-mobile md:px-margin-desktop py-4 max-w-[1280px] mx-auto">
      <nav class="hidden md:flex gap-8 items-center desktop-nav" aria-label="Main navigation">
        <a
          v-for="link in links"
          :key="link.href"
          class="desktop-nav-link font-body-md text-body-md hover:scale-105 transition-all"
          :class="{ 'is-active': activeHref === link.href }"
          :href="link.href"
          @click.prevent="scrollToSection(link.href)"
        >
          {{ link.label }}
        </a>
      </nav>

      <button
        class="mobile-menu-button"
        type="button"
        :aria-expanded="isOpen"
        aria-label="Toggle navigation menu"
        @click="isOpen = !isOpen"
      >
        <Menu v-if="!isOpen" class="menu-icon" />
        <X v-else class="menu-icon" />
      </button>
    </div>

    <nav v-if="isOpen" class="mobile-nav" aria-label="Mobile navigation">
      <a
        v-for="link in links"
        :key="link.href"
        class="mobile-nav-link"
        :class="{ 'is-active': activeHref === link.href }"
        :href="link.href"
        @click.prevent="handleMobileClick(link.href)"
      >
        {{ link.label }}
      </a>
    </nav>
  </header>
</template>

<script setup>
import { Menu, X } from '@lucide/vue'
import { onBeforeUnmount, onMounted, ref } from 'vue'

const isOpen = ref(false)
const activeHref = ref('#home')

const links = [
  { label: 'Home', href: '#home' },
  { label: 'About', href: '#about' },
  { label: 'Projects', href: '#projects' },
  { label: 'Skills', href: '#skills' },
  { label: 'Contact', href: '#contact' },
]

const setActive = (href) => {
  activeHref.value = href
}

const scrollToSection = (href) => {
  const section = document.querySelector(href)

  if (!section) {
    setActive(href)
    return
  }

  const headerOffset = window.innerWidth < 768 ? 92 : 88
  const sectionTop = section.getBoundingClientRect().top + window.scrollY

  setActive(href)
  window.history.pushState(null, '', href)
  window.scrollTo({
    top: Math.max(sectionTop - headerOffset, 0),
    behavior: 'smooth',
  })
}

const handleMobileClick = (href) => {
  isOpen.value = false
  scrollToSection(href)
}

const updateActiveLink = () => {
  const scrollPosition = window.scrollY + 140
  const activeLink = links
    .map((link) => ({
      ...link,
      section: document.querySelector(link.href),
    }))
    .filter((link) => link.section)
    .reverse()
    .find((link) => link.section.offsetTop <= scrollPosition)

  activeHref.value = activeLink?.href || '#home'
}

onMounted(() => {
  updateActiveLink()
  window.addEventListener('scroll', updateActiveLink, { passive: true })
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', updateActiveLink)
})
</script>

<style scoped>
.navbar-shell {
  display: flex;
  justify-content: center;
  align-items: center;
}

.desktop-nav-link {
  color: #5f6368;
  border-bottom: 2px solid transparent;
  font-weight: 500;
}

.desktop-nav-link.is-active {
  color: #d92d20;
  font-weight: 700;
  border-bottom: 2px solid #d92d20;
}

.mobile-menu-button {
  display: none;
  width: 2.75rem;
  height: 2.75rem;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  background: #ffffff;
  color: #1f1f1f;
  border: 1px solid rgba(207, 214, 221, 0.35);
  box-shadow: 0 8px 24px rgba(31, 31, 31, 0.08);
}

.menu-icon {
  width: 1.25rem;
  height: 1.25rem;
}

.mobile-nav {
  display: none;
}

@media (max-width: 767px) {
  .navbar-shell {
    justify-content: flex-end;
  }

  .mobile-menu-button {
    display: inline-flex;
  }

  .mobile-nav {
    display: grid;
    gap: 0.25rem;
    width: calc(100% - 40px);
    margin: 0 auto 1rem;
    padding: 0.75rem;
    border-radius: 0.75rem;
    background: rgba(255, 255, 255, 0.96);
    border: 1px solid rgba(207, 214, 221, 0.25);
    box-shadow: 0 18px 50px rgba(31, 31, 31, 0.1);
  }

  .mobile-nav-link {
    display: block;
    padding: 0.9rem 1rem;
    border-radius: 0.5rem;
    color: #5f6368;
    font-weight: 700;
    text-align: center;
  }

  .mobile-nav-link.is-active,
  .mobile-nav-link:hover {
    background: #f4f6f8;
    color: #d92d20;
  }
}
</style>
