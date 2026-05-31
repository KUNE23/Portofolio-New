<template>
  <button :class="['ui-button', `ui-button--${variant}`, `ui-button--${size}`]" v-bind="$attrs">
    <slot />
  </button>
</template>

<script setup>
defineOptions({
  inheritAttrs: false,
})

defineProps({
  variant: {
    type: String,
    default: 'default',
  },
  size: {
    type: String,
    default: 'default',
  },
})
</script>

<style scoped>
.ui-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  white-space: nowrap;
  border-radius: 0.5rem;
  border: 1px solid transparent;
  font-weight: 700;
  line-height: 1;
  transition: color 0.18s ease, background-color 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
}

.ui-button:focus-visible {
  outline: 2px solid #d92d20;
  outline-offset: 2px;
}

.ui-button:disabled {
  pointer-events: none;
  opacity: 0.5;
}

.ui-button--default {
  background: #d92d20;
  color: #ffffff;
  border-color: #d92d20;
}

.ui-button--default:hover {
  background: #b42318;
  border-color: #b42318;
}

.ui-button--outline {
  background: #ffffff;
  color: #18181b;
  border-color: #e4e4e7;
}

.ui-button--outline:hover {
  background: #f4f4f5;
}

.ui-button--ghost {
  background: transparent;
  color: #18181b;
}

.ui-button--ghost:hover {
  background: #f4f4f5;
}

.ui-button--destructive {
  background: #dc2626;
  color: #ffffff;
  border-color: #dc2626;
}

.ui-button--destructive:hover {
  background: #b91c1c;
  border-color: #b91c1c;
}

.ui-button--default.ui-button--default,
.ui-button--outline.ui-button--default,
.ui-button--ghost.ui-button--default,
.ui-button--destructive.ui-button--default {
  min-height: 2.5rem;
  padding: 0 1rem;
}

.ui-button--sm {
  min-height: 2.25rem;
  padding: 0 0.75rem;
  font-size: 0.875rem;
}

.ui-button--lg {
  min-height: 2.75rem;
  padding: 0 1.25rem;
}
</style>
