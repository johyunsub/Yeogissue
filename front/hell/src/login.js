import axios from '@/services/axios';

const kakaoHeader = {
    'Authorization': '8d78badd27d67f4a24eca70c6344d858',
    'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
};

const getKakaoToken = async (code) => {
    console.log('loginWithKakao');
    try {
        const data = {
            grant_type: 'authorization_code',
            client_id: 'b6579181daf5eca8f6d24674d64cc6f3',
            redirect_uri: 'http://localhost:8080/auth',
            code: code,
        };
        const queryString = Object.keys(data)
            .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(data[k]))
            .join('&');
        const result = await axios.post('https://kauth.kakao.com/oauth/token', queryString, { headers: kakaoHeader });
        console.log('카카오 토큰', queryString);
        return result;
    } catch (e) {
        return e;
    }
};
const getKakaoUserInfo = async () => {
    let data = '';
    await window.Kakao.API.request({
        url: "/v2/user/me",
        success: function (response) {
            data = response;
        },
        fail: function (error) {
            console.log(error);
        },
    });
    console.log('카카오 계정 정보', data);
    return data;
}

const getGoogleToken = (googleUser) => {
    console.log('test');
    var profile = googleUser.getBasicProfile();
    console.log('ID Token: ', googleUser.getAuthResponse().id_token);
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
};


const emailService = () => {
    const emailLogin = async (email, password) => {
        const data = {
            email,
            password,
        };
        const result = await axios.post('/emailLogin', data);
        console.log(result);
    };
    return {
        emailLogin,
    };
};
export {
    getKakaoToken,
    getKakaoUserInfo,
    emailService,
};