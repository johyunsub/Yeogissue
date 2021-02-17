<template>
  <v-container>
    <v-row class="mr-tp mb-10">
      <v-col cols="3"></v-col>
      <v-col>
        <v-row class="mr-tp mx-auto mr-5">
          <v-col class="d-flex" sm="3">
            <v-select
              v-model="createData.category"
              :items="categoryItems"
              label="카테고리"
              solo
              rounded
            ></v-select>
          </v-col>
          <v-col class="d-flex" sm="3">
            <v-select
              v-model="comment_type"
              :items="commentItems"
              label="댓글 형태"
              solo
              rounded
            ></v-select>
          </v-col>
        </v-row>

        <!-- 제목란 -->
        <v-row>
          <v-text-field
            v-model="createData.title"
            label="제목"
            hide-details="auto"
            width=""
          ></v-text-field>
          <v-col cols="3"></v-col>
        </v-row>

        <!-- 내용 -->
        <v-row class="mt-7">

          <Editor ref="toastuiEditor" height="500px" initialEditType="wysiwyg" :initialValue="initialValue"/>
          
        </v-row>

        <!-- 해시태그 -->
        <v-sheet height="7vh" lighten-5></v-sheet>
        <v-row>
        <v-tooltip right>
        <template v-slot:activator="{ on, attrs }">
           <v-btn color="pink" rounded outlined medium @click="hashtag_suggest" v-bind="attrs" v-on="on">해시태그 추천</v-btn>
        </template>
        <span
          >입력된 글을 분석하여, 해당 문서에 중요하게 작용하는 키워드를 추출해드립니다.</span>
      </v-tooltip>
        
        </v-row>
        <v-row>
          <v-text-field v-model="input_tag" @keypress.enter="createHashtags" label="해시태그 입력 후 엔터로 등록해주세요 :) (최대 10개)" hide-details="auto" width=""></v-text-field>
          <v-col cols="3"></v-col>
        </v-row>
        <v-row class="mr-tp">
          <v-chip-group mandatory active-class="primary--text">
            <v-chip v-for="(tag,index) in tags" :key="tag" close @click:close="hashtag_delete(index)"> 
              {{ tag }}
            </v-chip>
            <!-- <h1>tags</h1   > -->
          </v-chip-group>
          <v-col cols="4"></v-col>
        </v-row>

          <div cols="4" class="" style="text-align : center">
            <!-- <v-spacer></v-spacer> -->
            <v-btn  color="blue" rounded large  @click="createform_check">
              <span style="color: white;"> 작성완료 </span></v-btn>
            
          </div>

      </v-col>
      <v-col cols="1"></v-col>

      <!-- footer쓸까? -->
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import 'codemirror/lib/codemirror.css'; 
import '@toast-ui/editor/dist/toastui-editor.css';
import { Editor } from '@toast-ui/vue-editor';


export default {
  components: {
    Editor
  },
  computed: {
    ...mapState('opinionStore', ['opinionData','hashtags']),
  },
  data: function() {
    return {
      createData: {
        title: null,
        content: null,
        comment_type: true,
        category: null,
        //미정
        user: '',
        name: [],
        club_pk:'',
      },
      initialValue: '',
      id: '',
      comment_type: '',
      toggle_multiple: '',
      toggle_exclusive: '',

      categoryItems: ['연예', 'IT/과학', '해외', '경제', '스포츠', '정치', '사회', '생활'],
      commentItems: ['토의', '찬반'],

      tags: [],
      input_tag : '',
    };
  },
  methods: {
    ...mapActions('opinionStore', ['opinionCreate', 'opinionUpdate','getHashtag']),
    CreateOpinion: function() {
      if (this.comment_type == '토의') this.createData.comment_type = true;
      else this.createData.comment_type = false;
      this.createData.club_pk = this.$route.query.club_pk;
      this.createData.content = this.$refs.toastuiEditor.invoke("getMarkdown");
      this.createData.name = this.tags;

      console.log('들어옴 ' + this.$store.state.userInfo.id);

      this.createData.user = this.$store.state.userInfo.id;
      if (this.$route.query.type === 'write') {
        this.opinionCreate(this.createData);
        console.log(this.createData.content, this.club_pk);
        if (this.createData.club_pk == '0') {
          console.log(this.$route.query.club_pk,'2121212121212');
          this.$router.push({ name: 'Opinion' });
        }
        else {
          console.log(this.$route.query.club_pk,'121221121212');
          this.$router.push(`/clubDetail?id=${this.createData.club_pk}`);
        }
      } else if (this.$route.query.type === 'update') {
        this.opinionUpdate(this.createData);
        this.$router.push(`/opinionDetail?id=${this.id}`);
      }
      

    },

    createform_check() {
      //변수에 담아주기
      // console.log("ada" + this.createData.category)
      // var uid = document.getElementById("uid");
      
      if (this.createData.category === null) { //해당 입력값이 없을 경우 같은말: if(!uid.value)
        alert("카테고리를 선택해주세요");
        //uid.focus(); //focus(): 커서가 깜빡이는 현상, blur(): 커서가 사라지는 현상
        return; //return: 반환하다 return false:  아무것도 반환하지 말아라 아래 코드부터 아무것도 진행하지 말것
      }

      if (this.createData.comment_type === null) { 
        alert("댓글 형태를 선택해주세요");
        return; 
      }

      if (this.createData.title === null) { 
        alert("제목을 입력해주세요");
        return; 
      }

      // if (this.createData.content === null) { 
      //   alert("내용을 선택해주세요");
      //   return; 
      // }
      //입력 값 전송
      this.CreateOpinion(); //유효성 검사의 포인트  
      console.log('폼체크'); 
    },
    hashtag_suggest() {
      this.createData.content = this.$refs.toastuiEditor.invoke("getMarkdown");
      this.getHashtag(this.createData);
      console.log(this.createData.content);
      this.tags = this.hashtags.keyword;
      
      console.log('this.tags');
      console.log(this.tags);
    },
    createHashtags: function () {
      this.tags.push(this.input_tag);
      console.log(this.tags);
      this.input_tag = '';
  },
    hashtag_delete: function (index) {
      console.log(index)
      this.tags.splice(index,1);
      console.log(this.tags);
    },
  },
 

  created() {
    if (this.$route.query.type === 'update') {
      this.createData = this.opinionData;
      this.id = this.opinionData.id;
      this.initialValue = this.opinionData.content;
      if (this.opinionData.comment_type == true) this.comment_type = '토의';
      else this.comment_type = '찬반';
    }
  },

};
</script>

<style lang="scss" scoped></style>


