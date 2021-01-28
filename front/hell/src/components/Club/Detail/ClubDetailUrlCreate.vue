<template>
  <v-row>
    <v-dialog v-model="getDialog" persistent max-width="600px">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-card>
          <div class="text-center ml-3 mr-3">
            <div class="headline text-center pt-3">링크 등록</div>
            <v-card-text>
              <v-row>
                <v-col cols="12">
                  <v-select :items="items" label="카테고리*"> </v-select>
                </v-col>
                <v-col cols="12">
                  <v-text-field label="제목*"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field label="URL*"></v-text-field>
                </v-col>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="OnOff()">Create</v-btn>
              <v-btn color="blue darken-1" text @click="OnOff()">Close</v-btn>
            </v-card-actions>
          </div>
        </v-card>
      </v-form>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    email: '',
    items: ['News', 'Youtube', 'etc'],
  }),
  computed: {
    getDialog: {
      get: function() {
        return this.$store.state.clubDetailUrlDialog;
      },
      set: function() {},
    },
  },

  methods: {
    OnOff: function() {
      this.$store.commit('CLUB_DETAIL_URL_DIALOG', false);
    },
    validate() {
      this.$refs.form.validate();
    },
  },
};
</script>
