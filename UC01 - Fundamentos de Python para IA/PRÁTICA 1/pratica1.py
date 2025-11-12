# Sistema de Recomendação de Viagens

def coletar_preferencias():
    """Solicita as preferências do usuário com validação de entrada."""
    print("=== Sistema de Recomendação de Viagens ===")

    while True:
        clima = input("Você prefere clima quente ou frio? ").strip().lower()
        if clima in ["quente", "frio"]:
            break
        print("Resposta inválida! Digite apenas 'quente' ou 'frio'.\n")

    while True:
        ambiente = input("Prefere lugares com natureza ou paisagens urbanas? ").strip().lower()
        if ambiente in ["natureza", "urbano", "urbanas"]:
            ambiente = "urbano" if ambiente.startswith("urban") else "natureza"
            break
        print("Resposta inválida! Digite apenas 'natureza' ou 'urbanas'.\n")

    while True:
        try:
            orcamento = float(input("Qual é o seu orçamento disponível (em R$)? ").strip())
            if orcamento > 0:
                break
            else:
                print("O valor deve ser maior que zero.\n")
        except ValueError:
            print("Digite apenas números! Exemplo: 1500\n")

    return clima, ambiente, orcamento

def recomendar_destino(clima, ambiente, orcamento, destinos):
    """Compara as preferências do usuário com os destinos cadastrados e retorna o mais adequado."""
    recomendacoes = []

    for destino in destinos:
        if (destino["clima"] == clima and
            destino["ambiente"] == ambiente and
            destino["preco_min"] <= orcamento <= destino["preco_max"]):
            recomendacoes.append(destino)

    if not recomendacoes:
        return None

    recomendacoes.sort(key=lambda d: d["preco_min"])
    return recomendacoes[0]

def exibir_recomendacao(destino):
    """Mostra o destino recomendado com uma justificativa simples."""
    print("\n=== Recomendação de Viagem ===")
    print(f"Destino sugerido: {destino['nome']}")
    print(f"Clima: {destino['clima'].capitalize()} | Ambiente: {destino['ambiente'].capitalize()}")
    print(f"Faixa de preço: R$ {destino['preco_min']} - R$ {destino['preco_max']}")
    print(f"Justificativa: {destino['justificativa']}")

def main():
    destinos = [
        {"nome": "Parnaíba (PI)", "clima": "quente", "ambiente": "praia",
         "preco_min": 800, "preco_max": 2000,
         "justificativa": "Cidade litorânea com belas praias e o Delta do Parnaíba, um dos únicos deltas em mar aberto do mundo."},

        {"nome": "Teresina (PI)", "clima": "quente", "ambiente": "urbano",
         "preco_min": 600, "preco_max": 1500,
         "justificativa": "Capital piauiense com rica cultura, culinária regional e bons eventos culturais."},

        {"nome": "Barra Grande (PI)", "clima": "quente", "ambiente": "praia",
         "preco_min": 1000, "preco_max": 2500,
         "justificativa": "Vilarejo paradisíaco com mar calmo, ideal para descanso e prática de kitesurfe."},

        {"nome": "Jericoacoara (CE)", "clima": "quente", "ambiente": "praia",
         "preco_min": 1200, "preco_max": 3000,
         "justificativa": "Um dos destinos mais famosos do Nordeste, com dunas, lagoas e um pôr do sol inesquecível."},

        {"nome": "São Luís (MA)", "clima": "quente", "ambiente": "urbano",
         "preco_min": 900, "preco_max": 2200,
         "justificativa": "Cidade histórica com casarões coloniais e acesso aos Lençóis Maranhenses."},

        {"nome": "Lençóis Maranhenses (MA)", "clima": "quente", "ambiente": "natureza",
         "preco_min": 1500, "preco_max": 3500,
         "justificativa": "Paisagem única com dunas e lagoas cristalinas, ideal para quem busca aventura e natureza."},

        {"nome": "Natal (RN)", "clima": "quente", "ambiente": "praia",
         "preco_min": 1100, "preco_max": 2800,
         "justificativa": "Destino com praias incríveis, dunas e ótima infraestrutura turística."},

        {"nome": "Recife (PE)", "clima": "quente", "ambiente": "urbano",
         "preco_min": 1000, "preco_max": 2500,
         "justificativa": "Capital cultural com belas praias, marcos históricos e fácil acesso a Porto de Galinhas."},

        {"nome": "João Pessoa (PB)", "clima": "quente", "ambiente": "praia",
         "preco_min": 900, "preco_max": 2200,
         "justificativa": "Cidade tranquila e charmosa, com praias limpas e clima acolhedor."},

        {"nome": "Serra da Ibiapaba (CE/PI)", "clima": "frio", "ambiente": "natureza",
         "preco_min": 700, "preco_max": 2000,
         "justificativa": "Região serrana com clima ameno, belas paisagens e cachoeiras, ideal para quem quer fugir do calor nordestino."},

        {"nome": "Gramado (RS)", "clima": "frio", "ambiente": "urbano",
         "preco_min": 1500, "preco_max": 4000,
         "justificativa": "Destino encantador com arquitetura europeia, clima ameno e gastronomia excelente."},

        {"nome": "Campos do Jordão (SP)", "clima": "frio", "ambiente": "natureza",
         "preco_min": 1000, "preco_max": 3500,
         "justificativa": "Local de clima frio, montanhas, trilhas e paisagens deslumbrantes."},

        {"nome": "Monte Verde (MG)", "clima": "frio", "ambiente": "natureza",
         "preco_min": 900, "preco_max": 2800,
         "justificativa": "Vilarejo nas montanhas com clima serrano, pousadas aconchegantes e natureza exuberante."},

        {"nome": "Urubici (SC)", "clima": "frio", "ambiente": "natureza",
         "preco_min": 800, "preco_max": 2500,
         "justificativa": "Destino de montanhas e cachoeiras, conhecido pelas baixas temperaturas e belas trilhas."},

        {"nome": "Bento Gonçalves (RS)", "clima": "frio", "ambiente": "urbano",
         "preco_min": 1200, "preco_max": 3000,
         "justificativa": "Cidade do vinho e do charme colonial, ideal para passeios românticos e gastronômicos."},

        {"nome": "São Joaquim (SC)", "clima": "frio", "ambiente": "natureza",
         "preco_min": 1000, "preco_max": 3200,
         "justificativa": "Uma das cidades mais frias do Brasil, com produção de vinhos e possibilidade de geada e neve no inverno."},

        {"nome": "Salvador (BA)", "clima": "quente", "ambiente": "urbano",
         "preco_min": 1000, "preco_max": 2500,
         "justificativa": "Rica em história, cultura afro-brasileira e belas praias urbanas."},

        {"nome": "Fortaleza (CE)", "clima": "quente", "ambiente": "urbano",
         "preco_min": 900, "preco_max": 2400,
         "justificativa": "Cidade vibrante com praias, feiras de artesanato e vida noturna animada."},
    ]

    while True:
        clima, ambiente, orcamento = coletar_preferencias()
        destino = recomendar_destino(clima, ambiente, orcamento, destinos)

        if destino:
            exibir_recomendacao(destino)
        else:
            print("\n Nenhum destino encontrado com essas preferências. Tente ajustar seu orçamento ou tipo de destino.")

        continuar = input("\nDeseja buscar outro destino? (s/n): ").strip().lower()
        if continuar != "s":
            print("\nObrigado por usar o sistema de recomendação de viagens!")
            break

if __name__ == "__main__":
    main()
