programa {
  inclua biblioteca Matematica
  funcao inicio() {
    real raio, pi = 3.14, area

    escreva("Digite valor do raio do c�rculo: ")
    leia(raio)

    area = Matematica.arredondar(pi * (raio*raio), 2)
    escreva("Area do c�rculo = ", area)
  }
}