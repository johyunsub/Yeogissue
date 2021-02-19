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
                    v-model="clubCreateData.category"
                    :items="categoryItems"
                    label="카테고리"
                    outlined
                  ></v-select>
                </v-col>
                <v-col>

                 <figure class="profile_area" id="preview">
                  <img
                    v-if="image"
                    :src="image"
                    id="picture"
                    class="profileImg"
                  />
                </figure>
                  <div class="filebox">
                  <label for="ex_file">프로필 사진 변경</label>
                  <input
                    type="file"
                    ref="imageInput"
                    id="ex_file"
                    class="inp-img profileChage_btn"
                    accept=".gif, .jpg, .png"
                    @change="onChangeImages"
                  />
                </div>
                </v-col>
                <v-col cols="12">
                  <v-text-field v-model="clubCreateData.title" label="제목*"></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea v-model="clubCreateData.content" label="내용" rows="10"></v-textarea>
                </v-col>

                <!-- 공개 비공개 -->
                <div class="ml-3">
                  <!--  v-model="clubCreateData.check" -->
                  <v-radio-group row mandatory>
                    <v-radio label="공개" value="공개" @click="private_ra(false)"></v-radio>
                    <v-radio label="비공개" value="비공개" @click="private_ra(true)"></v-radio>
                  </v-radio-group>
                </div>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="createform_check()">등록</v-btn>
              <v-btn color="blue darken-1" text @click="OnOff('close')">취소</v-btn>
            </v-card-actions>
          </div>
        </v-card>
      </v-form>
    </v-dialog>
  </v-row>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import axios from "axios";
import { API_BASE_URL } from "../../config";

export default {
  data: () => ({
    valid: true,
    email: '',
    row: '',
    value: '',

    flag: false,
    btnCheck: false,
    files: null,

    image: 'https://cdn.vuetifyjs.com/images/cards/cooking.png',
    
    categoryItems: ['연예', 'IT/과학', '해외', '경제', '스포츠', '정치', '사회', '생활'],
    clubCreateData: {
      title: null,
      category: null,
      content: null,
      master: '',
      is_private: false,
      
    },
  }),
  props: {
    type: String,
  },
  computed: {
    ...mapState('clubStore', ['clubData']),
    getDialog: {
      get: function() {
        return this.$store.state.clubStore.clubDialog;
      },
      set: function() {},
    },
  },

  methods: {
    ...mapActions('clubStore', ['clubUpdate', 'clubCreate']),
    ClubCreate() {
      if (this.type == 'create') {
        this.clubCreateData.master = this.$store.state.userInfo.id;
        this.clubCreate(this.clubCreateData);
        
        this.clubCreateData = {};
        


      } else if (this.type == 'update') {
        this.clubUpdate(this.clubCreateData);
        this.clubCreateData = {};
        this.flag = false;
        this.changeImage()
      }

      this.OnOff('create');
    },
    OnOff(check) {
      if (check == 'create') this.btnCheck = false;
      else if (check == 'close') this.btnCheck = true;

      this.$store.commit('clubStore/CLUB_CREATE_DIALOG', false);
      if (check == 'create') this.$router.go(this.$router.currentRoute);
    },
    validate() {
      this.$refs.form.validate();
    },
    typeCheck() {
      return { ddd: this.type };
    },

    private_ra(check) {
      this.clubCreateData.is_private = check;
    },
    changeImage() {
      const formdata = new FormData();
      formdata.append('image',this.files);
      axios
        .post(`${API_BASE_URL}club/club_image/${this.clubData.id}/`,formdata)
        .then(() => this.$router.push(`/clubDetail?id=${this.clubData.id}`))
        .catch((res) => console.log(res))
    },
    onChangeImages(e) {
      const file = e.target.files[0];
      this.image = URL.createObjectURL(file);
      
      this.files = this.$refs.imageInput.files[0]
      
    },
    createform_check() {
      if (this.clubCreateData.category === null) {
        alert("카테고리를 선택해주세요");
        return; 
      }

      if (this.clubCreateData.title === null) { 
        alert("제목을 입력해주세요");
        return; 
      }
      if (this.clubCreateData.content === null) { 
        alert("내용을 입력해주세요");
        return; 
      }
      this.ClubCreate();   
    },
  },

  updated() {
    if (this.typeCheck().ddd == 'update' && this.flag == false && this.btnCheck == false) {
      console.log('하이');
      this.clubCreateData.title = this.clubData.title;
      this.clubCreateData.category = this.clubData.category;
      this.clubCreateData.content = this.clubData.content;
      this.clubCreateData.user = this.clubData.master;
      this.flag = true;
    }
  },
};
</script>

<style>
.bo-ra {
  border: 1px solid b;
}
</style>
