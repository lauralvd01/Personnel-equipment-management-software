<template>
  <h2>Vista Jefe Motores</h2>
  <div class="posicionboton">
    <nav>
      <button @click="logout">
        <span class="button_top"> Cerrar Sesión
        </span>
        <br />
      </button>
    </nav>
    <RouterView />
  </div>
    <div class="containerGeneral">
    <div class="radio-inputs">
    <!--pestañistas de arriba -->
    <label class="radio">
      <input type="radio" name="radio" value="motor" v-model="selectedOption" />
      <span class="name">Crear Motor</span>
    </label>
    <label class="radio">
      <input type="radio" name="radio" value="camion" v-model="selectedOption" />
      <span class="name">Crear Camión</span>
    </label>
    <label class="radio">
      <input type="radio" name="radio" value="asign" v-model="selectedOption" />
      <span class="name">Manejo Asignaciones Motor</span>
    </label>

     <!--
    <label class="radio">
      <input type="radio" name="radio" value="asignincidencia" v-model="selectedOption" />
      <span class="name">Manejo Asignaciones Incidencia</span>
    </label>
    -->
    
    </div>
  </div>


  
  <!-- Formulario creación de motor -->
<div v-if="selectedOption === 'motor'">
  <div class="containerGeneral">
    <section class="container">
      <!-- Título del formulario -->
      <header>Formulario Creación de Motores </header>
      
      <!-- Formulario para crear un nuevo motor -->
      <form @submit.prevent="submitMotor">
        <div class="column">
          <div class="input-box">
            <!-- Campo para el número de serie del motor -->
            <label>Número de Serie Motor</label>
            <input v-model="motor.n_serie" required placeholder="Ingrese numero de serie" type="text">
          </div>
        </div>

        <!-- Etiqueta para el estado operativo del motor -->
        <label>¿Operativo?</label>
        <div class="column">
          <div class="radio-button-container">
            <div class="radio-button">
              <!-- Radio button para marcar el motor como operativo -->
              <input v-model="motor.operativo" type="radio" class="radio-button__input" id="radio1" value="true" name="radio-group">
              <label class="radio-button__label" for="radio1">
                <span class="radio-button__custom"></span>
                Si
              </label>
            </div>
            <div class="radio-button">
              <!-- Radio button para marcar el motor como no operativo -->
              <input v-model="motor.operativo" type="radio" class="radio-button__input" id="radio2" value="false" name="radio-group">
              <label class="radio-button__label" for="radio2">
                <span class="radio-button__custom"></span>
                No
              </label>
            </div>
          </div>
        </div>

        <div class="column">
          <div class="input-box">
            <!-- Campo para la fecha de llegada del motor -->
            <label>Fecha Llegada Motor</label>
            <input v-model="motor.fecha_inicio" required placeholder="(fecha)" type="date">
          </div>
        </div>
        
        <!-- Botón para enviar el formulario -->
        <button type="submit">Submit</button>
      </form>

      <!-- Mensaje de éxito o error al enviar el formulario -->
      <div v-if="message" :class="{'success': isSuccess, 'error': !isSuccess}">
        {{ message }}
      </div>

      <!-- Datos de la respuesta del servidor después de enviar el formulario -->
      <div v-if="responseData">
        <h3>Datos de la Respuesta:</h3>
        <pre>{{ responseData }}</pre>
      </div>
    </section>
  </div>
</div>

