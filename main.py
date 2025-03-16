import streamlit as st


st.set_page_config(layout='wide')

st.divider()
st.markdown('# :blue[Projetos - Jorge Carvalho :material/monitoring:]')
st.divider()

pag1, pag2, pag3, pag4 = st.columns([1, 1, 1, 9])

with pag1:
    if st.button('Quem eu sou'):
        st.session_state.page = 'home'

with pag2:
    if st.button('Projetos'):
        st.session_state.page = 'pag1'

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'pag1':
    col1, col2 = st.columns([0.5, 0.5], border=True)

    with col1:
        st.markdown('## :gray[Evolução do preço da gasolina no Brasil -:material/local_gas_station:]')

        st.markdown('[![GitHub](https://img.shields.io/badge/GitHub-blue?logo=github&logoColor=white)](https://github.com/jorgecarvalhopi/Python_Analise-Precos-Gasolina-Comum)')

        st.divider()
        text = '''
                Já se perguntou como o preço da gasolina no Brasil veio sofrendo modificações nos últimos anos?

                Será que essas oscilações que vemos nos jornais sempre existiram? Pensando em responder essas perguntas, resolvi analisar o comportamento do valor dessa mercadoria em nosso país no intervalo entre os anos de 2013 e 2021.

                Abaixo estarão algumas prévias dos resultados desse estudo.
        '''
        st.markdown(text)
        st.image('./images/analise_serie.png')
        text = '''
                Conseguiu ver que claramente houve um aumento a partir de 2015? E como a variação desse produto disparou significativamente?
        '''
        st.markdown(text)
        st.image('./images/visao_geral_dados_quant.png')

    with col2:
        st.markdown('## :gray[Dados do Enem - :material/menu_book:]')
        st.markdown('[![GitHub](https://img.shields.io/badge/GitHub-blue?logo=github&logoColor=white)](https://github.com/jorgecarvalhopi/Python_Analise-Precos-Gasolina-Comum)')

if st.session_state.page == 'home':
    col1, col2 = st.columns([0.6, 1.7])

    with col1:
        st.image('./images/perfil.jpg')
    with col2:
        st.markdown("""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
            <a href="https://www.linkedin.com" target="_blank">
                <button style="font-size: 16px; padding: 10px; display: flex; align-items: center;">
                    <i class="bi bi-linkedin" style="font-size: 1.5rem; margin-right: 8px;"></i>
                    LinkedIn
                </button>
            </a>
        """, unsafe_allow_html=True)

        st.markdown('## Sobre')
        st.markdown('''
                        Sou um Analista de Dados apaixonado por otimizar processos e transformar dados em insights acionáveis. Com sólida experiência em transformação digital, ETL, automação de relatórios e criação de paineis analíticos, minha missão é aprimorar a tomada de decisão e aumentar a eficiência operacional por meio da análise de dados. Tenho facilidade em me comunicar com diferentes equipes, seja para buscar auxílio em desafios técnicos ou para compartilhar resultados de maneira clara e objetiva.

                        :blue[Resultados Conseguidos:]

                        * Aumento da Eficiência Operacional: Redução drástica do tempo de geração de relatórios, passando de uma média de 3 horas para 1 minuto, por meio da criação de ferramentas automatizadas com Python e SQL, a custo praticamente zero.

                        * Análises Mais Customizadas: Desenvolvimento de análises de correlação multivariada e estudos de lucratividade por SKU, ampliando a flexibilidade das decisões da equipe de gestão, com base em dados personalizados, sem depender de relatórios predefinidos.

                        * Expansão da Capacidade Analítica: Criação de painéis dinâmicos e de fácil acesso para a equipe operacional de varejo, com atualização automática quase em tempo real. Essa solução, desenvolvida majoritariamente com Python, eliminou custos com licenças de software e agilizou a atualização de dados, melhorando a eficiência nas decisões operacionais.

                        * Identificação e Prevenção de Fraudes: Implementação de análise cruzada entre bases de dados, como clientes e funcionários, para identificar padrões e comportamentos suspeitos, mitigando fraudes e gerando economia significativa para a empresa.

                        *Habilidades: #Python, #SQL, #PowerBI, #Excel, #WebScraping, #ETL, #Análise de Dados, #Business Intelligence.*
        ''')