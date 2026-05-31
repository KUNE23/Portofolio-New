<template>
  <div class="min-h-screen bg-background text-on-background">
    <!-- Header / TopNavBar -->
    <NavBar />

    <!-- Main Content -->
    <main class="max-w-[1280px] mx-auto px-margin-mobile md:px-margin-desktop overflow-hidden">
      <!-- Hero Section -->
      <HeroSection />

      <!-- About Section -->
      <AboutSection />

      <!-- Projects Section -->
      <ProjectsSection />

      <!-- Skills Section -->
      <SkillsSection />

      <!-- Journey Section -->
      <JourneySection />

      <!-- Contact Section -->
      <ContactSection />
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import NavBar from '@/components/layout/NavBar.vue'
import HeroSection from '@/components/sections/HeroSection.vue'
import AboutSection from '@/components/sections/AboutSection.vue'
import ProjectsSection from '@/components/sections/ProjectsSection.vue'
import SkillsSection from '@/components/sections/SkillsSection.vue'
import JourneySection from '@/components/sections/JourneySection.vue'
import ContactSection from '@/components/sections/ContactSection.vue'
import Footer from '@/components/layout/Footer.vue'
</script>

<style>
/* Global styles if needed */
:root {
  --margin-desktop: 64px;
  --margin-mobile: 20px;
  --bento-gap: 24px;
  --gutter: 24px;
  --unit: 8px;
}
</style>