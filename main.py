from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkmb
import mysql.connector
from mysql.connector import connect, Error
from datetime import datetime

w = Tk()
w.title("Casa Do Leo")
largura = 800
altura = 500
largura_screen = w.winfo_screenwidth()
altura_screen = w.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
w.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
w.minsize(width=800, height=600)
w.resizable(False, False)
w['bg'] = "black"

conexao = mysql.connector.connect(
										host="localhost",
										user="root",
										password=""
								)
'''
cursor = conexao.cursor()
cursor.execute('drop database familias')'''

def criar_banco_auto():
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)
		except Error as e:
				if "Unknown database" in str(e):
						# Se o erro indica que o banco de dados é desconhecido, crie-o
						try:
								conexao = mysql.connector.connect(
										host="localhost",
										user="root",
										password=""
								)
								cursor = conexao.cursor()
								cursor.execute("CREATE DATABASE familias")
								mostrar_aviso("Banco de dados 'familias' criado!")
						except Error as e:
								mostrar_aviso(f"Erro ao criar o banco de dados 'familias': {str(e)}")
						finally:
								if conexao.is_connected():
										conexao.close()
										cursor.close()
				else:
						mostrar_aviso(f"Erro ao conectar ao banco de dados 'familias': {str(e)}")
		finally:
				if conexao.is_connected():
						conexao.close()

def criar_tabela_familia():
		try:
				conexao = mysql.connector.connect(
								host="localhost",
								user="root",
								password="",
								database="familias"
						)

				cursor = conexao.cursor()
				cursor.execute("""
						CREATE TABLE IF NOT EXISTS familia (
								id_familia INT AUTO_INCREMENT PRIMARY KEY,
								estado VARCHAR(255),
								cidade VARCHAR(255),
								bairro VARCHAR(255)
						)
				""")
				conexao.commit()
				cursor.close()
		except Error as e:
				mostrar_aviso(f"Erro ao criar a tabela 'familia': {str(e)}")

def criar_tabela_beneficiario():
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)

				cursor = conexao.cursor()
				cursor.execute("""
						CREATE TABLE IF NOT EXISTS beneficiario (
								id_beneficiario INT AUTO_INCREMENT PRIMARY KEY,
								id_familia INT,
								nome_responsavel VARCHAR(255),
								telefone1 VARCHAR(255),
								telefone2 VARCHAR(255),
								data_nascimento VARCHAR(10),
								rua VARCHAR(255),
								numero VARCHAR(255),
								complemento VARCHAR(255),
								estado VARCHAR(255),
								cidade VARCHAR(255),
								bairro VARCHAR(255),
								sexo INT
						)
				""")
				conexao.commit()
				cursor.close()
		except Error as e:
				mostrar_aviso(f"Erro ao criar a tabela 'beneficiario': {str(e)}")

def criar_tabela_produto():
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)

				cursor = conexao.cursor()
				cursor.execute("""
						CREATE TABLE IF NOT EXISTS produto (
								id_produto INT AUTO_INCREMENT PRIMARY KEY,
								nome VARCHAR(255),
								descricao TEXT,
								preco DECIMAL(10, 2)
						)
				""")
				conexao.commit()
				cursor.close()
		except Error as e:
				mostrar_aviso(f"Erro ao criar a tabela 'produto': {str(e)}")

def cdb():
		criar_banco_auto()

def mostrar_aviso(mensagem):
		aviso = Tk()
		aviso.title("Aviso")
		label = Label(aviso, text=mensagem)
		label.pack(padx=10, pady=10)
		botao_ok = Button(aviso, text="OK", command=aviso.destroy)
		botao_ok.pack(pady=10)
		aviso.mainloop()

def sair():
		resl = tkmb.askquestion("Sair", "Tem certeza?")
		if resl == "yes":
				w.destroy()

exit_B = Button(w, text="Sair", command=sair)
exit_B.place(x=750, y=550)

