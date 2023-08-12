# while True:
#     resposta = input('Qual a capital do Brasil? ').capitalize()
#     if resposta == "Brasilia":
#         print('Muito Bem, você acertou')
#         break
#     else:
#         print('Tente novamente!')


while True:
    username = input('username? ')
    if username != "neo":
        print('Nunca nem vi')
        continue
    senha = input('Qual sua senha?')
    if senha == "1234":
        print('Bem Vindo, {}'.format(username))
        print('Aceita um café? ')
        break