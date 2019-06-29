<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
body {
  background-color: #050505;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-size: 14pt;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #fafafada;
  
  max-width: 700pt;
  left: 0;
  right: 0;
  margin: 0 auto;
}
// #nav {
//   padding: 30px;
//   a {
//     font-weight: bold;
//     color: #2c3e50;
//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }
</style>
