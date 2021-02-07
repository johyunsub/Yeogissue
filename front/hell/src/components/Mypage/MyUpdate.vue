<template>
    <v-container borederd="1px">
        <section class="section">
            <div class="contentInner">
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
                        <div class="">
                            <div class="mypage_profileBox">
                                <figure class="profile_area" id="preview">
                                    <img src="https://static.some.co.kr/sometrend/images/mypage/profile/w_01.png" id="picture" class="profileImg">
                                </figure>
                                <div class="filebox">
                                    <label for="ex_file">프로필 사진 변경</label>
                                    <input type="file" id="ex_file" class="inp-img profileChage_btn" accept=".gif, .jpg, .png" onchange="test(this);">
                                </div>
                            </div>
                        </div>
                        <div class="border-box">
                            <table  height="30">
                                
                                <tr>
                                    <th>  이메일 </th>
                                    <td>  {{userInfo.email}} </td>
                                </tr>
                                <tr >
                                    <th width="100"> 닉네임 </th>
                                    <td> <v-text-field
                                        v-model="message2"
                                        solo
                                        :label="userInfo.email"
                                        clearable
                                    ></v-text-field></td>
                                </tr>
                                <tr>
                                    <th >  자기소개 </th>
                                    <td> <Editor ref="toastuiEditor" height="500px" initialEditType="wysiwyg" :initialValue="initialValue"/></td>
                                </tr>
                            </table>
                        </div>
                        <div>
                            <v-btn class="mr-4" @click="submit">정보 수정</v-btn>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </v-container>
</template>
<script>
import { mapState } from 'vuex';

import 'codemirror/lib/codemirror.css'; 
import '@toast-ui/editor/dist/toastui-editor.css';
import { Editor } from '@toast-ui/vue-editor';
export default {
    components: {
        Editor
    },
    computed: {
        ...mapState(['userData']),
    },
    data: function() {
        return {
            modData: {
                email: '',
                introduce: '',
            },            
            initialValue: '',
        };
    },
    created() {
        this.modData.email = this.userInfo.email;
        this.modData.nickname = this.userInfo.nickname;
        this.initialValue = this.userInfo.introduce;//
    },
    methods: {
        modify() {
            this.modData.introduce = this.$refs.toastuiEditor.invoke("getMarkdown");

            this.$router.push({ name: 'Mypage' });       
        },
    }
}
</script>

<style>
    body {margin: 10px}
    .where {
    display: block;
    margin: 25px 15px;
    font-size: 11px;
    color: #000;
    text-decoration: none;
    font-family: verdana;
    font-style: italic;
    } 
    .filebox {display:inline-block; margin-right: 10px;}


    .filebox label {
    display: inline-block;
    padding: .5em .75em;
    color: rgb(12, 1, 1);
    font-size: inherit;
    line-height: normal;
    vertical-align: middle;
    background-color: #fdfdfd;
    cursor: pointer;
    border: 1px solid #ebebeb;
    border-bottom-color: #e2e2e2;
    border-radius: .25em;
    }

    .filebox input[type="file"] {  /* 파일 필드 숨기기 */
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip:rect(0,0,0,0);
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
</style>