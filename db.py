# arquivo db.py

import sqlite3

# conecta ao banco de dados 'task-crud'
# caso o banco de dados não exista ele será criado
conn = sqlite3.connect("task-crud.db")

def criar_tabela_task():
    """ cria a tabela 'tarefa' caso ela não exista """
    cursor = conn.cursor()
    conn.execute("""
    create table if not exists tarefa (
        cd_tarefa integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
    """)

def update_codigo_tarefa():
    conn.execute( " delete from sqlite_sequence where name= 'tarefa' " )
    conn.commit()

def add_tarefa(tarefa):
    """ adiciona uma nova tarefa """
    conn.execute("insert into tarefa (tarefa, concluido) values (?, 0)", (tarefa, ))
    conn.commit()

def excluir_tarefa(cd_tarefa):
    """ remove a tarefa da tabela """
    conn.execute("delete from tarefa where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()

def concluir_tarefa(cd_tarefa):
    """ marca a tarefa como concluida """
    conn.execute("update tarefa set concluido = 1 where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()

def get_tarefas(): # retorna um cursor
    """ retorna a lista de tarefas cadastradas """
    return conn.execute("select cd_tarefa, tarefa, concluido from tarefa")
