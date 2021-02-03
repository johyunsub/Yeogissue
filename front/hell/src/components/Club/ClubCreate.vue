<template>
  <v-row>
    <v-dialog v-model="getDialog" persistent max-width="600px">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-card>
          <div class="text-center ml-3 mr-3">
            <div class="headline text-center pt-3">클럽 생성</div>
            <v-card-text>
              <v-row>
                <v-col class="12">
                  <v-select
                    v-model="clubData.category"
                    :items="categoryItems"
                    label="카테고리"
                    outlined
                  ></v-select>
                </v-col>
                <v-col cols="12">
                  <v-text-field v-model="clubData.title" label="제목*"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea v-model="clubData.content" label="내용" rows="10"></v-textarea>
                </v-col>

                <!-- 공개 비공개 -->
                <div class="ml-3">
                  <v-radio-group v-model="clubData.check" row>
                    <v-radio label="공개" value="공개"></v-radio>
                    <v-radio label="비공개" value="비공개"></v-radio>
                  </v-radio-group>
                </div>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="OnOff('create')">Create</v-btn>
              <v-btn color="blue darken-1" text @click="OnOff('close')">Close</v-btn>
            </v-card-actions>
          </div>
        </v-card>
      </v-form>
    </v-dialog>
  </v-row>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  data: () => ({
    valid: true,
    categoryItems: ['연예', 'IT/과학', '해외', '경제', '스포츠', '정치', '사회', '생활'],
    clubData: {
      title: '',
      category: '',
      content: '',
      master: '',
      // check: '',
    },
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
    ...mapActions('clubStore', ['clubCreate']),
    OnOff: function(check) {
      if (check == 'create') {
        this.clubData.master = this.$store.state.userInfo.id;
        this.clubCreate(this.clubData);
        this.clubData = {};
      }
      this.$store.commit('CLUB_CREATE_DIALOG', false);
    },
    validate() {
      this.$refs.form.validate();
    },
  },
};
</script>
