<script setup>
</script>
//----------------------------------------------------------------
<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h3> Languages </h3>
    <FontAwesomeIcon icon="fa-python" class="language-icon"></FontAwesomeIcon>
    <h3>Frameworks</h3>
    <span uk-icon="uikit"></span>

    <h3> Projects </h3>
    <img src="../assets/Bluebox-SS2.jpg" alt="BlueBox" class="inline-image"/>
  </div>
</template>
//----------------------------------------------------------------
<style>
.about{
  flex-flow: column;
}
.language-icon{
  height: 2rem
}
.inline-image {
  width: 16rem;
  height: 10rem;
}
@media (max-width: 720px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>