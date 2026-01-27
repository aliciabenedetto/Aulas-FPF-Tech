class Tarefa:
    def __init__(self, tarefa_id, categoria, descricao, urgencia, dias_restante):
        self.id = tarefa_id
        self.categoria = categoria
        self.descricao = descricao
        self.urgencia = urgencia
        self.dias_restante = dias_restante
        self.status = 'Pendente'

    #Imprimir os cabeçalhos (Method)
    def __str__(self):
        return f"{self.id} - {self.categoria} - {self.descricao} - {self.urgencia} - {self.dias_restante} - {self.status}"

#Classe Gerenciador de Tarefas
class GerenciadorTarefas:
    def __init__(self):
        self.lista_tarefas = [] #Inicia a lista de Tarefa Vazia
        self.proximo_id = 1  # Cria o ID

    #Criando lista de tarefas (Função)
    def criar_tarefa(self):
        # tarefa_id = len(self.lista_tarefas) + cont #Criando ID
        print(f'-'*20,'Criando Tarefa','-'*20)
        categoria = input('Categoria: ').capitalize()
        descricao = input('Descrição: ').capitalize()
        urgencia = input('Urgência (Moderado, Importante, Critico): ').capitalize()
        dias_restante = int(input('Dias restante: '))

        tarefa = Tarefa(self.proximo_id, categoria, descricao, urgencia, dias_restante)
        self.lista_tarefas.append(tarefa)
        self.proximo_id += 1  # incrementa SEMPRE
        print('Tarefa criada com sucesso!')

    def listar_tarefas(self):
        if not self.lista_tarefas:
            print('Lista de tarefas vazia!')
        else:
            print('ID - Categoria - Descrição - Urgência - Dias Restante - Status')
            for tarefa in self.lista_tarefas:
                print(tarefa)

    def alterar_status(self):
        self.listar_tarefas()
        if self.lista_tarefas:
            erro = True
            try:
                id_tarefa = int(input('Informe o ID da tarefa: '))
            except ValueError:
                print('Erro: ID Inválido. Digite apenas números válidos!')
                # input("\nPressione Enter para voltar ao menu...")
                erro = False

            if erro == True:
                for tarefa in self.lista_tarefas:
                    if tarefa.id == id_tarefa:
                        novo_status = input('Informe o novo Status: ').capitalize()

                        if novo_status == 'Concluido':
                            self.lista_tarefas.remove(tarefa)
                            print('Tarefa concluída e removida com sucesso!')

                        else:
                            tarefa.status = novo_status
                            print('Status atualizado com sucesso!')
                        return

                print('ID inválido.')

    def menu(self):
        while True:
            print('1 Criar Tarefa!')
            print('2 Alterar Status!')
            print('3 Listar Tarefas!')
            print('0 Sair!')

            # try:
            opcao = input('Opção: ')
            match opcao:
                    case '1':
                        self.criar_tarefa()
                    case '2':
                        self.alterar_status()
                    case '3':
                        self.listar_tarefas()
                    case '0':
                        print('Saindo do sistema...')
                        break
                    case _:
                        print('Opção Inválida!')

# Programa principal
gerenciador = GerenciadorTarefas()
gerenciador.menu()
input("\nPressione Enter para voltar ao menu...")