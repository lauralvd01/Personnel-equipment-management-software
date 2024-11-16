<template>
  <div>
    <h2>Vista Conductor</h2>
    <div class="posicionboton">
      <nav>
        <button @click="logout">
          <span class="button_top">Cerrar Sesión</span>
        </button>
      </nav>
      <RouterView />
    </div>
    <div class="containerGeneral">
      <div class="radio-inputs">
        <label class="radio">
          <input type="radio" name="radio" value="report" v-model="selectedOption" />
          <span class="name">Ingresar Antecedentes</span>
        </label>
        <label class="radio">
          <input type="radio" name="radio" value="search" v-model="selectedOption" />
          <span class="name">Ver Mis Antecedentes</span>
        </label>
        <label class="radio">
          <input type="radio" name="radio" value="settings" v-model="selectedOption" />
          <span class="name">Cambiar mi contraseña</span>
        </label>
      </div>
    </div>

    <!-- -------------------------Ingresar antecedente-------------------------------->
    <div v-if="selectedOption === 'report'">
      <div class="containerGeneral">
        <section class="container">
          <header>Formulario de informe de un antecedente</header>
          <form @submit.prevent="submitForm">
            <div class="column">
              <div class="input-box">
                <label>Patente del Camión</label>
                <input v-model="report.patente" required placeholder="Ingrese la patente del camión" type="text" />
              </div>
              <!-- <div class="input-box">
                <label>ID del Usuario</label>
                <input v-model="report.user_id" required placeholder="Ingrese su ID de usuario" type="text" />
              </div> -->
              <div class="input-box">
                <label>Fecha del antecedente</label>
                <input v-model="report.record_date" required placeholder="Inserte Fecha" type="date" />
              </div>
            </div>
            <div class="input-box">
              <label>Descripción del problema</label>
              <textarea v-model="report.problem_description" required placeholder="Describa el/los problemas asociados a la incidencia"></textarea>
            </div>
            <button type="submit">Ingresar</button>
          </form>

          <!-- Mensajes de éxito o error -->
          <div v-if="message">
            <p :class="isSuccess ? 'success' : 'error'">{{ message }}</p>
          </div>

          <!-- Tabla de respuesta -->
          <div v-if="response_report">
            <h3>Antecedente creado :</h3>
            <table>
              <thead>
                <tr>
                  <th>Patente</th>
                  <th>ID de Usuario</th>
                  <th>Fecha de antecedente</th>
                  <th>Descripción del problema</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{ response_report.patente }}</td>
                  <td>{{ response_report.user_id }}</td>
                  <td>{{ response_report.record_date }}</td>
                  <td>{{ response_report.problem_description }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </div>
    </div>
    <!---------  Historial de incidencias del usuario ------------->
    <div v-if="selectedOption === 'search'">
      <div class = 'containerGeneral'>
        <section class="container">
            <header>Historial de antecedentes</header>
            <div v-if="historial.length > 0">
              <table>
                <thead>
                  <tr>
                    <th>Patente</th>
                    <th>Fecha de antecedente</th>
                    <th>Descripción del problema</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="record in historial" :key="record.id">
                    <td>{{ record.patente}}</td>
                    <td>{{ record.record_date }}</td>
                    <td>{{ record.problem_description }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p v-else> No hay antecedentes disponibles.</p>
        </section>

      </div>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  name: 'vistaConductores',
  setup() {
    const router = useRouter();
    return {
      selectedOption: ref('report'),
      router,
    };
  },
  data() {
    return {
      response_report: null,
      historial: [],
      report: {
        patente: '', // Nuevo campo para patente del camión
        problem_description: '',
        record_date: '',
      },
      message: '',
      isSuccess: false, // Variable para el estado del mensaje de éxito o error
    };
  },
  watch: {
        selectedOption(newOption) {
          if (newOption === 'search') {
          this.fetchRecords();
        }
      }
    },
  methods: {
    async submitReport() {
      try {
        const response = await axios.post('http://localhost:8000/antecedente/', this.report);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.response_report = response.data;
      } catch (error) {
        const reportString = JSON.stringify(this.report, null, 2);
        const serializerErrors =
          error.response && error.response.data
            ? JSON.stringify(error.response.data, null, 2)
            : 'No se pudo obtener los errores del servidor.';
        this.message = `Error al enviar el formulario. Datos del formulario: ${reportString}. Errores del servidor: ${serializerErrors}`;
        this.isSuccess = false;
      }
    },
    async fetchRecords() {
      try {
        const response = await axios.get('api/antecedentes/{user_id>}');
        if (response.ok) {                            
          this.historial = await response.data;
        } else {
          this.message = 'Error al obtener historial de antecedentes';
        }
      } catch (error) {
        this.message = 'Error en la conexión con el servidor';
      }
    },
  }
};
</script>

<style scoped>
.posicionboton{
  position: relative;
  max-width: 1000px;
  /* Ajustado para permitir que el contenedor se expanda */
  width: 100%;
  padding-left: 25%;
  /*border-radius: 8px;*/
}
.button_top{
  max-width: 100px;
  margin-left: 0px;
}
.radio-inputs {
  position: relative;
  display: flex;
  border-radius: 0.5rem;
  background-color: #ffffff;
  box-sizing: border-box;
  font-size: 17px;
  max-width: 1050px;
  width: 100%;
  padding: 1rem 1rem 0 1rem;
}

.radio-inputs .radio input {
  display: none;
}

.radio-inputs .radio .name {
  display: flex;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
  border: none;
  padding: 0.5rem 0.8rem;
  transition: all 0.15s ease-in-out;
  position: relative;
}

.radio-inputs .radio input:checked+.name {
  background-color: #FCEDDA;
  font-weight: 600;
}

.radio-inputs .radio input+.name:hover {
  color: #a3a3a3;
}

.radio-inputs .radio input:checked+.name:hover {
  color: #1d1d29;
}

.radio-inputs .radio input:checked+.name::after,
.radio-inputs .radio input:checked+.name::before {
  content: "";
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: #ffffff;
  bottom: 0;
}

.radio-inputs .radio input:checked+.name::after {
  right: -10px;
  border-bottom-left-radius: 300px;
  box-shadow: -3px 3px 0px 3px #FCEDDA;
}

.radio-inputs .radio input:checked+.name::before {
  left: -10px;
  border-bottom-right-radius: 300px;
  box-shadow: 3px 3px 0px 3px #FCEDDA;
}



/* Formulario Mecanicos */

.success {
  color: green;
}

.error {
  color: red;
}

.containerGeneral {
  display: flex;
  justify-content: center;
  height: 100%;
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

.container {
  position: relative;
  max-width: 1000px;
  height: auto;
  /* Ajustado para permitir que el contenedor se expanda */
  width: 100%;
  background: #FCEDDA;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

.container header {
  font-size: 1.2rem;
  color: #000;
  font-weight: 600;
  text-align: center;
}

.form .input-box {
  width: 100%;
  margin-top: 10px;
}

.input-box label {
  color: #000;
}

.input-box input,
.input-box textarea {
  width: 100%;
  outline: none;
  font-size: 1rem;
  color: #585858;
  margin-top: 5px;
  border: 1px solid #EE4E34;
  border-radius: 6px;
  padding: 10px;
  /* Añadido padding */
  background: #FCEDDA;
  box-sizing: border-box;
  /* Incluido para asegurarse de que el padding no afecte el tamaño total */
}

.input-box input:focus,
.input-box textarea:focus {
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1);
}

.column {
  margin-top: 10px;
  display: flex;
  column-gap: 15px;
  justify-content: center;
  width: 100%;
}

.nav {
  margin-top: 10px;
  display: flex;
  column-gap: 15px;
  justify-content: space-between;
  width: 100%;
}

.solution-box {
  margin-top: 10px;
}

.solution-option,
.solution {
  display: flex;
  justify-content: center;
  align-items: center;
  column-gap: 50px;
  flex-wrap: wrap;
}

.gender {
  column-gap: 5px;
}

.gender input {
  accent-color: #EE4E34;
}

.gender input,
.gender label {
  cursor: pointer;
}

.gender label {
  color: #000;
}

.address input,
.address .select-box {
  margin-top: 10px;
}

.select-box select {
  height: 100%;
  width: 100%;
  outline: none;
  border: none;
  color: #808080;
  font-size: 1rem;
  background: #FCEDDA;
}

button {
  height: 40px;
  width: 100%;
  color: #000;
  font-size: 1rem;
  font-weight: 400;
  margin-top: 15px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  background: #EE4E34;
}

button:hover {
  background: #EE3E34;
}

/* Estilo de los campos Togle */
.radio-button-container {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
}

.radio-button {
  display: inline-block;
  position: relative;
  cursor: pointer;
}

.radio-button__input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.radio-button__label {
  display: inline-block;
  padding-left: 30px;
  margin-bottom: 10px;
  position: relative;
  font-size: 15px;
  color: #181717;
  font-weight: 600;
  cursor: pointer;
  text-transform: uppercase;
  transition: all 0.3s ease;
}

.radio-button__custom {
  position: absolute;
  top: 0;
  left: 0;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid #555;
  transition: all 0.3s ease;
}

.radio-button__input:checked+.radio-button__label .radio-button__custom {
  background-color: #4c8bf5;
  border-color: transparent;
  transform: scale(0.8);
  box-shadow: 0 0 20px #4c8bf580;
}

.radio-button__input:checked+.radio-button__label {
  color: #4c8bf5;
}

.radio-button__label:hover .radio-button__custom {
  transform: scale(1.2);
  border-color: #4c8bf5;
  box-shadow: 0 0 20px #4c8bf580;
}

table {
  width: 100%;
  border-collapse: collapse;
}

table th, table td {
  border: 2px solid #555;
  padding: 10px;
}

table th {
  background-color: #f2f2f2;
  text-align: left;
}
</style>