<template>
   <v-card width="60%" outlined class="mr-rt">
    <v-tabs
      v-model="tab"
      background-color="#C8E6C9"
      dark
    >
      <v-tab
        v-for="item in items"
        :key="item.tab"
      >
        {{ item.tab }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="item in items"
        :key="item.tab"
      >
        <v-card flat>
          <v-card-text v-for="(con, j) in item.content" :key="con.tab" > {{j}}. {{ con }}</v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
import axios from "axios";

  export default {
    data () {
      return {
        tab: null,
        items: [
          { tab: '연예', content: ['Tab 1 Content', 'Tab 1 Content','Tab 1 Content','Tab 1 Content', 'Tab 1 Content']},
          { tab: 'IT/과학', content: ['Tab 1 Content', 'Tab 1 Content','Tab 1 Content','Tab 1 Content', 'Tab 1 Content']},
          { tab: '해외', content: ['Tab 1 Content', 'Tab 1 Content','Tab 1 Content','Tab 1 Content', 'Tab 1 Content']},
          { tab: '경제', content: ['Tab 1 Content', 'Tab 1 Content','Tab 1 Content','Tab 1 Content', 'Tab 1 Content']},

        //   { tab: '스포츠', content: 'Tab 5 Content' },
        //   { tab: '정치', content: 'Tab 6 Content' },
        //   { tab: '사회', content: 'Tab 7 Content' },
        //   { tab: '생활', content: 'Tab 8 Content' },
        ],
      }
    },
    created(){
        const json = JSON.stringify({
            "key": "6c620248-b652-4d3a-bdca-0991812f5ab8",
            "serviceId": "11484686567",
            "argument": {
                "date": "2020-07-01",
                "category": "ENTERTAINMENT"
            }
        });

        axios.post('http://svc.saltlux.ai:31781', json, { headers: {'Content-Type': 'application/json',
                                                                    }})
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
        }
  }
</script>