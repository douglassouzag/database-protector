<template>
    <div>
		<v-row class="ma-12" justify="center" v-if="alertaSucesso.msg">
			<v-alert
			color="green"
			dark
			border="top"
			icon="mdi-alert-box"
			transition="scale-transition"
			>
			{{alertaSucesso.msg}}
			</v-alert>
		</v-row>
		<v-row class="ma-12" justify="center" v-if="alertaErro.msg">
			<v-alert
			color="red"
			dark
			border="top"
			icon="mdi-alert-box"
			transition="scale-transition"
			>
			{{alertaErro.msg}}
			</v-alert>
		</v-row>
        <v-row class="ma-12" justify="space-between">
            <v-card width="500" class="mx-auto pa-12" name="cardAdm">
				<v-card-title class="justify-center">Conexão de Administrador</v-card-title>
				<v-col>
					<v-row justify="center">
						<v-text-field
							v-model="formularioADM.inputHost"
							name="host"
							label="Host"
							outlined
							:disabled="formularioADM.input"
						></v-text-field>
					</v-row>
					<v-row justify="center">
						<v-text-field
							v-model="formularioADM.inputUser"
							name="user"
							label="Usuário"
							outlined
							:disabled="formularioADM.input"
						></v-text-field>
					</v-row>
					<v-row justify="center">
						<v-text-field
							v-model="formularioADM.inputSenha"
							name="name"
							label="Senha"
							outlined
							:type="'password'"
							:disabled="formularioADM.input"
						></v-text-field>
					</v-row>
					<v-row justify="center">
						<v-textarea
						v-model="formularioADM.inputToken"
						outlined
						name="token"
						label="Token"
						:disabled="formularioADM.input"
						></v-textarea>
					</v-row>
					<v-row justify="space-between">
						<v-btn 
						large 
						color="primary"
						@click="desabilitarInputADM()"
						:disabled="formularioADM.inputConfigurar"
						>Configurar</v-btn>

						<v-btn 
						large
						class="white--text" 
						color="deep-orange"
						@click="habilitarInputADM()"
						:disabled="formularioADM.inputParar"
						>Editar</v-btn>
					</v-row>
				</v-col>
			</v-card>
			<v-card width="500" class="mx-auto pa-12" name="cardDEV">
			<v-card-title class="justify-center">Conta de Desenvolvimento</v-card-title>
				<v-col>
					<v-row justify="center">
						<v-text-field
							v-model="formularioDEV.inputHost"
							name="host"
							label="Host"
							outlined
							:disabled="formularioDEV.input"
						></v-text-field>
					</v-row>
					<v-row justify="center">
						<v-text-field
							v-model="formularioDEV.inputUser"
							name="user"
							label="Usuário"
							outlined
							:disabled="formularioDEV.input"
						></v-text-field>
					</v-row>
					<v-row justify="center">
						<v-text-field
						v-model="formularioDEV.inputConnName"
						outlined
						name="nome-conn"
						label="Nome da conexão"
						:disabled="formularioDEV.input"
						></v-text-field>
					</v-row>
					<v-row justify="center">
						<v-text-field
						v-model="formularioDEV.inputEmail"
						outlined
						name="email"
						label="Email"
						:disabled="formularioDEV.input"
						></v-text-field>
					</v-row>
					<v-row justify="space-between">
						<v-btn 
						large 
						color="primary"
						@click="desabilitarInputDEV()"
						:disabled="formularioDEV.inputConfigurar"
						>Configurar</v-btn>

						<v-btn 
						large
						class="white--text" 
						color="deep-orange"
						@click="habilitarInputDEV()"
						:disabled="formularioDEV.inputParar"
						>Editar</v-btn>
					</v-row>
				</v-col>
			</v-card>
        </v-row>
		<v-divider></v-divider>
		<v-row class="ma-12" justify="center">
			<v-card>
				<v-row justify="space-between">	
					<v-btn :disabled="formulatorioAPI.botaoParar" @click="iniciar()">
						Iniciar
					</v-btn>
					<v-spacer></v-spacer>
					<v-btn :disabled="formulatorioAPI.botaoLigar" @click="parar()">
						Parar
					</v-btn>
				</v-row>
			</v-card>
		</v-row>
		<v-row justify="center" name="barraProgresso" v-if="formulatorioAPI.botaoParar">
			 <v-col
			class="subtitle-1 text-center"
			cols="12"
			>
			</v-col>
			<v-col cols="6">
			<v-progress-linear
				color="deep-purple accent-4"
				indeterminate
				rounded
				height="6"
			></v-progress-linear>
			</v-col>
		</v-row>
		<v-row class="ma-12" justify="center">
			<v-card>
				<v-img src="../../../public/qrcode.svg">

				</v-img>
			</v-card>
		</v-row>
    </div>
</template>

<script src="./PainelController.js"></script>