<template>
  <v-container>
    <v-row class="mr-tp mb-10">
      <v-col cols="3"></v-col>
      <v-col>
        <v-row class="mr-tp">
          <v-col class="d-flex" sm="2">
            <v-select
              v-model="createData.category"
              :items="categoryItems"
              label="카테고리"
              solo
            ></v-select>
          </v-col>
          <v-col class="d-flex" sm="2">
            <v-select
              v-model="comment_type"
              :items="commentItems"
              label="댓글 형태"
              solo
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
        <v-row class="mr-tp">#해시태그</v-row>
        <v-row>
          <v-text-field label="해시태그" hide-details="auto" width=""></v-text-field>
          <v-col cols="3"></v-col>
        </v-row>
        <v-row class="mr-tp">
          <v-chip-group mandatory active-class="primary--text">
            <v-chip v-for="tag in tags" :key="tag">
              {{ tag }}
            </v-chip>
          </v-chip-group>
          <v-col cols="4"></v-col>
        </v-row>

        <v-row class="mt-10">
          <v-btn class="" color="blue" large @click="createform_check">작성완료</v-btn>
        </v-row>

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
    ...mapState('opinionStore', ['opinionData']),
  },
  data: function() {
    return {
      createData: {
        title: null,
        content: null,
        comment_type: true,
        category: null,
        //미정
        user: 1,
        name: '나에용',
      },
      initialValue: '',
      id: '',
      comment_type: '',
      toggle_multiple: '',
      toggle_exclusive: '',

      categoryItems: ['연예', 'IT/과학', '해외', '경제', '스포츠', '정치', '사회', '생활'],
      commentItems: ['토의', '찬반'],

      tags: [
        'Work',
        'Home Improvement',
        'Vacation',
        'Food',
        'Drawers',
        'Shopping',
        'Art',
        'Tech',
        'Creative Writing',
      ],
    };
  },
  methods: {
    ...mapActions('opinionStore', ['opinionCreate', 'opinionUpdate']),
    CreateOpinion: function() {
      if (this.comment_type == '토의') this.createData.comment_type = true;
      else this.createData.comment_type = false;

      this.createData.content = this.$refs.toastuiEditor.invoke("getMarkdown");  

      console.log('들어옴1');

      if (this.$route.query.type === 'write') {
        this.opinionCreate(this.createData);
        console.log(this.createData.content);
        this.$router.push({ name: 'Opinion' });
      } else if (this.$route.query.type === 'update') {
        this.opinionUpdate(this.createData);
        this.$router.push(`/opinionDetail?id=${this.id}`);
      }
      

    },

    createform_check() {
      //변수에 담아주기
      
      // var uid = document.getElementById("uid");
      
      if (this.createData.category === '') { //해당 입력값이 없을 경우 같은말: if(!uid.value)
        alert("카테고리를 선택해주세요");
        //uid.focus(); //focus(): 커서가 깜빡이는 현상, blur(): 커서가 사라지는 현상
        return; //return: 반환하다 return false:  아무것도 반환하지 말아라 아래 코드부터 아무것도 진행하지 말것
      }

      if (this.createData.comment_type === '') { 
        alert("댓글 형태를 선택해주세요");
        return; 
      }

      if (this.createData.title === '') { 
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
    }
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


