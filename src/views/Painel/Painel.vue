<template>
    <div>
        <v-row class="ma-12">
            <v-card width="500" height="550" class="mx-auto pa-12">
			<v-col>
				<v-row justify="center">
					<v-text-field
						v-model="objetoCampos.displayHost"
                        name="host"
						label="Host"
						outlined
						:disabled="objetoCampos.display"
					></v-text-field>
				</v-row>
                <v-row justify="center">
					<v-text-field
						v-model="objetoCampos.displayUser"
                        name="user"
						label="Usuário"
						outlined
						:disabled="objetoCampos.display"
					></v-text-field>
				</v-row>
				<v-row justify="center">
					<v-text-field
						v-model="objetoCampos.displaySenha"
                        name="name"
						label="Senha"
						outlined
						:type="'password'"
						:disabled="objetoCampos.display"
					></v-text-field>
				</v-row>
				<v-row justify="center">
					<v-textarea
					v-model="objetoCampos.displayToken"
                    outlined
                    name="token"
                    label="Token"
					:disabled="objetoCampos.display"
                    ></v-textarea>
				</v-row>
                <v-row justify="space-between">
				    <v-btn 
					large 
					color="primary"
					@click="desabilitarDisplay()"
					:disabled="objetoCampos.displayConfigurar"
					>Configurar</v-btn>

					<v-btn 
					large
					class="white--text" 
					color="deep-orange"
					@click="habilitarDisplay()"
					:disabled="objetoCampos.displayParar"
					>Parar</v-btn>
                </v-row>
			</v-col>
		</v-card>
        <v-card width="500" height="500" class="mx-auto pa-12">
                <v-col>
                    <v-row justify="center">
                        <v-img
                        src="../../../public/qrcode.svg"
                        ></v-img>
                    </v-row>
                </v-col>
            </v-card>
        </v-row>
    </div>
</template>

<script src="./PainelController.js"></script>