import streamlit as st
import google.generativeai as genai

chave = st.secrets["chave"]
# Configura a API key do Gemini corretamente para a versão instalada
genai.configure(api_key= chave)

model = genai.GenerativeModel("gemini-2.0-flash")

def gerar_resposta_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"


# Configuração da página
st.set_page_config(page_title="Minha App", page_icon="🚀")


st.header("Exercício IA 1 - Criador de Histórias Interativas com IA 📚")

# Interface para o usuário
nome = st.text_input("Qual o nome do protagonista?")
generoliterario = st.selectbox("Qual o gênero literário da história?", ["Fantasia", "Ficção Científica", "Mistério", "Aventura"])
localInicial = st.radio("Onde esta aventura irá começar?",["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado", "Uma nave espacial à deriva"])
frasextra = st.text_input("Adiciona uma frase adicional que será inserida na história:", placeholder=("E de repente, tudo ficou escuro, O mapa indicava um perigo iminente."))
                     


if st.button("Gerar Sugestão de história"):
    if not nome:
        st.warning("Por favor, informe o nome do protagonista")
    elif not generoliterario:
        st.warning("Insira o genero literário da história")
    elif not localInicial:
        st.warning("Insira onde a jornada deve iniciar")
    else:
        if frasextra:
            prompt_aluno = (
                f"Crie o início de uma história de {generoliterario} com o protagonista chamado {nome}.A história começa em {localInicial}.Incorpore a seguinte frase ou desafio no início: {frasextra}."
            )
        else:
            prompt_aluno = (f"Crie o início de uma história de {generoliterario}com o protagonista chamado {nome}.A história começa em {localInicial}.")

        st.markdown("---")
        st.markdown("⚙️ **Prompt que será enviado para a IA (para fins de aprendizado):**")
        st.text_area("",prompt_aluno, height=250)
        st.markdown("---")

        st.info("Aguarde, a IA está montando sua história dos sonhos...")
        resposta_ia = gerar_resposta_gemini(prompt_aluno)

        if resposta_ia:
            st.markdown("### ✨ Sugestão de história da IA:")
            st.markdown(resposta_ia)
        else:
            st.error("Não foi possível gerar a história. Verifique as mensagens acima ou tente novamente mais tarde.")

st.header("Exercício IA 2 - Gerador de Receitas Culinárias Personalizadas com IA 🧑‍🍳")

ingredientes = st.text_area("Digite os ingredientes principais da receita:")
culinariaOpcoes = ["Italiana", "Brasileira", "Asiática", "Mexicana", "Qualquer uma"]
culinaria = st.selectbox("Qual o tipo de culinária dessa receita?", culinariaOpcoes,index=4)
dificuldade = st.slider("Qual a dificuldade desejada para a receita? 1 - Muito Fácil ... 5 - Muito Difícil", 1, 5)
restricao = st.checkbox("Possui restrição alimentar?")
if restricao:
    restricaoEspecifica = st.text_area("Diga quais restrições alimentares você possui:",placeholder=("sem glúten, vegetariana, sem lactose"))

if st.button("Gerar Sugestão de receita"):
    if not ingredientes:
        st.warning("Por favor, informe os ingredientes necessários para a receita")
    else:
        if restricao:
            prompt_aluno = (f"Sugira uma receita {culinaria} com nível de dificuldade {dificuldade} (sendo 1 muito fácil e 5 desafiador). Deve usar principalmente os seguintes ingredientes: {ingredientes}, com exceção dos {restricaoEspecifica}.  Apresente o nome da receita e uma lista de ingredientes adicionais se necessário, e um breve passo a passo.")
        else:
            prompt_aluno = (f"Sugira uma receita {culinaria} com nível de dificuldade {dificuldade} (sendo 1 muito fácil e 5 desafiador). Deve usar principalmente os seguintes ingredientes: {ingredientes}. Apresente o nome da receita e uma lista de ingredientes adicionais se necessário, e um breve passo a passo.")

        st.markdown("---")
        st.markdown("⚙️ **Prompt que será enviado para a IA (para fins de aprendizado):**")
        st.text_area("",prompt_aluno, height=250)
        st.markdown("---")

        st.info("Aguarde, a IA está montando sua receita dos sonhos...")
        resposta_ia = gerar_resposta_gemini(prompt_aluno)

        if resposta_ia:
            st.markdown("### ✨ Sugestão de receita da IA:")
            st.markdown(resposta_ia)
        else:
            st.error("Não foi possível gerar a receita. Verifique as mensagens acima ou tente novamente mais tarde.")