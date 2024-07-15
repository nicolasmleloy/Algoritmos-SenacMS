from produto import Produto
from cliente import Cliente

prod01 = Produto("Nestlé", "Nescau", "Achocolatado", 11.99)
prod01.getNome()

"""-----------------------------------------------------------------"""

cliente01 = Cliente("023325643", "Nícolas", 18)
cliente01 = cliente01.getNome_Idade()
print(f"{cliente01[0]} tem {cliente01[1]} anos.")
print(type(cliente01))

cliente02 = Cliente("1426135672", "Alek", 44)
print(cliente02.getCpf())