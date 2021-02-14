<template>
  <v-navigation-drawer v-model="getDrawer" absolute temporary right width="50vh">
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
      </v-list-item-avatar>

      <v-list-item-content>
          <v-list-item-title>{{ nickname }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>


    <v-divider></v-divider>

    <v-btn text color="red" @click="Out">로그아웃</v-btn>

    <v-list dense>
      <v-list-item v-for="item in items" :key="item.title" link>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <button style="display:none" id="chagemenu" @click="OnOffMenu">ddd</button>
  </v-navigation-drawer>
</template>

<script>
import $ from 'jquery';
import { mapState} from 'vuex';
import axios from 'axios';
import { API_BASE_URL } from "../../config";

export default {
  computed: {
    ...mapState('index', ['userData']),
    getDrawer: {
      get: function() {
        return this.$store.state.drawer;
      },
      set: function() {},
    },
  },
  data() {
    return {
      items: [
        { title: 'Home', icon: 'mdi-view-dashboard' },
        { title: 'About', icon: 'mdi-forum' },
      ],
      nickname: '',
    }
  },
  created(){
        axios.post(`${API_BASE_URL}accounts/get_user/`, { email: localStorage.getItem('email')})
        .then((res) => {
          this.nickname = res.data.nickname
        })
        
    },

  updated() {
    // 바탕화면 누르면 vuex 값을 바꿔주기 위해
    $(document).ready(function() {
      $('.v-overlay').on('click', function() {
        $('#chagemenu').trigger('click');
      });
    });
  },
  methods: {
    Out: function() {
      this.$store.dispatch('userLogout');
      this.$store.commit('CHANGE_DRAWER', false);
    },
    OnOffMenu: function() {
      this.$store.commit('CHANGE_DRAWER', false);
    },
  },
}
</script>
