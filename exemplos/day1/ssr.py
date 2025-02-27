# carregar os dados
dados = [
    {"nome": "Bruno", "cidade": "Viana"},
    {"nome": "Guido", "cidade": "Amsterdam"},
]

# processar
template = """\
<!DOCTYPE html>
<html>
<body>
    <ul>
        <li>Nome: {dado[nome]} </li>
        <li>Cidade: {dado[cidade]} </li>
    </ul>
</body>
"""

# renderizar
for item in dados:
    print(template.format(dado=item))
