<template>
  <h2>Vista Mecánico</h2>
  <div class="containerGeneral">
    <div class="radio-inputs">
      <label class="radio">
        <input type="radio" name="radio" value="asign" v-model="selectedOption" />
        <span class="name">Asignaciones</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" value="report" v-model="selectedOption" />
        <span class="name">Ingresar Incidencia</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" value="search" v-model="selectedOption" />
        <span class="name">Ver Incidencias</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" value="todo" v-model="selectedOption" />
        <span class="name">Mis tareas</span>
      </label>
    </div>
  </div>


<!-- -------------------------------------------- Ver las asignaciones entre motores y camiones -->
<div v-if="selectedOption === 'asign'">
    <div class="containerGeneral">
      <section class="container">
        <header>Buscar las asignaciones de un motor o de un camión</header>
        <h3>¿Buscar por motor o por camión?</h3>
        <section class="container">
          <div class="radio-inputs">
            <label class="radio">
              <input type="radio" name="radio" value="asignByMotor" v-model="selectedOptionSearch" />
              <span class="name">Motor</span>
            </label>
            <label class="radio">
              <input type="radio" name="radio" value="asignByCamion" v-model="selectedOptionSearch" />
              <span class="name">Camión</span>
            </label>
          </div>
        </section>

        <div v-if="selectedOptionSearch === 'asignByMotor'">
          <div class="input-box">
            <label>Motor ID</label>
            <input v-model="asign.motor_id" required placeholder="Ingrese el identificador del motor" type="text">
          </div>
          <div>
          <button @click="getAsignByMotor">Buscar</button>
          </div>
        </div>

        <div v-else-if="selectedOptionSearch === 'asignByCamion'">
          <div class="input-box">
            <label>Camión ID</label>
            <input v-model="asign.camion_id" required placeholder="Ingrese el identificador del camión" type="text">
          </div>
          <div>
          <button @click="getAsignByCamion">Buscar</button>
          </div>
        </div>

        <table v-if="asignList.length">
          <thead>
            <tr>
              <th>Motor ID</th>
              <th>Camión ID</th>
              <th>Fecha asignación</th>
              <th>Fecha desasignación</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="asign in asignList" :key="asign.id">
              <td>{{ asign.motor_id }}</td>
              <td>{{ asign.camion_id }}</td>
              <td>{{ asign.asign_date }}</td>
              <td>{{ asign.unassign_date }}</td>
            </tr> 
          </tbody>
        </table>

        <div v-else>No hay asignaciones para este elemento</div>

        
<!--         
        <div>
          <label for="asign">Motor ID:</label>
          <input type="text" v-model="searchMotorId" id="searchMotorId">
        </div>
        
        <div>
          <button @click="getAllIncidents">Buscar</button>
        </div>
        
        <table v-if="incidentsList.length">
          <thead>
            <tr>
              <th>Motor ID</th>
              <th>Mechanic ID</th>
              <th>Incident Date</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Solved</th>
              <th>Problem Description</th>
              <th>Work To Do</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="incident in incidentsList" :key="incident.id">
              <td>{{ incident.motor_id }}</td>
              <td>{{ incident.mechanic_id }}</td>
              <td>{{ incident.incident_date }}</td>
              <td>{{ incident.start_date }}</td>
              <td>{{ incident.end_date }}</td>
              <td>{{ incident.solved ? 'Yes' : 'No' }}</td>
              <td>{{ incident.problem_description }}</td>
              <td>{{ incident.work_to_do }}</td>
            </tr> 
          </tbody>
        </table>
        <div v-else>Todavia no hay incidencias</div> -->
      </section>
    </div>
  </div>



