agendamentos = {}

def adicionar_agendamento():
    data_hora = input("Digite a data e a hora do agendamento (ex: '2025-08-05 14:00'): ")
    
    if data_hora in agendamentos:
        print("Horário já agendado. Por favor, escolha outro.")
        return

    cliente = input("Digite o nome do cliente: ")
    servico = input("Digite o serviço a ser agendado: ")
    
    agendamentos[data_hora] = {'cliente': cliente, 'servico': servico}
    print(f"Agendamento para {cliente} no dia {data_hora} para o serviço '{servico}' adicionado com sucesso!")

def visualizar_agendamentos():
    if not agendamentos:
        print("Nenhum agendamento encontrado.")
        return

    print("\n--- Lista de Agendamentos ---")
    for data_hora, detalhes in agendamentos.items():
        print(f"Data/Hora: {data_hora} | Cliente: {detalhes['cliente']} | Serviço: {detalhes['servico']}")
    print("----------------------------")

def cancelar_agendamento():
    data_hora = input("Digite a data e a hora do agendamento que deseja cancelar (ex: '2025-08-05 14:00'): ")
    
    if data_hora in agendamentos:
        del agendamentos[data_hora]
        print(f"Agendamento do dia {data_hora} cancelado com sucesso!")
    else:
        print("Agendamento não encontrado. Verifique a data e a hora digitadas.")

def menu_principal():
    while True:
        print("\n--- Sistema de Agendamento ---")
        print("1. Adicionar Agendamento")
        print("2. Visualizar Agendamentos")
        print("3. Cancelar Agendamento")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_agendamento()
        elif opcao == '2':
            visualizar_agendamentos()
        elif opcao == '3':
            cancelar_agendamento()
        elif opcao == '4':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    
    menu_principal()
    
    
