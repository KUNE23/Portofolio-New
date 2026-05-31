<template>
  <section class="py-20" id="about">
    <div class="grid grid-cols-1 md:grid-cols-12 gap-bento-gap">
      <div class="md:col-span-12 mb-8">
        <h2 class="font-display text-headline-lg text-on-background mb-4">Not just writing code — I build experiences.</h2>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-3xl">
                  Saya adalah mahasiswa Informatika yang suka membuat website, sistem informasi, dan tampilan digital yang sederhana tapi berguna. My approach combines technical rigor with a deep focus on user-centric design principles.
              </p>
      </div>
      <div class="md:col-span-4 p-8 bg-surface-container-lowest rounded-lg bento-shadow border border-outline-variant/10 group hover:border-primary/30 transition-all">
        <div class="w-12 h-12 rounded-full bg-soft-blue flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
          <Palette class="text-primary" />
        </div>
        <h3 class="font-headline-md mb-2">I design clean interfaces</h3>
        <p class="text-on-surface-variant">Focusing on clarity and visual hierarchy to create intuitive user paths.</p>
      </div>
      <div class="md:col-span-4 p-8 bg-surface-container-lowest rounded-lg bento-shadow border border-outline-variant/10 group hover:border-primary/30 transition-all">
        <div class="w-12 h-12 rounded-full bg-soft-pink flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
          <Terminal class="text-primary" />
        </div>
        <h3 class="font-headline-md mb-2">I build web systems</h3>
        <p class="text-on-surface-variant">Scalable, robust backend architectures that power modern digital solutions.</p>
      </div>
      <div class="md:col-span-4 p-8 bg-surface-container-lowest rounded-lg bento-shadow border border-outline-variant/10 group hover:border-primary/30 transition-all">
        <div class="w-12 h-12 rounded-full bg-soft-yellow flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
          <Psychology class="text-primary" />
        </div>
        <h3 class="font-headline-md mb-2">I enjoy solving user problems</h3>
        <p class="text-on-surface-variant">Analyzing needs and translating them into efficient functional requirements.</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { Brain as Psychology, Palette, Terminal } from '@lucide/vue'
</script>

<style scoped>

</style>
