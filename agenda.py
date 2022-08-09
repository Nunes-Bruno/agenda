nome = ''
telefone = ''
contatos = {}

def menu():
  print("=========Agenda Telefónica=========")
  print("1 - Adicionar Contato")
  print("2 - Consultar Contato")
  print("3 - Excluir Contato")
  print("4 - Editar Contato")
  print("5 - Display de Contatos")
  print("6 - Sair")
  print("======" * 5 )
  opcao = int(input("Escolha a opção:"))
  return opcao

def adicionar_contato():
  print("======Adicionar Contato======")
  nome = str(input("Nome:"))
  telefone = int(input("Telefone:"))
  contatos[nome] = {"nome" : nome, "telefone" : telefone}
  print(contatos)
  return
  

def consultar_contato():
  print("======Consultar Agenda=====")
  buscar = str(input("Buscar Contato:"))
  if buscar in contatos.keys():
    print("Contato Encontrado")
  else:
    print("Contato não Encontrado")
  print(contatos.get(buscar))

def excluir_contato():
  print("======Excluir Contato======")
  excluir = str(input("Excluir Contato:"))
  if excluir in contatos.keys():
      del contatos[excluir]
      print("Contato Excluido com Sucesso")
  else:
    print("Contato não Existe")
  print(contatos)

def editar_contato():
  print("======Editar Contato======")
  contato_antigo = str(input("Editar Contato:"))
  if contato_antigo in contatos.keys():
    contato_novo = str(input("Nome:"))
    telefone = int(input("Telefone:"))
    contatos[contato_antigo] = {'nome': contato_novo, 'telefone': telefone}
    contatos[contato_novo] = contatos.pop(contato_antigo)
    print("Edição feita com Sucesso")
  else:
    print("Contato não Encontrado")
  print(contatos)

def dados():
  contatos = {'fox': {'nome': 'fox', 'telefone': 123}, 'asta': {'nome': 'asta', 'telefone': 456}}
  print("======Seus Contatos======")
  # for k in contatos.items():
  #   print(k[1])
  for k in contatos:
    print(f'nome\n{k}\t')
    

while True:
  opcao = menu()

  if opcao == 1:
   adicionar_contato()

  if opcao == 2:
    consultar_contato()

  if opcao == 3:
    excluir_contato()

  if opcao == 4:
    editar_contato()  

#   if opcao == 5:
#     dados()

  if opcao == 5:
    print("Programa Encerrado...")
    break
  
  # else:
  #   print("opção Invalida")  
  #   menu()


  
