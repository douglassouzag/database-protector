import { http } from './config'

export default{
    iniciar:() => {
        return http.post('iniciar')
    },
    parar:() => {
        return http.post('parar')
    },
    configADM:(host,user,password) => {
        const formData = new FormData()
        formData.append('host', host);
        formData.append('user', user);
        formData.append('password', password);
        console.log(formData);
        return http.post('configadm', formData)
    },
    configDEV:(user,host,nome_con,email) => {
        return http.post('configdev')
    },
    login:(user,login) => {
        return http.post('login')
    },
    teste:() => {
        return http.get('teste')
    }

}