import streamlit as st

# Função principal do app
def main():
    # Título do app
    st.title("Exemplo de App com Botão")

    # Texto explicativo
    st.write("Este é um exemplo de aplicativo simples usando Streamlit. O botão abaixo realiza uma ação quando clicado.")

    # Botão
    if st.button('Clique aqui'):
        st.balloons()
        # Ação quando o botão for pressionado
        st.write("Você clicou no botão!")
    
    # Para mostrar um pouco mais de interação
    nome = st.text_input("Digite seu nome:")
    if nome:
        st.write(f"Olá, {nome}! Seja bem-vindo ao app!")

# Inicia o aplicativo
if __name__ == "__main__":
    main()
