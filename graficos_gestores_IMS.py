import matplotlib.pyplot as plt

array = [
    "8.2 Caso a resposta anterior tenha sido positiva, por favor nos diga qual/quais: ",
    "Conselho de Turismo do Recife",
    "",
    "Conselho de Turismo do Recife",
    "Conselho da Cidade do Recife, Comissão de Controle Urbanístico, Conselho de Desenvolvimento Urbano",
    "Comissão de Controle Urbanístico, Conselho de Desenvolvimento Urbano",
    "",
    "",
    "Conselho da Cidade do Recife, Conselho de Desenvolvimento Urbano, Conselho de Meio Ambiente",
    "Conselho da Cidade do Recife, Comissão de Controle Urbanístico, Conselho Municipal de Meio Ambiente",
    "Comissão de Controle Urbanístico, Conselho de Desenvolvimento Urbano",
    "Conselho Municipal de Meio Ambiente",
    "Conselho Municipal de Saúde do Recife",
    "CTTU",
    "Conselho Municipal de Meio Ambiente",
    "",
    "Conselho da Cidade do Recife, Conselho de Desenvolvimento Urbano",
    "Conselho da Cidade do Recife",
    "Conselho da Cidade do Recife, Comissão de Controle Urbanístico, Conselho de Desenvolvimento Urbano",
    "Comitê da Bacia Hidrográfica do Capibaribe",
    "Conselho Municipal da Pessoa com Deficiência do Recife",
    "",
    "",
    "",
    "",
    "Conselho Municipal de Política Cultural do Recife",
    "",
    "",
    "Conselho da Cidade do Recife",
    "",
    "",
    "",
    "Comissão de Controle Urbanístico, Conselho de Desenvolvimento Urbano, COMEA",
    "Conselho da Cidade do Recife, Conselho de Desenvolvimento Urbano",
    "Comissão de Controle Urbanístico, Conselho de Desenvolvimento Urbano",
    "",
    "",
    "Conselho da Cidade do Recife",
    "Conselho da Cidade do Recife, Conselho Municipal de Educação do Recife, Conselho Municipal de Saúde do Recife",
]


def separar_string(string):
    return string.split(",")


def transformar_lista_strings_lista_arrays(lista):
    lista_arrays = list(map(separar_string, lista))
    lista_arrays = lista_arrays[1:]
    return lista_arrays


def listar_opcoes(array):
    opcoes = []
    frequencia_opcoes = []
    for i in array:
        for j in i:
            j = j.strip()
            if j == "":
                pass

            elif j not in opcoes:
                opcoes.append(j)
                frequencia_opcoes.append(1)

            else:
                for i in range(len(opcoes)):
                    if j == opcoes[i]:
                        frequencia_opcoes[i] += 1

    return [opcoes, frequencia_opcoes]


lista = transformar_lista_strings_lista_arrays(array)

opcoes, frequencia_opcoes = listar_opcoes(lista)

plt.rcParams.update({"font.size": 8})

plt.barh(opcoes, frequencia_opcoes, color="royalblue")
plt.ylabel("Conselhos")
plt.xlabel("Gestores")

plt.show()

# print(opcoes)
# for n in frequencia_opcoes:
#     porcentagens_opcoes.append(n /)

# print()
