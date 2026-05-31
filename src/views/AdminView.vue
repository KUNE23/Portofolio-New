<template>
  <main class="admin-page">
    <div v-if="!isAuthed" class="auth-shell">
      <Card class="login-card">
        <CardHeader>
          <p class="eyebrow">Admin Access</p>
          <CardTitle>Portfolio Dashboard</CardTitle>
          <CardDescription>Masukkan admin token untuk mengelola Projects dan Skills dari database production.</CardDescription>
        </CardHeader>
        <CardContent>
          <form class="form-stack" @submit.prevent="login">
            <Label>
              Admin Token
              <Input v-model="tokenInput" type="password" placeholder="Paste ADMIN_TOKEN" autocomplete="current-password" />
            </Label>
            <Button type="submit">Masuk Dashboard</Button>
            <p v-if="error" class="error-text">{{ error }}</p>
          </form>
        </CardContent>
      </Card>
    </div>

    <section v-else class="dashboard-shell">
      <aside class="sidebar">
        <div class="brand-block">
          <div class="brand-mark">AS</div>
          <div>
            <p class="brand-title">Alfiansyah</p>
            <p class="brand-subtitle">Portfolio CMS</p>
          </div>
        </div>

        <nav class="sidebar-nav" aria-label="Admin navigation">
          <button :class="{ active: activeTab === 'projects' }" type="button" @click="activeTab = 'projects'">
            <span>Projects</span>
            <Badge>{{ projects.length }}</Badge>
          </button>
          <button :class="{ active: activeTab === 'skills' }" type="button" @click="activeTab = 'skills'">
            <span>Skills</span>
            <Badge>{{ skills.length }}</Badge>
          </button>
          <button :class="{ active: activeTab === 'messages' }" type="button" @click="activeTab = 'messages'">
            <span>Messages</span>
            <Badge>{{ contactMessages.length }}</Badge>
          </button>
        </nav>

        <Card class="sidebar-card">
          <CardContent>
            <p class="eyebrow">Environment</p>
            <p class="sidebar-card-title">Vercel + Supabase</p>
            <p class="muted">API aktif di domain production.</p>
          </CardContent>
        </Card>
      </aside>

      <div class="dashboard-main">
        <header class="dashboard-header">
          <div>
            <p class="eyebrow">Dashboard</p>
            <h1>Portfolio Content</h1>
            <p class="muted">Kelola konten portfolio tanpa mengubah source code.</p>
          </div>
          <Button variant="outline" type="button" @click="logout">Logout</Button>
        </header>

        <section class="stats-grid" aria-label="Content overview">
          <Card>
            <CardContent class="stat-card">
              <span class="stat-label">Total Projects</span>
              <strong>{{ projects.length }}</strong>
              <span class="muted">{{ publishedProjects }} published</span>
            </CardContent>
          </Card>
          <Card>
            <CardContent class="stat-card">
              <span class="stat-label">Total Skills</span>
              <strong>{{ skills.length }}</strong>
              <span class="muted">{{ activeSkills }} active</span>
            </CardContent>
          </Card>
          <Card>
            <CardContent class="stat-card">
              <span class="stat-label">Admin Token</span>
              <strong>Protected</strong>
              <span class="muted">Header based auth</span>
            </CardContent>
          </Card>
          <Card>
            <CardContent class="stat-card">
              <span class="stat-label">Inbox</span>
              <strong>{{ contactMessages.length }}</strong>
              <span class="muted">pesan masuk</span>
            </CardContent>
          </Card>
        </section>

        <div class="tabs-panel">
          <button :class="{ active: activeTab === 'projects' }" type="button" @click="activeTab = 'projects'">Projects</button>
          <button :class="{ active: activeTab === 'skills' }" type="button" @click="activeTab = 'skills'">Skills</button>
          <button :class="{ active: activeTab === 'messages' }" type="button" @click="activeTab = 'messages'">Messages</button>
        </div>

        <div v-if="activeTab === 'projects'" class="content-grid">
          <Card>
            <CardHeader>
              <CardTitle>{{ projectForm.id ? 'Edit Project' : 'Tambah Project' }}</CardTitle>
              <CardDescription>Isi detail project yang akan tampil di halaman portfolio.</CardDescription>
            </CardHeader>
            <CardContent>
              <form class="form-stack" @submit.prevent="saveProject">
                <Label>Title <Input v-model="projectForm.title" required maxlength="140" /></Label>
                <Label>Category <Input v-model="projectForm.category" required maxlength="80" /></Label>
                <Label>Description <Textarea v-model="projectForm.description" required maxlength="600" /></Label>
                <Label>Image URL <Input v-model="projectForm.image_url" required type="url" /></Label>
                <Label>Technologies <Input v-model="projectTechInput" placeholder="Vue.js, Laravel, PostgreSQL" /></Label>
                <Label>Case Study URL <Input v-model="projectForm.case_study_url" type="url" /></Label>
                <Label>Live URL <Input v-model="projectForm.live_url" type="url" /></Label>
                <Label>Sort Order <Input v-model="projectForm.sort_order" min="0" max="9999" type="number" /></Label>
                <div class="switch-row">
                  <Switch v-model:checked="projectForm.is_featured" />
                  <span>Tampilkan di portfolio</span>
                </div>
                <div class="button-row">
                  <Button type="submit">Simpan Project</Button>
                  <Button variant="outline" type="button" @click="resetProjectForm">Reset</Button>
                </div>
              </form>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Project Records</CardTitle>
              <CardDescription>Daftar project yang tersimpan di Supabase.</CardDescription>
            </CardHeader>
            <CardContent>
              <div class="table-list">
                <article v-for="project in projects" :key="project.id" class="table-row">
                  <div class="row-main">
                    <div class="item-head">
                      <Badge>{{ project.category }}</Badge>
                      <Badge :variant="project.is_featured ? 'secondary' : 'destructive'">
                        {{ project.is_featured ? 'Published' : 'Hidden' }}
                      </Badge>
                    </div>
                    <h3>{{ project.title }}</h3>
                    <p class="muted">{{ project.description }}</p>
                    <div class="chip-row">
                      <Badge v-for="tech in project.technologies" :key="tech">{{ tech }}</Badge>
                    </div>
                  </div>
                  <div class="row-actions">
                    <Button variant="outline" type="button" @click="editProject(project)">Edit</Button>
                    <Button variant="destructive" type="button" @click="removeProject(project.id)">Hapus</Button>
                  </div>
                </article>
              </div>
            </CardContent>
          </Card>
        </div>

        <div v-else-if="activeTab === 'skills'" class="content-grid">
          <Card>
            <CardHeader>
              <CardTitle>{{ skillForm.id ? 'Edit Skill' : 'Tambah Skill' }}</CardTitle>
              <CardDescription>Gunakan URL logo SVG/PNG agar carousel skill tetap ringan.</CardDescription>
            </CardHeader>
            <CardContent>
              <form class="form-stack" @submit.prevent="saveSkill">
                <Label>Name <Input v-model="skillForm.name" required maxlength="80" /></Label>
                <Label>Logo URL <Input v-model="skillForm.logo_url" required type="url" /></Label>
                <Label>Sort Order <Input v-model="skillForm.sort_order" min="0" max="9999" type="number" /></Label>
                <div class="switch-row">
                  <Switch v-model:checked="skillForm.is_active" />
                  <span>Tampilkan di portfolio</span>
                </div>
                <div class="button-row">
                  <Button type="submit">Simpan Skill</Button>
                  <Button variant="outline" type="button" @click="resetSkillForm">Reset</Button>
                </div>
              </form>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Skill Records</CardTitle>
              <CardDescription>Logo dan urutan skill untuk carousel portfolio.</CardDescription>
            </CardHeader>
            <CardContent>
              <div class="table-list">
                <article v-for="skill in skills" :key="skill.id" class="table-row skill-row">
                  <img :src="skill.logo_url" :alt="`${skill.name} logo`" />
                  <div class="row-main">
                    <h3>{{ skill.name }}</h3>
                    <p class="muted">Order {{ skill.sort_order }}</p>
                  </div>
                  <Badge :variant="skill.is_active ? 'secondary' : 'destructive'">
                    {{ skill.is_active ? 'Active' : 'Hidden' }}
                  </Badge>
                  <div class="row-actions">
                    <Button variant="outline" type="button" @click="editSkill(skill)">Edit</Button>
                    <Button variant="destructive" type="button" @click="removeSkill(skill.id)">Hapus</Button>
                  </div>
                </article>
              </div>
            </CardContent>
          </Card>
        </div>

        <div v-else class="content-grid">
          <Card>
            <CardHeader>
              <CardTitle>Contact Messages</CardTitle>
              <CardDescription>Pesan yang dikirim dari form kontak website.</CardDescription>
            </CardHeader>
            <CardContent>
              <div v-if="contactMessages.length" class="table-list">
                <article v-for="message in contactMessages" :key="message.id" class="table-row message-row">
                  <div class="row-main">
                    <div class="item-head">
                      <Badge>{{ formatMessageDate(message.created_at) }}</Badge>
                    </div>
                    <h3>{{ message.name }}</h3>
                    <p class="muted">{{ message.email }}</p>
                    <p class="message-body">{{ message.message }}</p>
                  </div>
                </article>
              </div>
              <p v-else class="muted">Belum ada pesan masuk.</p>
            </CardContent>
          </Card>
        </div>

        <p v-if="error" class="error-text">{{ error }}</p>
        <p v-if="notice" class="notice-text">{{ notice }}</p>
      </div>
    </section>
  </main>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Switch } from '@/components/ui/switch'
