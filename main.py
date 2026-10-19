from pathlib import Path
import shutil


# Categorias e extensoes aceitas; adicione novas extensoes aqui.
EXTENSOES = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".tiff", ".heic"},
    "Documentos": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt", ".ods", ".csv", ".rtf"},
    "Codigos": {".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css", ".json", ".xml", ".yaml", ".yml", ".sql", ".sh"},
    "Compactados": {".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"},
}


def organizar_pasta(caminho: str) -> None:
    pasta_alvo = Path(caminho).expanduser()

    # Valida o caminho antes de listar ou mover qualquer arquivo.
    if not pasta_alvo.is_dir():
        print(f"Erro: '{pasta_alvo}' não existe ou não é uma pasta.")
        return

    arquivos_para_mover = []
    sem_categoria = 0

    # Monta a prévia sem alterar a pasta; subpastas não são processadas.
    for arquivo in sorted(pasta_alvo.iterdir()):
        if not arquivo.is_file():
            continue

        categoria = next(
            (nome for nome, extensoes in EXTENSOES.items() if arquivo.suffix.lower() in extensoes),
            None,
        )
        if categoria is None:
            sem_categoria += 1
        else:
            arquivos_para_mover.append((arquivo, categoria))

    if not arquivos_para_mover:
        print(f"Nenhum arquivo reconhecido para mover. Sem categoria: {sem_categoria}.")
        return

    print("Prévia dos arquivos:")
    for arquivo, categoria in arquivos_para_mover:
        print(f"  {arquivo.name} -> {categoria}/")

    # A confirmação evita mover arquivos sem uma revisão prévia.
    if input("\nConfirma a organização? (s/N): ").strip().lower() != "s":
        print("Operação cancelada. Nenhum arquivo foi movido.")
        return

    movidos = 0
    conflitos = 0
    erros = 0

    # Cria as pastas necessárias e move os arquivos, sem substituir nomes existentes.
    for arquivo, categoria in arquivos_para_mover:
        pasta_destino = pasta_alvo / categoria
        destino = pasta_destino / arquivo.name

        if destino.exists():
            print(f"Conflito: '{destino.name}' já existe em '{categoria}/'; arquivo ignorado.")
            conflitos += 1
            continue

        try:
            pasta_destino.mkdir(exist_ok=True)
            shutil.move(str(arquivo), str(destino))
            print(f"Movido: {arquivo.name} -> {categoria}/")
            movidos += 1
        except OSError as erro:
            print(f"Erro ao mover '{arquivo.name}': {erro}")
            erros += 1

    # Resume o resultado para deixar claro o que foi movido ou ignorado.
    print(
        "\nOrganização concluída: "
        f"{movidos} movido(s), {sem_categoria} sem categoria, "
        f"{conflitos} conflito(s), {erros} erro(s)."
    )


if __name__ == "__main__":
    caminho = input("Digite o caminho completo da pasta que deseja organizar: ").strip()
    organizar_pasta(caminho)
