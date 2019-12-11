from interagirAuthenticator import senhaAtual
from flask import Flask, jsonify, request, make_response, session
from flask_cors import CORS
from functools import wraps
import jwt
import time
import datetime
import pickle
import os
import hashlib, binascii, os
import mysql.connector
import pyqrcode
import pyotp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ASAFK4994KDJA932KSPZKD93273FNDNNCKSF782733CHCKXJKD78833BBMX'
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)

#VALIDADOR DO TOKEN
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = session['X-ACCESS-TOKEN']
        except:
            token = ''
        #token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'erro':'Token sem tamanho!'}),403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'erro':'Token inválido!'}), 403
            
        return f(*args, **kwargs)
    return decorated

#CONFIGURAR CONEXÃO DO ADMINISTRADOR
@app.route('/configadm', methods=['POST'])
@token_required
def configurarBancoADM():
    session['HOST'] = request.form['host']
    session.modified = True
    session['USER'] = request.form['user']
    session.modified = True
    session['PASSWORD'] = request.form['password']
    session.modified = True
    
    if not session['HOST'] or not session['USER'] or not session['PASSWORD']:
        return jsonify({'erro':'Credênciais vazias'})
    else:
        try:
            CONEXAO = mysql.connector.connect(
                host=session['HOST'],
                user=session['USER'],
                passwd=session['PASSWORD']
            )
            CONEXAO.close()
        except Exception as e:
            return jsonify({'erro':'Não foi possivel estabelecer uma conexão de Administrador'})
    return jsonify({'msg':'Conexão de administrador foi estabelecida com sucesso!'})


#CONFIGURAR CONEXÃO DE DESENVOLVEDOR
@app.route('/configdev', methods=['POST'])
@token_required
def configurarBancoDEV():
    try:
        CONEXAO = mysql.connector.connect(
            host=session['HOST'],
            user=session['USER'],
            passwd=session['PASSWORD']
        )
        CONEXAO.close()
    except Exception as e:
        return jsonify({'erro':'Não foi possivel estabelecer uma conexão de Administrador'})

    session['HOST_DEV'] = request.form['host']
    session.modified = True
    session['USER_DEV'] = request.form['user']
    session.modified = True
    session['NOME_CON_DEV'] = request.form['nome-con']
    session.modified = True
    session['EMAIL_DEV'] = request.form['email']
    session.modified = True

    if not session['HOST_DEV'] or not session['USER_DEV'] or not session['NOME_CON_DEV'] or not session['EMAIL_DEV']:
        return jsonify({'erro':'Algumas configurações estão vazias.'})
    
    return jsonify({'msg':'As configurações do usuario a ser protegido foram salvas'})

@app.route('/desativar', methods=['POST'])
@token_required
def desativarLoop():
    file = open('flag.txt','w')
    file.write('0')
    file.close()
    return jsonify({'msg':'Parando o loop...'})

@app.route('/iniciar', methods=['POST'])
@token_required
def ativarLoop():
    file = open('flag.txt','w')
    file.write('1')
    file.close()
    def mudarSenha(usuario,host,senha):
        try:
            CONEXAO = mysql.connector.connect(
                host=session['HOST'],
                user=session['USER'],
                passwd=session['PASSWORD']
            )
            CURSOR = CONEXAO.cursor()
        except Exception as e:
            return jsonify({'erro':e})

        try:
            sql = "ALTER USER '%s'@'%s' IDENTIFIED BY '%s';" % (usuario,host,senha)
            CURSOR.execute(sql)
            sql = "FLUSH PRIVILEGES;"
            CURSOR.execute(sql)
            CONEXAO.commit()
            CONEXAO.close()
        except Exception as e:
            print(e)

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
    def gerarQRCode(url):
        print('[AUTHENTICATOR]Gerando código QR no diretório do script...')
        try:
            url = pyqrcode.create(url) 
            svg = url.svg("./public/qrcode.svg", scale = 8)
            print('[AUTHENTICATOR]Código QR gerado com sucesso!')
            return svg
        except Exception as e:
            print('[AUTHENTICATOR]Não foi possivel gerar o código QR...')
            print('[AUTHENTICATOR]:',e)

    try:
        OBJ_TOKEN_QR = open("token","rb")
        OBJ_TOKEN_QR = pickle.load(OBJ_TOKEN_QR)
    except:
        base32 = 'LCU34MILJ4YSSHXU'
        OBJ_TOKEN_QR = gerarObjetoTOTP(base32)
        file = open("token","wb")
        pickle.dump(OBJ_TOKEN_QR,file)
        file.close()
        link_qr = gerarLinkAcessoQR(base32,session['EMAIL_DEV'],session['NOME_CON_DEV'])
        gerarQRCode(link_qr)
        
    while True:
        with open('flag.txt', 'r') as flag:
            loop = flag.read()
            flag.close()
        senha = senhaAtual(OBJ_TOKEN_QR)
        mudarSenha(session['USER_DEV'],session['HOST_DEV'],senha)
        time.sleep(5)
        if loop == '0':
            return jsonify({'msg':'Loop parou'})

@app.route('/login', methods=['POST'])
def login():

    user = request.form['user']

    def gerarHashSenha(password):
        #Retorna a senha em hash
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')
 
    def verificaSenha(stored_password, provided_password):
        #Verifica se a senha recebida é igual a senha do banco
        #Compara hash(senha no banco) com senha recebida

        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512', 
            provided_password.encode('utf-8'), 
            salt.encode('ascii'), 
            100000
        )
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    CONEXAO_BANCO_API = mysql.connector.connect(
        host='localhost',
        database='database_protector',
        user='root',
        password='root'
    )

    QUERY_USERS_API = "SELECT * FROM usuarios WHERE email = '"+user+"'"
    cursor = CONEXAO_BANCO_API.cursor()
    cursor.execute(QUERY_USERS_API)
    dados_usuario = cursor.fetchall()
    CONEXAO_BANCO_API.close()

    if user and verificaSenha(dados_usuario[0][2],request.form['password']) :
        token = jwt.encode({'user' : user, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=3600)}, app.config['SECRET_KEY'])
        session['X-ACCESS-TOKEN'] = token.decode('UTF-8')
        session.modified = True
        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Não foi possivel verificar',401,{'WWW-Authenticate' : 'Basic real="Login required"'})


@app.route('/teste', methods=['GET'])
def teste():
    return 'API Funcionando!'

if __name__ == '__main__':
    app.run(debug=True,port=5000)