import { Textarea } from '@/components/ui/textarea'
import { defaultProjects, defaultSkills } from '@/data/defaultContent'
import {
  checkAdminToken,
  getAdminContactMessages,
  createProject,
  createSkill,
  deleteProject,
  deleteSkill,
  getAdminProjects,
  getAdminSkills,
  updateProject,
  updateSkill,
} from '@/services/api'

const tokenInput = ref('')
const adminToken = ref(localStorage.getItem('adminToken') || '')
const isAuthed = ref(false)
const activeTab = ref('projects')
const error = ref('')
const notice = ref('')
const projects = ref([])
const skills = ref([])
const contactMessages = ref([])
const projectTechInput = ref('')

const publishedProjects = computed(() => projects.value.filter((project) => project.is_featured).length)
const activeSkills = computed(() => skills.value.filter((skill) => skill.is_active).length)

const emptyProject = () => ({
  id: '',
  title: '',
  category: '',
  description: '',
  image_url: '',
  technologies: [],
  case_study_url: '',
  live_url: '',
  sort_order: 0,
  is_featured: true,
})

const emptySkill = () => ({
  id: '',
  name: '',
  logo_url: '',
  sort_order: 0,
  is_active: true,
})

const projectForm = reactive(emptyProject())
const skillForm = reactive(emptySkill())

