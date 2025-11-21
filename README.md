# Desafio MBA Engenharia de Software com IA - Full Cycle

## Como executar a solução

### 1. Configuração do ambiente virtual (venv)

Antes de instalar as dependências, recomenda-se criar um ambiente virtual Python:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate    # Windows
```

### 2. Ingestão do PDF

A primeira etapa consiste em processar e salvar o conteúdo do PDF no banco de dados vetorial.

**Passos:**
1. Certifique-se de que o arquivo PDF desejado está no diretório do projeto e defina o caminho absoluto na variável de ambiente `PDF_PATH`.
2. Configure as variáveis de ambiente necessárias em um arquivo `.env`:
   - `PDF_PATH`: Caminho para o PDF a ser ingerido
   - `GOOGLE_API_KEY` ou `OPENAI_API_KEY`: Chave da API do modelo de linguagem
   - `GOOGLE_EMBEDDING_MODEL` ou `OPENAI_EMBEDDING_MODEL`: Nome do modelo de embeddings
   - `PG_VECTOR_COLLECTION_NAME`: Nome da coleção do banco vetorial
   - `DATABASE_URL`: URL de conexão do banco Postgres (ex: `postgresql://postgres:postgres@localhost:5432/rag`)
  ### Observações Importantes
   - **Configuração das chaves de ambiente:**
     - Se for usar o Google, defina **obrigatoriamente** `GOOGLE_API_KEY` e `GOOGLE_EMBEDDING_MODEL`.
     - Se for usar a OpenAI, defina **obrigatoriamente** `OPENAI_API_KEY` e `OPENAI_EMBEDDING_MODEL`.
     - **Não é permitido** misturar: não utilize o modelo de linguagem do Google com o embedding da OpenAI, nem o contrário. Sempre utilize ambos da mesma provedora.

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o script de ingestão:
   ```bash
   python src/ingest.py
   ```
   - O script irá dividir o PDF em chunks e salvar no banco vetorial.

### 3. Executar o Chat

Após a ingestão, você pode interagir com o chatbot para buscar informações presentes no PDF.

**Passos:**
1. Execute o script do chat:
   ```bash
   python src/chat.py
   ```
2. Digite sua pergunta em português no terminal. Para encerrar, digite `sair`.

---
- Certifique-se que o banco Postgres está rodando e acessível.
- Recomenda-se utilizar o DBeaver ou outro cliente para verificar os dados salvos.
- As respostas do chat são baseadas apenas no conteúdo do PDF ingerido.
- Mensagens de erro e logs técnicos são exibidos em inglês; a interação do usuário permanece em português.

---

## Exemplo de arquivo `.env`
```env
PDF_PATH=document.pdf
GOOGLE_API_KEY=your_google_api_key
GOOGLE_EMBEDDING_MODEL=gemini-2.5-flash-lite
PG_VECTOR_COLLECTION_NAME=meus_documentos
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag
```

---

## Dúvidas
Em caso de dúvidas, consulte os comentários nos arquivos ou entre em contato com o autor do projeto.
