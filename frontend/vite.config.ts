import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'


//Because Codespace runs in the cloud, the React page in your browser cant reach the API, this lets Vite forward API requests//

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/calculation': 'http://127.0.0.1:8000',
    },
  },
})
