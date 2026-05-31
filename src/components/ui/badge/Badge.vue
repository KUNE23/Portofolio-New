<template>
  <span :class="['ui-badge', `ui-badge--${variant}`]">
    <slot />
  </span>
</template>

<script setup>
defineProps({
  variant: {
    type: String,
    default: 'secondary',
  },
})
</script>

<style scoped>
.ui-badge {
  display: inline-flex;
  width: fit-content;
  align-items: center;
  border-radius: 999px;
  border: 1px solid transparent;
  padding: 0.2rem 0.65rem;
  font-size: 0.75rem;
  font-weight: 800;
  line-height: 1.2;
}

.ui-badge--secondary {
  background: #f4f4f5;
  color: #3f3f46;
}

.ui-badge--destructive {
  background: #fee2e2;
  color: #991b1b;
}
</style>
