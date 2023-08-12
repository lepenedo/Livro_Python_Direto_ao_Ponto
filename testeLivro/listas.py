usuarios = ['Leandro', 'Nicole', 'Helena']

while True:
    user = input('username? ')
    if user not in usuarios:
        print('Nunca nem vi')
    else: 
        print('Seja bem vindo {}'.format(user))
        break
