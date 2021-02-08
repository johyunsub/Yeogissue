<template>
  <div>
    <v-row>
      <v-col md="4"></v-col>
      <v-col md="4" offset-md="4"></v-col>
    </v-row>
    <v-row> </v-row>
  </div>
</template>

<script>
export default {
  data: () => ({
    items: ["Foo", "Bar", "Fizz", "Buzz"],
  }),
  methods: {
    select() {
      console.log("dd");
    },
  },
};
</script>