# Define entry variables globally
id_familia_entry = None
nome_responsavel_entry = None
telefone1_entry = None
telefone2_entry = None
data_nascimento_entry = None
rua_entry = None
numero_entry = None
complemento_entry = None
estado_entry = None
cidade_entry = None
bairro_entry = None
sexo_var = IntVar()  # Variável para armazenar o valor do sexo
def abrir_n_j_b():
		n_j = Toplevel(w)
		n_j.title('Cadastro Beneficiário')
		n_j.geometry('250x600')
		global id_familia_entry, nome_responsavel_entry, telefone1_entry, telefone2_entry, data_nascimento_entry, rua_entry, numero_entry, complemento_entry, estado_entry, cidade_entry, bairro_entry, sexo_var
		id_familia_label = Label(n_j, text="ID da Família:")
		id_familia_label.grid(row=0, column=0)
		id_familia_entry = Entry(n_j)
		id_familia_entry.grid(row=0, column=1)
		nome_responsavel_label = Label(n_j, text="Nome: ")
		nome_responsavel_label.grid(row=1, column=0)
		nome_responsavel_entry = Entry(n_j)
		nome_responsavel_entry.grid(row=1, column=1)
		telefone1_label = Label(n_j, text="Telefone 1:")
		telefone1_label.grid(row=2, column=0)
		telefone1_entry = Entry(n_j)
		telefone1_entry.grid(row=2, column=1)
		telefone2_label = Label(n_j, text="Telefone 2:")
		telefone2_label.grid(row=3, column=0)
		telefone2_entry = Entry(n_j)
		telefone2_entry.grid(row=3, column=1)
		data_nascimento_label = Label(n_j, text="Data Nascimento:")
		data_nascimento_label.grid(row=4, column=0)
		data_nascimento_entry = Entry(n_j)
		data_nascimento_entry.grid(row=4, column=1)
		rua_label = Label(n_j, text="Rua:")
		rua_label.grid(row=5, column=0)
		rua_entry = Entry(n_j)
		rua_entry.grid(row=5, column=1)
		numero_label = Label(n_j, text="Número:")
		numero_label.grid(row=6, column=0)
		numero_entry = Entry(n_j)
		numero_entry.grid(row=6, column=1)
		complemento_label = Label(n_j, text="Complemento:")
		complemento_label.grid(row=7, column=0)
		complemento_entry = Entry(n_j)
		complemento_entry.grid(row=7, column=1)
		estado_label = Label(n_j, text="Estado:")
		estado_label.grid(row=8, column=0)
		estado_entry = Entry(n_j)
		estado_entry.grid(row=8, column=1)
		cidade_label = Label(n_j, text="Cidade:")
		cidade_label.grid(row=9, column=0)
		cidade_entry = Entry(n_j)
		cidade_entry.grid(row=9, column=1)
		bairro_label = Label(n_j, text="Bairro:")
		bairro_label.grid(row=10, column=0)
		bairro_entry = Entry(n_j)
		bairro_entry.grid(row=10, column=1)
		sexo_label = Label(n_j, text="Sexo:")
		sexo_label.grid(row=11, column=0)
		masculino_rdb = Radiobutton(n_j, text="Masculino", variable=sexo_var, value=1)
		masculino_rdb.grid(row=12, column=0)
		feminino_rdb = Radiobutton(n_j, text="Feminino", variable=sexo_var, value=2)
		feminino_rdb.grid(row=12, column=1)
		benf_var = IntVar()
		ben_label = Label(n_j, text="Beneficiário:")
		ben_label.grid(row=13, column=0)
		temporario_rdb = Radiobutton(n_j, text="Temporário", variable=benf_var, value=1)
		temporario_rdb.grid(row=14, column=0)
		fixo_rdb = Radiobutton(n_j, text="Fixo", variable=benf_var, value=2)
		fixo_rdb.grid(row=14, column=1)
		bcb_B = Button(n_j, text="Cadastrar Beneficiário", command=cadastrar_beneficiario)
		bcb_B.grid(row=16, column=0)
		criar_tabela_beneficiario()
