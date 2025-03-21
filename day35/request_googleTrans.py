import httpx
from googletrans import Translator
import asyncio

# Função assíncrona para buscar a piada
async def fetch_joke():
    url = "https://api.chucknorris.io/jokes/random"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['value']
        else:
            raise Exception("Erro ao chamar a API.")

# Função assíncrona para traduzir o texto
async def translate_text(text, src='en', dest='pt'):
    translator = Translator()
    # A tradução é síncrona, mas podemos usar asyncio.to_thread para não bloquear o loop de eventos
    translated = await asyncio.to_thread(translator.translate, text, src=src, dest=dest)
    return translated.text

# Função principal assíncrona
async def main():
    try:
        # Busca a piada
        joke = await fetch_joke()
        print("Piada em inglês:")
        print(joke)

        # Traduz a piada
        translated_joke = await translate_text(joke)
        print("\nPiada em português:")
        print(translated_joke)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa o loop de eventos do asyncio
if __name__ == "__main__":
    asyncio.run(main())
