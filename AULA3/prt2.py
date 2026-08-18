#x = 15
#y = 20
#print("x é maior que y?", x > y)
#print("x é igual a y?", x == y)

#resposta = x>y
#print(resposta)
#print(type(resposta))

#tem_carteira = True
#idade = 18
#tem_carro = False
#pode_dirigir = idade >= 18 and tem_carteira
#print("Pode dirigir?", pode_dirigir)
#print("Pode dirigir e tem carro?", pode_dirigir and tem_carro)

# CNH = True
# bebidinha = False

# posso_dirigir = CNH and not bebidinha
# print(posso_dirigir)

# busaum = True
# trenzin = True

# venho_pra_aula = busaum or trenzin 
# print("Venho pra aula?",venho_pra_aula)

locomocao = input("Diga qual sua locomocao")
choveu = True

if choveu and locomocao== 'moto':
    resultado = "tô todo molhado :("
elif not choveu and locomocao== 'moto':
  resultado= "tô seco :)"
else: 
    resultado= "tô seco :)"

print(resultado)