from search import search_prompt
from src.clients.pgvector import vector_store


def retrieve_context(question):
    """Retrieves relevant context using the vector_store."""
    try:
        retrieved_docs = vector_store.similarity_search(question, k=10)
        return retrieved_docs
    except Exception as e:
        print(f"Error retrieving context: {e}")
        return []


def main():
    """Main chatbot loop."""
    chain = search_prompt()

    if not chain:
        print("Error: Could not start the chat. Check initialization errors.")
        return

    while True:
        question = input("Digite sua pergunta ou 'sair' para encerrar:> ")
        if question.strip().lower() == "sair":
            break
        context = retrieve_context(question)
        try:
            response = chain.invoke({"contexto": context, "pergunta": question})
            print(f"Resposta: {response.content}")
        except Exception as e:
            print(f"Error generating response: {e}")

    print("Obrigado por usar nosso chatbot!")


if __name__ == "__main__":
    main()
