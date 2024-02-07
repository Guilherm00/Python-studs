#analisador completo 56
infos = []
quantidade = int(input("quantas pessoas deseja adicionar? "))
for l in range(quantidade):
  nome = input("Digite o nome: ")
  sexo = input("Digite o sexo F/M: ").upper()
  idade = int(input("digite a idade: "))
  pessoa ={"nome":nome, "sexo":sexo, "idade":idade}
  infos.append(pessoa)
  idades = [pessoa["idade"] for pessoa in infos]
  media_idades = sum(idades) / len(idades)
  homens = [pessoa for pessoa in infos if pessoa["sexo"] == "M"]
  homem_mais_velho = max(homens, key=lambda x: x["idade"])["nome"]
  mulheres_menos_de_20 = [pessoa for pessoa in infos if pessoa["sexo"] == "F" and pessoa["idade"] < 20]
  quantidade_mulheres_menos_de_20 = len(mulheres_menos_de_20)
print("Média das idades:", media_idades)
print("Nome do homem mais velho:", homem_mais_velho)
print("Quantidade de mulheres com menos de 20 anos:", quantidade_mulheres_menos_de_20)