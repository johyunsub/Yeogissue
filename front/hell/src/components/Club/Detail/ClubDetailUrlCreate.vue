<template>
  <v-dialog v-model="getDialog" persistent max-width="600px">
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-card>
        <div class="text-center ml-3 mr-3">
          <div class="headline text-center pt-3" v-if="type == 'create'">링크 등록</div>
          <div class="headline text-center pt-3" v-if="type == 'update'">링크 수정</div>
          <v-card-text>
            <v-select :items="items" label="카테고리*" v-model="DetailUrlData.category"> </v-select>
            <v-text-field v-model="DetailUrlData.comment" label="코멘트*"></v-text-field>
            <v-text-field v-model="DetailUrlData.url" label="URL*"></v-text-field>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="CreateOption(type)">Create</v-btn>
            <v-btn color="blue darken-1" text @click="OnOff()">Close</v-btn>
          </v-card-actions>
        </div>
      </v-card>
    </v-form>
  </v-dialog>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  props: {
    type: { Type: String },
  },
  data: () => ({
    valid: true,
    email: '',
    items: ['News', 'Youtube', 'etc'],
    DetailUrlData: {
      comment: '',
      url: '',
      user: '',
      club: '',
      category: '',
    },
  }),
  computed: {
    ...mapState('clubStore', ['clubData']),
    getDialog: {
      get: function() {
        return this.$store.state.clubStore.clubDetailUrlDialog;
      },
      set: function() {},
    },
  },

  methods: {
    ...mapActions('clubStore', ['clubDetailUrlCreate', 'clubDetailUrlUpdate']),
    CreateOption(check) {
      if (check === 'create') {
        if (!this.DetailUrlData.url.includes('http'))
          this.DetailUrlData.url = 'https://' + this.DetailUrlData.url;

        this.DetailUrlData.user = this.$store.state.userInfo.id;
        console.log(this.$store.state.clubData);
        this.DetailUrlData.club = this.clubData.id;
        console.log(this.DetailUrlData);
        this.clubDetailUrlCreate(this.DetailUrlData);
        this.DetailUrlData.category = '';
      } else if (this.check === 'update') {
        this.clubDetailUrlUpdate(this.DetailUrlData);
      }
      this.DetailUrlData = {};
      this.OnOff();
    },
    OnOff: function() {
      this.$store.commit('clubStore/CLUB_DETAIL_URL_DIALOG', false);
      this.DetailUrlData.category = '';
    },
    validate() {
      this.$refs.form.validate();
    },
  },
};
</script>