<!-- -------------------------------------------- Ingresar una incidencia -->
  <div v-if="selectedOption === 'report'">
    <div class="containerGeneral">
      <section class="container">
        <header>Formulario de Incidencias</header>
        <form @submit.prevent="submitForm">
          <div class="input-box">
            <label>Identificador de Motor</label>
            <input v-model="form.motor_id" required placeholder="Ingrese el identificador del motor" type="text">
          </div>
          <div class="column">
            <div class="input-box">
              <label>Identificador Mecánico</label>
              <input v-model="form.mechanic_id" required placeholder="Ingrese su identificador" type="text">
            </div>
            <div class="input-box">
              <label>Fecha Incidencia</label>
              <input v-model="form.incident_date" required placeholder="Inserte Fecha" type="date">
            </div>
          </div>
          <div class="column">
            <div class="input-box">
              <label>Fecha Inicio Trabajo</label>
              <input v-model="form.start_date" required placeholder="Inserte Fecha" type="date">
            </div>
            <div class="input-box">
              <label>Fecha Fin Trabajo</label>
              <input v-model="form.end_date" required placeholder="Inserte Fecha" type="date">
            </div>
          </div>
          <div class="solution-box">
            <label>¿Solucionado?</label>
            <div class="radio-button-container">
              <div class="radio-button">
                <input v-model="form.solved" type="radio" class="radio-button__input" id="radio1" :value="true"
                  name="radio-group">
                <label class="radio-button__label" for="radio1">
                  <span class="radio-button__custom"></span>
                  Si
                </label>
              </div>
              <div class="radio-button">
                <input v-model="form.solved" type="radio" class="radio-button__input" id="radio2" :value="false"
                  name="radio-group">
                <label class="radio-button__label" for="radio2">
                  <span class="radio-button__custom"></span>
                  No
                </label>
              </div>
            </div>
          </div>
          <div class="input-box">
            <label>Descripción del problema</label>
            <textarea v-model="form.problem_description" required
              placeholder="Describa el/los problemas asociados a la incidencia"></textarea>
          </div>
          <div class="input-box">
            <label>Trabajo por realizar</label>
            <textarea v-model="form.work_to_do" required placeholder="Indique qué es lo que falta por hacer"></textarea>
          </div>
          <button type="submit">Submit</button>
        </form>
        <div v-if="responseData">
          <h3>Datos de la Respuesta:</h3>
          <pre>{{ responseData }}</pre>
        </div>
      </section>
    </div>
  </div>


<!-- -------------------------------------------- Ver las incidencias de un motor -->
  <div v-if="selectedOption === 'search'">
    <div class="containerGeneral">
      <section class="container">
        <header>Todas las incidencias</header>
        <div>
          <button @click="getAllIncidents">Buscar</button>
        </div>
        
        <table v-if="incidentsList.length">
          <thead>
            <tr>
              <th>Motor ID</th>
              <th>Mechanic ID</th>
              <th>Incident Date</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Solved</th>
              <th>Problem Description</th>
              <th>Work To Do</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="incident in incidentsList" :key="incident.id">
              <td>{{ incident.motor_id }}</td>
              <td>{{ incident.mechanic_id }}</td>
              <td>{{ incident.incident_date }}</td>
              <td>{{ incident.start_date }}</td>
              <td>{{ incident.end_date }}</td>
              <td>{{ incident.solved ? 'Yes' : 'No' }}</td>
              <td>{{ incident.problem_description }}</td>
              <td>{{ incident.work_to_do }}</td>
            </tr> 
          </tbody>
        </table>
        <div v-else>Todavia no hay incidencias</div>
      </section>
    </div>
  </div>





  <div v-if="selectedOption === 'search'">
    <div class="containerGeneral">
      <section class="container">
        <!--
        <div>
          <label for="searchMotorId">Motor ID:</label>
          <input type="text" v-model="searchMotorId" id="searchMotorId">
          <button @click="search">Buscar</button>
        </div>

        <table v-if="searchResults.length">
          <thead>
            <tr>
              <th>Motor ID</th>
              <th>Mechanic ID</th>
              <th>Incident Date</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Solved</th>
              <th>Problem Description</th>
              <th>Work To Do</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="incident in searchResults" :key="incident.id">
              <td>{{ incident.motor_id }}</td>
              <td>{{ incident.mechanic_id }}</td>
              <td>{{ incident.incident_date }}</td>
              <td>{{ incident.start_date }}</td>
              <td>{{ incident.end_date }}</td>
              <td>{{ incident.solved ? 'Yes' : 'No' }}</td>
              <td>{{ incident.problem_description }}</td>
              <td>{{ incident.work_to_do }}</td>
            </tr>
          </tbody>
        </table>
        <div v-else>No hay resultados</div>-->
      </section>
    </div>
  </div>





<!-- -------------------------------------------- Ver las incidencias asignadas al mecanico -->

