<template>
    <v-container>
    <v-card>
      <v-card-title>
        가입 요청
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="member"
        :search="search"
      ></v-data-table>
    </v-card>
  </v-container>
    
</template>
<script>
export default {
    
}
</script>