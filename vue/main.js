import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
//----------------------------------------------------------------
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import UIkit from 'uikit';
import Icons from 'uikit/dist/js/uikit-icons.min.js';
UIkit.use(Icons);
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPython} from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faPython)
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
createApp(App)
    .use(router)
    .component('fai', FontAwesomeIcon)
    .mount('#app')