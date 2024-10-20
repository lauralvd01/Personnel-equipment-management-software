<template>
  <h2>Vista Mecánico</h2> <!-- Título de la vista para el mecánico -->

<div class="posicionboton">
  <!-- Contenedor para el botón de cerrar sesión -->
  <nav>
    <!-- Botón de cerrar sesión -->
    <button @click="logout">
      <span class="button_top"> Cerrar Sesión </span>
      <br />
    </button>
  </nav>
  <!-- Vista del enrutador para mostrar componentes según la ruta -->
  <RouterView />
</div>

<div class="containerGeneral">
  <!-- Contenedor para las opciones de radio -->
  <div class="radio-inputs">
    <!-- Opción de radio para ingresar una incidencia -->
    <label class="radio">
      <input type="radio" name="radio" value="incidencia" v-model="selectedOption" />
      <span class="name">Ingresar Incidencia</span>
    </label>
    <!-- Opción de radio para ver el historial de incidencias -->
    <label class="radio">
      <input type="radio" name="radio" value="search" v-model="selectedOption" />
      <span class="name">Historial incidencias</span>
    </label>
    <!-- Opción de radio para ver las incidencias pendientes -->
    <label class="radio">
      <input type="radio" name="radio" value="todo" v-model="selectedOption" />
      <span class="name">Incidencias pendientes</span>
    </label>
    <!-- Opción de radio para ajustar parámetros -->
    <label class="radio">
      <input type="radio" name="radio" value="settings" v-model="selectedOption" />
      <span class="name">Parámetros</span>
    </label>
  </div>
</div>


  <!-- -------------------------------------------- Ingresar una incidencia -->
