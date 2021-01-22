<template>
    <!-- :content="messages" -->
        <!-- :value="messages" -->
        <v-badge
        color="green"
        overlap
      >
      
          <v-icon medium>
          mdi-bell-outline
        </v-icon>
      </v-badge>
</template>

<script>
export default {
    data: () => ({
      items: [
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me 2' },
      ],
    }),
}
</script>