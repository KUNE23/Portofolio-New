<template>
  <section class="contact-section" id="contact">
    <div class="contact-blob contact-blob--pink" aria-hidden="true"></div>
    <div class="contact-blob contact-blob--green" aria-hidden="true"></div>

    <div class="contact-layout">
      <div class="contact-copy">
        <div class="contact-intro">
          <span class="contact-pill">GET IN TOUCH</span>
          <h2 class="font-display text-headline-lg-mobile md:text-headline-lg text-on-background contact-heading">
            Have an idea? Let's make it real.
          </h2>
          <p class="font-display text-body-lg text-on-surface-variant contact-lead">
            Whether you have a question or just want to say hi, my inbox is always open.
          </p>
        </div>

        <div class="contact-details">
          <div class="info-row">
            <div class="info-icon">
              <Mail class="w-5 h-5" aria-hidden="true" />
            </div>
            <div>
              <p class="info-label">Email</p>
              <p class="info-value">hello@alfiansyah.dev</p>
            </div>
          </div>

          <a class="info-row" href="#">
            <div class="info-icon">
              <Phone class="w-5 h-5" aria-hidden="true" />
            </div>
            <div>
              <p class="info-label">Phone / WhatsApp</p>
              <p class="info-value">+62 8xx-xxxx-xxxx</p>
            </div>
          </a>

          <div class="info-row">
            <div class="info-icon">
              <MapPin class="w-5 h-5" aria-hidden="true" />
            </div>
            <div>
              <p class="info-label">Location</p>
              <p class="info-value">Surabaya, Indonesia</p>
            </div>
          </div>

          <div class="social-block">
            <p class="social-title">Follow Me</p>
            <div class="social-row">
              <a
                v-for="item in socialLinks"
                :key="item.label"
                class="social-button"
                :href="item.href"
                rel="noreferrer"
                target="_blank"
                :aria-label="item.label"
              >
                <svg
                  class="social-icon"
                  aria-hidden="true"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path v-for="path in item.paths" :key="path" :d="path" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="contact-form-wrap">
        <article class="contact-card">
          <div class="card-corner" aria-hidden="true"></div>

          <form class="contact-form" @submit.prevent="submitMessage">
            <div class="contact-grid">
              <Label>
                Full Name
                <Input v-model="form.name" autocomplete="name" maxlength="140" required placeholder="John Doe" />
              </Label>
              <Label>
                Email Address
                <Input
                  v-model="form.email"
                  autocomplete="email"
                  maxlength="254"
                  required
                  type="email"
                  placeholder="john@example.com"
                />
              </Label>
            </div>

            <Label>
              Message
              <Textarea v-model="form.message" maxlength="2000" required placeholder="How can I help you today?" rows="5" />
            </Label>

            <Button class="contact-button" :disabled="sending" type="submit">
              <LoaderCircle v-if="sending" class="button-icon button-icon--spin" aria-hidden="true" />
              <span>{{ sending ? 'Sending...' : 'Send Message' }}</span>
              <Send v-if="!sending" class="button-icon" aria-hidden="true" />
            </Button>
          </form>
        </article>

        <div
          v-if="notice"
          class="contact-status"
          :class="noticeType === 'success' ? 'contact-status--success' : 'contact-status--error'"
        >
          <component :is="noticeType === 'success' ? CheckCircle2 : AlertCircle" class="w-5 h-5" aria-hidden="true" />
          <span>{{ notice }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { reactive, ref } from 'vue'
import {
  AlertCircle,
  CheckCircle2,
  LoaderCircle,
  Mail,
  MapPin,
  Phone,
  Send,
} from '@lucide/vue'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import { createContactMessage } from '@/services/api'

const socialLinks = [
  {
    label: 'YouTube',
    href: '#',
    paths: [
      'M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31.2 31.2 0 0 0 0 12a31.2 31.2 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31.2 31.2 0 0 0 24 12a31.2 31.2 0 0 0-.5-5.8ZM9.6 15.6V8.4L15.8 12l-6.2 3.6Z',
    ],
  },
  {
    label: 'Instagram',
    href: '#',
    paths: [
      'M7.8 2h8.4A5.8 5.8 0 0 1 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8A5.8 5.8 0 0 1 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2Zm0 2A3.8 3.8 0 0 0 4 7.8v8.4A3.8 3.8 0 0 0 7.8 20h8.4a3.8 3.8 0 0 0 3.8-3.8V7.8A3.8 3.8 0 0 0 16.2 4H7.8Zm4.2 3.4a4.6 4.6 0 1 1 0 9.2 4.6 4.6 0 0 1 0-9.2Zm0 2a2.6 2.6 0 1 0 0 5.2 2.6 2.6 0 0 0 0-5.2Zm5-2.3a1.1 1.1 0 1 1 0 2.2 1.1 1.1 0 0 1 0-2.2Z',
    ],
  },
  {
    label: 'LinkedIn',
    href: '#',
    paths: [
      'M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.8h4v10.7H3V9.8Zm6.1 0h3.8v1.5h.1a4.2 4.2 0 0 1 3.8-2.1c4 0 4.7 2.6 4.7 6v5.3h-4v-4.7c0-1.1 0-2.6-1.6-2.6s-1.9 1.2-1.9 2.5v4.8h-4V9.8Z',
    ],
  },
  {
    label: 'GitHub',
    href: '#',
    paths: [
      'M12 .5A11.5 11.5 0 0 0 8.4 22.9c.6.1.8-.3.8-.6v-2.1c-3.4.7-4.1-1.5-4.1-1.5-.5-1.4-1.3-1.8-1.3-1.8-1.1-.8.1-.8.1-.8 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.4 11.4 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.5.4.9 1.1.9 2.2v3.3c0 .3.2.7.8.6A11.5 11.5 0 0 0 12 .5Z',
    ],
  },
  {
    label: 'Threads',
    href: '#',
    paths: [
      'M12.3 2C6.4 2 3 5.9 3 12.1c0 6.1 3.4 9.9 9.2 9.9 5.1 0 8.5-3 8.5-7.2 0-3.2-1.9-5.1-4.9-5.8-.5-2.5-2-3.9-4.6-3.9-2 0-3.5.8-4.5 2.4l1.7 1.2c.7-1 1.5-1.5 2.7-1.5 1.4 0 2.2.7 2.5 2.1h-1.8c-3.4 0-5.3 1.7-5.3 4.2 0 2.4 1.9 4 4.6 4 2.9 0 4.7-1.8 4.9-4.6v-1.6c1.6.6 2.5 1.7 2.5 3.4 0 3-2.4 5-6.3 5-4.5 0-7-3-7-7.7 0-4.9 2.6-7.8 7.1-7.8 2.6 0 4.6 1 5.9 3l1.8-1.2C18.3 3.4 15.7 2 12.3 2Zm1.6 9.6v.9c0 1.9-1 3-2.8 3-1.4 0-2.3-.8-2.3-1.9 0-1.2.9-2 3-2h2.1Z',
    ],
  },
]

const form = reactive({
  name: '',
  email: '',
  message: '',
})

const sending = ref(false)
const notice = ref('')
const noticeType = ref('success')

async function submitMessage() {
  notice.value = ''
  sending.value = true

  try {
    await createContactMessage({
      name: form.name.trim(),
      email: form.email.trim(),
      message: form.message.trim(),
    })

    form.name = ''
    form.email = ''
    form.message = ''
    noticeType.value = 'success'
    notice.value = 'Message sent successfully! I will get back to you soon.'
  } catch (err) {
    noticeType.value = 'error'
    notice.value = err.message
  } finally {
    sending.value = false
  }
}
</script>

<style scoped>
.contact-section {
  position: relative;
  padding: 6rem 0;
  isolation: isolate;
}

.contact-layout {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 24px;
}

.contact-copy {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 1rem 0;
}

.contact-intro {
  display: grid;
  gap: 1rem;
}

.contact-pill {
  display: inline-flex;
  align-items: center;
  width: fit-content;
  min-height: 2rem;
  padding: 0.45rem 1rem;
  border-radius: 999px;
  background: #fce4ec;
  color: #ba0036;
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.contact-heading {
  max-width: 13ch;
  margin: 0;
}

.contact-lead {
  max-width: 28rem;
  margin: 0;
}

.contact-details {
  display: grid;
  gap: 1.5rem;
  padding-top: 0.25rem;
}

.info-row {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.info-icon {
  width: 3rem;
  height: 3rem;
  display: grid;
  flex: 0 0 auto;
  place-items: center;
  border-radius: 1rem;
  background: #eeeeee;
  color: #ba0036;
  transition: transform 0.2s ease, background-color 0.2s ease, color 0.2s ease;
}

.info-row:hover .info-icon {
  transform: translateY(-1px);
  background: #ff385c;
  color: #ffffff;
}

.info-label,
.social-title {
  margin: 0;
  color: #5f5e5e;
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.info-value {
  margin: 0.25rem 0 0;
  color: #1a1c1c;
  font-size: 1rem;
  font-weight: 800;
}

.social-block {
  padding-top: 0.25rem;
}

.social-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1rem;
}

.social-button,
.contact-card {
  border: 1px solid rgba(34, 34, 34, 0.06);
  background: rgba(255, 255, 255, 0.82);
  backdrop-filter: blur(12px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 20px 40px -10px rgba(0, 0, 0, 0.05);
}

.social-button {
  width: 3rem;
  height: 3rem;
  display: grid;
  place-items: center;
  border-radius: 1rem;
  color: #1a1c1c;
  transition: transform 0.2s ease, box-shadow 0.2s ease, color 0.2s ease, border-color 0.2s ease;
}

.social-button:hover {
  transform: scale(1.1);
  border-color: rgba(255, 56, 92, 0.24);
  color: #ff385c;
  box-shadow: 0 10px 25px -12px rgba(255, 56, 92, 0.45);
}

.social-button:focus-visible {
  outline: 2px solid #ff385c;
  outline-offset: 2px;
}

.social-icon {
  width: 1.15rem;
  height: 1.15rem;
}

.contact-form-wrap {
  width: 100%;
}

.contact-card {
  position: relative;
  overflow: hidden;
  padding: 1.25rem;
  border-radius: 2rem;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.contact-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 30px 60px -15px rgba(0, 0, 0, 0.08);
}

.card-corner {
  position: absolute;
  top: 0;
  right: 0;
  width: 8rem;
  height: 8rem;
  border-bottom-left-radius: 999px;
  background: rgba(255, 56, 92, 0.06);
}

.contact-form {
  position: relative;
  z-index: 1;
  display: grid;
  gap: 1.5rem;
}

.contact-grid {
  display: grid;
  gap: 1.5rem;
}

.contact-button {
  width: 100%;
  min-height: 3.5rem;
  padding: 0 2rem;
  border-radius: 0.875rem;
  background: #ff385c;
  border-color: #ff385c;
  color: #ffffff;
  font-size: 1.125rem;
  font-weight: 800;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
}

.contact-button:hover {
  transform: scale(1.02);
  background: #ff385c;
  border-color: #ff385c;
  box-shadow: 0 10px 25px -5px rgba(255, 56, 92, 0.4);
}

.contact-button:active {
  transform: scale(0.98);
}

.button-icon {
  width: 1.25rem;
  height: 1.25rem;
}

.button-icon--spin {
  animation: iconSpin 0.8s linear infinite;
}

.contact-status {
  margin-top: 1rem;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.9rem 1rem;
  border-radius: 0.875rem;
  font-size: 0.95rem;
  font-weight: 700;
  line-height: 1.5;
}

.contact-status--success {
  background: #80f9bd;
  color: #002113;
}

.contact-status--error {
  background: #ffdad6;
  color: #93000a;
}

.contact-blob {
  position: absolute;
  z-index: -1;
  width: min(65vw, 400px);
  aspect-ratio: 1;
  border-radius: 999px;
  filter: blur(80px);
  pointer-events: none;
}

.contact-blob--pink {
  top: 1.5rem;
  left: -8rem;
  background: linear-gradient(135deg, rgba(252, 228, 236, 0.7), rgba(227, 242, 253, 0.7));
}

.contact-blob--green {
  right: -8rem;
  bottom: 1rem;
  background: linear-gradient(135deg, rgba(128, 249, 189, 0.24), rgba(255, 249, 196, 0.36));
}

:deep(.ui-label) {
  gap: 0.5rem;
  color: #1a1c1c;
  font-size: 0.95rem;
}

:deep(.ui-input),
:deep(.ui-textarea) {
  border-radius: 0.875rem;
  border-color: rgba(229, 189, 190, 0.65);
  background: rgba(243, 243, 244, 0.55);
  padding: 1rem 1.5rem;
  color: #1a1c1c;
}

:deep(.ui-input) {
  min-height: 3.5rem;
}

:deep(.ui-textarea) {
  min-height: 10rem;
  resize: none;
}

:deep(.ui-input::placeholder),
:deep(.ui-textarea::placeholder) {
  color: #8a8f98;
}

:deep(.ui-input:focus),
:deep(.ui-textarea:focus) {
  border-color: #ff385c;
  box-shadow: 0 0 0 3px rgba(255, 56, 92, 0.14);
}

@keyframes iconSpin {
  to {
    transform: rotate(360deg);
  }
}

@media (min-width: 768px) {
  .contact-layout {
    flex-direction: row;
    align-items: center;
  }

  .contact-copy {
    width: 41.666667%;
  }

  .contact-form-wrap {
    width: 58.333333%;
  }

  .contact-card {
    padding: 3rem;
  }

  .contact-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .contact-button {
    width: fit-content;
    min-width: 13rem;
  }
}

@media (max-width: 767px) {
  .contact-section {
    padding: 4.5rem 0;
  }

  .contact-heading,
  .contact-lead {
    max-width: 100%;
  }
}
</style>
