# Organizador de Arquivos

Script simples em Python que organiza arquivos de uma pasta em categorias, de acordo com a extensão.

## Requisitos

- Python 3 instalado.

## Como usar

1. Abra o PowerShell ou terminal do VS Code.
2. Acesse a pasta do projeto:

   ```powershell
   cd "C:\Users\diego\Desktop\organizar-arquivos"
   ```

3. Execute o script:

   ```powershell
   py main.py
   ```

   Se `py` não funcionar, tente `python main.py`.

4. Digite o caminho da pasta que deseja organizar, sem aspas. Exemplo:

   ```text
   C:\Users\diego\Downloads
   ```

5. Confira a prévia e digite `s` para confirmar. Qualquer outra resposta cancela a operação.

## Categorias

O script organiza imagens, documentos, códigos, arquivos compactados, áudios e vídeos. As extensões reconhecidas estão definidas no dicionário `EXTENSOES` de `main.py`.

## Observações

- Os arquivos são **movidos**, não copiados.
- Arquivos sem extensão reconhecida ficam onde estão.
- Subpastas não são processadas.
- Se já existir um arquivo com o mesmo nome na pasta de destino, o arquivo não é movido e um aviso é exibido.

## 👨‍💻 Autor

### Diego Francisco da Silva

Desenvolvedor Front-End em formação e estudante de Engenharia de Software.

- **[Site Empresa](https://diegofranciscodasilva.github.io/dev-software-web/)**: dev.software.web Site Empresa
- **[LinkedIn](https://www.linkedin.com/in/diego-francisco-da-silva/)**: diego-francisco-da-silva
- **[GitHub](https://github.com/diegofranciscodasilva)**: diegofranciscodasilva
- **[Instagram](https://www.instagram.com/diego_francisco_da_silva/)**: @diego_francisco_da_silva
- **[Instagram](https://www.instagram.com/dev.software.web/)**: @dev.software.web

---

Feito com ❤️ por Diego.
