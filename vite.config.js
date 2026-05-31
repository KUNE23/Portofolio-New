import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import viteImagemin from 'vite-plugin-imagemin'
import Critters from 'critters'
import { readFile, writeFile } from 'node:fs/promises'
import { resolve } from 'node:path'

const inlineCriticalCss = () => ({
  name: 'inline-critical-css',
  apply: 'build',
  async closeBundle() {
    const outDir = resolve(process.cwd(), 'dist')
    const indexPath = resolve(outDir, 'index.html')
    const html = await readFile(indexPath, 'utf8')
    const critters = new Critters({
      path: outDir,
      preload: 'swap',
      pruneSource: false,
    })

    await writeFile(indexPath, await critters.process(html))
  },
})

export default defineConfig(async ({ command, mode }) => {
  const visualizerPlugin = command === 'build' && mode !== 'production'
    ? (await import('rollup-plugin-visualizer')).visualizer({
      filename: './stats.html',
      open: true,
      gzipSize: true,
    })
    : null

  return {
    plugins: [
      vue(),
      viteImagemin({
        gifsicle: false,
        svgo: false,
        mozjpeg: {
          quality: 80,
          progressive: true,
        },
        pngquant: {
          quality: [0.7, 0.82],
          speed: 4,
          strip: true,
        },
        webp: {
          quality: 80,
          metadata: 'none',
        },
      }),
      inlineCriticalCss(),
      visualizerPlugin,
    ].filter(Boolean),
    server: {
      proxy: {
        '/api': 'http://127.0.0.1:8000'
      }
    },
    resolve: {
      alias: {
        '@': '/src'
      }
    }
  }
})