def abrir_n_j_f():
		n_j_f = Toplevel(w)
		n_j_f.title('Cadastro')
		n_j_f.geometry('250x600')
		global id_familia_entry, estado_entry, cidade_entry, bairro_entry
		estado_label = Label(n_j_f, text="Estado:")
		estado_label.grid(row=1, column=0)
		estado_entry = Entry(n_j_f)
		estado_entry.grid(row=1, column=1)
		cidade_label = Label(n_j_f, text="Cidade:")
		cidade_label.grid(row=2, column=0)
		cidade_entry = Entry(n_j_f)
		cidade_entry.grid(row=2, column=1)
		bairro_label = Label(n_j_f, text="Bairro:")
		bairro_label.grid(row=3, column=0)
		bairro_entry = Entry(n_j_f)
		bairro_entry.grid(row=3, column=1)
		bcb_f = Button(n_j_f, text="Cadastrar", command=cadastrar_familia)
		bcb_f.grid(row=4, column=0)
		criar_tabela_familia()
def abrir_n_j_p():
		n_j_p = Toplevel(w)
		n_j_p.title('Cadastro de Produto')
		n_j_p.geometry('250x600')
		global nome_produto_entry, descricao_produto_entry, preco_produto_entry
		nome_produto_label = Label(n_j_p, text="Nome do Produto:")
		nome_produto_label.grid(row=0, column=0)
		nome_produto_entry = Entry(n_j_p)
		nome_produto_entry.grid(row=0, column=1)
		descricao_produto_label = Label(n_j_p, text="Descrição:")
		descricao_produto_label.grid(row=1, column=0)
		descricao_produto_entry = Entry(n_j_p)
		descricao_produto_entry.grid(row=1, column=1)
		preco_produto_label = Label(n_j_p, text="Preço:")
		preco_produto_label.grid(row=2, column=0)
		preco_produto_entry = Entry(n_j_p)
		preco_produto_entry.grid(row=2, column=1)
		bcb_p = Button(n_j_p, text="Cadastrar Produto", command=cadastrar_produto)
		bcb_p.grid(row=4, column=0)
		criar_tabela_produto()
def cadastrar_familia():
		estado = estado_entry.get()
		cidade = cidade_entry.get()
		bairro = bairro_entry.get()
		if not estado or not cidade or not bairro:
				mostrar_aviso("Por favor, preencha todos os campos.")
		else:
				try:
						conexao = mysql.connector.connect(
								host="localhost",
								user="root",
								password="",
								database="familias"
						)
						cursor = conexao.cursor()
						cursor.execute("INSERT INTO familia (id_familia, estado, cidade, bairro) VALUES (NULL, %s, %s, %s)", (estado, cidade, bairro))
						conexao.commit()
						cursor.close()
						mostrar_aviso("Família cadastrada com sucesso!")
				except Error as e:
						mostrar_aviso(f"Erro ao cadastrar a família: {str(e)}")
def ver_fam():
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)
				cursor = conexao.cursor()
				query = "SELECT * FROM `familia`"
				cursor.execute(query)
				resultados = cursor.fetchall()
				cursor.close()
				conexao.close()

				jan_res = Tk()
				jan_res.title("Resultados da Consulta")

				# Criar uma área de texto para exibir os resultados
				tex_res = Text(jan_res)
				tex_res.pack()

				# Exibir os resultados na área de texto
				for resultado in resultados:
						tex_res.insert(END, resultado)
						tex_res.insert(END, "\n")

				jan_res.mainloop()

		except mysql.connector.Error as err:
				print(f"Erro ao consultar o banco de dados: {err}")
