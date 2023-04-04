<script setup>
import { RouterLink, RouterView } from 'vue-router'
/* import specific icons */
//----------------------------------------------------------------
</script>

<template>
  <header>
      <nav>
        <RouterLink to="/" uk-icon="home" class="nav-icon" />
        <h1 id="Logo"> Josh S Wilkinson </h1>
        <RouterLink to="/about" uk-icon="code" class="nav-icon" />
      </nav>
  </header>
  <RouterView id="main-body" />
</template>


<style>
@import '@/assets/base.css';
#app {
  width: 100vw;
  height: 100vh;
  margin: 0;
  flex-flow: column;
  justify-content: center;
}
header {
  height: 4rem;
  width: 100vw;
  flex-flow: row;
  align-items: center;
  justify-content: center;
}
a,
.green {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.4s;
}
@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}
nav {
  width: 100%;
  height: 4rem;
  flex-flow: row;
  font-size: 16px;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}
#Logo { 
  width: 15rem;
  align-items: center;
  justify-content: center;
}
.nav-icon {
  width: 4rem;
  height: 4rem;
  font-size: 2rem;
  align-items: center;
  justify-content: center;
}
#main-body{
  height: 95%;
  width: 100%;
}
@media (max-width: 720px) {
  body {
    display: flex;
    place-items: center;
  }
  #app {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  }
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
  .logo {
    margin: 0 2rem 0 0;
  }
  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;
    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>