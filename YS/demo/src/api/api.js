import axios from 'axios'
// export const users = params => {return axios.get(`${base}/users`,params).then(res => res.data).catch((error) => {console.log(error)}); };

/*
* author Dave
* params 参数
* return 请求
* */
export const users = params => {return axios.get('/users/');}

export const login = params => {return axios.get('/yisheng/testlogin/',{params: params});}
// export const login = params => {return axios.get('/user/testlogin/',{params: params});}
export const getMsg = params => {return axios.get('/modeloperations/getMsg',{params: params});}
export const addMsg = params => {return axios.get('/modeloperations/addMsg',{params: params});}
export const delMsg = params => {return axios.get('/modeloperations/delMsg',{params: params});}
export const updateMsg = params => {return axios.get('/modeloperations/updateMsg',{params: params});}
export const downloadExcel = params => {return axios.get('/modeloperations/downloadExcel',{params: params},{responseType: 'blob'});}
export const uploadExcel = params => {return axios.get('/modeloperations/uploadExcel',{params: params});}
