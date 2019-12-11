import pyqrcode
import pyotp
#GERA UM QRCODE.SVG NA PASTA DO ARQUIVO
def gerarQRCode(url):
    print('[AUTHENTICATOR]Gerando código QR no diretório do script...')
    try:
        url = pyqrcode.create(url) 
        svg = url.svg("qrcode.svg", scale = 8)
        print('[AUTHENTICATOR]Código QR gerado com sucesso!')
        return svg
    except Exception as e:
        print('[AUTHENTICATOR]Não foi possivel gerar o código QR...')
        print('[AUTHENTICATOR]:',e)
#RETORNA UMA BASE32
def gerarBase32():
    print('[AUTHENTICATOR]Gerando base32 aléatoria...')
    try:
        base32 = pyotp.random_base32()
        print('[AUTHENTICATOR]Base32 gerada com sucesso!')
        return base32
    except Exception as e:
        print('[AUTHENTICATOR]Não foi possivel gerar a base32...')
        print('[AUTHENTICATOR]:',e)

#CRIA LINK DE ACESSO
def gerarLinkAcessoQR(base32,email,nome):
    print('[AUTHENTICATOR]Gerando link de acesso para a senha...')
    try:
        link_acesso = pyotp.totp.TOTP(base32).provisioning_uri(email, issuer_name=nome)
        print('[AUTHENTICATOR]Link de acesso para a senha gerado!')
        return link_acesso
    except Exception as e:
        print('[AUTHENTICATOR]Não foi possivel gerar o link...')
        print('[AUTHENTICATOR]:',e)

#CRIA OBJETO DE AUTENTICAÇÃO
def gerarObjetoTOTP(base32):
    print('[AUTHENTICATOR]Gerando objeto de autenticação na memória do computador...')
    try:
        obj = pyotp.TOTP(base32)
        print('[AUTHENTICATOR]Objeto criado com sucesso!')
        return obj
    except Exception as e:
        print('[AUTHENTICATOR]Não foi possivel gerar o objeto...')
        print('[AUTHENTICATOR]:',e)

#RETORNA SENHA ATUAL
def senhaAtual(obj_base32):
    print('[AUTHENTICATOR]Retornando senha atual...')
    try:
        senha = obj_base32.now()
        print('[AUTHENTICATOR]Senha atual do authenticator: ',senha)
        return senha
    except Exception as e:
        print('[AUTHENTICATOR]Não foi possivel retornar a senha...')
        print('[AUTHENTICATOR]:',e)
