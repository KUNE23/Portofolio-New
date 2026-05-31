<template>
  <textarea
    class="ui-textarea"
    :value="modelValue"
    v-bind="$attrs"
    @input="$emit('update:modelValue', $event.target.value)"
  />
</template>

<script setup>
defineOptions({
  inheritAttrs: false,
})

defineProps({
  modelValue: {
    type: String,
    default: '',
  },
})

defineEmits(['update:modelValue'])
</script>

<style scoped>
.ui-textarea {
  width: 100%;
  min-height: 7rem;
  border: 1px solid #d4d4d8;
  border-radius: 0.5rem;
  background: #ffffff;
  padding: 0.625rem 0.75rem;
  color: #18181b;
  font: inherit;
  resize: vertical;
  transition: border-color 0.18s ease, box-shadow 0.18s ease;
}

.ui-textarea:focus {
  border-color: #d92d20;
  outline: 0;
  box-shadow: 0 0 0 3px rgba(217, 45, 32, 0.12);
}
</style>