<!-- Formulario creación de camión -->
<div v-if="selectedOption === 'camion'">
  <div class="containerGeneral">
    <section class="container">
      <!-- Título del formulario -->
      <header>Formulario Creación de Camiones</header>
      
      <!-- Formulario para crear un nuevo camión -->
      <form @submit.prevent="submitCamion">
        <div class="column">
          <div class="input-box">
            <!-- Campo para el número de serie del camión -->
            <label>Número de Serie Camión</label>
            <input v-model="camion.n_serie" required placeholder="Ingrese numero de serie" type="text">
          </div>
          <div class="input-box">
            <!-- Campo para la patente del camión -->
            <label>Patente Camión</label>
            <input v-model="camion.placa" required placeholder="Ingrese patente" type="text">
          </div>
        </div>

        <!-- Etiqueta para el estado operativo del camión -->
        <label>¿Operativo?</label>
        <div class="column">
          <div class="radio-button-container">
            <div class="radio-button">
              <!-- Radio button para marcar el camión como operativo -->
              <input v-model="camion.estado" type="radio" class="radio-button__input" id="radio1" value="true" name="radio-group">
              <label class="radio-button__label" for="radio1">
                <span class="radio-button__custom"></span>
                Si
              </label>
            </div>
            <div class="radio-button">
              <!-- Radio button para marcar el camión como no operativo -->
              <input v-model="camion.estado" type="radio" class="radio-button__input" id="radio2" value="false" name="radio-group">
              <label class="radio-button__label" for="radio2">
                <span class="radio-button__custom"></span>
                No
              </label>
            </div>
          </div>
        </div>

        <div class="column">
          <div class="input-box">
            <!-- Campo para la fecha de llegada del camión -->
            <label>Fecha Llegada Camión</label>
            <input v-model="camion.fecha_inicio" required placeholder="(fecha)" type="date">
          </div>
        </div>
        
        <!-- Botón para enviar el formulario -->
        <button type="submit">Submit</button>
      </form>

      <!-- Mensaje de éxito o error al enviar el formulario -->
      <div v-if="message" :class="{'success': isSuccess, 'error': !isSuccess}">
        {{ message }}
      </div>

      <!-- Datos de la respuesta del servidor después de enviar el formulario -->
      <div v-if="responseData">
        <h3>Datos de la Respuesta:</h3>
        <pre>{{ responseData }}</pre>
      </div>
    </section>
  </div>
</div>

