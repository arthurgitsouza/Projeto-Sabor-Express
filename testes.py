projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

None == True


for projeto in projetos:
  if projeto:
    print(f"Projeto: {projeto}")
  else:
    print("Projeto não disponível.")