<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Vista Mecánicos</h2>
    <div class="containerGeneral">
      <section class="container">
        <header>Formulario de Incidencias</header>
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
</template>

<script>
import axios from 'axios';

export default {
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
.success {
  color: green;
}

.error {
  color: red;
}

.containerGeneral {
  display: flex;
  justify-content: center;
  height: 100vh;
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

/* Formulario Mecanicos */
.container {
  position: relative;
  max-width: 750px;
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
  display: flex;
  column-gap: 15px;
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
