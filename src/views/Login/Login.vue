<template>
	<v-row class="ma-12">
		<v-card width="500" height="300" class="mx-auto pa-12">
			<v-col>
				<v-row justify="center">
					<v-text-field
						v-model="email"
						name="email"
						label="Email"
						outlined
					></v-text-field>
				</v-row>
				<v-row justify="center">
					<v-text-field
						v-model="senha"
						name="senha"
						label="Senha"
						outlined
						:type="'password'"
					></v-text-field>
				</v-row>
				<v-row align="center" justify="center">
					<v-btn large @click="login()" color="primary">Login</v-btn>
					<v-spacer></v-spacer>
					<a href="www.google.com">Esqueceu sua senha?</a>
				</v-row>
			</v-col>
		</v-card>
	</v-row>
</template>

<script src="./LoginController.js"></script>