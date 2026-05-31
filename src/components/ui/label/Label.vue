<template>
  <label class="ui-label">
    <slot />
  </label>
</template>

<style scoped>
.ui-label {
  display: grid;
  gap: 0.375rem;
  color: #3f3f46;
  font-size: 0.875rem;
  font-weight: 700;
  line-height: 1.35;
}
</style>
