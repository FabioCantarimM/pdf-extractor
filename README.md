# PDF Extractor

Este projeto é uma ferramenta para extrair dados de arquivos PDF usando Python. Ele utiliza diversas bibliotecas para processamento de PDFs, manipulação de dados e interação com bancos de dados.

## Dependências

Certifique-se de que você tem as seguintes dependências instaladas:

```toml
[tool.poetry.dependencies]
python = "^3.12"
camelot-py = "^0.11.0"
opencv-python = "^4.9.0.80"
matplotlib = "^3.8.3"
ghostscript = "^0.7"
pandas = "^2.2.2"
psycopg2-binary = "^2.9.9"
sqlalchemy = "^2.0.32"
unidecode = "^1.3.8"
```

## Variáveis de Ambiente

O projeto requer as seguintes variáveis de ambiente para configurar o acesso ao banco de dados PostgreSQL:

- `DB_NAME`: Nome do banco de dados
- `DB_USER`: Nome de usuário do banco de dados
- `DB_PASSWORD`: Senha do banco de dados
- `DB_HOST`: Host do banco de dados (ex.: `localhost` ou IP do servidor)

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone <URL do repositório>
   cd <nome do repositório>
   ```

2. Instale as dependências usando Poetry:
   ```bash
   poetry install
   ```

3. Defina as variáveis de ambiente. Você pode criar um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```env
   DB_NAME=seu_nome_de_banco_de_dados
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_HOST=seu_host
   ```

4. Execute o projeto:
   ```bash
   poetry run python <nome_do_seu_script>.py
   ```

## Uso

Descreva aqui como usar o projeto, incluindo exemplos de comandos ou código para realizar operações básicas.

## Contribuição

Se você deseja contribuir para este projeto, por favor, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

Substitua `<URL do repositório>`, `<nome do repositório>` e `<nome_do_seu_script>.py` com as informações específicas do seu projeto. Ajuste a seção "Uso" conforme as funcionalidades do seu projeto.