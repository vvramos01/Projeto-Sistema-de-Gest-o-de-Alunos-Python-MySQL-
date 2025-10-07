from conexao import conectar

def cadastrar_aluno():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota final: "))
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (%s,%s,%s)", (nome, idade, nota))
    conn.commit()
    conn.close()
    print("Aluno cadastrado!\n")

def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    print("\n--- Lista de Alunos ---")
    for id, nome, idade, nota in cursor.fetchall():
        print(f"{id} - {nome}, {idade} anos, Nota: {nota}")
    conn.close()

def relatorio():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(nota) FROM alunos")
    media = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM alunos WHERE nota >= 6")
    aprovados = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM alunos WHERE nota < 6")
    reprovados = cursor.fetchone()[0]
    conn.close()
    print(f"\n--- Relatório ---")
    print(f"Média das notas: {media:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}\n")

def main():
    while True:
        print("=== Sistema de Alunos ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Relatório")
        print("4 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            relatorio()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    main()
