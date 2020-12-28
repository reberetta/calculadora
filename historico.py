#salvar
def salvar_historico(linha:str) -> None:
    arquivo = open("historico.txt", 'a')
    arquivo.write(f'{linha}\n')
    arquivo.close()

#listar
def ler_historico() -> list:
    lista = []
    arquivo = open('historico.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        linha = linha.split(';')
        linha = f'{linha[0]}{linha[1]}{linha[2]} = {linha[3]}'
        lista.append(linha)
    arquivo.close()
    return lista


#salvar_historico('1;+;4;5;')
#salvar_historico('1;-;4;-3')

#print('\n'*2)
#print(ler_historico())
#print('\n'*2)