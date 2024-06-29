<template>
  <h2>Vista Mecánico</h2>
  <div class="posicionboton">
    <nav>
      <button @click="logout">
        <span class="button_top"> Cerrar Sesión
        </span>
      </button>
    </nav>
    <RouterView />
  </div>
  <div class="containerGeneral">

    <div class="radio-inputs">
      <label class="radio">
        <input type="radio" name="radio" value="incidencia" v-model="selectedOption" />
        <span class="name">Ingresar Incidencia</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" value="search" v-model="selectedOption" />
        <span class="name">Historial incidencias</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" value="todo" v-model="selectedOption" />
        <span class="name">Incidencias pendientes</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" value="settings" v-model="selectedOption" />
        <span class="name">Parametros</span>
      </label>
    </div>
  </div>


  <!-- -------------------------------------------- Ingresar una incidencia -->
  <div v-if="selectedOption === 'incidencia'">
    <div class="containerGeneral">
      <section class="container">
        <header>Formulario de informe de una incidencia</header>
          <div class="input-box">
            <label>Camión</label>
            <button @click="getCamiones">Actualizar</button>
            <select class="form-control" v-model="incidencia.camion">
              <option value="null">Seleccione un camión</option>
              <option v-for="camion in camiones" :key="camion.id_camion" :value="camion.id_camion" >{{ camion.placa }}</option>
            </select>
          </div>

        <form @submit.prevent="submit_incidencia">
          
          <div class="input-box">
            <label>Descripción de la causa (falla / tarea programada)</label>
            <textarea v-model="incidencia.descripcion_problema" required
              placeholder="Describa el(los) problema(s) o la(s) tarea(s) asociado(s) a la incidencia"></textarea>
          </div>
          
          <div class="input-box">
            <label>Mecánicos relacionados con la incidencia</label>
            <textarea v-model="incidencia.mecanicos_asociados"
              placeholder="Escribe los nombres y apellidos de los Mecánicos relacionados con la incidencia, separados por una coma"></textarea>
          </div>
          <div class="input-box">
            <label>Trabajo por realizar</label>
            <textarea v-model="incidencia.descripcion_trabajo_necesario" placeholder="Indique qué es lo que falta por hacer"></textarea>
          </div>

          <button type="submit">Ingresar</button>
        </form>

        <div v-if="incidencia_creada">
          <h3>Incidencia creada :</h3>
          <table v-if="incidencia_creada">
            <thead>
              <tr>
                <th>Camión</th>
                <th>Fecha informe</th>
                <th>Causa</th>
                <th>Mecánicos relacionados</th>
                <th>Trabajo por hacer</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{{ incidencia_creada.camion }}</td>
                <td>{{ formatDate(incidencia_creada.fecha_incidencia) }}</td>
                <td>{{ incidencia_creada.descripcion_problema }}</td>
                <td>{{ incidencia_creada.mecanicos_asociados }}</td>
                <td>{{ incidencia_creada.descripcion_trabajo_necesario }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </div>
  </div>


  <!-- -------------------------------------------- Ver las incidencias de un motor -->
  <div v-if="selectedOption === 'search'">
    <div class="containerGeneral">
      <section class="container">
        <div class="nav">
          <header>Ver las incidencias de un motor</header>
          <div>
            <button @click="searchAll">Todas</button>
          </div>
        </div>

        <div class="column">
          <div class="input-box">
            <label for="search_motor_id">Motor ID</label>
            <input v-model="search_motor_id" type="text" id="search_motor_id">
          </div>
          <button @click="searchByMotor">Buscar</button>
        </div>

        <table v-if="incidentsList.length">
          <thead>
            <tr>
              <th>Motor ID</th>
              <th>Fecha de incidencia</th>
              <th>Descripción de la causa</th>
              <th>Mecánicos relacionados</th>
              <th>Trabajo por hacer</th>
              <th>Mecánico asignado</th>
              <th>Fecha inicio del trabajo</th>
              <th>Fecha fin del trabajo</th>
              <th>¿Solucionado?</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(incident, index) in incidentsList" :key="index">
              <td>{{ incident.motor_id }}</td>
              <td>{{ incident.incident_date }}</td>
              <td>{{ incident.problem_description }}</td>
              <td>{{ incident.mechanics_associated }}</td>
              <td>{{ incident.work_to_do }}</td>
              <td>{{ incident.mechanic_id }}</td>
              <td>{{ incident.start_date }}</td>
              <td>{{ incident.end_date }}</td>
              <td>{{ incident.solved ? 'Si' : 'No' }}</td>
              <td>
                <button @click="updateIndex(index)">Editar</button>
              </td>
            </tr>
          </tbody>
        </table>
        <div v-else>Todavía no hay incidencias</div>
      </section>
    </div>

    <!-- -------------------------------------------- Modificar una incidencia -->
    <div class="containerGeneral">
      <section class="container" v-if="editIndex || editIndex === 0">
        <table>
          <thead>
            <tr>
              <th>Motor ID</th>
              <th>Fecha de incidencia</th>
              <th>Descripción de la causa</th>
              <th>Mecánicos relacionados</th>
              <th>Trabajo por hacer</th>
              <th>Mecánico asignado</th>
              <th>Fecha inicio del trabajo</th>
              <th>Fecha fin del trabajo</th>
              <th>¿Solucionado?</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ incidentsList[editIndex].motor_id }}</td>
              <td>{{ incidentsList[editIndex].incident_date }}</td>
              <td>{{ incidentsList[editIndex].problem_description }}</td>
              <td>{{ incidentsList[editIndex].mechanics_associated }}</td>
              <td>{{ incidentsList[editIndex].work_to_do }}</td>
              <td>{{ incidentsList[editIndex].mechanic_id }}</td>
              <td>{{ incidentsList[editIndex].start_date }}</td>
              <td>{{ incidentsList[editIndex].end_date }}</td>
              <td>{{ incidentsList[editIndex].solved ? 'Si' : 'No' }}</td>
            </tr>
          </tbody>
        </table>

        <header style="margin-top: 2%;">Modificar los datos de la incidencia</header>
        <form @submit.prevent="edit_incidencia">
          <div class="column">
            <div class="input-box">
              <label>Identificador del Motor</label>
              <input v-model="edit.motor_id" :placeholder="[[incidentsList[editIndex].motor_id]]" type="text">
            </div>
            <div class="input-box">
              <label>Fecha de la incidencia</label>
              <input v-model="edit.incident_date" :placeholder="[[incidentsList[editIndex].incident_date]]" type="date">
            </div>
          </div>
          <div class="input-box">
            <label>Descripción de la causa (falla / tarea programada)</label>
            <textarea v-model="edit.problem_description"
              :placeholder="[[incidentsList[editIndex].problem_description]]"></textarea>
          </div>
          <div class="input-box">
            <label>Mecánicos relacionados con la incidencia</label>
            <textarea v-model="edit.mechanics_associated"
              :placeholder="[[incidentsList[editIndex].mechanics_associated]]"></textarea>
          </div>
          <div class="input-box">
            <label>Trabajo por realizar</label>
            <textarea v-model="edit.work_to_do" :placeholder="[[incidentsList[editIndex].work_to_do]]"></textarea>
          </div>

          <!-- CUIDADO normalmente solo un Jefe de Motores puede ver esa posibilidad de asignar la incidencia a un Mecánico -->
          <!-- <div class="input-box">
            <label>Identificador del Mecánico asignado</label>
            <input v-model="edit.mechanic_id" placeholder="Ingrese el identificador del Mecánico asignado" type="text">
          </div> -->
          <div class="column">
            <div class="input-box">
              <label>Fecha Inicio Trabajo</label>
              <input v-model="edit.start_date" placeholder="Inserte Fecha" type="date">
            </div>
            <div class="input-box">
              <label>Fecha Fin Trabajo</label>
              <input v-model="edit.end_date" placeholder="Inserte Fecha" type="date">
            </div>
          </div>
          <div class="solution-box">
            <label>¿Solucionado?</label>
            <div class="radio-button-container">
              <div class="radio-button">
                <input v-model="edit.solved" type="radio" class="radio-button__input" id="radio1" :value="true"
                  name="radio-group">
                <label class="radio-button__label" for="radio1">
                  <span class="radio-button__custom"></span>
                  Si
                </label>
              </div>
              <div class="radio-button">
                <input v-model="edit.solved" type="radio" class="radio-button__input" id="radio2" :value="false"
                  name="radio-group">
                <label class="radio-button__label" for="radio2">
                  <span class="radio-button__custom"></span>
                  No
                </label>
              </div>
            </div>
          </div>

          <button type="submit">Editar</button>
        </form>
      </section>
    </div>


  </div>




  <!-- -------------------------------------------- Ver las incidencias asignadas al mecanico -->
  <div v-if="selectedOption === 'todo'">
    <div class="containerGeneral">
      <section class="container">
        <div style="width: max-content;">
          <button @click="getIncidentsToDo($route.params.id)">Ver mis tareas</button>
        </div>
        <table v-if="tareasList.length">
          <thead>
            <tr>
              <th>Motor ID</th>
              <th>Fecha de incidencia</th>
              <th>Descripción de la causa</th>
              <th>Mecánicos relacionados</th>
              <th>Trabajo por hacer</th>
              <th>Fecha inicio del trabajo</th>
              <th>Fecha fin del trabajo</th>
              <th>¿Solucionado?</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(tarea, index) in tareasList" :key="index">
              <td>{{ tarea.motor_id }}</td>
              <td>{{ tarea.incident_date }}</td>
              <td>{{ tarea.problem_description }}</td>
              <td>{{ tarea.mechanics_associated }}</td>
              <td>{{ tarea.work_to_do }}</td>
              <td>{{ tarea.start_date }}</td>
              <td>{{ tarea.end_date }}</td>
              <td>{{ tarea.solved ? 'Si' : 'No' }}</td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
  </div>

  <!-- -------------------------------------------- Modificar la contrasena del mecanico -->
  <div v-if="selectedOption === 'settings'">
    <div class="containerGeneral">
      <section class="container">
        <div style="width: max-content;">
          <button @click="updateMechanicId($route.params.id)">Cambiar mi contraseña</button>
        </div>
        <form @submit.prevent="changePassword" v-if="mechanic_id">
          <div class="input-box">
            <label>Contraseña actual</label>
            <input v-model="editPassword.oldPassword" required placeholder="Ingresa tu contraseña actual"
              type="password">
          </div>
          <div class="input-box">
            <label>Nueva contraseña</label>
            <input v-model="editPassword.newPassword" required placeholder="Ingresa tu nueva contraseña"
              type="password">
          </div>
          <div class="input-box">
            <label>Repite la contraseña</label>
            <input v-model="editPassword.validNewPassword" required placeholder="Repetir contraseña" type="password">
          </div>

          <button type="submit">Cambiar</button>
        </form>
      </section>
    </div>
  </div>

  <!-- 
  <div>
    <div class="containerGeneral">
      <section class="container">
        <div v-if="message" :class="{ 'success': isSuccess, 'error': !isSuccess }">
          {{ message }}
        </div>
      </section>
    </div>
  </div> -->


