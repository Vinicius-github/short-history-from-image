from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama.llms import OllamaLLM  # Importando a classe correta para Ollama

def story_generator(scenario):
    template = """
    Você é um especialista contador de histórias infantis.
    Você pode criar histórias curtas com base em uma narrativa simples.
    Sua história deve ter mais de 50 palavras.
    A história deve ter um começo, meio e fim. Não precisa identificar no texto.
    Sempre de um título para as suas histórias. Não precisa identificar no texto.
    Escreva o texto em português Brasil.

    CONTEXT: {scenario}
    STORY:
    """
    prompt = PromptTemplate(
            template=template, 
            input_variables = ["scenario"])
    
    # Usando o modelo Ollama com LangChain
    story_llm = LLMChain(
        llm = OllamaLLM(  # Alterado para OllamaLLM
           model="mistral",  # Substitua pelo modelo que deseja usar
            temperature = 1),  # Temperatura configurada
        prompt=prompt, 
        verbose=True)
    
    story = story_llm.predict(scenario=scenario)
    return story