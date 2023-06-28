#criação da tabela
import sqlite3
banco = sqlite3.connect('ChatBot.db')

#criação do cursor para digitar os comandos SQL
cursor = banco.cursor()

#inserção de itens na tabela
#cursor.execute("CREATE TABLE calendario (mes text, data integer, evento text, link_informacoes text)")
cursor.execute("INSERT INTO calendario VALUES('junho',01,'Processamento de rematrícula','link do pdf disponibilizado')")
cursor.execute("INSERT INTO calendario VALUES('junho',05,'Matrícula extraordinária','link do pdf disponibilizado')")
cursor.execute("INSERT INTO calendario VALUES('junho',08,'Feriado - Corpus Christi. Não haverá aula','link do aviso')")

cursor.execute("DELETE from calendario WHERE data = 1")

banco.commit()

#agora para ver os dados inseridos

cursor.execute("SELECT * FROM calendario")
print(cursor.fetchall())