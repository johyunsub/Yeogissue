

<script>
import { Doughnut } from 'vue-chartjs';
import { mapState } from 'vuex';
import axios from 'axios';
import { API_BASE_URL } from '../../config';

export default {
  extends: Doughnut,
  computed: {
    ...mapState('opinionStore', ['opinionData']),
  },
  props: {
    id: Number,
  },
  data: () => ({
    chartdata: {
      labels: ['찬성', '반대'],
      datasets: [
        {
          backgroundColor: ['blue', 'red'],
          data: [0, 0],
          borderAlign: 'center',
        },
      ],
    },
    options: {
      responsive: false,
      maintainAspectRatio: false,
    },
  }),

  methods: {
    getId() {
      return this.id;
    },
  },

  mounted() {
    axios
      .get(`${API_BASE_URL}articles/${this.getId()}/`)
      .then((res) => {
        this.chartdata.datasets[0].data[0] = res.data.agree_count;
        this.chartdata.datasets[0].data[1] = res.data.disagree_count;
        this.renderChart(this.chartdata, this.options);
      })
      .catch((err) => console.log(err.response));
  },
};
</script>

<style>
.chartjs-render-monitor {
  height: 200px;
  text-align: center;
}
</style>
