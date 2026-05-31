const configuredApiUrl = import.meta.env.VITE_API_URL || ''
const API_BASE_URL =
  import.meta.env.PROD && /^https?:\/\/(127\.0\.0\.1|localhost)(:\d+)?/i.test(configuredApiUrl) ? '' : configuredApiUrl

function formatApiError(data) {
  if (!data) {
    return 'Request failed'
  }

  if (typeof data.detail === 'string') {
    return data.detail
  }

  if (Array.isArray(data.detail)) {
    return data.detail
      .map((item) => {
        const field = Array.isArray(item.loc) ? item.loc.filter((part) => part !== 'body').join('.') : ''
        return field ? `${field}: ${item.msg}` : item.msg
      })
      .join(', ')
  }

  if (data.detail && typeof data.detail === 'object') {
    return JSON.stringify(data.detail)
  }

  if (data.message) {
    return data.message
  }

  return 'Request failed'
}

async function request(path, options = {}) {
  let response
  const { headers = {}, ...fetchOptions } = options

  try {
    response = await fetch(`${API_BASE_URL}${path}`, {
      ...fetchOptions,
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
    })
  } catch (error) {
    const target = API_BASE_URL || 'same-origin /api'
    throw new Error(`Backend tidak bisa diakses di ${target}. Jalankan dulu: npm run dev:backend`)
  }

  if (response.status === 204) {
    return null
  }

  const data = await response.json().catch(() => null)

  if (!response.ok) {
    throw new Error(formatApiError(data))
  }

  return data
}

export function getProjects() {
  return request('/api/projects')
}

export function getSkills() {
  return request('/api/skills')
}

export function createContactMessage(payload) {
  return request('/api/contact/messages', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}

export function checkAdminToken(token) {
  return request('/api/admin/check-token', {
    method: 'POST',
    headers: {
      'X-Admin-Token': token.trim(),
    },
  })
}

export function getAdminProjects(token) {
  return request('/api/admin/projects', {
    headers: {
      'X-Admin-Token': token.trim(),
    },
  })
}

export function getAdminSkills(token) {
  return request('/api/admin/skills', {
    headers: {
      'X-Admin-Token': token.trim(),
    },
  })
}

export function getAdminContactMessages(token) {
  return request('/api/admin/contact-messages', {
    headers: {
      'X-Admin-Token': token.trim(),
    },
  })
}

export function createProject(token, payload) {
  return request('/api/admin/projects', {
    method: 'POST',
    headers: {
      'X-Admin-Token': token.trim(),
    },
    body: JSON.stringify(payload),
  })
}

export function updateProject(token, id, payload) {
  return request(`/api/admin/projects/${id}`, {
    method: 'PUT',
    headers: {
      'X-Admin-Token': token.trim(),
    },
    body: JSON.stringify(payload),
  })
}

export function deleteProject(token, id) {
  return request(`/api/admin/projects/${id}`, {
    method: 'DELETE',
    headers: {
      'X-Admin-Token': token.trim(),
    },
  })
}

export function createSkill(token, payload) {
  return request('/api/admin/skills', {
    method: 'POST',
    headers: {
      'X-Admin-Token': token.trim(),
    },
    body: JSON.stringify(payload),
  })
}

export function updateSkill(token, id, payload) {
  return request(`/api/admin/skills/${id}`, {
    method: 'PUT',
    headers: {
      'X-Admin-Token': token.trim(),
    },
    body: JSON.stringify(payload),
  })
}

export function deleteSkill(token, id) {
  return request(`/api/admin/skills/${id}`, {
    method: 'DELETE',
    headers: {
      'X-Admin-Token': token.trim(),
    },
  })
}