<!-- Formulario asignación motor a camión -->
  <div v-if="selectedOption === 'asign'">
    <div class="containerGeneral">
      <section class="container">
        <header>Formulario Asignación de Motores</header>
        <form @submit.prevent="asignMotor">
          <div class="column">
            <div class="input-box">
              <label>Camiones Disponibles: </label>
              <select v-model="asignacioncamionmotor.camion">
                <option v-for="camion in camiones" :key="camion.id_camion" :value="camion.id_camion">
                  {{ camion.placa }}
                </option>
              </select>
            </div>
            <div class="input-box">
              <label>Motores Disponibles: </label>
              <select v-model="asignacioncamionmotor.motor">
                <option v-for="motor in motores" :key="motor.id_motor" :value="motor.id_motor">
                  {{ motor.id_motor }}
                </option>
              </select>
            </div>
          </div>
          <button type="submit">Asignar Motor a Camión</button>
        </form>

        <form @submit.prevent="desasignMotor">
          <div class="column">
            <div class="input-box">
              <label>Camiones con Motor Asignados</label>
              <select v-model="desaginacionmotorcamion.id_aborrar">
                <option v-for="asignacioncamionmotor in asignacioncamionmotores" :key="asignacioncamionmotor.id_asignacion" :value="asignacioncamionmotor.camion">
                 {{ asignacioncamionmotor.motor }}
                </option>
              </select>
            </div>
          </div>
          <button type="submit">Borrar Asignación</button>
        </form>

        <div v-if="message" :class="{'success': isSuccess, 'error': !isSuccess}">
          {{ message }}
        </div>
        <div v-if="responseData">
          <h3>Datos de la Respuesta:</h3>
          <pre>{{ responseData }}</pre>
        </div>
      </section>
    </div>
  </div>

  <!-- 
  <div v-if="selectedOption === 'asignincidencia'">
    <div class="containerGeneral">
      <form @submit.prevent="searchAll">
        <section class="container">
          <div class="nav">
            <header>Todas las Incidencias</header>
          </div>
        
          <table>
            <thead>
              <tr>
                <th>ID Camión</th>
                <th>ID Motor</th>
                <th>Fecha de Incidencia</th>
                <th>Descripción del Problema</th>
                <th>Mecánicos Asociados</th>
                <th>Descripción del Trabajo Necesario</th>
                <th>Mecánico Asignado</th>
                <th>Fecha de Inicio del Trabajo</th>
                <th>Fecha de Término del Trabajo</th>
                <th>Solucionado</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="incidencia in incidentsList" :key="incidencia.id_incidencia">
                <td>{{ incidencia.camion_id }}</td>
                <td>{{ incidencia.motor_id }}</td>
                <td>{{ formatDate(incidencia.fecha_incidencia) }}</td>
                <td>{{ incidencia.descripcion_problema }}</td>
                <td>{{ incidencia.mecanicos_asociados }}</td>
                <td>{{ incidencia.descripcion_trabajo_necesario }}</td>
                <td>{{ incidencia.mecanico_asignado }}</td>
                <td>{{ formatDate(incidencia.fecha_inicio_trabajo) }}</td>
                <td>{{ formatDate(incidencia.fecha_termino_trabajo) }}</td>
                <td>{{ incidencia.solucionado ? 'Sí' : 'No' }}</td>
              </tr>
            </tbody>
          </table>  
        </section>
      </form>
    </div>
  </div>
  -->
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default{
  name: 'App',
  setup() {
    const router = useRouter();
    return {
      selectedOption: ref('motor'),
      router
    };
  },

          

  data() {
    return {
      motores: [],
      camiones: [],
      asignacioncamionmotores: [],
      incidentsList: [],
      desaginacionmotorcamion: {
        id_aborrar:'',
        fecha_desasignacion: null,
        motor:'',
        camion: ''
      },
      form: {
        motorId: '',
        mechanicId: '',
        incidentDate: '',
        startDate: '',
        endDate: '',
        solved: '',
        problemDescription: '',
        workToDo: ''
      },
      motor: {
        n_serie: '',
        operativo: null,
        fecha_inicio: '',
        tiempo_en_uso: 0, // Provide a default value for tiempo_en_uso
        durabilidad: 0 // Provide a default value for durabilidad
      },
      camion: {
        n_serie:'',
        placa: '',
        estado: '',
        fecha_inicio: '',
        durabilidad: 0
      },
      asignacioncamionmotor: {
        fecha_desasignacion: null,
        motor:'',
        camion: ''
      },
      message: '',
      isSuccess: false,
      responseData: null // Añadido para almacenar la respuesta
    };
  },
  methods: {
    // Método para enviar el formulario de incidentes
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:8000/api/incidents/', this.form);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.responseData = response.data; // Almacenar la respuesta en responseData
        this.resetForm();
      } catch (error) {
        this.message = 'Error al enviar el formulario.' + JSON.stringify(this.form);
        this.isSuccess = false;
        if (error.response) {
          this.message += ` Detalles del error: ${error.response.data}`;
        }
      }
    },

    // Método para enviar el formulario de motor
    async submitMotor() {
      try {
        const response = await axios.post('http://localhost:8000/api/motor/create', this.motor);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.responseData = response.data; // Almacenar la respuesta en responseData
        this.resetFormMotor();
      } catch (error) {
        this.message = 'Error al enviar el formulario.' + JSON.stringify(this.motor);
        this.isSuccess = false;
        if (error.response) {
          this.message += ` Detalles del error: ${error.response.data}`;
        }
      }
    },

    // Método para enviar el formulario de camión
    async submitCamion() {
      try {
        const response = await axios.post('http://localhost:8000/api/camion/create', this.camion);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.responseData = response.data; // Almacenar la respuesta en responseData
        this.resetFormCamion();
      } catch (error) {
        this.message = 'Error al enviar el formulario.' + JSON.stringify(this.camion);
        this.isSuccess = false;
        if (error.response) {
          this.message += ` Detalles del error: ${error.response.data}`;
        }
      }
    },

    // Método para obtener la lista de camiones
    async fetchCamiones() {
      try {
        const response = await axios.get('http://localhost:8000/api/camion/all');
        this.camiones = response.data;
      } catch (error) {
        console.error('Error fetching camiones:', error);
      }
    },

    // Método para obtener la lista de motores
    async fetchMotores() {
      try {
        const response = await axios.get('http://localhost:8000/api/motor/all');
        this.motores = response.data;
      } catch (error) {
        console.error('Error fetching motores:', error);
      }
    },

    // Método para obtener la lista de asignaciones de motores a camiones
    async fetchAsginacionMotores() {
      try {
        const response = await axios.get('http://localhost:8000/api/asignacion/all');
        this.asignacioncamionmotores = response.data;
        this.desaginacionmotorcamion = response.data;
      } catch (error) {
        console.error('Error fetching motores:', error);
      }
    },

    // Método para obtener la lista de incidentes
    async fetchIncidents() {
      try {
        const response = await axios.get('http://localhost:8000/api/incidents/all/');
        this.incidentsList = response.data;
      } catch (error) {
        console.error('Error fetching Incidents:', error);
      }
    },

    // Método para asignar un motor a un camión
    async asignMotor() {
      try {
        const response = await axios.post('http://localhost:8000/asignacion/', this.asignacioncamionmotor);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.responseData = response.data; // Almacenar la respuesta en responseData
        this.resetFormasignacioncamionmotor();
        this.fetchAsginacionMotores();
      } catch (error) {
        this.message = 'Error al enviar el formulario.' + JSON.stringify(this.asignacioncamionmotor);
        this.isSuccess = false;
        if (error.response) {
          this.message += ` Detalles del error: ${error.response.data}`;
        }
      }
    },

    // Método para desasignar un motor de un camión
    async desasignMotor() {
      try {
        const pathborrar = 'http://localhost:8000/asignacion/' + this.desaginacionmotorcamion.id_aborrar;
        this.message = pathborrar;
        const response = await axios.delete(pathborrar);
        this.message = 'Objeto borrado correctamente';
        this.isSuccess = true;
        this.responseData = response.data; // Almacenar la respuesta en responseData
        this.resetFormdesaginacionmotorcamion();
        this.fetchAsginacionMotores();
      } catch (error) {
        this.message = 'Error al enviar el formulario.' + JSON.stringify(this.asignacioncamionmotor);
        this.isSuccess = false;
        if (error.response) {
          this.message += ` Detalles del error: ${error.response.data}`;
        }
      }
    },

    // Método para restablecer el formulario de incidentes
    resetForm() {
      this.form = {
        motorId: '',
        mechanicId: '',
        incidentDate: '',
        startDate: '',
        endDate: '',
        solved: '',
        problemDescription: '',
        workToDo: ''
      };
    },

    // Método para restablecer el formulario de motor
    resetFormMotor() {
      this.motor = {
        n_serie: '',
        operativo: null,
        fecha_inicio: '',
        tiempo_en_uso: 0,
        durabilidad: 0
      };
    },

    // Método para restablecer el formulario de camión
    resetFormCamion() {
      this.camion = {
        n_serie: '',
        placa: '',
        estado: '',
        fecha_inicio: '',
        durabilidad: 0
      };
    },

    // Método para restablecer el formulario de asignación de motor a camión
    resetFormasignacioncamionmotor() {
      this.asignacioncamionmotor = {
        fecha_desasignacion: null,
        motor: '',
        camion: ''
      };
    },

    // Método para restablecer el formulario de desasignación de motor de camión
    resetFormdesaginacionmotorcamion() {
      this.asignacioncamionmotor = {
        id_aborrar: '',
        fecha_desasignacion: null,
        motor: '',
        camion: ''
      };
    },

    // Método para cerrar sesión
    async logout() {
      this.$router.push('/');
    }
  },
  mounted() {
    // Cargar datos iniciales al montar el componente
    this.fetchCamiones();
    this.fetchMotores();
    this.fetchAsginacionMotores();
    this.fetchIncidents();
  }
};
</script>




























