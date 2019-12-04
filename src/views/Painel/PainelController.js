import Api from '../../services/api'

export default {
    components: {

    },
    data () {
      return {
        alertaErro: {
          msg: null
        },
        alertaSucesso:{
          msg: null
        },
        formularioDEV: {
          inputConfigurar: false,
          inputParar: true,
          inputHost: null,
          inputUser: null,
          inputSenha: null,
          inputToken: null,
          input: false,
        },
        formularioADM: {
          inputConfigurar: false,
          inputParar: true,
          inputHost: null,
          inputUser: null,
          inputSenha: null,
          inputToken: null,
          input: false,
        },
        formulatorioAPI:{
          botaoParar: false,
          botaoLigar: true,
        }
      }
    },
    methods: {
       desabilitarInputADM(){
        this.formularioADM.input=true;
        this.formularioADM.inputParar=false;
        this.formularioADM.inputConfigurar=true;

        Api.configADM(this.formularioADM.inputHost,this.formularioADM.inputUser,this.formularioADM.inputSenha).then(resposta =>{
          this.alertaErro.msg = resposta.data.erro;
          this.alertaSucesso.msg = resposta.data.sucesso;
        })
       },
       habilitarInputADM(){
        this.formularioADM.input=false;
        this.formularioADM.inputConfigurar=false;
        this.formularioADM.inputParar=true;
       },
       desabilitarInputDEV(){
        this.formularioDEV.input=true;
        this.formularioDEV.inputParar=false;
        this.formularioDEV.inputConfigurar=true;
        },
        habilitarInputDEV(){
        this.formularioDEV.input=false;
        this.formularioDEV.inputConfigurar=false;
        this.formularioDEV.inputParar=true;
        },
        iniciar(){
          this.formulatorioAPI.botaoParar = true;
          this.formulatorioAPI.botaoLigar = false;
        },
        parar(){
          this.formulatorioAPI.botaoParar = false;
          this.formulatorioAPI.botaoLigar = true;
        }
    },
}
