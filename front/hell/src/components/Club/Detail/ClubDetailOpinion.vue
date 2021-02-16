<template>
  <div>
    <v-row class="mr-tp">
      <!-- <h1 v-for='item in opinionPaging' :key='item.title'>{{item}}이게 맞냐</h1> -->
      <v-col cols="1"> </v-col>
      <v-col>
        <v-list two-line>
          <card-list v-for="(item, index) in opinionPaging" :key="`${index}_items`" :data="item" />
        </v-list>
      </v-col>
      <v-col cols="1"> </v-col>
    </v-row>
    <div class="text-center">
      <v-pagination v-model="page" :length="pagingCnt" circle></v-pagination>
    </div>
    <v-row>
      <v-col cols="auto" class="mr-auto"></v-col>
      <v-col cols="auto">
        <!-- <v-btn class="ma-2 btnLC" outlined large fab color="indigo"  @click="MovePage('write')"> <v-icon>mdi-pencil</v-icon></v-btn> -->
        <v-btn class="btnLC" color="blue" rounded @click="MovePage('write')">
          <v-icon color="white">mdi-pencil</v-icon>
          <span style="color: white;"> 글쓰기 </span></v-btn
        >
      </v-col>
      <v-col cols="1"> </v-col>
    </v-row>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";
import CardList from "../../Opinion/CardList.vue";

export default {
  components: { CardList },
  computed: {
    ...mapState("opinionStore", ["opinionPaging", "pagingCnt"]),
  },
  data() {
    return {
      page: 1,
    };
  },
  watch: {
    page: function(newVal) {
      this.$store.commit("opinionStore/SET_OPINION_PAGING", (newVal - 1) * 10);
    },
  },
  methods: {
    ...mapActions("opinionStore", ["opinionListClub"]),
    MovePage: function(check) {
      switch (check) {
        case "write":
          this.$router.push(`/opinionWrite?type=write&club_pk=${this.$route.query.id}`);
          break;
      }
    },
  },
  created() {
    console.log(this.$route.query.id);
    this.opinionListClub(this.$route.query.id);
  },
};
</script>