<style scoped>
.posicionboton {
  position: relative;
  max-width: 1000px;
  /* Ajustado para permitir que el contenedor se expanda */
  width: 100%;
  padding-left: 25%;
  /*border-radius: 8px;*/
}

.button_top {
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

.radio-inputs .radio input:checked + .name {
  background-color: #FCEDDA;
  font-weight: 600;
}
.radio-inputs .radio input + .name:hover {
  color: #a3a3a3;
}
.radio-inputs .radio input:checked + .name:hover {
  color: #1d1d29;
}

.radio-inputs .radio input:checked + .name::after,
.radio-inputs .radio input:checked + .name::before {
  content: "";
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: #ffffff;
  bottom: 0;
}

.radio-inputs .radio input:checked + .name::after {
  right: -10px;
  border-bottom-left-radius: 300px;
  box-shadow: -3px 3px 0px 3px #FCEDDA;
}
.radio-inputs .radio input:checked + .name::before {
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
  height: auto; /* Ajustado para permitir que el contenedor se expanda */
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
  padding: 10px; /* Añadido padding */
  background: #FCEDDA;
  box-sizing: border-box; /* Incluido para asegurarse de que el padding no afecte el tamaño total */
}

.input-box input:focus,
.input-box textarea:focus {
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1);
}

.column {
  margin-top: 10px;
  display:flex;
  column-gap: 15px;
  justify-content: center;
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

.radio-button__input:checked + .radio-button__label .radio-button__custom {
  background-color: #4c8bf5;
  border-color: transparent;
  transform: scale(0.8);
  box-shadow: 0 0 20px #4c8bf580;
}

.radio-button__input:checked + .radio-button__label {
  color: #4c8bf5;
}

.radio-button__label:hover .radio-button__custom {
  transform: scale(1.2);
  border-color: #4c8bf5;
  box-shadow: 0 0 20px #4c8bf580;
}



</style>