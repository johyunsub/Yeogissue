import { createInstance } from './index.js';

const instance = createInstance();
// const config = {
//   headers: { "access-token": localStorage.getItem("access-token") }
// };

function listComment(articleno, success, fail) {
  instance
      .get(`memo/${articleno}`)
    .then(success)
    .catch(fail);
}

function registerComment(memo, success, fail) {
  instance
    .post(`memo`, JSON.stringify(memo))
    .then(success)
    .catch(fail);
}
function modifyComment(memo, success, fail) {
  instance
    .put(`memo`, JSON.stringify(memo))
    .then(success)
    .catch(fail);
}

function deleteComment(articleno, memono, success, fail) {
  instance
    .delete(`memo/${articleno}/${memono}`)
    .then(success)
    .catch(fail);
}

export {
  listComment,
  registerComment,
  modifyComment,
  deleteComment,
};
