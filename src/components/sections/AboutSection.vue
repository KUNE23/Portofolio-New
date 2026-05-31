<template>
  <section class="py-20" id="about">
    <div class="grid grid-cols-1 md:grid-cols-12 gap-bento-gap">
      <div class="md:col-span-12 mb-8">
        <h2 class="font-display text-headline-lg text-on-background mb-4">Building web experiences while exploring the future of AI.</h2>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-3xl">
                 I am an Informatics Engineering student and Fullstack Developer who enjoys building modern, functional, and meaningful digital products. Currently, I am expanding my skills in Artificial Intelligence to create smarter, more efficient, and impactful technology solutions.
              </p>
      </div>
      <div class="md:col-span-4 p-8 bg-surface-container-lowest rounded-lg bento-shadow border border-outline-variant/10 group hover:border-primary/30 transition-all">
        <div class="w-12 h-12 rounded-full bg-soft-blue flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
          <Code2 class="text-primary" />
        </div>
        <h3 class="font-headline-md mb-2">Website Development</h3>
        <p class="text-on-surface-variant">I build responsive and scalable web applications using frontend and backend technologies, focusing on performance, usability, and clean system architecture.</p>
      </div>
      <div class="md:col-span-4 p-8 bg-surface-container-lowest rounded-lg bento-shadow border border-outline-variant/10 group hover:border-primary/30 transition-all">
        <div class="w-12 h-12 rounded-full bg-soft-pink flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
          <Puzzle class="text-primary" />
        </div>
        <h3 class="font-headline-md mb-2">Problem Solving</h3>
        <p class="text-on-surface-variant">I turn ideas and real-world problems into digital solutions through structured thinking, clean code, and user-focused development.</p>
      </div>
      <div class="md:col-span-4 p-8 bg-surface-container-lowest rounded-lg bento-shadow border border-outline-variant/10 group hover:border-primary/30 transition-all">
        <div class="w-12 h-12 rounded-full bg-soft-yellow flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
          <Psychology class="text-primary" />
        </div>
        <h3 class="font-headline-md mb-2">AI Exploration</h3>
        <p class="text-on-surface-variant">I am actively learning Artificial Intelligence to understand how intelligent systems, automation, and AI-powered features can improve digital products.</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { Brain as Psychology, Code2, Puzzle } from '@lucide/vue'
</script>

<style scoped>

</style>
