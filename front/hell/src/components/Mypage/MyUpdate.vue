<template>
    <v-container borederd="1px">
        <section class="section">
            <div class="contentInner">
                <h3 class="mypage_contentsTitle">
                    <span class="title_text">회원 정보</span>
                </h3>
                <div>
                    <div class="mypage_member">
                        <div class="withdraw_wrap">
                            <div class="withdraw_box">
                                <a href="/mypage/account/withdrawal" class=""><span class="withdraw_text"><i class="zmdi zmdi-info"></i> 회원 탈퇴</span></a>
                            </div>
                        </div>
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
                                    <tr ><!-- 첫번째 줄 시작 -->
                                        <th width="100"> 닉네임 </th>
                                        <td> 안동동동</td>
                                    </tr><!-- 첫번째 줄 끝 -->
                                    <tr><!-- 두번째 줄 시작 -->
                                        <th>  이메일 </th>
                                        <td>  popo@na.com </td>
                                    </tr>
                                    <tr rowspan="2">
                                        <th >  자기소개 </th>
                                        <td>  안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하안녕하세요안녕하세요안녕하안녕하세요안녕하세요안녕하안녕하세요안녕하세요안녕하안녕하세요안녕하세요안녕하안녕하세요안녕하세요안녕하세요 </td>
                                        
                                    </tr>
                                    <tr>
                                        
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
export default {
    
}
</script>

<html>
  
</html>