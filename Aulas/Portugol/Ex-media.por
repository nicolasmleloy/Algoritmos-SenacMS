programa {
  funcao inicio() {
    real n1, n2, media

    escreva("Digite a primeira nota da prova: ")
    leia(n1)
    escreva("Digite a segunda nota da prova: ")
    leia(n2)

    media = (n1 + n2) / 2

    se(media >= 7.0){
      escreva("\nA primeira nota do estudante é = ", n1)
      escreva("\nA segunda nota do estudante é = ", n2)
      escreva("\nA média do estudante é = ", media)
      escreva("\nO aluno está aprovado!")
    }
    escreva("\nFim do programa...")
  }
}
