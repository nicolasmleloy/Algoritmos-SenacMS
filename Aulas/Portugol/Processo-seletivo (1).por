programa {
  funcao inicio() {
    cadeia cargo, nome_completo, email, curso, mensagem
    inteiro idade, nota

    mensagem = "Parab�ns, voc� passou para a pr�xima fase!!!"

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
      escreva("\nVoc� possui algum curso de qualifica��o?\n SIM ou N�O: ")
      leia(curso)

      se(curso == "Sim" ou curso == "sim"){
        escreva(mensagem, " Fase 03:\n")

        escreva("Nessa 3� fase voc� realizou uma prova, informe sua nota: ")
        leia(nota)

        se(nota >= 7){
        escreva(mensagem, " Fim...")
        }senao{
        escreva("Nota insuficiente!!!Obrigado pela sua participa��o...")
        }
      }senao se(curso == "Nao" ou curso == "N�o" ou curso == "nao"){
        escreva("\nObrigado pela sua participa��o!!!\n")
      }
      
      }senao{
      escreva("Idade n�o suficiente! Obrigado pela sua participa��o...")
    }
}
}