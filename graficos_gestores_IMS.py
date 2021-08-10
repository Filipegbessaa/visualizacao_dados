from google.colab import auth 
import gspread 
from oauth2client.client import GoogleCredentials
import matplotlib.pyplot as plt

def split_string(string):
    return string.split(",")


def transform_strings_list_arrays_list(strings_list):
    arrays_list = list(map(separar_string, strings_list))
    arrays_list = arrays_list[1:]
    return arrays_list


def list_options(array):
    options = []
    options_freq = []
    for i in array:
        for j in i:
            j = j.strip()
            if j == "":
                pass

            elif j not in options:
                options.append(j)
                options_freq.append(1)

            else:
                for i in range(len(options)):
                    if j == options[i]:
                        options_freq[i] += 1

    return [options, options_freq]
  
def transform_column_cod_num(column_string):
  if len(column_string) == 1:
    num_column = int(ord(column_string) - 64)
    if num_column < 1 or num_column > 26:
      print("Digite novamente.")
      pass

  elif len(column_string) > 1:
    array_column_string = list(column_string)
    num_column = 0
    mult_factor = len(array_column_string) - 1
    for i in range(len(array_column_string)):
      character_num = int(ord(array_column_string[i]) - 64)
      if mult_factor > 0:
        character_num *= 26
      mult_factor -= 1
      if character_num < 1 or character_num > 26:
        print("Digite novamente.")
        pass
      num_column += character_num
  
  print(num_column)
  return num_column



auth.authenticate_user()
gc = gspread.authorize(GoogleCredentials.get_application_default())

gc = gspread.authorize(GoogleCredentials.get_application_default())
spreadsheet = gc.open('TRATAMENTO SOCIEDADE CIVIL 1 - Pesquisa quantitativa (respostas)')
page = spreadsheet.sheet1


print("Digite o código dá coluna que deseja visualizar o gráfico de barra:")
column_string = input()
transform_column_cod_num(column_string)


# col_num = int(chr(col_ascII)) 
array = page.col_values(num_column)
lista = transform_strings_list_arrays_list(array)
options, options_freq = listar_opcoes(lista)

plt.rcParams.update({"font.size": 16})
plt.figure(figsize=(20, 20))
plt.barh(options, options_freq, color="royalblue", height=0.8)
plt.ylabel("Conselhos")
plt.xlabel("Gestores")
plt.grid(axis="x")
plt.show()