#criação da tabela
import sqlite3
banco = sqlite3.connect('ChatBot')

#criação do cursor para digitar os comandos SQL
cursor = banco.cursor()

cursor.execute("CREATE TABLE calendario (mes text, data integer, evento text, link_informacoes text)")
cursor.execute("INSERT INTO calendario ('junho',01,'Processamento de rematrícula','link do pdf disponibilizado')")