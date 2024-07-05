programa {
  funcao inicio() {
    cadeia cargo, nome_completo, email, curso, mensagem
    inteiro idade, nota

    mensagem = "Parabéns, você passou para a próxima fase!!!"

    escreva("Digite seu nome: ")
    leia(nome_completo)
    escreva("Digite seu email: ")
    leia(email)
    escreva("Informe o cargo desejado: ")
    leia(cargo)
    escreva("Digite sua idade: ")
    leia(idade)
    

    se(idade >= 18){
      escreva(mensagem, " Fase 02:\n")
      escreva("\nVocê possui algum curso de qualificação?\n SIM ou NÃO: ")
      leia(curso)

      se(curso == "Sim" ou curso == "sim"){
        escreva(mensagem, " Fase 03:\n")

        escreva("Nessa 3ª fase você realizou uma prova, informe sua nota: ")
        leia(nota)

        se(nota >= 7){
        escreva(mensagem, " Fim...")
        }senao{
        escreva("Nota insuficiente!!!Obrigado pela sua participação...")
        }
      }senao se(curso == "Nao" ou curso == "Não" ou curso == "nao"){
        escreva("\nObrigado pela sua participação!!!\n")
      }
      
      }senao{
      escreva("Idade não suficiente! Obrigado pela sua participação...")
    }
}
}