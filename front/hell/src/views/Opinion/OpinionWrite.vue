<template>
    <v-container>
        <v-row class="mr-tp">
        <v-col cols="2"></v-col>
            <v-col>
            <v-row class="mr-tp"> 
                <v-col
                    class="d-flex"
                    sm="2"
                >
                    <v-select
                    :items="items"
                    label="카테고리"
                    solo
                    ></v-select>
                </v-col>
                <v-col
                class="py-2"
                >
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
                </v-col>

                <v-col
                sm="3"
                class="py-2"
                >
                <v-btn-toggle
                    v-model="toggle_multiple"
                    dense
                    background-color="primary"
                    dark
                    multiple
                >
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

            <!-- 제목란 -->
            <v-row>
                <v-text-field
                    label="제목"
                    :rules="rules"
                    hide-details="auto"
                    width=""
                    ></v-text-field>
                <v-col cols="3"></v-col>
            </v-row>
            <!-- 내용 -->
            <v-row>
                <v-textarea
                label="Text"
                rows="20"
                :value="value"
                class="mr-tp"
                ></v-textarea>
                <v-col cols="3"></v-col>
            </v-row>

            <!-- 해시태그 -->
            <v-row class="mr-tp">#해시태그</v-row>
            <v-row>
                <v-text-field
                    label="해시태그"
                    :rules="rules"
                    hide-details="auto"
                    width=""
                    ></v-text-field>
                <v-col cols="3"></v-col>
            </v-row>
            <v-row class="mr-tp">
                    <v-chip-group
                    mandatory
                    active-class="primary--text"
                    >
                    <v-chip
                        v-for="tag in tags"
                        :key="tag"
                    >
                        {{ tag }}
                    </v-chip>
                    </v-chip-group>
                <v-col cols="4"></v-col>
            </v-row>
            </v-col>
        <v-col cols="1"></v-col>

        <!-- footer쓸까? -->
        </v-row>
      </v-container>
</template>

<script>

export default {
  components : {},
  data: function() {
    return {
        category : 'dd',
        items: ['연예', 'IT/과학', '사회', '스포츠'],
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
  methods:{

  },
}
</script>

<style lang="scss" scoped>

</style>