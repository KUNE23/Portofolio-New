<template>
  <footer class="border-t border-outline-variant/20 bg-surface">
    <div class="footer-content max-w-[1280px] mx-auto px-margin-mobile md:px-margin-desktop py-8 flex flex-col md:flex-row justify-between gap-4">
      <p class="text-on-surface-variant text-label-md">Fullstack Developer · Informatics Engineering Student · AI Explorer</p>
      <p class="font-label-md text-on-background">Alfiansyah Sibyanurrizki.</p>
      <p class="text-on-surface-variant text-label-md">© 2026 Built with Vue, Vite, and curiosity.</p>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer-content {
  text-align: center;
  align-items: center;
}

@media (min-width: 768px) {
  .footer-content {
    text-align: left;
    align-items: flex-start;
  }
}
</style>
