<template>
  <button
    class="ui-switch"
    :class="{ 'ui-switch--checked': checked }"
    type="button"
    role="switch"
    :aria-checked="checked"
    @click="$emit('update:checked', !checked)"
  >
    <span class="ui-switch-thumb"></span>
  </button>
</template>

<script setup>
defineProps({
  checked: {
    type: Boolean,
    default: false,
  },
})

defineEmits(['update:checked'])
</script>

<style scoped>
.ui-switch {
  position: relative;
  width: 2.5rem;
  height: 1.35rem;
  border-radius: 999px;
  border: 1px solid transparent;
  background: #d4d4d8;
  padding: 0;
  transition: background-color 0.18s ease;
}

.ui-switch--checked {
  background: #d92d20;
}

.ui-switch-thumb {
  position: absolute;
  top: 0.12rem;
  left: 0.12rem;
  width: 1.05rem;
  height: 1.05rem;
  border-radius: 999px;
  background: #ffffff;
  box-shadow: 0 1px 3px rgba(24, 24, 27, 0.25);
  transition: transform 0.18s ease;
}

.ui-switch--checked .ui-switch-thumb {
  transform: translateX(1.12rem);
}
</style>
