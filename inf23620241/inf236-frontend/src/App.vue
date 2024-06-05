<template>
  <HelloWorld msg="Sistema de monitoreo de fallas en motores mineros"/>
  <p><strong>Current route path:</strong> {{ $route.fullPath }}</p>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <p> </p>
    <RouterLink to="/vistaMecanico/4">Vista Mecánico</RouterLink>
    <p> </p>
    <RouterLink to="/vistaJefemotores">Vista Jefe motores</RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
