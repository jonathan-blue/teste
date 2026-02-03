"""
Apresentação Interativa: Por que Streamlit?
Execute com: streamlit run apresentacao_streamlit.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Configuração da página
st.set_page_config(
    page_title="Por que Streamlit?",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para visual mais bonito (compatível com tema dark)
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #FF4B4B, #7B68EE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 2rem;
        color: #FF4B4B;
        border-bottom: 3px solid #FF4B4B;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .highlight-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .compare-python {
        background: #306998;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    .compare-powerbi {
        background: #F2C811;
        color: black;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    /* Métricas com fundo escuro */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #3d3d5c;
    }
    [data-testid="stMetricLabel"] {
        color: #a0a0b0 !important;
    }
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }
    [data-testid="stMetricDelta"] {
        color: #4ade80 !important;
    }
    /* Cards de exemplo com fundo escuro */
    .dark-card {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #3d3d5c;
        color: #e0e0e0;
        height: 200px;
    }
    .dark-card h4 {
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    /* Steps cards */
    .step-card {
        background: linear-gradient(135deg, #1e3a5f 0%, #1e5a3a 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        height: 250px;
        color: #e0e0e0;
    }
    .step-card h3 {
        color: #ffffff;
    }
    .step-card code {
        background: #0d1117;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        color: #58a6ff;
    }
</style>
""", unsafe_allow_html=True)

