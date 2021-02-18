<template>
  <v-container borederd="1px">
    <section class="section">
      <div class="contentInner ml-10 mt-10">
        <h3 class="mypage_contentsTitle">
          <span class="title_text">회원 정보</span>
        </h3>
        <div>
          <div class="mypage_member">
            <!-- <div class="withdraw_wrap">
                            <div class="withdraw_box">
                                <a href="/mypage/account/withdrawal" class=""><span class="withdraw_text"><i class="zmdi zmdi-info"></i> 회원 탈퇴</span></a>
                            </div>
                        </div> -->
            <div class="mr-10" align="center">
              <div class="mypage_profileBox">
                <v-avatar class="profile_area" id="preview" size=164>
                  <img
                    v-if="modData.imageUrl"
                    :src="modData.imageUrl"
                    id="picture"
                    class="profileImg"
                  />
                </v-avatar>
              <br />
                <div class="filebox my-5">
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
              </div>
            </div>
            <div class="border-box" >
              <table height="50">
                <tr height="100">
                  <th>이메일</th>
                  <td>{{ userInfo.email }}</td>
                </tr>
                <tr>
                  <th width="120">닉네임</th>
                  <td>
                    <v-text-field
                      
                      v-model="modData.nickname"
                      solo
                      :label="userInfo.nickname"
                      clearable
                    ></v-text-field>
                  </td>
                  <td align="center" valign="top">
                    <v-btn
                      class="ml-10"
                      @click="nicknameCheck"
                      v-bind:disabled="modData.nickname.length < 1"
                      >닉네임 중복확인</v-btn
                    >
                  </td>
                </tr>
                <tr>
                  <th>나의 소개</th>
                  <td colspan="2">
                    <!-- <textarea
                      ref="toastuiEditor"
                      height="500px"
                      :initialValue="initialValue"
                    /> -->
                    <v-textarea
                      outlined
                      name="input-7-4"
                      label="나의 소개글을 입력해주세요"
                      height="150px"
                      no-resize
                      v-model="modData.introduce"
                    ></v-textarea>
                  </td>
                </tr>
                <tr>
                  <td></td>
                  <td align="center">
                    <v-btn class="mr-4" @click="modify">정보 수정</v-btn>
                  </td>
                  <td></td>
                </tr>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>
  </v-container>
</template>
<script>
import { mapState } from "vuex";

import "codemirror/lib/codemirror.css";
import "@toast-ui/editor/dist/toastui-editor.css";
import axios from "axios";
import { API_BASE_URL } from "../../config";

export default {
  components: {
  
  },
  computed: {
    ...mapState(["userInfo"]),
  },
  props: {
    image: { Type: String },
  },
  data: function() {
    return {
      modData: {
        email: null,
        nickname: null,
        introduce: null,
        imageUrl: null,
      },
      message: "",
      valid: "",
      files: null,
      flag: false,
    };
  },
  created() {
    this.modData.email = this.userInfo.email;
    this.modData.nickname = this.userInfo.nickname;
    this.modData.introduce = this.userInfo.introduce_text; //
    this.modData.imageUrl = this.image;
  },
  methods: {
    modify() {
      // this.modData.introduce = this.$refs.toastuiEditor.invoke("getMarkdown");
      this.$store.dispatch("userUpdate", this.modData);
      this.modData.imageUrl = this.$refs.imageInput.files
      if(this.flag){
        this.changeImage();
      }
      
      this.$fire({
        title: "회원 정보가 수정되었습니다.",
        type: "success",
      }).then((r) => {
        console.log(r.value);
        this.$router.push({ name: "Home" });
      });
    },
    nicknameCheck() {
      console.log(this.nickname);
      axios
        .post(`${API_BASE_URL}accounts/nickname_check/`, {
          nickname: this.modData.nickname,
        })
        .then((res) => {
          console.log('dd');
          console.log(res.data);
          if (res.data == "success") {
            this.message = "사용할 수 있는 닉네임입니다.";
            this.valid = true;
            this.successPop();
          } else {
            this.message = "이미 존재하는 닉네임입니다";
            this.errorPop();
            this.nickname = "";
          }
        })
        .catch((err) => console.log(err.response));
    },
    successPop() {
      this.$fire({
        title: `${this.message}`,
        type: "success",
      });
      this.message = "";
    },
    errorPop() {
      this.$fire({
        title: `${this.message}`,
        type: "error",
      });
      this.message = "";
    },
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      const file = e.target.files[0];
      this.modData.imageUrl = URL.createObjectURL(file);
      
      this.files = this.$refs.imageInput.files[0]
      this.flag = true;
    },
    
    changeImage() {
      const formdata = new FormData();
      formdata.append('image',this.files);
      axios
        .post(`${API_BASE_URL}accounts/profile_image/${this.userInfo.id}/`,formdata)
        .then((res) => console.log(res))
        .catch((res) => console.log(res))
    },
    
  },
};
</script>

<style>
body {
  margin: 10px;
}
.where {
  display: block;
  margin: 25px 15px;
  font-size: 11px;
  color: #000;
  text-decoration: none;
  font-family: verdana;
  font-style: italic;
}
.filebox {
  display: inline-block;
  margin-right: 10px;
}

.filebox label {
  display: inline-block;
  padding: 0.5em 0.75em;
  color: rgb(12, 1, 1);
  font-size: inherit;
  line-height: normal;
  vertical-align: middle;
  background-color: #fdfdfd;
  cursor: pointer;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 0.25em;
}

.filebox input[type="file"] {
  /* 파일 필드 숨기기 */
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.filebox.bs3-primary label {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}

.filebox.bs3-success label {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}

.profile_area {
  size: "164";
  margin: 0 auto;
  overflow: hidden;
  border: 1px solid #cdd4db;
  position: relative;
}
</style>