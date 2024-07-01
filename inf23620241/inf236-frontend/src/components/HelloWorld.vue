<template>
  <div class="hello">
    <!-- Título del sistema -->
    <h2>Sistema de monitoreo de fallas en motores mineros</h2>
    
    <!-- Contenedor del formulario de inicio de sesión -->
    <div class="container">
      <!-- Formulario de inicio de sesión -->
      <form class="form" @submit.prevent="login">
        <div class="title">
          Por favor<br><span>Ingrese su rut y contraseña</span>
        </div>
        
        <!-- Campo de entrada para el RUT -->
        <input v-model="usuario.rut" type="text" placeholder="Rut en bdd" name="rut_en_bdd" class="input" required>
        
        <!-- Campo de entrada para la contraseña -->
        <input v-model="usuario.contrasena" type="password" placeholder="Contraseña en bdd" name="password_en_bdd" class="input" required>
        
        <!-- Botón de enviar para el formulario -->
        <button @click="login" class="button-confirm">Ingresar</button>
      </form>
    </div>
    
    <!-- Mensaje de error o éxito -->
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  data() {
    return {
      // Datos del usuario para el formulario de inicio de sesión
      usuario: {
        rut: '',
        contrasena: ''
      },
      // Mensaje de error o éxito
      msg: ''
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    async login() {
      try {
        // Realizar una solicitud POST a la API para el inicio de sesión
        const response = await axios.post('http://localhost:8000/api/sesion/', {
          rut: this.usuario.rut,
          contrasena: this.usuario.contrasena
        });

        // Guardar la respuesta en un mensaje (para depuración)
        this.message = JSON.stringify(response);

        // Verificar si el inicio de sesión fue exitoso
        if (response.data.success) {
          // Redirigir al usuario basado en su rol
          if (response.data.rol == 'mecanico') {
            this.$router.push('/vistaMecanico/' + response.data.id);
          } else {
            this.$router.push('/vistaJefeMotores/' + response.data.id); 
          }
        } else {
          // Mostrar mensaje de error si las credenciales son incorrectas
          this.msg = 'Usuario o contraseña incorrectos';
        }
      } catch (error) {
        // Mostrar mensaje de error si ocurre un error durante la solicitud
        this.msg = 'Usuario o contraseña incorrectos';
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
