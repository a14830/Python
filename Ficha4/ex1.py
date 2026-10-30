escola = {
    "aluno1": {
        "nome": "Ana Silva",
        "idade": 17,
        "cidade": "Porto",
        "curso": "Programador",
        "Disciplina": {"Matemática", "Física", "Informática"},
        "notas": {
            "Matemática": 18,
            "Física": 17,
            "Informática": 19,
        },
        "contacto": {
            "email": "ana@email.com",
            "telefone": "912345678"
        }
    },
}

escola["aluno1"]["idade"] = 18
escola["aluno1"]["Disciplina"].add("Português")
escola["aluno1"]["notas"]["Português"] = 16

for aluno in escola.values():
  nome_aluno = aluno["nome"]
  notas_aluno = []
  for nota in aluno["notas"].values():
     notas_aluno.append(nota)
     print(f"Aluno(a) {nome_aluno} teve de {nota} valores")

media = round(sum(notas_aluno)/len(notas_aluno),2)
print(f"Aluno(a) {nome_aluno} teve de {media} valores de media final")

# texto = "Waner Ribeiro De Souza Filho"

# contagem = {}
# for letra in texto:
#    letra = letra.lower()
#    if letra.isspace() == False:
#       if letra in contagem.keys():
#          contagem[letra]+=1
#       else :
#          contagem[letra]=1
#          print(contagem)
