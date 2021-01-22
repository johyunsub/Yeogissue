import { createInstance } from "./index.js";

const instance = createInstance();
// const config = {
//   headers: { "access-token": localStorage.getItem("access-token") }
// };

function login(user, success, fail) {
  instance.defaults.headers["access-token"] = window.localStorage.getItem(
    "access-token"
  );
  const body = {
    userid: user.userid,
    userpwd: user.userpwd
  };

  instance
    .post("user/confirm/login", JSON.stringify(body))
    .then(success)
    .catch(fail);
}

async function findById(userid, success, fail) {
  instance.defaults.headers["access-token"] = window.localStorage.getItem(
    "access-token"
  );
  await instance
    .get(`/user/info/${userid}`)
    .then(success)
    .catch(fail);
}

export { login, findById };
