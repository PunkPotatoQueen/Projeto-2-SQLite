import sqlite3

try:

    banco = sqlite3.connect('ChatBot.db')
    cursor = banco.cursor()

    cursor.execute("DELETE from calendario WHERE data = 1")

    banco.commit()
    banco.close()
    print ('Linha excluida')

except sqlite3.Error as erro:
    print ('Erro ao exluir ', erro)