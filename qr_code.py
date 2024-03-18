import qrcode

'''link_website = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'''

print('Digite as informações do QRCode:')

qtd = int(input('\nQuantos QRcodes deseja fazer: '))

for i in range(qtd):
    print(f'Criando QRcode {i+1}')
    link_website = input('\nDigite o link do website que deseja criar um QRCode: ')
    versao = int(input('\nDigite a versão (tamanho) [1 - 40]: '))
    caixa = int(input('\nDigite quantos pixels tem cada "caixa": '))
    borda = int(input('\nDigite o tamanho da borda: '))
    
    qr = qrcode.QRCode(version = versao, box_size = caixa, border = borda)
    qr.add_data(link_website)
    qr.make()

    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save(f'qr{i+1}.png')