def cadastrar_beneficiario():
		id_familia = id_familia_entry.get()
		nome_responsavel = nome_responsavel_entry.get()
		telefone1 = telefone1_entry.get()
		telefone2 = telefone2_entry.get()
		data_nascimento = data_nascimento_entry.get()
		rua = rua_entry.get()
		numero = numero_entry.get()
		complemento = complemento_entry.get()
		estado = estado_entry.get()
		cidade = cidade_entry.get()
		bairro = bairro_entry.get()
		sexo = sexo_var.get()  # Obtem o valor selecionado do radiobutton

		try:
				data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')
		except ValueError:
				mostrar_aviso("Formato de data inválido. Use o formato DD/MM/AAAA.")
				return

		if not id_familia or not nome_responsavel or not telefone1 or not data_nascimento or not rua or not numero or not estado or not cidade or not bairro or not sexo:
				mostrar_aviso("Por favor, preencha todos os campos.")
		else:
				try:
						conexao = mysql.connector.connect(
								host="localhost",
								user="root",
								password="",
								database="familias"
						)

						cursor = conexao.cursor()
						cursor.execute("INSERT INTO beneficiario (id_beneficiario, id_familia, nome_responsavel, telefone1, telefone2, data_nascimento, rua, numero, complemento, estado, cidade, bairro, sexo) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_familia, nome_responsavel, telefone1, telefone2, data_nascimento, rua, numero, complemento, estado, cidade, bairro, sexo))
						conexao.commit()
						cursor.close()
						mostrar_aviso("Beneficiário cadastrado com sucesso!")
				except Error as e:
						mostrar_aviso(f"Erro ao cadastrar o beneficiário: {str(e)}")

def ver_ben():
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)
				cursor = conexao.cursor()
				query = "SELECT * FROM `beneficiario`"
				cursor.execute(query)
				resultados = cursor.fetchall()
				cursor.close()
				conexao.close()

				jan_res = Tk()
				jan_res.title("Resultados da Consulta")

				# Criar uma área de texto para exibir os resultados
				tex_res = Text(jan_res)
				tex_res.pack()

				# Exibir os resultados na área de texto
				for resultado in resultados:
						tex_res.insert(END, resultado)
						tex_res.insert(END, "\n")

				jan_res.mainloop()

		except mysql.connector.Error as err:
				print(f"Erro ao consultar o banco de dados: {err}")

def cadastrar_produto():
		nome = nome_produto_entry.get()
		descricao = descricao_produto_entry.get()
		preco = preco_produto_entry.get()

		if not nome or not descricao or not preco:
				mostrar_aviso("Por favor, preencha todos os campos.")
		else:
				try:
						conexao = mysql.connector.connect(
								host="localhost",
								user="root",
								password="",
								database="familias"
						)

						cursor = conexao.cursor()
						cursor.execute("INSERT INTO produto (id_produto, nome, descricao, preco) VALUES (NULL, %s, %s, %s)", (nome, descricao, preco))
						conexao.commit()
						cursor.close()
						mostrar_aviso("Produto cadastrado com sucesso!")
				except Error as e:
						mostrar_aviso(f"Erro ao cadastrar o produto: {str(e)}")
def ver_pro():
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)
				cursor = conexao.cursor()
				query = "SELECT * FROM `produto`"
				cursor.execute(query)
				resultados = cursor.fetchall()
				cursor.close()
				conexao.close()

				jan_res = Tk()
				jan_res.title("Resultados da Consulta")

				tex_res = Text(jan_res)
				tex_res.pack()

				# Exibir os resultados na área de texto
				for resultado in resultados:
						tex_res.insert(END, resultado)
						tex_res.insert(END, "\n")

				jan_res.mainloop()

		except mysql.connector.Error as err:
				print(f"Erro ao consultar o banco de dados: {err}")

def remover_produto_por_id(id_produto):
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)

				if conexao.is_connected():
						cursor = conexao.cursor()

						cursor.execute("SELECT * FROM produto WHERE id_produto = %s", (id_produto,))
						produto = cursor.fetchone()

						if produto:
								cursor.execute("DELETE FROM produto WHERE id_produto = %s", (id_produto,))
								conexao.commit()
								mostrar_aviso(f"Produto com ID {id_produto} removido com sucesso!")
						else:
								mostrar_aviso(f"Produto com ID {id_produto} não encontrado.")

						cursor.close()

		except Error as e:
				mostrar_aviso(f"Erro ao remover o produto: {str(e)}")

		finally:
				if conexao.is_connected():
						conexao.close()

def remover_familia_por_id(id_familia):
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)

				if conexao.is_connected():
						cursor = conexao.cursor()

						cursor.execute("SELECT * FROM familia WHERE id_familia = %s", (id_familia,))
						familia = cursor.fetchone()

						if familia:
								cursor.execute("DELETE FROM familia WHERE id_familia = %s", (id_familia,))
								conexao.commit()
								mostrar_aviso(f"Família com ID {id_familia} removida com sucesso!")
						else:
								mostrar_aviso(f"Família com ID {id_familia} não encontrada.")

						cursor.close()

		except Error as e:
				mostrar_aviso(f"Erro ao remover a família: {str(e)}")

		finally:
				if conexao.is_connected():
						conexao.close()

