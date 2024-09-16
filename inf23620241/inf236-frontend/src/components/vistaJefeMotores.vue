<template>
  <div>
    <h2>Vista Jefe Motores</h2>
    <div class="containerGeneral">
      <div class="radio-inputs">
        <label class="radio">
          <input type="radio" name="radio" value="html" v-model="selectedOption" />
          <span class="name">Asignar Motor a Camión</span>
        </label>
        <label class="radio">
          <input type="radio" name="radio" value="react" v-model="selectedOption" />
          <span class="name">Revisar Incidencias</span>
        </label>
        <label class="radio">
          <input type="radio" name="radio" value="vue" v-model="selectedOption" />
          <span class="name">Gráficos y Análisis</span>
        </label>
        <label class="radio">
          <input type="radio" name="radio" value="list" v-model="selectedOption" />
          <span class="name">Lista de Camiones</span>
        </label>
      </div>
    </div>

    <div v-if="selectedOption === 'html'">
      <div class="containerGeneral">
        <section class="container">
          <header>Formulario Asignación de Motores a Camiones</header>
          <form @submit.prevent="submitForm">
            <div class="input-box">
              <label>Identificador de Motor</label>
              <input v-model="form.motorId" required placeholder="Ingrese el identificador del motor" type="text">
            </div>
            <div class="column">
              <div class="input-box">
                <label>Identificador Mecánico</label>
                <input v-model="form.mechanicId" required placeholder="Ingrese su identificador" type="text">
              </div>
              <div class="input-box">
                <label>Fecha Incidencia</label>
                <input v-model="form.incidentDate" required placeholder="Inserte Fecha" type="date">
              </div>
            </div>
            <div class="column">
              <div class="input-box">
                <label>Fecha Inicio Trabajo</label>
                <input v-model="form.startDate" required placeholder="Inserte Fecha" type="date">
              </div>
              <div class="input-box">
                <label>Fecha Fin Trabajo</label>
                <input v-model="form.endDate" required placeholder="Inserte Fecha" type="date">
              </div>
            </div>
            <div class="solution-box">
              <label>¿Solucionado?</label>
              <div class="radio-button-container">
                <div class="radio-button">
                  <input v-model="form.solved" type="radio" class="radio-button__input" id="radio1" value="Si" name="radio-group">
                  <label class="radio-button__label" for="radio1">
                    <span class="radio-button__custom"></span>
                    Si
                  </label>
                </div>
                <div class="radio-button">
                  <input v-model="form.solved" type="radio" class="radio-button__input" id="radio2" value="No" name="radio-group">
                  <label class="radio-button__label" for="radio2">
                    <span class="radio-button__custom"></span>
                    No
                  </label>
                </div>
              </div>
            </div>
            <div class="input-box">
              <label>Descripción del problema</label>
              <textarea v-model="form.problemDescription" required placeholder="Describa el/los problemas asociados a la incidencia"></textarea>
            </div>
            <div class="input-box">
              <label>Trabajo por realizar</label>
              <textarea v-model="form.workToDo" required placeholder="Indique qué es lo que falta por hacer"></textarea>
            </div>
            <button type="submit">Submit</button>
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

    <div v-if="selectedOption === 'react'">
      <div class="containerGeneral">
        <section class="container">
          <!-- Contenido para "Revisar Incidencias" aquí -->
        </section>
      </div>
    </div>

    <div v-if="selectedOption === 'vue'">
      <div class="containerGeneral">
        <section class="container">
          <form>
            <label for="vue-name">Name:</label>
            <input type="text" id="vue-name" name="vue-name" />
            <button type="submit">Submit</button>
          </form>
        </section>
      </div>
    </div>
    <div v-if="selectedOption === 'list'">
      <div class="containerGeneral">
        <section class="container">
          <h3>Lista de Camiones</h3>
          <table>
            <thead>
              <tr>
                <th>ID Camión</th>
                <th>Número de Serie</th>
                <th>Placa</th>
                <th>Estado</th>
                <th>Fecha de Inicio</th>
                <th>Durabilidad</th>
                <th> Cambiar Estado</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="camion in camiones" :key="camion.id_camion">
                <td>{{ camion.id_camion }}</td>
                <td>{{ camion.n_serie }}</td>
                <td>{{ camion.placa }}</td>
                <td>{{ camion.estado }}</td>
                <td>{{ camion.fecha_inicio ? new Date(camion.fecha_inicio).toLocaleDateString() : 'No disponible' }}</td>
                <td>{{ camion.durabilidad || 'No disponible' }}</td>
                <td>
                  <label class="switch">
                    <input type="checkbox" :checked="camion.estado === 'Activo'" @change="updateCamion(camion)">
                    <span class="slider round"></span>
                  </label>
                </td>
              </tr>
            </tbody>
          </table>
        </section>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'VistaJefeMotores',
  setup() {
    const selectedOption = ref('html');
    const camiones = ref([]);
    const fetchCamiones = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/camiones/');
        camiones.value = response.data;
      } catch (error) {
        console.error('Error fetching camiones:', error);
      }
    };

    const updateCamion = async (camion) => {
      try {
        const updatedEstado = camion.estado === 'Activo' ? 'Inactivo' : 'Activo';
        await axios.patch(`http://localhost:8000/api/camiones/${camion.id_camion}/`, {
          estado: updatedEstado
        });
        camion.estado = updatedEstado;
      } catch (error) {
        console.error('Error updating camion:', error);
      }
    };

    onMounted(() => {
      fetchCamiones();
    });

    return {
      selectedOption,
      camiones,
      updateCamion
    };
    
  },
  data() {
    return {
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
      message: '',
      isSuccess: false,
      responseData: null 
    };
  },
  methods: {
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
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 34px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  border-radius: 50%;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:checked + .slider:before {
  transform: translateX(26px);
}

.round {
  border-radius: 34px;
}


</style>