<div v-if="selectedOption === 'incidencia'">
  <div class="containerGeneral">
    <section class="container">
      <!-- Encabezado del formulario de informe de una incidencia -->
      <header>Formulario de informe de una incidencia</header>

      <!-- Formulario para ingresar una incidencia -->
      <form @submit.prevent="submit_incidencia">
        <!-- Selección de camión -->
        <div class="input-box">
          <label>Camión</label>
          <select class="form-control" required v-model="incidencia.camion">
            <option value="null">Seleccione un camión</option>
            <!-- Listar los camiones disponibles -->
            <option v-for="camion in camiones" :key="camion.id_camion" :value="camion.id_camion">
              {{ camion.placa }}
            </option>
          </select>
        </div>

        <!-- Descripción de la causa (falla / tarea programada) -->
        <div class="input-box">
          <label>Descripción de la causa (falla / tarea programada)</label>
          <textarea v-model="incidencia.descripcion_problema" required placeholder="Describa el(los) problema(s) o la(s) tarea(s) asociado(s) a la incidencia"></textarea>
        </div>

        <!-- Mecánicos relacionados con la incidencia -->
        <div class="input-box">
          <label>Mecánicos relacionados con la incidencia</label>
          <textarea v-model="incidencia.mecanicos_asociados" placeholder="Escribe los nombres y apellidos de los Mecánicos relacionados con la incidencia, separados por una coma"></textarea>
        </div>

        <!-- Trabajo por realizar -->
        <div class="input-box">
          <label>Trabajo por realizar</label>
          <textarea v-model="incidencia.descripcion_trabajo_necesario" placeholder="Indique qué es lo que falta por hacer"></textarea>
        </div>

        <!-- Botón para enviar el formulario -->
        <button type="submit">Ingresar</button>
      </form>

      <!-- Mostrar los detalles de la incidencia creada -->
      <div v-if="incidencia_creada">
        <h3>Incidencia creada :</h3>
        <table v-if="incidencia_creada">
          <thead>
            <tr>
              <th>Placa del camión</th>
              <th>N°serie del motor</th>
              <th>Fecha informe</th>
              <th>Descripción</th>
              <th>Mecánicos relacionados</th>
              <th>Trabajo por hacer</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <!-- Mostrar la placa del camión correspondiente a la incidencia creada -->
              <td>{{ camiones.filter((camion) => camion.id_camion == incidencia_creada.camion)[0].placa }}</td>
              <!-- Mostrar el número de serie del motor correspondiente a la incidencia creada -->
              <td>{{ motores.filter((motor) => motor.id_motor == incidencia_creada.motor)[0].n_serie }}</td>
              <!-- Mostrar la fecha del informe de la incidencia creada -->
              <td>{{ formatDate(incidencia_creada.fecha_incidencia) }}</td>
              <!-- Mostrar la descripción del problema de la incidencia creada -->
              <td>{{ incidencia_creada.descripcion_problema }}</td>
              <!-- Mostrar los mecánicos relacionados con la incidencia creada -->
              <td>{{ incidencia_creada.mecanicos_asociados }}</td>
              <!-- Mostrar el trabajo por hacer de la incidencia creada -->
              <td>{{ incidencia_creada.descripcion_trabajo_necesario }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</div>



  <!-- -------------------------------------------- Buscar las incidencias por camion, motor, o fecha -->
  <div v-if="selectedOption === 'search'">
    <div class="containerGeneral">
      <section class="container">
        <!-- Encabezado para buscar incidencias por camión, motor o fecha -->
        <div class="nav">
          <header>Buscar las incidencias por camión, motor o fecha</header>
        </div>

        <!-- Filtro por placa del camión -->
        <div class="input-box">
          <label>Placa del camión</label>
          <select class="form-control" v-model="filtro_historial.camion" @change="get_incidencias_filtradas">
            <option value="null">Seleccione un camión</option>
            <!-- Listar los camiones disponibles -->
            <option v-for="camion in camiones" :key="camion.id_camion" :value="camion.id_camion">
              {{ camion.placa }}
            </option>
          </select>
        </div>

        <!-- Filtro por número de serie del motor -->
        <div class="input-box">
          <label>N°serie del motor</label>
          <select class="form-control" v-model="filtro_historial.motor" @change="get_incidencias_filtradas">
            <option value="null">Seleccione un motor</option>
            <!-- Listar los motores disponibles -->
            <option v-for="motor in motores" :key="motor.id_motor" :value="motor.id_motor">
              {{ motor.n_serie }}
            </option>
          </select>
        </div>

        <!-- Filtro por fecha de reporte de la incidencia -->
        <div class="input-box">
          <label>Fecha de reporte de la incidencia</label>
          <input v-model="filtro_historial.fecha" type="date" @change="get_incidencias_filtradas">
        </div>

        <!-- Tabla de incidencias filtradas -->
        <table v-if="incidencias_filtradas.length">
          <thead>
            <tr>
              <th>Camión</th>
              <th>Motor</th>
              <th>Fecha de reporte</th>
              <th>Descripción</th>
              <th>Mecánicos relacionados</th>
              <th>Trabajo por hacer</th>
              <th>Mecánico asignado</th>
              <th>Trabajo hecho</th>
              <th>Fecha inicio del trabajo</th>
              <th>Fecha fin del trabajo</th>
              <th>¿Solucionado?</th>
            </tr>
          </thead>
          <tbody>
            <!-- Listar las incidencias filtradas -->
            <tr v-for="incidencia_filtrada in incidencias_filtradas" :key="incidencia_filtrada.id_incidencia">
              <!-- Mostrar la placa del camión correspondiente a la incidencia filtrada -->
              <td>{{ camiones.filter((camion) => camion.id_camion == incidencia_filtrada.camion)[0].placa }}</td>
              <!-- Mostrar el número de serie del motor correspondiente a la incidencia filtrada -->
              <td>{{ motores.filter((motor) => motor.id_motor == incidencia_filtrada.motor)[0].n_serie }}</td>
              <!-- Mostrar la fecha del informe de la incidencia filtrada -->
              <td>{{ formatDate(incidencia_filtrada.fecha_incidencia) }}</td>
              <!-- Mostrar la descripción del problema de la incidencia filtrada -->
              <td>{{ incidencia_filtrada.descripcion_problema }}</td>
              <!-- Mostrar los mecánicos relacionados con la incidencia filtrada -->
              <td>{{ incidencia_filtrada.mecanicos_asociados }}</td>
              <!-- Mostrar el trabajo por hacer de la incidencia filtrada -->
              <td>{{ incidencia_filtrada.descripcion_trabajo_necesario }}</td>
              <!-- Mostrar el mecánico asignado a la incidencia filtrada -->
              <td>{{ incidencia_filtrada.mecanico_asignado }}</td>
              <!-- Mostrar la fecha de inicio del trabajo de la incidencia filtrada -->
              <td>{{ formatDate(incidencia_filtrada.fecha_inicio_trabajo) }}</td>
              <!-- Mostrar la fecha de término del trabajo de la incidencia filtrada -->
              <td>{{ formatDate(incidencia_filtrada.fecha_termino_trabajo) }}</td>
              <!-- Mostrar si la incidencia filtrada está solucionada -->
              <td>{{ incidencia_filtrada.solucionado ? 'Si' : 'No' }}</td>
            </tr>
          </tbody>
        </table>

        <!-- Mostrar mensaje si no hay incidencias correspondientes a los filtros -->
        <div v-else>Ninguna incidencia corresponde</div>
      </section>
    </div>
  </div>


    <!-- -------------------------------------------- Modificar una incidencia -->
  <div class="containerGeneral">
    <!-- Sección para editar una incidencia -->
    <section class="container" v-if="editIndex || editIndex === 0">
      <!-- Tabla que muestra los datos actuales de la incidencia seleccionada -->
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

      <!-- Formulario para modificar los datos de la incidencia -->
      <header style="margin-top: 2%;">Modificar los datos de la incidencia</header>
      <form @submit.prevent="edit_incidencia">
        <div class="column">
          <!-- Campo para modificar el ID del motor -->
          <div class="input-box">
            <label>Identificador del Motor</label>
            <input v-model="edit.motor_id" :placeholder="[[incidentsList[editIndex].motor_id]]" type="text">
          </div>
          <!-- Campo para modificar la fecha de la incidencia -->
          <div class="input-box">
            <label>Fecha de la incidencia</label>
            <input v-model="edit.incident_date" :placeholder="[[incidentsList[editIndex].incident_date]]" type="date">
          </div>
        </div>
        <!-- Campo para modificar la descripción de la causa de la incidencia -->
        <div class="input-box">
          <label>Descripción de la causa (falla / tarea programada)</label>
          <textarea v-model="edit.problem_description"
            :placeholder="[[incidentsList[editIndex].problem_description]]"></textarea>
        </div>
        <!-- Campo para modificar los mecánicos relacionados con la incidencia -->
        <div class="input-box">
          <label>Mecánicos relacionados con la incidencia</label>
          <textarea v-model="edit.mechanics_associated"
            :placeholder="[[incidentsList[editIndex].mechanics_associated]]"></textarea>
        </div>
        <!-- Campo para modificar el trabajo por realizar -->
        <div class="input-box">
          <label>Trabajo por realizar</label>
          <textarea v-model="edit.work_to_do" :placeholder="[[incidentsList[editIndex].work_to_do]]"></textarea>
        </div>

        <!-- Nota: normalmente solo un Jefe de Motores puede ver la opción de asignar la incidencia a un Mecánico -->
        <!-- Campo opcional para modificar el ID del mecánico asignado -->
        <!--
        <div class="input-box">
          <label>Identificador del Mecánico asignado</label>
          <input v-model="edit.mechanic_id" placeholder="Ingrese el identificador del Mecánico asignado" type="text">
        </div>
        -->

        <div class="column">
          <!-- Campo para modificar la fecha de inicio del trabajo -->
          <div class="input-box">
            <label>Fecha Inicio Trabajo</label>
            <input v-model="edit.start_date" placeholder="Inserte Fecha" type="date">
          </div>
          <!-- Campo para modificar la fecha de fin del trabajo -->
          <div class="input-box">
            <label>Fecha Fin Trabajo</label>
            <input v-model="edit.end_date" placeholder="Inserte Fecha" type="date">
          </div>
        </div>

        <!-- Campo para modificar el estado de si la incidencia está solucionada -->
        <div class="solution-box">
          <label>¿Solucionado?</label>
          <div class="radio-button-container">
            <div class="radio-button">
              <input v-model="edit.solved" type="radio" class="radio-button__input" id="radio1" :value="true" name="radio-group">
              <label class="radio-button__label" for="radio1">
                <span class="radio-button__custom"></span>
                Si
              </label>
            </div>
            <div class="radio-button">
              <input v-model="edit.solved" type="radio" class="radio-button__input" id="radio2" :value="false" name="radio-group">
              <label class="radio-button__label" for="radio2">
                <span class="radio-button__custom"></span>
                No
              </label>
            </div>
          </div>
        </div>

        <!-- Botón para enviar el formulario de edición -->
        <button type="submit">Editar</button>
      </form>
    </section>
  </div>




  <!-- -------------------------------------------- Ver las incidencias asignadas al mecanico que no son solucionadas -->
  <div v-if="selectedOption === 'todo'">
    <div class="containerGeneral">
      <section class="container">
        <table v-if="tareasList.length">
          <thead>
            <tr>
              <th>Camión</th>
              <th>Motor</th>
              <th>Fecha de reporte</th>
              <th>Descripción</th>
              <th>Mecánicos relacionados</th>
              <th>Trabajo por hacer</th>
              <th>Fecha inicio del trabajo</th>
              <th>Trabajo hecho</th>
              <th>Fecha fin del trabajo</th>
              <th>¿Solucionado?</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="incidencia_pendiente in incidencias_pendientes" :key="incidencia_pendiente.id_incidencia">
              <td>{{ camiones.filter((camion) => camion.id_camion == incidencia_pendiente.camion)[0].placa }}</td>
              <td>{{ motores.filter((motor) => motor.id_motor == incidencia_pendiente.motor)[0].n_serie }}</td>
              <td>{{ formatDate(incidencia_pendiente.fecha_incidencia) }}</td>
              <td>{{ incidencia_pendiente.descripcion_problema }}</td>
              <td>{{ incidencia_pendiente.mecanicos_asociados }}</td>
              <td>{{ incidencia_pendiente.descripcion_trabajo_necesario }}</td>
              {
              incidencia_pendiente.fecha_inicio_trabajo ?
              <td>{{ formatDate(incidencia_pendiente.fecha_inicio_trabajo) }}</td>
              } else {
              <td>
                <button @click="() => { console.log(incidencia_pendiente) }">
                  Iniciar
                </button>
              </td>
              }
              <td>
                <button @click="() => { console.log(incidencia_pendiente.descripcion_trabajo_hecho) }">
                  {{ incidencia_pendiente.descripcion_trabajo_hecho }}
                </button>
              </td>
              {
              incidencia_pendiente.fecha_termino_trabajo ?
              <td>{{ formatDate(incidencia_pendiente.fecha_termino_trabajo) }}</td>
              } else {
              <td>
                <button @click="() => { console.log(incidencia_pendiente) }">
                  Finalizar
                </button>
              </td>
              }
              <td>{{ incidencia_pendiente.solucionado ? 'Si' : 'No' }}</td>
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
import { ref } from 'vue';  // Importa la función ref para crear referencias reactivas
import axios from 'axios';  // Importa axios para realizar solicitudes HTTP
import { useRouter } from 'vue-router';  // Importa useRouter para manejar la navegación

export default {
  name: 'App',
  setup() {
    const router = useRouter();  // Configura el router
    return {
      selectedOption: ref('incidencia'),  // Crea una referencia reactiva para la opción seleccionada
      router  // Retorna el router para usarlo en el componente
    };
  },
  data() {
    return {
      motores: [],  // Almacena la lista de motores
      camiones: [],  // Almacena la lista de camiones
      incidencia: {
        camion: null,  // Datos del camión asociado a la incidencia
        descripcion_problema: null,  // Descripción del problema
        descripcion_trabajo_necesario: null,  // Descripción del trabajo necesario
        mecanicos_asociados: null  // Mecánicos asociados a la incidencia
      },
      incidencia_creada: null,  // Almacena la incidencia creada
      filtro_historial: {
        camion: null,  // Filtro por camión
        motor: null,  // Filtro por motor
        fecha: null  // Filtro por fecha
      },
      incidencias_filtradas: [],  // Almacena las incidencias filtradas
      usuario_id: null,  // Almacena el ID del usuario
      incidencias_pendientes: [],  // Almacena las incidencias pendientes

      search_motor_id: '',  // ID del motor a buscar
      incidentsList: [],  // Lista de incidencias
      editIndex: null,  // Índice de la incidencia a editar
      edit: {
        motor_id: null,  // ID del motor
        incident_date: null,  // Fecha de la incidencia
        problem_description: null,  // Descripción del problema
        mechanics_associated: null,  // Mecánicos asociados
        work_to_do: null,  // Trabajo a realizar
        mechanic_id: null,  // ID del mecánico
        start_date: null,  // Fecha de inicio
        end_date: null,  // Fecha de finalización
        solved: null,  // Estado de la incidencia (resuelta o no)
        id: null  // ID de la incidencia
      },
      tareasList: [],  // Lista de tareas
      mechanic_id: null,  // ID del mecánico
      editPassword: {
        mechanic_id: null,  // ID del mecánico para cambiar la contraseña
        oldPassword: '',  // Contraseña antigua
        newPassword: '',  // Nueva contraseña
        validNewPassword: ''  // Confirmación de la nueva contraseña
      },
      message: '',  // Mensaje para mostrar al usuario
      isSuccess: false  // Estado de éxito de las operaciones
    };
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleDateString();  // Formatea la fecha a un formato legible
    },
    async getCamiones() {
      try {
        const response = await axios.get('http://localhost:8000/camion/');  // Solicita la lista de camiones
        this.camiones = response.data;  // Almacena la lista de camiones
      } catch (error) {
        this.message = 'Error al obtener los camiones.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },
    async getMotores() {
      try {
        const response = await axios.get('http://localhost:8000/motor/');  // Solicita la lista de motores
        this.motores = response.data;  // Almacena la lista de motores
      } catch (error) {
        this.message = 'Error al obtener los motores.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },
    async submit_incidencia() {
      try {
        const incidenciaData = {
          camion: this.incidencia.camion,
          descripcion_problema: this.incidencia.descripcion_problema,
          descripcion_trabajo_necesario: this.incidencia.descripcion_trabajo_necesario,
          mecanicos_asociados: this.incidencia.mecanicos_asociados || null,
          solucionado: false
        }
        const response = await axios.post('http://localhost:8000/incidencia/', incidenciaData);  // Envía los datos de la incidencia
        this.message = 'Formulario enviado exitosamente.';  // Muestra un mensaje de éxito
        this.isSuccess = true;  // Indica que la operación tuvo éxito
        this.incidencia_creada = response.data;  // Almacena la incidencia creada
      } catch (error) {
        this.message = 'Error al enviar el formulario.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },
    async get_incidencias_filtradas() {
      try {
        if (this.filtro_historial.camion && this.filtro_historial.camion == "null") this.filtro_historial.camion = null;
        if (this.filtro_historial.motor && this.filtro_historial.motor == "null") this.filtro_historial.motor = null;
        if (this.filtro_historial.fecha && this.filtro_historial.motor == "") this.filtro_historial.fecha = null;
        const response = await axios.get(`http://localhost:8000/api/incidencias/${this.filtro_historial.camion ? '?camion=' + this.filtro_historial.camion : ''}${this.filtro_historial.motor ? `${this.filtro_historial.camion ? '&' : '?'}motor=` + this.filtro_historial.motor : ''}${this.filtro_historial.fecha ? `${this.filtro_historial.camion || this.filtro_historial.motor ? '&' : '?'}fecha=` + this.filtro_historial.fecha : ''}`);  // Solicita las incidencias filtradas
        this.incidencias_filtradas = response.data;  // Almacena las incidencias filtradas
        this.message = `Se encontraron ${this.incidencias_filtradas.length} resultados.`;  // Muestra un mensaje con el número de resultados
        this.success = true;  // Indica que la operación tuvo éxito
      } catch (error) {
        this.message = 'Error al obtener las incidencias.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },
    async get_incidencias_pendientes() {
      console.log(this.usuario_id)
      try {
        const response = await axios.get(`http://localhost:8000/api/incidencias/?mecanico_asignado=${this.usuario_id}&solucionado=False`);  // Solicita las incidencias pendientes para el mecánico actual
        this.incidencias_pendientes = response.data;  // Almacena las incidencias pendientes
        this.message = `Se encontraron ${this.incidencias_pendientes.length} resultados.`;  // Muestra un mensaje con el número de resultados
        this.success = true;  // Indica que la operación tuvo éxito
      } catch (error) {
        this.message = 'Error al obtener las incidencias.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },

    async searchAll() {
      this.updateIndex(null);
      try {
        const response = await axios.get('http://localhost:8000/api/incidents/all/');  // Solicita todas las incidencias
        this.incidentsList = response.data;  // Almacena la lista de incidencias
        this.message = `Se encontraron ${this.incidentsList.length} resultados.`;  // Muestra un mensaje con el número de resultados
        this.success = true;  // Indica que la operación tuvo éxito
      } catch (error) {
        this.message = 'Error al obtener las incidencias.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },
    async searchByMotor() {
      this.updateIndex(null);
      try {
        const response = await axios.get(`http://localhost:8000/api/incidents/?motor_id=${this.search_motor_id}`);  // Solicita incidencias filtradas por el ID del motor
        this.incidentsList = response.data;  // Almacena la lista de incidencias
        this.message = `Se encontraron ${response.data.length} resultados.`;  // Muestra un mensaje con el número de resultados
        this.success = true;  // Indica que la operación tuvo éxito
      } catch (error) {
        this.message = 'Error al buscar incidentes.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },
    updateIndex(index) {
      this.editIndex = index;  // Actualiza el índice de la incidencia a editar
      if (index || index === 0) {
        this.edit.id = this.incidentsList[index].id  // Almacena el ID de la incidencia a editar
      }
    },
    logout() {
      this.$router.push('/');  // Redirige al usuario a la página de inicio
    },
    async edit_incidencia() {
      try {
        const response = await axios.post(`http://localhost:8000/api/incidents/edit/`, this.edit);  // Envía los datos editados de la incidencia
        this.message = 'Formulario enviado exitosamente.';  // Muestra un mensaje de éxito
        this.isSuccess = true;  // Indica que la operación tuvo éxito
        this.incidencia_creada = response.data;  // Almacena la incidencia editada
        this.editIndex = null;  // Resetea el índice de edición
        this.reset(this.edit);  // Resetea los datos de edición
        this.searchAll();  // Refresca la lista de incidencias
      } catch (error) {
        this.message = `Error al enviar el formulario.`;  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },
    reset(dict) {
      for (const key in dict) {
        dict[key] = null;  // Resetea todos los valores en el diccionario
      }
    },
    async getIncidentsToDo(mechanic_id) {
      console.log(mechanic_id)
      try {
        const response = await axios.get(`http://localhost:8000/api/incidents/?mechanic_id=${mechanic_id}`);  // Solicita las incidencias asignadas al mecánico
        this.message = `Se encontraron ${response.data.length} resultados.`;  // Muestra un mensaje con el número de resultados
        this.success = true;  // Indica que la operación tuvo éxito
        this.tareasList = response.data;  // Almacena la lista de tareas
      } catch (error) {
        this.message = 'Error al buscar tareas.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    },
    updateMechanicId(id) {
      this.mechanic_id = id;  // Actualiza el ID del mecánico
      this.editPassword.mechanic_id = id;  // Actualiza el ID del mecánico para el cambio de contraseña
    },
    async changePassword() {
      try {
        const response = await axios.patch('http://localhost:8000/api/login/edit/', this.editPassword);  // Envía la solicitud para cambiar la contraseña
        this.isSuccess = true;  // Indica que la operación tuvo éxito
        this.message = 'Contraseña cambiada exitosamente.';  // Muestra un mensaje de éxito
        if (response.data.success) {
          this.mechanic_id = null;  // Resetea el ID del mecánico
          this.reset(this.editPassword);  // Resetea los datos de la contraseña
          this.$router.push('/');  // Redirige al usuario a la página de inicio
        } else {
          this.msg = 'Al menos una de las contraseñas es incorrecta';  // Muestra un mensaje de error
        }
      } catch (error) {
        this.message = 'Error al cambiar la contraseña.';  // Muestra un mensaje de error
        this.isSuccess = false;  // Indica que la operación no tuvo éxito
      }
    }
  },
  mounted() {
    this.getCamiones();  // Obtiene la lista de camiones al montar el componente
    this.getMotores();  // Obtiene la lista de motores al montar el componente
    this.usuario_id = this.$route.params.id;  // Obtiene el ID del usuario de los parámetros de la ruta
    this.get_incidencias_pendientes();  // Obtiene las incidencias pendientes al montar el componente
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


label{
  font-size: 19px;
}

:root {
  --arrow-bg: rgba(255, 255, 255, 0.3);
  --arrow-icon: url(https://upload.wikimedia.org/wikipedia/commons/9/9d/Caret_down_font_awesome_whitevariation.svg);
  --option-bg: black;
  --select-bg: rgba(255, 255, 255, 0.2);
}

body {
  display: grid;
  place-items: center;
  min-height: 100vh;
  background: linear-gradient(35deg, red, purple);
}

.form-control {
  /* Reset */
  text-align: center;
  margin: 10px 10px 10px 0px;
  margin-left: 10px;
  appearance: none;
  border: 0px;
  border-color: #000;
  outline: 0;
  font: inherit;
  border-radius: 10px;
  /* Personalize */
  width: 20rem;
  padding-top: 5px;
  padding-bottom: 5px;
  background: var(--select-bg);
  background-color: rgb(255, 255, 255);
  color: black;
  /* Texto en negro */
  box-shadow: 0 0 1em 0 rgba(0, 0, 0, 0.2);
  cursor: pointer;

  /* Remove IE arrow */
  &::-ms-expand {
    display: none;
  }

  /* Remove focus outline */
  &:focus {
    outline: none;
  }
}

.form-control:hover {
  background-color: #ffa395;
}

.form-control option {
  color: inherit;
  background-color: var(--option-bg);
}
</style>