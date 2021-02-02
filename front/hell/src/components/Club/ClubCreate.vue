<template>
  <v-row>
    <v-dialog v-model="getDialog" persistent max-width="600px">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-card>
          <div class="text-center ml-3 mr-3">
            <div class="headline text-center pt-3">클럽 생성</div>
            <v-card-text>
              <v-row>
                <v-col cols="12">
                  <v-text-field label="제목*"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea label="내용" rows="10" :value="value"></v-textarea>
                </v-col>

                <!-- 공개 비공개 -->
                <div class="ml-3">
                  <v-radio-group v-model="row" row>
                    <v-radio label="공개" value="radio-1"></v-radio>
                    <v-radio label="비공개" value="radio-2"></v-radio>
                  </v-radio-group>
                </div>
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
    value: '',
    row: '',
  }),
  computed: {
    getDialog: {
      get: function() {
        return this.$store.state.clubDialog;
      },
      set: function() {},
    },
  },

  methods: {
    OnOff: function() {
      this.$store.commit('CLUB_CREATE_DIALOG', false);
    },
    validate() {
      this.$refs.form.validate();
    },
  },
};
</script>
