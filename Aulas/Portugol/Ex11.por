programa {
  funcao inicio() {
    // Ex11

    real saldo, saque

    escreva("Digite seu saldo: ")
    leia(saldo)

    se(saldo < 0){
      escreva("\nUsu�rio n�o possui saldo para entregar dinheiro ao cliente...\n")
    }senao{
      escreva("\nSaldo atual = ", saldo)
      escreva("\nDigite o valor a ser sacado: ")
      leia(saque)

      se(saque > saldo){
        escreva("N�o � poss�vel sacar esse valor!")
        escreva("\nDigite novamente: ")
      }senao{
        saldo = saldo - saque
        escreva("\nSaldo atual = ", saldo)
      }
    }
  }
}