def remover_beneficiario_por_id(id_beneficiario):
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)

				if conexao.is_connected():
						cursor = conexao.cursor()
						cursor.execute("SELECT * FROM beneficiario WHERE id_beneficiario = %s", (id_beneficiario,))
						beneficiario = cursor.fetchone()

						if beneficiario:
								cursor.execute("DELETE FROM beneficiario WHERE id_beneficiario = %s", (id_beneficiario,))
								conexao.commit()
								mostrar_aviso(f"Beneficiário com ID {id_beneficiario} removido com sucesso!")
						else:
								mostrar_aviso(f"Beneficiário com ID {id_beneficiario} não encontrado.")

						cursor.close()

		except Error as e:
				mostrar_aviso(f"Erro ao remover o beneficiário: {str(e)}")

		finally:
				if conexao.is_connected():
						conexao.close()

def remover_produto_window():
		window = Toplevel(w)
		window.title("Remover Produto por ID")
		window.geometry('300x300')

		def remover_produto():
				id_produto = entry_id_produto.get()
				if id_produto:
						remover_produto_por_id(int(id_produto))
				else:
						mostrar_aviso("Por favor, insira o ID do produto.")

		label_id_produto = Label(window, text="ID do Produto:")
		label_id_produto.pack(pady=10)
		entry_id_produto = Entry(window, width=10)
		entry_id_produto.pack(pady=10)

		b_remover_produto = Button(window, text="Remover Produto", width=15, height=2, command=remover_produto)
		b_remover_produto.pack(pady=10)

def remover_familia_window():
		window = Toplevel(w)
		window.title("Remover Família por ID")
		window.geometry('300x300')

		def remover_familia():
				id_familia = entry_id_familia.get()

				if id_familia:
						remover_familia_por_id(int(id_familia))
				else:
						mostrar_aviso("Por favor, insira o ID da família.")

		label_id_familia = Label(window, text="ID da Família:")
		label_id_familia.pack(pady=10)
		entry_id_familia = Entry(window, width=10)
		entry_id_familia.pack(pady=10)

		b_remover_familia = Button(window, text="Remover Família", width=15, height=2, command=remover_familia)
		b_remover_familia.pack(pady=10)

def remover_beneficiario_window():
		window = Toplevel(w)
		window.title("Remover Beneficiário por ID")
		window.geometry('300x300')

		def remover_beneficiario():
				id_beneficiario = entry_id_beneficiario.get()
				if id_beneficiario:
						remover_beneficiario_por_id(int(id_beneficiario))
				else:
						mostrar_aviso("Por favor, insira o ID do beneficiário.")

		label_id_beneficiario = Label(window, text="ID do Beneficiário:")
		label_id_beneficiario.pack(pady=10)
		entry_id_beneficiario = Entry(window, width=10)
		entry_id_beneficiario.pack(pady=10)

		b_remover_beneficiario = Button(window, text="Remover Beneficiário", width=20, height=2, command=remover_beneficiario)
		b_remover_beneficiario.pack(pady=10)

def atualizar_beneficiario_por_id(
		id_beneficiario,
		novo_nome_responsavel,
		novo_telefone1,
		novo_telefone2,
		nova_data_nascimento,
		nova_rua,
		novo_numero,
		novo_complemento,
		novo_estado,
		nova_cidade,
		novo_bairro,
		novo_sexo
):
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)

				if conexao.is_connected():
						cursor = conexao.cursor()

						# Atualize os dados do beneficiário com base no ID
						sql = """
								UPDATE beneficiario
								SET
										nome_responsavel = %s,
										telefone1 = %s,
										telefone2 = %s,
										data_nascimento = %s,
										rua = %s,
										numero = %s,
										complemento = %s,
										estado = %s,
										cidade = %s,
										bairro = %s,
										sexo = %s
								WHERE id_beneficiario = %s
						"""
						valores = (
								novo_nome_responsavel,
								novo_telefone1,
								novo_telefone2,
								nova_data_nascimento,
								nova_rua,
								novo_numero,
								novo_complemento,
								novo_estado,
								nova_cidade,
								novo_bairro,
								novo_sexo,
								id_beneficiario
						)
						cursor.execute(sql, valores)

						conexao.commit()
						mostrar_aviso(f"Beneficiário com ID {id_beneficiario} atualizado com sucesso!")

						cursor.close()

		except Error as e:
				mostrar_aviso(f"Erro ao atualizar o beneficiário: {str(e)}")

		finally:
				if conexao.is_connected():
						conexao.close()

