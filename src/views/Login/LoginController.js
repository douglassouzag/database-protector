import Api from '../../services/api'

export default {
    components: {

    },
    data () {
      return {
          email: '',
          senha: '',
      }
    },
    methods: {
      login(){
        Api.login(this.email,this.senha);
        this.$router.push('painel');           
      },
    }
}
