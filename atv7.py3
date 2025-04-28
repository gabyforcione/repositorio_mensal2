convidados = []

for i in range(6):
    nome = input(f"Digite o nome do convidado {i + 1}: ").strip()
    convidados.append(nome)

# Remover duplicados e ordenar
lista_final = sorted(set(convidados))

print(f"\nLista final de convidados (sem duplicatas e ordenada): {lista_final}")