def atualizar_beneficiario_window():
		window = Toplevel(w)
		window.title("Atualizar Beneficiário por ID")
		window.geometry('400x700')

		def atualizar_beneficiario():
				beneficiario_id = entry_id_beneficiario.get()
				novo_nome_responsavel = entry_novo_nome_responsavel.get()
				novo_telefone1 = entry_novo_telefone1.get()
				novo_telefone2 = entry_novo_telefone2.get()
				nova_data_nascimento = entry_nova_data_nascimento.get()
				nova_rua = entry_nova_rua.get()
				novo_numero = entry_novo_numero.get()
				novo_complemento = entry_novo_complemento.get()
				novo_estado = entry_novo_estado.get()
				nova_cidade = entry_nova_cidade.get()
				novo_bairro = entry_novo_bairro.get()
				novo_sexo = entry_novo_sexo.get()

				if beneficiario_id and novo_nome_responsavel and novo_telefone1 and nova_data_nascimento and nova_rua and novo_numero and novo_estado and nova_cidade and novo_bairro and novo_sexo:

						atualizar_beneficiario_por_id(
								int(beneficiario_id),
								novo_nome_responsavel,
								novo_telefone1,
								novo_telefone2,
								nova_data_nascimento,
								nova_rua,
								novo_numero,
								novo_complemento,
								novo_estado,
								nova_cidade,
								novo_bairro,
								novo_sexo
						)  # Fecha a janela após a atualização
				else:
						mostrar_aviso("Por favor, preencha todos os campos obrigatórios.")

		label_id_beneficiario = Label(window, text="ID do Beneficiário:")
		label_id_beneficiario.grid(row=0, column=0, pady=10)
		entry_id_beneficiario = Entry(window, width=10)
		entry_id_beneficiario.grid(row=0, column=1, pady=10)

		label_novo_nome_responsavel = Label(window, text="Novo Nome Responsável:")
		label_novo_nome_responsavel.grid(row=1, column=0, pady=10)
		entry_novo_nome_responsavel = Entry(window, width=30)
		entry_novo_nome_responsavel.grid(row=1, column=1, pady=10)

		label_novo_telefone1 = Label(window, text="Novo Telefone 1:")
		label_novo_telefone1.grid(row=2, column=0, pady=10)
		entry_novo_telefone1 = Entry(window, width=30)
		entry_novo_telefone1.grid(row=2, column=1, pady=10)

		label_novo_telefone2 = Label(window, text="Novo Telefone 2:")
		label_novo_telefone2.grid(row=3, column=0, pady=10)
		entry_novo_telefone2 = Entry(window, width=30)
		entry_novo_telefone2.grid(row=3, column=1, pady=10)

		label_nova_data_nascimento = Label(window, text="Nova Data de Nascimento:")
		label_nova_data_nascimento.grid(row=4, column=0, pady=10)
		entry_nova_data_nascimento = Entry(window, width=30)
		entry_nova_data_nascimento.grid(row=4, column=1, pady=10)

		label_nova_rua = Label(window, text="Nova Rua:")
		label_nova_rua.grid(row=5, column=0, pady=10)
		entry_nova_rua = Entry(window, width=30)
		entry_nova_rua.grid(row=5, column=1, pady=10)

		label_novo_numero = Label(window, text="Novo Número:")
		label_novo_numero.grid(row=6, column=0, pady=10)
		entry_novo_numero = Entry(window, width=30)
		entry_novo_numero.grid(row=6, column=1, pady=10)

		label_novo_complemento = Label(window, text="Novo Complemento:")
		label_novo_complemento.grid(row=7, column=0, pady=10)
		entry_novo_complemento = Entry(window, width=30)
		entry_novo_complemento.grid(row=7, column=1, pady=10)

		label_novo_estado = Label(window, text="Novo Estado:")
		label_novo_estado.grid(row=8, column=0, pady=10)
		entry_novo_estado = Entry(window, width=30)
		entry_novo_estado.grid(row=8, column=1, pady=10)

		label_nova_cidade = Label(window, text="Nova Cidade:")
		label_nova_cidade.grid(row=9, column=0, pady=10)
		entry_nova_cidade = Entry(window, width=30)
		entry_nova_cidade.grid(row=9, column=1, pady=10)

		label_novo_bairro = Label(window, text="Novo Bairro:")
		label_novo_bairro.grid(row=10, column=0, pady=10)
		entry_novo_bairro = Entry(window, width=30)
		entry_novo_bairro.grid(row=10, column=1, pady=10)

		label_novo_sexo = Label(window, text="Novo Sexo:")
		label_novo_sexo.grid(row=11, column=0, pady=10)
		entry_novo_sexo = Entry(window, width=30)
		entry_novo_sexo.grid(row=11, column=1, pady=10)

		b_atualizar_beneficiario = Button(window, text="Atualizar Beneficiário", width=20, height=2, command=atualizar_beneficiario)
		b_atualizar_beneficiario.grid(row=13, column=0, columnspan=2, pady=10)

