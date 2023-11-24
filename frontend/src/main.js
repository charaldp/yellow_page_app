import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import ContactsList from './components/ContactsList.vue'
import styles from 'jqwidgets-scripts/jqwidgets/styles/jqx.base.css';
const app = createApp(App)
app
  .component('ContactsList', ContactsList)
app.use(router)
app.use(styles)
app.mount('#app')
