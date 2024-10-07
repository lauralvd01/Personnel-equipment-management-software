<template>
    <h2>Vista Conductor</h2>
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
        <form @submit.prevent="submitReport">
          <div class="column">
            <div class="input-box">
              <label>Identificador del Camión</label>
              <input v-model="report.placa_camion" required placeholder="Ingrese el identificador del motor" type="text">
            </div>
            <div class="input-box">
              <label>Fecha del antecedente</label>
              <input v-model="report.record_date" required placeholder="Inserte Fecha" type="date">
            </div>
          </div>
          <div class="input-box">
            <label>Descripción del problema</label>
            <textarea v-model="report.problem_description" required
              placeholder="Describa el/los problemas asociados a la incidencia"></textarea>
          </div>
          <button type="submit">Ingresar</button>
        </form>
        <div v-if="response_report">
          <h3>Antecedente creado :</h3>
          <table v-if="response_report">
            <thead>
              <tr>
                <th>Camión ID</th>
                <th>Fecha de antecedente</th>
                <th>Descripción del problema</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{{ response_report.id_camion }}</td>
                <td>{{ response_report.record_date }}</td>
                <td>{{ response_report.problem_description }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
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
            router

        };
    },
    data() {
        return{
            response_report: null,
            search_placa_camion: '',
            report: {
                placa_camion: '',
                record_date: '',
                problem_description: ''
            },
            response_report: null,
            search_id_camion: '',
            recordsList: [],
            editIndex: null,
            edit: {
                placa_camion: null,
                record_date: null,
                problem_description: null,
                id: null
            },
        }
    },
    methods:{
        async submitReport() {
            try {
                const response = await axios.post('http://localhost:8000/api/records/submit/', this.report);
                this.message = 'Formulario enviado exitosamente.';
                this.isSuccess = true;
                this.response_report = response.data;
            } catch (error) {
                const formString = JSON.stringify(this.form, null, 2);
                const serializerErrors = error.response && error.response.data ? JSON.stringify(error.response.data, null, 2) : 'No se pudo obtener los errores del servidor.';
                this.message = `Error al enviar el formulario. Datos del formulario: ${formString}. Errores del servidor: ${serializerErrors}`;
                this.isSuccess = false;
            }
        },
        async searchByPlaca() {
            this.updateIndex(null);
            try {
                const response = await axios.get(`http://localhost:8000/api/records/?placa_motor=${this.search_placa_camion}`);
                this.recordsList = response.data;
                this.message = `Se encontraron ${response.data.length} resultados.`;
                this.success = true;
            } catch (error) {
                this.message = 'Error al buscar antecedentes.';
                this.isSuccess = false;
            }
        },
        updateIndex(index) {
            this.editIndex = index;
            if (index || index === 0) {
                this.edit.id = this.recordsList[index].id
            }
        }
    }
}