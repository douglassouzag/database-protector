export default {
    components: {

    },
    data () {
      return {
        objetoCampos: {
            displayConfigurar: false,
            displayParar: true,
            displayHost: null,
            displayUser: null,
            displaySenha: null,
            displayToken: null,
            display: false,
        }
      }
    },
    methods: {
       desabilitarDisplay(){
           this.objetoCampos.display=true;
           this.objetoCampos.displayParar=false;
           this.objetoCampos.displayConfigurar=true;
       },
       habilitarDisplay(){
        this.objetoCampos.display=false;
        this.objetoCampos.displayConfigurar=false;
        this.objetoCampos.displayParar=true;
       },
    },
}
