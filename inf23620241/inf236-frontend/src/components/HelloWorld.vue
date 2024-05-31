<template>
  <div class="hello">
    <h2>Vista Home</h2>
    <div class="container">
      <form class="form" @submit.prevent="submitForm">
        <div class="title">Por favor<br><span>Ingrese su rol y contraseña</span></div>
        <input v-model="form.role" type="text" placeholder="Rol" name="role" class="input" required>
        <input v-model="form.password" type="password" placeholder="Contraseña" name="password" class="input" required>
        <button type="submit" class="button-confirm">Ingresar</button>
      </form>
      
    </div>
    <p>{{ msg }}</p> <!-- Para mostrar el mensaje de éxito o error -->
  </div>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  data() {
    return {
      form: {
        role: '',
        password: ''
      },
      msg: ''
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:8000/api/login/', this.form);
        if (response.data.success) {
          this.$router.push('/vistamecanico'); // Redirigir a la vista del mecánico
        } else {
          this.msg = 'Usuario o contraseña incorrectos';
        }
      } catch (error) {
        this.msg = 'Error al enviar el formulario';
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  display: flex; /* Configura el contenedor como un flex container */
  justify-content: center; /* Centra el contenido horizontalmente */
  height: 100%; /* Establece la altura del contenedor al 100% del viewport */
}

.content {
  /* Estilos para tu objeto o contenido */
  margin: 0px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

/*Formulario*/
.form {
  height: 400px;
  --input-focus: #2d8cf0;
  --font-color: #323232;
  --font-color-sub: #666;
  --bg-color: #fff;
  --main-color: #323232;
  padding: 20px;
  background: lightgrey;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: top;
  gap: 20px;
  border-radius: 5px;
  border: 2px solid var(--main-color);
  box-shadow: 4px 4px var(--main-color);
}

.title {
  color: var(--font-color);
  font-weight: 900;
  font-size: 20px;
  margin-bottom: 25px;
}

.title span {
  color: var(--font-color-sub);
  font-weight: 600;
  font-size: 17px;
}

.input {
  width: 250px;
  height: 40px;
  border-radius: 5px;
  border: 2px solid var(--main-color);
  background-color: var(--bg-color);
  box-shadow: 4px 4px var(--main-color);
  font-size: 15px;
  font-weight: 600;
  color: var(--font-color);
  padding: 5px 10px;
  outline: none;
}

.input::placeholder {
  color: var(--font-color-sub);
  opacity: 0.8;
}

.input:focus {
  border: 2px solid var(--input-focus);
}

.login-with {
  display: flex;
  gap: 20px;
}

.button-log {
  cursor: pointer;
  width: 40px;
  height: 40px;
  border-radius: 100%;
  border: 2px solid var(--main-color);
  background-color: var(--bg-color);
  box-shadow: 4px 4px var(--main-color);
  color: var(--font-color);
  font-size: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon {
  width: 24px;
  height: 24px;
  fill: var(--main-color);
}

.button-log:active, .button-confirm:active {
  box-shadow: 0px 0px var(--main-color);
  transform: translate(3px, 3px);
}

.button-confirm {
  margin: 50px auto 0 auto;
  width: 120px;
  height: 40px;
  border-radius: 5px;
  border: 2px solid var(--main-color);
  background-color: var(--bg-color);
  box-shadow: 4px 4px var(--main-color);
  font-size: 17px;
  font-weight: 600;
  color: var(--font-color);
  cursor: pointer;
}

/*Fin Formulario*/ 
</style>
