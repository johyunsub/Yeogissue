<template>
    <v-card
    class="mx-auto mr-tp"
    max-width="1000"
    outlined
    >
    <v-card-text>
      <v-row>
          <v-col cols="auto" class="mr-auto">
            <p class="display-1 text--primary choice_cursor" @click="MovePage('opinionDetail')">
              제목
            </p>
          </v-col>
            <v-col cols="auto">
            <v-icon small>mdi-thumb-up-outline</v-icon> 100
        </v-col>
      </v-row>
      <p>작성자</p>
      <div class="text--primary choice_cursor">
        간단한 내용
      </div>
      
      <v-divider class="my-2"></v-divider>
      <div class="text--primary">
        #해시태그
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  methods:{
     MovePage : function(check){
        switch(check){
          case 'opinionDetail' : this.$router.push({ name: 'OpinionDetail' }); break;
        }
    }
  },
}
</script>

<style scoped>
</style>