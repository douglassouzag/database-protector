import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import firebase from 'firebase';

Vue.config.productionTip = false

// Iniciando Firebase
var config = {
  apiKey: "AIzaSyDgVWP1PohnIbz0_D5UI8cAqawM93-hEpg",
  authDomain: "database-protector.firebaseapp.com",
  databaseURL: "https://database-protector.firebaseio.com",
  projectId: "database-protector",
  storageBucket: "database-protector.appspot.com",
  messagingSenderId: "74653606919",
  appId: "1:74653606919:web:3d27a464e8ce2be99a36a2"
};
firebase.initializeApp(config);

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
