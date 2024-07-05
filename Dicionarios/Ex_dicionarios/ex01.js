var a
for(a = 0; a < 4; a++){
	var nome = prompt("Informe o nome da empresa: ")
  var unidade = prompt("Informe a unidade: ")
  var fone = prompt("Informe o fone: ")
  var email = prompt("Informe o E-mail: ")
  var cidade = prompt("Informe a cidade: ")
  var uf = prompt("Informe a UF: ")

	empresa = {
        "Nome": nome,
        "Unidade": unidade,
        "Fone": fone,
        "E-mail": email,
        "Cidade": cidade,
        "UF": uf
 	}
    
    empresa["Nome"] = nome
    empresa["Unidade"] = unidade
    empresa["Fone"] = fone
    empresa["E-mail"] = email
    empresa["Cidade"] = cidade
    empresa["UF"] = uf
    document.write("Nome: ", empresa["Nome"], ", email: ", empresa["E-mail"], "<br>")
}