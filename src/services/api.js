import { http } from './config'

export default{
    iniciar:() => {
        const formData = new FormData()
        return http.post('iniciar',formData,{withCredentials: true})
    },
    desativar:() => {
        const formData = new FormData()

        return http.post('desativar',formData,{withCredentials: true})
    },
    configADM:(host,user,password) => {
        const formData = new FormData()
        formData.append('host', host);
        formData.append('user', user);
        formData.append('password', password);
        return http.post('configadm', formData,{withCredentials: true})
    },
    configDEV:(user,host,nome_con,email) => {
        const formData = new FormData()
        formData.append('host', host);
        formData.append('user', user);
        formData.append('nome-con', nome_con);
        formData.append('email', email);
        return http.post('configdev', formData,{withCredentials: true})
    },
    login:(email,password) => {
        const formData = new FormData()
        formData.append('user', email);
        formData.append('password', password);
        return http.post('login',formData,{withCredentials: true})
    },
    teste:() => {
        return http.get('teste')
    }

}