function assignForm(target, source) {
  Object.keys(target).forEach((key) => {
    target[key] = source[key]
  })
}

function setMessage(message) {
  notice.value = message
  window.setTimeout(() => {
    notice.value = ''
  }, 2400)
}

async function loadData() {
  const [projectData, skillData, messageData] = await Promise.all([
    getAdminProjects(adminToken.value),
    getAdminSkills(adminToken.value),
    getAdminContactMessages(adminToken.value),
  ])

  projects.value = projectData
  skills.value = skillData
  contactMessages.value = messageData
}

async function login() {
  error.value = ''
  const cleanedToken = tokenInput.value.trim()

  try {
    await checkAdminToken(cleanedToken)
    adminToken.value = cleanedToken
    localStorage.setItem('adminToken', cleanedToken)
    isAuthed.value = true
    await loadData()
  } catch (err) {
    error.value = err.message
  }
}

function logout() {
  localStorage.removeItem('adminToken')
  adminToken.value = ''
  tokenInput.value = ''
  isAuthed.value = false
  contactMessages.value = []
}

function resetProjectForm() {
  assignForm(projectForm, emptyProject())
  projectTechInput.value = ''
}

function resetSkillForm() {
  assignForm(skillForm, emptySkill())
}

function cleanUrl(value) {
  const cleaned = value?.trim()
  return cleaned || undefined
}

function formatMessageDate(value) {
  return new Intl.DateTimeFormat('id-ID', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(new Date(value))
}

async function saveProject() {
  error.value = ''
  const payload = {
    ...projectForm,
    sort_order: Number(projectForm.sort_order) || 0,
    technologies: projectTechInput.value.split(',').map((item) => item.trim()).filter(Boolean),
  }
  payload.case_study_url = cleanUrl(projectForm.case_study_url)
  payload.live_url = cleanUrl(projectForm.live_url)
  delete payload.id

  try {
    if (projectForm.id) {
      await updateProject(adminToken.value, projectForm.id, payload)
    } else {
      await createProject(adminToken.value, payload)
    }
    resetProjectForm()
    await loadData()
    setMessage('Project tersimpan.')
  } catch (err) {
    error.value = err.message
  }
}

function editProject(project) {
  assignForm(projectForm, {
    ...project,
    case_study_url: project.case_study_url || '',
    live_url: project.live_url || '',
  })
  projectTechInput.value = project.technologies.join(', ')
}

async function removeProject(id) {
  error.value = ''
  try {
    await deleteProject(adminToken.value, id)
    await loadData()
    setMessage('Project dihapus.')
  } catch (err) {
    error.value = err.message
  }
}

async function saveSkill() {
  error.value = ''
  const payload = {
    ...skillForm,
    sort_order: Number(skillForm.sort_order) || 0,
  }
  delete payload.id

  try {
    if (skillForm.id) {
      await updateSkill(adminToken.value, skillForm.id, payload)
    } else {
      await createSkill(adminToken.value, payload)
    }
    resetSkillForm()
    await loadData()
    setMessage('Skill tersimpan.')
  } catch (err) {
    error.value = err.message
  }
}

function editSkill(skill) {
  assignForm(skillForm, skill)
}

async function removeSkill(id) {
  error.value = ''
  try {
    await deleteSkill(adminToken.value, id)
    await loadData()
    setMessage('Skill dihapus.')
  } catch (err) {
    error.value = err.message
  }
}

onMounted(async () => {
  projects.value = defaultProjects
  skills.value = defaultSkills

  if (!adminToken.value) {
    return
  }

  try {
    await checkAdminToken(adminToken.value)
    isAuthed.value = true
    await loadData()
  } catch {
    localStorage.removeItem('adminToken')
  }
})
</script>
