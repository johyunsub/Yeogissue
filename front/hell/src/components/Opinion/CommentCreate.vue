<template>
  <v-card class="mr-tp mb-5" max-width="1000" outlined>
    <v-row>
      <v-col cols="auto" class="mr-auto"
        ><v-card-title class="ml-2 subtitle-1">{{ userInfo.nickname }}님!</v-card-title>
      </v-col>
      <div v-if="opinionData.comment_type == false">
        <v-col cols="auto" class="mr-2"
          ><v-radio-group row mandatory>
            <v-radio label="찬성" selected @click="private_ra(true)"></v-radio>
            <v-radio label="반대" @click="private_ra(false)"></v-radio> </v-radio-group
        ></v-col>
      </div>
    </v-row>

    <div class="mt-plus">
      <v-card-text>
        <!-- 등록 -->
        <v-textarea
          v-model="content"
          append-icon="mdi-comment"
          class="mx-2"
          :label="massage"
          rows="3"
          auto-grow
        ></v-textarea>
        <v-row>
          <v-col cols="auto" class="mr-auto"> </v-col>
          <v-col cols="auto" class="mr-2">
            <v-btn @click="CommentCreate"> 등록</v-btn>
            <v-btn class="ml-2" v-if="type == 'update'" @click="change"> 취소</v-btn></v-col
          >
        </v-row>
      </v-card-text>
    </div>
  </v-card>
</template>

<script>
import axios from "axios";
import { mapState, mapActions } from "vuex";
import { API_BASE_URL } from "../../config";
import Swal from "sweetalert2";

export default {
  props: {
    type: { Type: String },
    propContent: { Type: String },
    no: { Type: Number },
  },
  computed: {
    ...mapState(["isLoginToken", "userInfo"]),
    ...mapState("opinionStore", ["opinionData"]),
  },
  data() {
    return {
      content: this.propContent,
      massage: "댓글을 입력하세요", // 로그인에 따라 내용 바꿔주고 disabled
      createData: {
        opinion_type: true, // 찬반 추후 수정
        content: "",
        user: 0, // 찬한 추후 수정
        emotion: "",
      },
    };
  },
  methods: {
    ...mapActions("opinionStore", ["opinionCommentEmotion", "opinionCommentUpdate",'opinionCommentCreate']),
    CommentCreate() {
      if (this.isLoginToken == "") {
        this.$store.commit("CHANGE_DIALOG", true);
        return;
      }

      this.createData.content = this.content;
      this.createData.user = this.$store.state.userInfo.id;

      axios
        .post(`${API_BASE_URL}articles/emotion_comment/`, this.createData)
        .then((res) => {
          if (res.data.emotion == "분노" || res.data.emotion == "혐오") {
            Swal.fire({
              title: "화가 많아보이는 댓글입니다. 그대로 저장하시겠습니까?",
              showCancelButton: true,
              confirmButtonText: `Save`,
            }).then((result) => {
              if (result.isConfirmed) {
                Swal.fire("Saved!", "", "success");
                if (this.type == "create") {
                  this.opinionCommentCreate(res.data);
                  this.content = "";
                }

                if (this.type == "update")
                  this.opinionCommentUpdate({
                    data: res.data,
                    no: this.no,
                  });
                this.change();
              }
            });
          } else {
            console.log("댓글 정보",res.data);
            if (this.type == "create") {
              this.opinionCommentCreate(res.data);
              this.content = "";
            }

            if (this.type == "update")
              this.opinionCommentUpdate({
                data: res.data,
                no: this.no,
              });
            this.change();
          }
        })
        .catch((err) => console.log(err.response));
    },

    change() {
      this.$emit("CommentDown");
    },

    private_ra(check) {
      this.createData.opinion_type = check;
    },
  },

  created() {},
};
</script>

<style>
.mt-plus {
  margin-top: -40px;
}
</style>