<div v-if="selectedOption === 'todo'">
    <div class="containerGeneral">
      <section class="container">
        <!--
        <div>
          <label for="searchMotorId">Motor ID:</label>
          <input type="text" v-model="searchMotorId" id="searchMotorId">
          <button @click="search">Buscar</button>
        </div>

        <table v-if="searchResults.length">
          <thead>
            <tr>
              <th>Motor ID</th>
              <th>Mechanic ID</th>
              <th>Incident Date</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Solved</th>
              <th>Problem Description</th>
              <th>Work To Do</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="incident in searchResults" :key="incident.id">
              <td>{{ incident.motor_id }}</td>
              <td>{{ incident.mechanic_id }}</td>
              <td>{{ incident.incident_date }}</td>
              <td>{{ incident.start_date }}</td>
              <td>{{ incident.end_date }}</td>
              <td>{{ incident.solved ? 'Yes' : 'No' }}</td>
              <td>{{ incident.problem_description }}</td>
              <td>{{ incident.work_to_do }}</td>
            </tr>
          </tbody>
        </table>
        <div v-else>No hay resultados</div>-->
      </section>
    </div>
  </div>


  <div>
    <div class="containerGeneral">
      <section class="container">
        <div v-if="message" :class="{ 'success': isSuccess, 'error': !isSuccess }">
          {{ message }}
        </div>
      </section>
    </div>
  </div>


</template>








<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  name: 'App',
  setup() {
    return {
      selectedOption: ref('asign'),
      selectedOptionSearch: ref('asignByMotor')
    };
  },
  data() {
    return {
      asign: {
        motor_id: '',
        camion_id: ''
      },
      form: {
        motor_id: '',  // Cambia a motor_id
        mechanic_id: '',  // Cambia a mechanic_id
        incident_date: '',  // Cambia a incident_date
        start_date: '',
        end_date: '',
        solved: '',
        problem_description: '',
        work_to_do: ''
      },
      message: '',
      isSuccess: false,
      responseData: null,
      asignList: [],
      incidentsList: []
    };
  },
  methods: {
    async getAsignByMotor() {
      try {
        const response = await axios.get(`http://localhost:8000/api/asignaciones/?motor_id=${this.asign.motor_id}`);
        this.asignList = response.data;
        this.message = `Se encontraron ${this.asignList.length} resultados.`;
      } catch (error) {
        this.message = 'Error al buscar asignaciones.';
        this.isSuccess = false;
      }
    },
    async getAsignByCamion() {
      try {
        const response = await axios.get(`http://localhost:8000/api/asignaciones/?camion_id=${this.asign.camion_id}`);
        this.asignList = response.data;
        this.message = `Se encontraron ${this.asignList.length} resultados.`;
      } catch (error) {
        this.message = 'Error al buscar asignaciones.';
        this.isSuccess = false;
      }
    },
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:8000/api/incidents/', this.form);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.responseData = response.data;
        /*this.resetForm();*/
      } catch (error) {
        const formString = JSON.stringify(this.form, null, 2);
        const serializerErrors = error.response && error.response.data ? JSON.stringify(error.response.data, null, 2) : 'No se pudo obtener los errores del servidor.';
        this.message = `Error al enviar el formulario. Datos del formulario: ${formString}. Errores del servidor: ${serializerErrors}`;
        this.isSuccess = false;
      }
    },
    async getAllIncidents() {
      try {
        const response = await axios.get('http://localhost:8000/api/allincidents/');
        this.incidentsList = response.data;
        this.message = `Se encontraron ${this.incidentsList.length} resultados.`;
      } catch (error) {
        this.message = 'Error al obtener las incidencias.';
        this.isSuccess = false;
      }
    },
    async search() {
      try {
        const response = await axios.get(`http://localhost:8000/api/search/?motor_id=${this.searchMotorId}`);
        this.searchResults = response.data;
        this.message = `Se encontraron ${response.data.length} resultados.`;
      } catch (error) {
        this.message = 'Error al buscar incidentes.';
        this.isSuccess = false;
      }
    },
    resetForm() {
      this.form = {
        motor_id: '',  // Cambia de 'motorId' a 'motor_id'
        mechanic_id: '',  // Cambia de 'mechanicId' a 'mechanic_id'
        incident_date: '',  // Cambia de 'incidentDate' a 'incident_date'
        start_date: '',
        end_date: '',
        solved: '',
        problem_description: '',
        work_to_do: ''
      };
    }
  }
};
</script>



























<style scoped>
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
</style>