def atualizar_familia_por_id(
		id_familia,
		novo_estado,
		novo_bairro,
		nova_cidade
):
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)

				if conexao.is_connected():
						cursor = conexao.cursor()

						sql = """
								UPDATE familia
								SET
										estado = %s,
										bairro = %s,
										cidade = %s
								WHERE id_familia = %s
						"""
						valores = (
								novo_estado,
								novo_bairro,
								nova_cidade,
								id_familia
						)
						cursor.execute(sql, valores)

						conexao.commit()
						mostrar_aviso(f"Família com ID {id_familia} atualizada com sucesso!")

						cursor.close()

		except Error as e:
				mostrar_aviso(f"Erro ao atualizar a família: {str(e)}")

		finally:
				if conexao.is_connected():
						conexao.close()


def atualizar_familia_window():

		window = Toplevel(w)
		window.title("Atualizar Família por ID")

		def atualizar_familia():
				id_familia = entry_id_familia.get()
				novo_estado = entry_novo_estado.get()
				novo_bairro = entry_novo_bairro.get()
				nova_cidade = entry_nova_cidade.get()

				if id_familia and novo_estado and novo_bairro and nova_cidade:
						atualizar_familia_por_id(
								int(id_familia),
								novo_estado,
								novo_bairro,
								nova_cidade
						)  # Fecha a janela após a atualização
				else:
						mostrar_aviso("Por favor, preencha todos os campos obrigatórios.")

		label_id_familia = Label(window, text="ID da Família:")
		label_id_familia.grid(row=0, column=0, pady=10)
		entry_id_familia = Entry(window, width=10)
		entry_id_familia.grid(row=0, column=1, pady=10)

		label_novo_estado = Label(window, text="Novo Estado:")
		label_novo_estado.grid(row=1, column=0, pady=10)
		entry_novo_estado = Entry(window, width=30)
		entry_novo_estado.grid(row=1, column=1, pady=10)

		label_novo_bairro = Label(window, text="Novo Bairro:")
		label_novo_bairro.grid(row=2, column=0, pady=10)
		entry_novo_bairro = Entry(window, width=30)
		entry_novo_bairro.grid(row=2, column=1, pady=10)

		label_nova_cidade = Label(window, text="Nova Cidade:")
		label_nova_cidade.grid(row=3, column=0, pady=10)
		entry_nova_cidade = Entry(window, width=30)
		entry_nova_cidade.grid(row=3, column=1, pady=10)

		b_atualizar_familia = Button(window, text="Atualizar Família", width=20, height=2, command=atualizar_familia)
		b_atualizar_familia.grid(row=4, column=0, columnspan=2, pady=10)

def atualizar_produto_por_id(id_produto, novo_nome, nova_descricao, novo_preco):
		try:
				conexao = mysql.connector.connect(
						host="localhost",
						user="root",
						password="",
						database="familias"
				)

				if conexao.is_connected():
						cursor = conexao.cursor()

						sql = """
								UPDATE produto
								SET
										nome = %s,
										descricao = %s,
										preco = %s
								WHERE id_produto = %s
						"""
						valores = (
								novo_nome,
								nova_descricao,
								novo_preco,
								id_produto
						)
						cursor.execute(sql, valores)

						conexao.commit()
						mostrar_aviso(f"Produto com ID {id_produto} atualizado com sucesso!")

						cursor.close()

		except Error as e:
				mostrar_aviso(f"Erro ao atualizar o produto: {str(e)}")

		finally:
				if conexao.is_connected():
						conexao.close()

