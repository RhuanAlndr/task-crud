# arquivo app.py

import db
import mensagens as msg

def main():
    NOVA_TAREFA = 1
    CONCLUIR_TAREFA = 2
    EXCLUIR_TAREFA = 3
    ATUALIZAR_TAREFA = 4
    while True:
        msg.exibir_cabeçalho()
        msg.exibir_tarefas()
        try:
            # exibe as opções disponíveis
            opção = int(input('O que deseja fazer? 1 = Nova tarefa, 2 = Concluir tarefa, 3 = Excluir tarefa, 4 = Atualizar tarefa => '))

            # verifica qual opção o usuário escolheu
            if opção == NOVA_TAREFA:
                msg.mostrar_opção_nova_tarefa()
            elif opção == CONCLUIR_TAREFA:
                msg.mostrar_opção_concluir_tarefa()
            elif opção == EXCLUIR_TAREFA:
                msg.mostrar_opção_excluir_tarefa()
            elif opção == ATUALIZAR_TAREFA:
                db.update_codigo_tarefa()
            else:
                print('Opção não reconhecida, por favor informar um número')
        except ValueError as e:
            print('Opção não reconhecida, por favor informar um número')
        

if __name__ == '__main__':
    db.criar_tabela_task()

    main()