listaTarefas = []

def criarTarefas():
    descricao = input('Digite a descrição da tarefa: ')
    categoria = input('Digite a categoria da tarefa: ')
    urgencia = input('Digite a urgência da tarefa (moderado, urgente, crítica): ')
    diasRestantes = input('Digite os dias restantes da tarefa: ')
    status = 'pendente'
    novoId = len(listaTarefas) + 1

    dictTarefas = {
        'novoId': novoId,
        'categoria': categoria,
        'descricao': descricao,
        'urgencia': urgencia,
        'diasRestantes': diasRestantes,
        'Status': status
    }

    return dictTarefas


while True:
    print('Escolha uma opção:')
    print('1 - Criar Tarefa')
    print('2 - Alterar Status')
    print('3 - Listar Tarefas')
    print('4 - Sair')

    escolha = int(input('Digite sua escolha (1, 2, 3 ou 4): '))

    if escolha == 1:
        listaTarefas.append(criarTarefas())
        print(listaTarefas)

    elif escolha == 2:
        inputid = int(input('Digite o id da tarefa: '))
        for item in listaTarefas:
            if item['novoId'] == inputid:
                item['Status'] = 'concluido'
                print('Tarefa finalizada!')
                break

    elif escolha == 3:
        for item in listaTarefas:
            print(item)

    else:
        break
