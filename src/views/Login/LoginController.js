import firebase from 'firebase'

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
        login: function() {
            firebase.auth().signInWithEmailAndPassword(this.email, this.senha).then(
              (user) => {
                this.$router.replace('painel')
                alert(`Bem Vindo, ${{email}}`)
              },
              (err) => {
                alert('Não foi possível realizar o login. ' + err.message)
              }
            );
        },
        async criarConta () {
            firebase.auth().createUserWithEmailAndPassword(this.email, this.senha).then(
            (user) => {
              this.$router.replace('painel')
                this.$notify.success('Sua conta foi criada com sucesso!')
                },
            (err) => {
                this.$notify.error('Aconteceu algo inesperado. ' + err.message)
                }
            )
        },
        async esqueciSenha () {
            return firebase.auth().sendPasswordResetEmail(this.email).then(() => {
                this.$notify.success('Você receberá um email para trocar sua senha!')
            }).catch((error) => {
                this.$notify.error(error)
            })
        },
    },
}
