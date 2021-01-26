//type에 따라 찬반, 의견으로 버튼이 보이고 안보이고 성질에 따라
<template>
   <v-card
    class="mr-tp"
    max-width="1000"
    outlined
    >
    <v-card-text>
        <v-row>
            <v-col>
                <div class="text--primary">
                    작성일
                </div>
            </v-col>
            <v-col cols="auto">
                <v-icon small>mdi-thumb-up-outline</v-icon> 100
                <v-icon small>mdi-thumb-down-outline</v-icon> 100
            </v-col>
        </v-row>

      <v-row
      >
        <v-col
          cols="2"
        >
          <v-avatar
            class="profile mr-le mr-tp"
            color="grey"
            size="100"
          >
            <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
          </v-avatar>
          <v-list-item-content>
              <v-list-item-title class="title">
                Marcus Obrien
              </v-list-item-title>
            </v-list-item-content>
        </v-col>
        
        <v-col cols="9">
            ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<style scoped>
.mr-le{
    margin-left: 15px;
}
</style>