def atualizar_produto_window():

		window = Toplevel(w)
		window.title("Atualizar Produto por ID")

		def atualizar_produto():
				id_produto = entry_id_produto.get()
				novo_nome = entry_novo_nome.get()
				nova_descricao = entry_nova_descricao.get()
				novo_preco = entry_novo_preco.get()

				if id_produto and novo_nome and nova_descricao and novo_preco:
						atualizar_produto_por_id(
								int(id_produto),
								novo_nome,
								nova_descricao,
								float(novo_preco)
						)
				else:
						mostrar_aviso("Por favor, preencha todos os campos obrigatórios.")

		label_id_produto = Label(window, text="ID do Produto:")
		label_id_produto.grid(row=0, column=0, pady=10)
		entry_id_produto = Entry(window, width=10)
		entry_id_produto.grid(row=0, column=1, pady=10)

		label_novo_nome = Label(window, text="Novo Nome:")
		label_novo_nome.grid(row=1, column=0, pady=10)
		entry_novo_nome = Entry(window, width=30)
		entry_novo_nome.grid(row=1, column=1, pady=10)

		label_nova_descricao = Label(window, text="Nova Descrição:")
		label_nova_descricao.grid(row=2, column=0, pady=10)
		entry_nova_descricao = Entry(window, width=30)
		entry_nova_descricao.grid(row=2, column=1, pady=10)

		label_novo_preco = Label(window, text="Novo Preço:")
		label_novo_preco.grid(row=3, column=0, pady=10)
		entry_novo_preco = Entry(window, width=30)
		entry_novo_preco.grid(row=3, column=1, pady=10)

		b_atualizar_produto = Button(window, text="Atualizar Produto", width=20, height=2, command=atualizar_produto)
		b_atualizar_produto.grid(row=4, column=0, columnspan=2, pady=10)

x = Menu(w)

arqvMenu = Menu(w, tearoff=0)

arqvMenu.add_command(label='Criar BD Familias', command=cdb)
arqvMenu.add_command(label='Criar Tabela Familia', command=criar_tabela_familia)
arqvMenu.add_command(label='Criar Tabela Beneficiario', command=criar_tabela_beneficiario)
arqvMenu.add_command(label='Criar Tabela Produto', command=criar_tabela_produto)

x.add_cascade(label='Banco de Dados', menu=arqvMenu)

cadsfamMenu = Menu(w, tearoff=0)

cadsfamMenu.add_command(label='Remover', command = remover_familia_window)
cadsfamMenu.add_command(label='Editar', command = atualizar_familia_window)
cadsfamMenu.add_command(label='Ver', command = ver_fam)

x.add_cascade(label="Familia", menu=cadsfamMenu)

cadsMenu = Menu(w, tearoff=0)

cadsMenu.add_command(label='Remover', command = remover_beneficiario_window)
cadsMenu.add_command(label='Editar', command=atualizar_beneficiario_window)
cadsMenu.add_command(label='Ver', command = ver_ben)

x.add_cascade(label="Beneficiário", menu=cadsMenu)

cadsMenu = Menu(w, tearoff=0)

cadsMenu.add_command(label='Remover', command = remover_produto_window)
cadsMenu.add_command(label='Editar', command = atualizar_produto_window)
cadsMenu.add_command(label='Ver',command = ver_pro)

x.add_cascade(label="Produto", menu=cadsMenu)

w.config(menu=x)


bf_B = Button(w, text="Cadastrar família", width=40, height=3, command=abrir_n_j_f)
bf_B.place(x=250, y=150)

bb_B = Button(w, text="Cadastrar beneficiário", width=40, height=3, command=abrir_n_j_b)
bb_B.place(x=250, y=250)

bp_B = Button(w, text="Cadastrar produto", width=40, height=3, command=abrir_n_j_p)
bp_B.place(x=250, y=350)

w.mainloop()
