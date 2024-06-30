<template>
    <h2>Vista Jefe Motores</h2>
    <div class="containerGeneral">
    <div class="radio-inputs">
    <!--pestañistas de arriba -->
    <label class="radio">
      <input type="radio" name="radio" value="motor" v-model="selectedOption" />
      <span class="name">Crear Motor</span>
    </label>
    <label class="radio">
      <input type="radio" name="radio" value="camion" v-model="selectedOption" />
      <span class="name">Crear Camion</span>
    </label>
    <label class="radio">
      <input type="radio" name="radio" value="asign" v-model="selectedOption" />
      <span class="name">Asignar Motor a Camion</span>
    </label>
    </div>
  </div>


  
  <!-- -------------------------------------------- Ver las asignaciones entre motores y camiones (Ya mudado a BBDD)-->
  <div v-if="selectedOption === 'motor'">
    <div class="containerGeneral">
        <section class="container">
          <header>Formulario Creación de Motores </header>
          <form @submit.prevent="submitMotor">
            <div class="column">
              <div class="input-box">
                <label>Numero de Serie Motor</label>
                <input v-model="motor.n_serie" required placeholder="Ingrese numero de serie" type="text">
              </div>
            </div>
            <label>¿Operativo?</label>
            <div class="column">
                <div class="radio-button-container">
                <div class="radio-button">
                  <input v-model="motor.operativo" type="radio" class="radio-button__input" id="radio1" value="true" name="radio-group">
                  <label class="radio-button__label" for="radio1">
                    <span class="radio-button__custom"></span>
                    Si
                  </label>
                </div>
                <div class="radio-button">
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
                <label>Fecha Llegada Motor</label>
                <input v-model="motor.fecha_inicio" required placeholder="(fecha)" type="date">
              </div>
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

<!-- -------------------------------------------- Ver las asignaciones entre motores y camiones (Ya mudado a BBDD)-->
    
  <div v-if="selectedOption === 'camion'">
    <div class="containerGeneral">
      <section class="container">
        <header>Formulario Creación de Camiones </header>
        <form @submit.prevent="submitCamion">
          <div class="column">
            <div class="input-box">
              <label>Numero de Serie Camión</label>
              <input v-model="camion.n_serie" required placeholder="Ingrese numero de serie" type="text">
            </div>
            <div class="input-box">
              <label>Patente Camión</label>
              <input v-model="camion.placa" required placeholder="Ingrese patente" type="text">
            </div>
          </div>
          <label>¿Operativo?</label>
          <div class="column">
              <div class="radio-button-container">
              <div class="radio-button">
                <input v-model="camion.estado" type="radio" class="radio-button__input" id="radio1" value="true" name="radio-group">
                <label class="radio-button__label" for="radio1">
                  <span class="radio-button__custom"></span>
                  Si
                </label>
              </div>
              <div class="radio-button">
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
              <label>Fecha Llegada Camión</label>
              <input v-model="camion.fecha_inicio" required placeholder="(fecha)" type="date">
            </div>
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

  <div v-if="selectedOption === 'asign'">
    <div class="containerGeneral">
      <section class="container">
        <header>Formulario Asignacion de Motores</header>
        <form @submit.prevent="asignMotor">
          <div class="column">
            <div class="input-box">
              <label>Fecha Desasignacion Motor</label>
              <input v-model="asignacioncamionmotor.fecha_desasignacion" required placeholder="(fecha)" type="date" />
            </div>
          </div>
          <div class="column">
            <div class="input-box">
              <label>Camiones Disponibles</label>
              <select v-model="asignacioncamionmotor.camion">
                <option v-for="camion in camiones" :key="camion.id_camion" :value="camion.id_camion">
                  {{ camion.placa }}
                </option>
              </select>
            </div>
            <div class="input-box">
              <label>Motores Disponibles</label>
              <select v-model="asignacioncamionmotor.motor">
                <option v-for="motor in motores" :key="motor.id_motor" :value="motor.id_motor">
                  {{ motor.id_motor }}
                </option>
              </select>
            </div>
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
        motor:'',
        camion: '',
        fecha_asignacion: '',
        fecha_desasignacion: ''
      },
      message: '',
      isSuccess: false,
      responseData: null // Añadido para almacenar la respuesta
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
        this.message = 'Error al enviar el formulario.'+ JSON.stringify(this.form);
        this.isSuccess = false;
        if (error.response) {
          this.message += ` Detalles del error: ${error.response.data}`;
        }
      }
    },
    async submitMotor() {
      try {
        const response = await axios.post('http://localhost:8000/api/motor/create', this.motor);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.responseData = response.data; // Almacenar la respuesta en responseData
        this.resetFormMotor();
      } catch (error) {
        this.message = 'Error al enviar el formulario.'+ JSON.stringify(this.motor);
        this.isSuccess = false;
        if (error.response) {
          this.message += ` Detalles del error: ${error.response.data}`;
        }
      }
    },
    async submitCamion() {
      try {
        const response = await axios.post('http://localhost:8000/api/camion/create', this.camion);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.responseData = response.data; // Almacenar la respuesta en responseData
        this.resetFormCamion();
      } catch (error) {
        this.message = 'Error al enviar el formulario.'+ JSON.stringify(this.camion);
        this.isSuccess = false;
        if (error.response) {
          this.message += ` Detalles del error: ${error.response.data}`;
        }
      }
    },
    async fetchCamiones() {
      try {
        const response = await axios.get('http://localhost:8000/api/camion/all');
        this.camiones = response.data;
      } catch (error) {
        console.error('Error fetching camiones:', error);
      }
    },
    async fetchMotores() {
      try {
        const response = await axios.get('http://localhost:8000/api/motor/all');
        this.motores = response.data;
      } catch (error) {
        console.error('Error fetching motores:', error);
      }
    },
    async asignMotor(){
      try {
        const response = await axios.post('http://localhost:8000/api/asignacionmotorcamion', this.asignacioncamionmotor);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.responseData = response.data; // Almacenar la respuesta en responseData
        this.resetFormasignacioncamionmotor();
      } catch (error) {
        this.message = 'Error al enviar el formulario.'+ JSON.stringify(this.asignacioncamionmotor);
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
    },
    resetFormMotor() {
      this.motor = {
        n_serie: '',
        operativo: null,
        fecha_inicio: '',
        tiempo_en_uso: 0,
        durabilidad: 0
      };
    },
    resetFormCamion() {
      this.motor = {
        n_serie:'',
        placa: '',
        estado: '',
        fecha_inicio: '',
        durabilidad: 0
      };
    },
    resetFormasignacioncamionmotor: {
        motor:'',
        camion: '',
        fecha_asignacion: '',
        fecha_desasignacion: ''
      }
  },
  mounted() {
    this.fetchCamiones();
    this.fetchMotores();
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



</style>