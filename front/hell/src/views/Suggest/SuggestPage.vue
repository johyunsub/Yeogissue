<template>
    <v-container>
        <v-row class="mr-tp"></v-row>
        <h2 class='text-center mr-tp'>클럽</h2>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col>
          <v-row class="mr-tp">
              <v-tabs>
                <v-tab>전체</v-tab>
                <v-tab>경제</v-tab>
                <v-tab>스포츠</v-tab>
                <v-tab>연예</v-tab>
              </v-tabs>
          </v-row>

          <!-- card -->
          <v-row class="mr-tp">
            <v-col
              v-for="n in 9"
              :key="n"
              class="d-flex child-flex"
            >
              <v-row
                align="center"
                justify="center"
              >
              <suggest-card/>  
              </v-row>
            </v-col>
          </v-row>

          <!-- paging -->
              <div class="text-center mr-tp">
                <v-pagination
                  v-model="page"
                  :length="pageCnt"
                  circle
                ></v-pagination>
              </div>
          </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </v-container>
</template>

<script>
import SuggestCard from '../../components/Suggest/SuggestCard.vue';
export default {
  components : {SuggestCard},
}
</script>