# Navegação lateral
st.sidebar.markdown("## 📚 Navegação")
pagina = st.sidebar.radio(
    "Escolha uma seção:",
    [
        "🏠 Início",
        "🤔 O que é Streamlit?",
        "⚔️ Streamlit vs Power BI",
        "🎯 Quando usar cada um",
        "🔄 Caso: ETL + Dashboard",
        "🔥 Demo ao Vivo",
        "☁️ Como Publicar",
        "🎓 Conclusão"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Dica")
st.sidebar.info("Esta apresentação foi feita com Streamlit! Você está vendo o framework em ação.")

# ============================================
# PÁGINA: INÍCIO
# ============================================
if pagina == "🏠 Início":
    st.markdown('<h1 class="main-title">🚀 Streamlit: De Script a Produto</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; font-size: 1.3rem; color: #666;">
            <p>Transforme seus scripts Python em aplicações web interativas</p>
            <p><strong>Sem precisar virar desenvolvedor front-end</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Métricas animadas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📝 Linhas de código", "~50", "para um app completo")
    with col2:
        st.metric("⏱️ Tempo de aprendizado", "1 hora", "para começar")
    with col3:
        st.metric("🐍 Linguagem", "Python", "que você já sabe!")
    with col4:
        st.metric("💰 Custo", "Grátis", "open source")

    st.markdown("---")

    # O que vamos ver
    st.markdown("### 📋 O que vamos ver hoje:")

    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ O que é Streamlit e pra que serve")
        st.success("✅ Comparação honesta com Power BI")
        st.success("✅ Quando usar cada ferramenta")
    with col2:
        st.success("✅ Demonstração ao vivo com código")
        st.success("✅ Como publicar seu app na internet")
        st.success("✅ Exemplos práticos que você pode copiar")

# ============================================
# PÁGINA: O QUE É STREAMLIT?
# ============================================
elif pagina == "🤔 O que é Streamlit?":
    st.markdown('<h2 class="section-title">O que é Streamlit?</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        **Streamlit** é um framework Python para criar **aplicações web interativas**
        de forma simples e rápida.

        ### A mágica acontece assim:
        """)

        st.code("""
# Você escreve isso...
import streamlit as st
import pandas as pd

st.title("Meu Dashboard")
dados = pd.read_csv("vendas.csv")
st.dataframe(dados)
st.bar_chart(dados["valor"])
        """, language="python")

        st.markdown("### E o Streamlit transforma em uma aplicação web! 👆")

    with col2:
        st.markdown("### Você ganha de graça:")
        st.markdown("""
        - 🖱️ Botões
        - 📊 Gráficos interativos
        - 📁 Upload de arquivos
        - 🔽 Filtros e selects
        - 📋 Tabelas
        - 📥 Download de dados
        - 📄 Múltiplas páginas
        - 🎨 Tema bonito
        """)

    st.markdown("---")

    # Casos de uso
    st.markdown("### 💼 Exemplos de uso real:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="dark-card">
            <h4>📈 Dashboard de Vendas</h4>
            <p>Conecta no SQL Server, puxa dados, mostra KPIs e gráficos. Atualiza em tempo real.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="dark-card">
            <h4>📄 Processador de PDF</h4>
            <p>Upload de PDF → extrai dados → processa → exporta Excel. Tudo no navegador.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="dark-card">
            <h4>🤖 App de ML</h4>
            <p>Modelo de previsão onde o usuário insere dados e recebe a predição na hora.</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# PÁGINA: STREAMLIT VS POWER BI
# ============================================
elif pagina == "⚔️ Streamlit vs Power BI":
    st.markdown('<h2 class="section-title">Streamlit vs Power BI</h2>', unsafe_allow_html=True)

    st.markdown("### 🎭 Filosofias diferentes para problemas parecidos")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="compare-python">
            <h3>🐍 Streamlit</h3>
            <p><strong>"Código-first"</strong></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        #### Vantagens:
        - ✅ Flexibilidade total (é Python!)
        - ✅ Integra com ML, automação, APIs
        - ✅ Lógica complexa sem sofrer
        - ✅ Qualquer biblioteca Python
        - ✅ Controle total da experiência
        - ✅ Gratuito e open source

        #### Desvantagens:
        - ⚠️ Precisa programar
        - ⚠️ Menos "pronto" para BI corporativo
        - ⚠️ Governança você constrói
        """)

    with col2:
        st.markdown("""
        <div class="compare-powerbi">
            <h3>📊 Power BI</h3>
            <p><strong>"Visual-first"</strong></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        #### Vantagens:
        - ✅ Drag-and-drop (low-code)
        - ✅ Visuais prontos e bonitos
        - ✅ Power Query para ETL
        - ✅ DAX para métricas
        - ✅ Publicação corporativa robusta
        - ✅ Governança enterprise

        #### Desvantagens:
        - ⚠️ DAX pode virar pesadelo
        - ⚠️ Customização limitada
        - ⚠️ Integração ML é trabalhosa
        """)

    st.markdown("---")

    # Comparação visual
    st.markdown("### 📊 Comparação lado a lado")

    comparacao = pd.DataFrame({
        "Critério": ["Curva de aprendizado", "Flexibilidade", "Visuais prontos",
                     "Integração ML", "Deploy corporativo", "Custo"],
        "Streamlit": [4, 5, 3, 5, 3, 5],
        "Power BI": [3, 3, 5, 2, 5, 3]
    })

    fig = go.Figure()
    fig.add_trace(go.Bar(name='Streamlit', x=comparacao["Critério"], y=comparacao["Streamlit"],
                         marker_color='#306998'))
    fig.add_trace(go.Bar(name='Power BI', x=comparacao["Critério"], y=comparacao["Power BI"],
                         marker_color='#F2C811'))
    fig.update_layout(barmode='group', height=400,
                      yaxis_title="Nota (1-5)",
                      legend=dict(orientation="h", yanchor="bottom", y=1.02))
    st.plotly_chart(fig, use_container_width=True)

    st.info("💡 **Nota:** Esta comparação é subjetiva e depende do contexto de uso!")

# ============================================
# PÁGINA: QUANDO USAR CADA UM
# ============================================
elif pagina == "🎯 Quando usar cada um":
    st.markdown('<h2 class="section-title">Quando usar cada ferramenta?</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Use Power BI quando...")
        st.markdown("""
        - 🏢 Precisa de **dashboards corporativos**
        - 👔 O time é mais **negócio** que dev
        - 🔐 Precisa de **governança enterprise**
        - 📈 Quer **relatórios padronizados**
        - 🤝 Integração forte com Microsoft 365
        - 📊 Foco é **visualização de KPIs**
        """)

        with st.expander("📝 Exemplo de cenário Power BI"):
            st.markdown("""
            **Cenário:** Diretoria quer ver vendas por região, comparativo mensal,
            meta vs realizado. Precisa publicar para 50 gerentes com controle de acesso.

            **Por que Power BI:** Governança, publicação em massa, visuais prontos,
            atualização automática agendada.
            """)

    with col2:
        st.markdown("### 🐍 Use Streamlit quando...")
        st.markdown("""
        - 🔧 Precisa de **lógica customizada**
        - 🤖 Quer integrar **ML/IA**
        - ⚡ Quer **prototipar rápido**
        - 🎨 Precisa de **experiência única**
        - 📤 App com **upload/processamento**
        - 🔄 Automação com Python
        """)

        with st.expander("📝 Exemplo de cenário Streamlit"):
            st.markdown("""
            **Cenário:** Time precisa de ferramenta para fazer upload de planilha Excel,
            validar dados, aplicar regras de negócio, e exportar resultado processado.

            **Por que Streamlit:** Lógica customizada, manipulação de arquivo,
            validações específicas, tudo em Python.
            """)

    st.markdown("---")

    # Cenário do Projeto OLIST
    st.markdown("### 🛒 Nosso Projeto: Análise OLIST")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d1b4e 100%); padding: 1.5rem; border-radius: 15px; border: 2px solid #667eea; margin-bottom: 1rem;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">🎯 O Desafio</h4>
        <p style="color: #e0e0e0;">
            Analisar dados da <strong style="color: #58a6ff;">OLIST</strong> — ecossistema de soluções tecnológicas para varejo
            (ERP, Hub de integração, logística e financeiro em uma plataforma).
        </p>
        <p style="color: #e0e0e0;">
            <strong>9 perguntas de negócio</strong> para responder com dados reais de e-commerce brasileiro.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📋 Os 9 Desafios:")
        st.markdown("""
        1. ⏱️ Tempo médio da aprovação até entrega
        2. 📅 Mês com mais vendas vs mais pagamentos
        3. ⭐ Análise de satisfação (notas e comentários)
        4. 🚚 Relação satisfação × prazo de entrega
        5. 📦 Categorias mais/menos vendidas
        6. ⚖️ Impacto peso/volume no frete
        7. 🗺️ Mapa de concentração clientes/vendedores
        8. 🔄 Atrasos em entregas interestaduais
        9. 🔁 Padrão dos clientes que fizeram recompra
        """)

    with col2:
        st.markdown("#### 🤔 Qual ferramenta usar?")

        st.error("""
        **Power BI teria dificuldade com:**
        - ❌ Cálculos de tempo complexos (mediana, distribuições)
        - ❌ Análise de texto dos comentários
        - ❌ Correlações estatísticas avançadas
        - ❌ Mapas customizados com densidade
        - ❌ Identificar padrões de recompra (requer lógica)
        """)

        st.success("""
        **Streamlit resolve com facilidade:**
        - ✅ Pandas para qualquer cálculo temporal
        - ✅ Análise de sentimento com Python
        - ✅ Scipy/Statsmodels para estatística
        - ✅ Plotly/Folium para mapas interativos
        - ✅ Lógica Python para padrões complexos
        """)

    # Demonstração com dados simulados do OLIST
    st.markdown("---")
    st.markdown("#### 🔥 Preview: Como ficaria no Streamlit")

    # Dados simulados OLIST
    import numpy as np
    np.random.seed(42)

    olist_sample = pd.DataFrame({
        'pedido_id': range(1, 101),
        'estado_cliente': np.random.choice(['SP', 'RJ', 'MG', 'RS', 'PR', 'BA'], 100),
        'estado_vendedor': np.random.choice(['SP', 'RJ', 'MG', 'PR'], 100),
        'dias_entrega': np.random.randint(3, 25, 100),
        'prazo_estimado': np.random.randint(7, 20, 100),
        'nota': np.random.choice([1, 2, 3, 4, 5], 100, p=[0.05, 0.05, 0.1, 0.3, 0.5]),
        'valor_pedido': np.random.uniform(50, 500, 100).round(2),
        'frete': np.random.uniform(10, 80, 100).round(2)
    })
    olist_sample['entrega_atrasada'] = olist_sample['dias_entrega'] > olist_sample['prazo_estimado']
    olist_sample['interestadual'] = olist_sample['estado_cliente'] != olist_sample['estado_vendedor']

    tab1, tab2, tab3 = st.tabs(["📊 Desafio 4: Satisfação × Entrega", "🗺️ Desafio 8: Atrasos Interestaduais", "📈 Visão Geral"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            # Análise satisfação vs atraso
            analise = olist_sample.groupby('entrega_atrasada')['nota'].mean().reset_index()
            analise['status'] = analise['entrega_atrasada'].map({True: 'Atrasou', False: 'No Prazo'})

            fig = px.bar(analise, x='status', y='nota', color='status',
                        color_discrete_map={'No Prazo': '#4ade80', 'Atrasou': '#f87171'},
                        title='Nota Média por Status de Entrega')
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            font_color='#e0e0e0', showlegend=False)
            fig.update_yaxes(range=[0, 5])
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("**Código Python para esta análise:**")
            st.code("""
# Carregar dados
df = pd.read_sql("SELECT * FROM pedidos", conn)

# Calcular atraso
df['atrasou'] = df['dias_entrega'] > df['prazo']

# Análise de satisfação por status
resultado = df.groupby('atrasou')['nota'].agg(['mean', 'median', 'count'])

# Teste estatístico
from scipy.stats import mannwhitneyu
stat, pvalue = mannwhitneyu(
    df[df['atrasou']]['nota'],
    df[~df['atrasou']]['nota']
)
            """, language="python")

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            # Análise atrasos interestaduais
            atraso_inter = olist_sample.groupby('interestadual')['entrega_atrasada'].mean().reset_index()
            atraso_inter['tipo'] = atraso_inter['interestadual'].map({True: 'Interestadual', False: 'Mesmo Estado'})
            atraso_inter['percentual'] = (atraso_inter['entrega_atrasada'] * 100).round(1)

            fig = px.bar(atraso_inter, x='tipo', y='percentual', color='tipo',
                        color_discrete_map={'Mesmo Estado': '#4ade80', 'Interestadual': '#fbbf24'},
                        title='% de Atrasos por Tipo de Entrega')
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            font_color='#e0e0e0', showlegend=False,
                            yaxis_title='% Atrasos')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.metric("Atrasos Mesmo Estado",
                     f"{atraso_inter[atraso_inter['tipo']=='Mesmo Estado']['percentual'].values[0]:.1f}%")
            st.metric("Atrasos Interestaduais",
                     f"{atraso_inter[atraso_inter['tipo']=='Interestadual']['percentual'].values[0]:.1f}%")

            st.info("💡 Com Streamlit você pode adicionar filtros por estado, período, categoria... tudo interativo!")

    with tab3:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Pedidos", f"{len(olist_sample):,}")
        with col2:
            st.metric("Ticket Médio", f"R$ {olist_sample['valor_pedido'].mean():.2f}")
        with col3:
            st.metric("Nota Média", f"{olist_sample['nota'].mean():.1f} ⭐")
        with col4:
            st.metric("% Atrasos", f"{olist_sample['entrega_atrasada'].mean()*100:.1f}%")

    st.markdown("---")

    st.success("""
    ### 🏆 Veredicto para o Projeto OLIST:

    **Streamlit é a escolha ideal** porque:
    - 📊 **Análises estatísticas** complexas (medianas, correlações, testes)
    - 📝 **Processamento de texto** para comentários de satisfação
    - 🗺️ **Mapas interativos** para visualização geográfica
    - 🔄 **Lógica de negócio** para identificar padrões de recompra
    - 🎯 **Apresentação profissional** para os desafios em sala

    *Power BI seria viável para visualizações simples, mas limitado nos desafios mais analíticos.*
    """)

    st.markdown("---")

    # Quiz interativo
    st.markdown("### 🎮 Mini Quiz: Qual ferramenta você usaria?")

    cenario = st.selectbox(
        "Escolha um cenário:",
        [
            "Selecione um cenário...",
            "Dashboard de vendas para diretoria com 100 usuários",
            "App que recebe foto e classifica com IA",
            "Relatório de RH com dados sensíveis e governança",
            "Ferramenta interna para calcular comissões complexas",
            "Protótipo rápido para validar ideia de produto"
        ]
    )

    if cenario != "Selecione um cenário...":
        respostas = {
            "Dashboard de vendas para diretoria com 100 usuários": ("Power BI", "Governança, publicação em massa, visuais prontos"),
            "App que recebe foto e classifica com IA": ("Streamlit", "Integração com bibliotecas de ML/IA em Python"),
            "Relatório de RH com dados sensíveis e governança": ("Power BI", "Controle de acesso robusto e governança enterprise"),
            "Ferramenta interna para calcular comissões complexas": ("Streamlit", "Lógica de negócio complexa é mais fácil em Python"),
            "Protótipo rápido para validar ideia de produto": ("Streamlit", "Velocidade de desenvolvimento e iteração")
        }

        resp, motivo = respostas[cenario]
        if resp == "Power BI":
            st.warning(f"📊 **Power BI** seria a melhor escolha!\n\n*Motivo: {motivo}*")
        else:
            st.success(f"🐍 **Streamlit** seria a melhor escolha!\n\n*Motivo: {motivo}*")

# ============================================
# PÁGINA: CASO ETL + DASHBOARD
# ============================================
elif pagina == "🔄 Caso: ETL + Dashboard":
    st.markdown('<h2 class="section-title">Caso Prático: ETL + Dashboard</h2>', unsafe_allow_html=True)

    st.markdown("""
    ### 🎯 O Cenário
    Você precisa criar uma solução que:
    1. **Receba dados brutos** (Excel, CSV, ou banco)
    2. **Trate e transforme** (limpeza, validação, cálculos)
    3. **Apresente em dashboard** (gráficos, filtros, KPIs)
    """)

    st.markdown("---")

    # Comparação lado a lado
    st.markdown("### ⚔️ Como cada ferramenta resolveria isso?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: #F2C811; color: black; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3>📊 Power BI</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        #### Fluxo no Power BI:
        """)

        st.warning("""
        1. **Importar dados** no Power Query
        2. **Transformar** usando interface visual (M language por trás)
        3. **Criar modelo** com relacionamentos
        4. **Escrever DAX** para métricas calculadas
        5. **Montar visuais** arrastando campos
        6. **Publicar** no Power BI Service
        """)

        st.error("""
        **Problemas comuns:**
        - ❌ Regras de negócio complexas viram DAX ilegível
        - ❌ Validações customizadas são limitadas
        - ❌ Não dá pra rodar Python/scripts livremente
        - ❌ Transformações avançadas exigem M (linguagem própria)
        - ❌ Difícil versionar e revisar mudanças (não é código)
        """)

    with col2:
        st.markdown("""
        <div style="background: #306998; color: white; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3>🐍 Streamlit</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        #### Fluxo no Streamlit:
        """)

        st.success("""
        1. **Carregar dados** com Pandas (qualquer fonte)
        2. **Transformar** com Python puro (lógica que você já sabe)
        3. **Validar** com regras customizadas
        4. **Criar gráficos** com Plotly/Altair
        5. **Adicionar filtros** interativos
        6. **Publicar** no Streamlit Cloud (grátis)
        """)

        st.success("""
        **Vantagens claras:**
        - ✅ Qualquer lógica Python funciona
        - ✅ Bibliotecas de ETL prontas (Pandas, NumPy)
        - ✅ Validações complexas são triviais
        - ✅ Código versionável (Git)
        - ✅ Testes automatizados possíveis
        - ✅ Reutilização de funções
        """)

    st.markdown("---")

    # Exemplo prático comparativo
    st.markdown("### 💻 Exemplo: Calcular comissão com regras complexas")

    st.markdown("""
    **Regra de negócio:**
    - Vendedor bateu meta → 10% de comissão
    - Vendedor superou meta em 20% → 15% de comissão
    - Vendedor é sênior E bateu meta → bônus extra de 5%
    - Se o produto é da categoria "Premium" → comissão dobra
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### No Power BI (DAX):")
        st.code("""
Comissao =
VAR MetaBatida = [Vendas] >= [Meta]
VAR Superou20 = [Vendas] >= [Meta] * 1.2
VAR Senior = RELATED(Vendedor[Nivel]) = "Senior"
VAR Premium = RELATED(Produto[Categoria]) = "Premium"
VAR BaseComissao =
    SWITCH(
        TRUE(),
        Superou20, 0.15,
        MetaBatida, 0.10,
        0
    )
VAR BonusSenior = IF(Senior && MetaBatida, 0.05, 0)
VAR Multiplicador = IF(Premium, 2, 1)
RETURN
    [Vendas] * (BaseComissao + BonusSenior) * Multiplicador
        """, language="text")
        st.error("😵 Difícil de ler, debugar e manter!")

    with col2:
        st.markdown("#### No Streamlit (Python):")
        st.code("""
def calcular_comissao(row):
    taxa = 0

    # Regra de meta
    if row['vendas'] >= row['meta'] * 1.2:
        taxa = 0.15
    elif row['vendas'] >= row['meta']:
        taxa = 0.10

    # Bônus sênior
    if row['nivel'] == 'Senior' and row['vendas'] >= row['meta']:
        taxa += 0.05

    # Multiplicador premium
    if row['categoria'] == 'Premium':
        taxa *= 2

    return row['vendas'] * taxa

df['comissao'] = df.apply(calcular_comissao, axis=1)
        """, language="python")
        st.success("✅ Legível, testável, fácil de manter!")

    st.markdown("---")

    # Demo interativa
    st.markdown("### 🎮 Teste você mesmo: Mini ETL ao vivo")

    # Dados de exemplo
    dados_brutos = pd.DataFrame({
        'vendedor': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
        'vendas': [15000, 8000, 22000, 18000, 5000],
        'meta': [12000, 10000, 15000, 15000, 10000],
        'nivel': ['Senior', 'Junior', 'Senior', 'Pleno', 'Junior'],
        'categoria': ['Premium', 'Standard', 'Premium', 'Standard', 'Standard']
    })

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📥 Dados Brutos:")
        st.dataframe(dados_brutos, use_container_width=True)

    with col2:
        st.markdown("#### ⚙️ Dados Tratados (ETL aplicado):")

        def calcular_comissao(row):
            taxa = 0
            if row['vendas'] >= row['meta'] * 1.2:
                taxa = 0.15
            elif row['vendas'] >= row['meta']:
                taxa = 0.10
            if row['nivel'] == 'Senior' and row['vendas'] >= row['meta']:
                taxa += 0.05
            if row['categoria'] == 'Premium':
                taxa *= 2
            return row['vendas'] * taxa

        dados_tratados = dados_brutos.copy()
        dados_tratados['bateu_meta'] = dados_tratados['vendas'] >= dados_tratados['meta']
        dados_tratados['comissao'] = dados_tratados.apply(calcular_comissao, axis=1)

        st.dataframe(dados_tratados, use_container_width=True)

    # Dashboard com os dados tratados
    st.markdown("---")
    st.markdown("#### 📊 Dashboard com dados tratados:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Vendas", f"R$ {dados_tratados['vendas'].sum():,.0f}")
    with col2:
        st.metric("Total Comissões", f"R$ {dados_tratados['comissao'].sum():,.0f}")
    with col3:
        taxa_bateu = (dados_tratados['bateu_meta'].sum() / len(dados_tratados)) * 100
        st.metric("% Bateu Meta", f"{taxa_bateu:.0f}%")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            dados_tratados,
            x='vendedor',
            y=['vendas', 'meta'],
            barmode='group',
            title='Vendas vs Meta por Vendedor',
            color_discrete_map={'vendas': '#4ade80', 'meta': '#f87171'}
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#e0e0e0'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.pie(
            dados_tratados,
            values='comissao',
            names='vendedor',
            title='Distribuição de Comissões'
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#e0e0e0'
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.success("""
    ### 🏆 Conclusão deste caso:

    Para **ETL + Dashboard** com regras de negócio customizadas, **Streamlit vence** porque:

    1. **Tratamento de dados** é Python puro (Pandas) - mais poderoso que Power Query
    2. **Lógica de negócio** é código legível - não DAX críptico
    3. **Tudo em um lugar** - ETL e visualização no mesmo código
    4. **Versionável** - Git para controle de mudanças
    5. **Testável** - você pode criar testes unitários para suas regras
    """)

# ============================================
# PÁGINA: DEMO AO VIVO
# ============================================
elif pagina == "🔥 Demo ao Vivo":
    st.markdown('<h2 class="section-title">Demo ao Vivo - Veja o Código em Ação!</h2>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Gráficos", "📁 Upload", "🎛️ Widgets", "📥 Download"])

    # TAB 1: Gráficos
    with tab1:
        st.markdown("### Gráfico interativo em 5 linhas de código")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.code("""
# Gerar dados fictícios
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "Mês": meses,
    "Vendas": valores
})

fig = px.bar(df, x="Mês", y="Vendas")
st.plotly_chart(fig)
            """, language="python")

        with col2:
            # Dados demo
            meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
            vendas = [random.randint(100, 500) for _ in range(6)]

            df = pd.DataFrame({"Mês": meses, "Vendas": vendas})
            fig = px.bar(df, x="Mês", y="Vendas", color="Vendas",
                        color_continuous_scale="Blues")
            st.plotly_chart(fig, use_container_width=True)

            if st.button("🔄 Gerar novos dados"):
                st.rerun()

    # TAB 2: Upload
    with tab2:
        st.markdown("### Upload e processamento de arquivo")

        st.code("""
arquivo = st.file_uploader("Envie seu CSV", type="csv")
if arquivo:
    df = pd.read_csv(arquivo)
    st.dataframe(df)
        """, language="python")

        arquivo = st.file_uploader("📤 Envie um arquivo CSV para testar", type="csv")

        if arquivo:
            df = pd.read_csv(arquivo)
            st.success(f"✅ Arquivo carregado! {len(df)} linhas encontradas.")
            st.dataframe(df, use_container_width=True)
        else:
            st.info("☝️ Faça upload de um CSV para ver a mágica acontecer!")

            # Dados de exemplo
            with st.expander("📋 Ver dados de exemplo"):
                exemplo = pd.DataFrame({
                    "Produto": ["Notebook", "Mouse", "Teclado", "Monitor"],
                    "Quantidade": [10, 50, 30, 15],
                    "Preço": [3500, 80, 200, 1200]
                })
                st.dataframe(exemplo)

    # TAB 3: Widgets
    with tab3:
        st.markdown("### Widgets interativos")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Entrada de dados")
            nome = st.text_input("Seu nome:", "Estudante")
            idade = st.slider("Sua idade:", 18, 60, 25)
            curso = st.selectbox("Área:", ["TI", "Dados", "Negócios", "Design"])
            aceita = st.checkbox("Aceito aprender Streamlit!")

        with col2:
            st.markdown("#### Resultado em tempo real")
            if aceita:
                st.success(f"""
                👋 Olá, **{nome}**!

                Você tem **{idade} anos** e trabalha com **{curso}**.

                Pronto para dominar Streamlit! 🚀
                """)
            else:
                st.warning("Marque a checkbox para ver a mágica! ✨")

        st.markdown("---")
        st.code("""
nome = st.text_input("Seu nome:")
idade = st.slider("Idade:", 18, 60, 25)
curso = st.selectbox("Área:", ["TI", "Dados", "Negócios"])
aceita = st.checkbox("Aceito aprender!")

if aceita:
    st.success(f"Olá, {nome}!")
        """, language="python")

    # TAB 4: Download
    with tab4:
        st.markdown("### Exportar dados para download")

        st.code("""
df = criar_relatorio()
csv = df.to_csv(index=False)
st.download_button(
    "📥 Baixar CSV",
    csv,
    "relatorio.csv"
)
        """, language="python")

        # Criar relatório demo
        relatorio = pd.DataFrame({
            "Data": pd.date_range(start="2024-01-01", periods=10, freq="D"),
            "Vendas": [random.randint(1000, 5000) for _ in range(10)],
            "Clientes": [random.randint(10, 50) for _ in range(10)]
        })

        st.dataframe(relatorio, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            csv = relatorio.to_csv(index=False)
            st.download_button(
                "📥 Baixar como CSV",
                csv,
                "relatorio.csv",
                "text/csv"
            )
        with col2:
            st.download_button(
                "📥 Baixar como JSON",
                relatorio.to_json(orient="records"),
                "relatorio.json",
                "application/json"
            )

# ============================================
# PÁGINA: COMO PUBLICAR
# ============================================
elif pagina == "☁️ Como Publicar":
    st.markdown('<h2 class="section-title">Como Publicar seu App</h2>', unsafe_allow_html=True)

    st.markdown("### 🌐 Streamlit Community Cloud (Grátis!)")

    st.markdown("""
    O Streamlit oferece hospedagem gratuita para seus apps. Qualquer pessoa com o link pode acessar!
    """)

    # Passos
    st.markdown("### 📋 Passo a Passo:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="step-card">
            <h3>1️⃣ Prepare o Projeto</h3>
            <p>Crie um repositório no GitHub com:</p>
            <code>app.py</code><br><br>
            <code>requirements.txt</code>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="step-card">
            <h3>2️⃣ Conecte</h3>
            <p>Acesse:</p>
            <a href="https://share.streamlit.io" target="_blank" style="color: #58a6ff;">share.streamlit.io</a>
            <p>Faça login com GitHub e conecte seu repositório</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="step-card">
            <h3>3️⃣ Deploy!</h3>
            <p>Clique em Deploy e aguarde.</p>
            <p>Você receberá uma URL pública:</p>
            <code>seuapp.streamlit.app</code>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Estrutura do projeto
    st.markdown("### 📁 Estrutura mínima do projeto:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**app.py** (seu código)")
        st.code("""
import streamlit as st
import pandas as pd

st.title("Meu App")
# ... seu código
        """, language="python")

    with col2:
        st.markdown("**requirements.txt** (dependências)")
        st.code("""
streamlit
pandas
plotly
        """, language="text")

    st.markdown("---")

    # Limitações
    with st.expander("⚠️ Limitações do plano gratuito"):
        st.markdown("""
        - **Recursos limitados:** RAM e CPU são compartilhados
        - **Apps pesados:** Podem ficar lentos
        - **Sleep automático:** Apps inativos "dormem" e demoram para acordar
        - **Banco privado:** Se seu banco não é público, pode precisar de configuração extra

        **Para uso corporativo sério:** Considere deploy em servidor próprio (AWS, Azure, etc.)
        """)

    with st.expander("🔐 Como usar senhas/tokens com segurança"):
        st.markdown("""
        **Nunca coloque senhas no código!**

        Use o sistema de Secrets do Streamlit:

        1. No Streamlit Cloud, vá em Settings > Secrets
        2. Adicione suas variáveis:
        ```toml
        [database]
        host = "seu-servidor"
        password = "sua-senha-segura"
        ```
        3. No código, acesse assim:
        ```python
        senha = st.secrets["database"]["password"]
        ```
        """)

# ============================================
# PÁGINA: CONCLUSÃO
# ============================================
elif pagina == "🎓 Conclusão":
    st.markdown('<h2 class="section-title">Conclusão</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h3>🎯 Resumo Final</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: #306998; color: white; padding: 2rem; border-radius: 15px; text-align: center;">
            <h3>🐍 Streamlit</h3>
            <p><em>"Um app que você programou com Python"</em></p>
            <br>
            <p>✅ Flexibilidade total</p>
            <p>✅ Integra com tudo de Python</p>
            <p>✅ De script a produto</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: #F2C811; color: black; padding: 2rem; border-radius: 15px; text-align: center;">
            <h3>📊 Power BI</h3>
            <p><em>"PowerPoint de dados + modelo analítico"</em></p>
            <br>
            <p>✅ BI corporativo pronto</p>
            <p>✅ Governança enterprise</p>
            <p>✅ Visual drag-and-drop</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 💡 A mensagem que fica:")

    st.success("""
    **Streamlit e Power BI não são concorrentes — são complementares.**

    - Power BI domina o **BI corporativo pronto**
    - Streamlit domina o **app personalizado com lógica Python**

    **Se você sabe Python, Streamlit vira uma arma — e Power BI vira só mais uma ferramenta.**
    """)

    st.markdown("---")

    # Próximos passos
    st.markdown("### 🚀 Próximos passos sugeridos:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **1. Pratique**
        - Pegue um script seu
        - Transforme em app Streamlit
        - Adicione interatividade
        """)

    with col2:
        st.markdown("""
        **2. Publique**
        - Crie conta no GitHub
        - Faça deploy no Streamlit Cloud
        - Compartilhe o link
        """)

    with col3:
        st.markdown("""
        **3. Evolua**
        - Explore a documentação
        - Veja a galeria de apps
        - Crie seu portfólio
        """)

    st.markdown("---")

    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white;">
        <h2>Obrigado! 🎉</h2>
        <p>Dúvidas? Vamos conversar!</p>
        <br>
        <p><strong>Recursos úteis:</strong></p>
        <p>📚 Documentação: <a href="https://docs.streamlit.io" style="color: #FFD700;">docs.streamlit.io</a></p>
        <p>🎨 Galeria: <a href="https://streamlit.io/gallery" style="color: #FFD700;">streamlit.io/gallery</a></p>
        <p>💬 Comunidade: <a href="https://discuss.streamlit.io" style="color: #FFD700;">discuss.streamlit.io</a></p>
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>Feito com ❤️ usando Streamlit</div>",
    unsafe_allow_html=True
)
