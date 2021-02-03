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

        <!-- 에디터 기능 -->
        <v-row class="mt-7">
          <v-btn-toggle v-model="toggle_exclusive">
            <v-btn>
              <v-icon>mdi-format-align-left</v-icon>
            </v-btn>
            <v-btn>
              <v-icon>mdi-format-align-center</v-icon>
            </v-btn>
            <v-btn>
              <v-icon>mdi-format-align-right</v-icon>
            </v-btn>
            <v-btn>
              <v-icon>mdi-format-align-justify</v-icon>
            </v-btn>
          </v-btn-toggle>

          <v-col class="py-2">
            <v-btn-toggle v-model="toggle_multiple" dense background-color="primary" dark multiple>
              <v-btn>
                <v-icon>mdi-format-bold</v-icon>
              </v-btn>
              <v-btn>
                <v-icon>mdi-format-italic</v-icon>
              </v-btn>
              <v-btn>
                <v-icon>mdi-format-underline</v-icon>
              </v-btn>
              <v-btn>
                <v-icon>mdi-format-color-fill</v-icon>
              </v-btn>
            </v-btn-toggle>
          </v-col>
        </v-row>

        <!-- 내용 -->
        <v-row>
          <v-textarea
            v-model="createData.content"
            label="Text"
            rows="20"
            class="mr-tp"
          ></v-textarea>
          <v-col cols="3"></v-col>
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
          <v-btn class="" color="blue" large @click="CreateOpinion()">작성완료</v-btn>
        </v-row>
      </v-col>
      <v-col cols="1"></v-col>

      <!-- footer쓸까? -->
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  components: {},
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
      },
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

      console.log('들어옴1');
      if (this.$route.query.type === 'write') {
        this.opinionCreate(this.createData);
        this.$router.push({ name: 'Opinion' });
      } else if (this.$route.query.type === 'update') {
        this.opinionUpdate(this.createData);
        this.$router.push(`/opinionDetail?id=${this.id}`);
      }
    },
  },

  created() {
    if (this.$route.query.type === 'update') {
      this.createData = this.opinionData;
      this.id = this.opinionData.id;
      if (this.opinionData.comment_type == true) this.comment_type = '토의';
      else this.comment_type = '찬반';
    }
  },
};
</script>

<style lang="scss" scoped></style>