</template>








<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';


onMounted(() => {
  console.log('mounted');
  async function getCamiones() {
    try {
      console.log('getCamiones');
      const response = await axios.get('http://localhost:8000/camion/');
      this.camiones = response.data;
      console.log(this.camiones);
    } catch (error) {
      this.message = 'Error al obtener los camiones.';
      this.isSuccess = false;
    }
  }
  getCamiones();
});

export default {
  name: 'App',
  setup() {
    const router = useRouter();
    return {
      selectedOption: ref('incidencia'),
      router
    };
  },
  data() {
    return {

      camiones: [],
      incidencia: {
        camion: null,
        descripcion_problema: null,
        descripcion_trabajo_necesario: null,
        mecanicos_asociados: null
      },
      incidencia_creada: null,
      search_motor_id: '',
      incidentsList: [],
      editIndex: null,
      edit: {
        motor_id: null,
        incident_date: null,
        problem_description: null,
        mechanics_associated: null,
        work_to_do: null,
        mechanic_id: null,
        start_date: null,
        end_date: null,
        solved: null,
        id: null
      },
      tareasList: [],
      mechanic_id: null,
      editPassword: {
        mechanic_id: null,
        oldPassword: '',
        newPassword: '',
        validNewPassword: ''
      },
      message: '',
      isSuccess: false
    };
  },
  methods: {formatDate(date) {
      return new Date(date).toLocaleDateString();
    },
    async getCamiones() {
      try {
        console.log('getCamiones');
        const response = await axios.get('http://localhost:8000/camion/');
        this.camiones = response.data;
        console.log(this.camiones);
      } catch (error) {
        this.message = 'Error al obtener los camiones.';
        this.isSuccess = false;
      }
    },
    async submit_incidencia() {
      try {
        const incidenciaData={
          camion: this.incidencia.camion,
          descripcion_problema: this.incidencia.descripcion_problema,
          descripcion_trabajo_necesario: this.incidencia.descripcion_trabajo_necesario,
          mecanicos_asociados: this.incidencia.mecanicos_asociados || null,
          solucionado: false
        }
        const response = await axios.post('http://localhost:8000/incidencia/', incidenciaData);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.incidencia_creada = response.data;
      } catch (error) {
        this.message = 'Error al enviar el formulario.';
        this.isSuccess = false;
      }
    },

    async searchAll() {
      this.updateIndex(null);
      try {
        const response = await axios.get('http://localhost:8000/api/incidents/all/');
        this.incidentsList = response.data;
        this.message = `Se encontraron ${this.incidentsList.length} resultados.`;
        this.success = true;
      } catch (error) {
        this.message = 'Error al obtener las incidencias.';
        this.isSuccess = false;
      }
    },
    async searchByMotor() {
      this.updateIndex(null);
      try {
        const response = await axios.get(`http://localhost:8000/api/incidents/?motor_id=${this.search_motor_id}`);
        this.incidentsList = response.data;
        this.message = `Se encontraron ${response.data.length} resultados.`;
        this.success = true;
      } catch (error) {
        this.message = 'Error al buscar incidentes.';
        this.isSuccess = false;
      }
    },
    updateIndex(index) {
      this.editIndex = index;
      if (index || index === 0) {
        this.edit.id = this.incidentsList[index].id
      }
    },
    logout() {
      this.$router.push('/');
    },
    async edit_incidencia() {
      try {
        const response = await axios.post(`http://localhost:8000/api/incidents/edit/`, this.edit);
        this.message = 'Formulario enviado exitosamente.';
        this.isSuccess = true;
        this.incidencia_creada = response.data;
        this.editIndex = null;
        this.reset(this.edit)
        this.searchAll()
      } catch (error) {
        this.message = `Error al enviar el formulario.`;
        this.isSuccess = false;
      }
    },
    reset(dict) {
      for (const key in dict) {
        dict[key] = null;
      }
    },
    async getIncidentsToDo(mechanic_id) {
      console.log(mechanic_id)
      try {
        const response = await axios.get(`http://localhost:8000/api/incidents/?mechanic_id=${mechanic_id}`);
        this.message = `Se encontraron ${response.data.length} resultados.`;
        this.success = true;
        this.tareasList = response.data;
      } catch (error) {
        this.message = 'Error al buscar tareas.';
        this.isSuccess = false;
      }
    },
    updateMechanicId(id) {
      this.mechanic_id = id;
      this.editPassword.mechanic_id = id;
    },
    async changePassword() {
      try {
        const response = await axios.post('http://localhost:8000/api/login/edit/', this.editPassword);
        this.isSuccess = true;
        this.message = 'Contraseña cambiada exitosamente.'
        if (response.data.success) {
          this.mechanic_id = null;
          this.reset(this.editPassword)
          this.$router.push('/');
        } else {
          this.msg = 'Al menos una de las contraseñas es incorrecta';
        }
      } catch (error) {
        this.message = 'Error al cambiar la contraseña.';
        this.isSuccess = false;
      }
    }
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
</style>