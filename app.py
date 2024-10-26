import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

# Dados de exemplo
data = pd.DataFrame({
    'CNPJ': ['12345678000101', '98765432000102', '45612378000103', '12312378000104'],
    'Bairro': ['Centro', 'Zona Sul', 'Zona Norte', 'Fátima'],
    'Atividade': ['Comércio', 'Indústria', 'Serviços', 'Tecnologia']
})

# Inicializando o app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Layout do aplicativo
app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="Busca Dinâmica de Empresas",
        brand_href="#",
        color="primary",
        dark=True
    ),
    
    html.H2("Busca Dinâmica de Empresas", className="mt-3"),
    
    dbc.Row([
        dbc.Col(dcc.Input(id="cnpj-input", placeholder="Digite o CNPJ", type="text", style={"height": "50px"}), width=2),
        
        dbc.Col(dcc.Dropdown(
            id="bairro-input",
            options=[{"label": bairro, "value": bairro} for bairro in data["Bairro"].unique()],
            placeholder="Selecione o bairro",
            clearable=True,
            style={"height": "50px", "lineHeight": "50px"}
        ), width=3),

        dbc.Col(dcc.Dropdown(
            id="atividade-input",
            options=[{"label": atividade, "value": atividade} for atividade in data["Atividade"].unique()],
            placeholder="Selecione a atividade",
            clearable=True,
            style={"height": "50px", "lineHeight": "50px"}
        ), width=3)
    ], className="mb-3"),
    
    # Tabela de resultados
    html.Div(id="results-table"),
    
    # Texto de contagem de resultados ao final da página
    html.Div(id="results-count", style={"marginTop": "10px", "fontWeight": "bold"})
])

# Callback para atualizar a tabela de resultados e a contagem
@app.callback(
    [Output("results-table", "children"),
     Output("results-count", "children")],
    [Input("cnpj-input", "value"),
     Input("bairro-input", "value"),
     Input("atividade-input", "value")]
)
def update_results(cnpj, bairro, atividade):
    # Filtra os dados com base nos valores de entrada
    filtered_data = data[
        data["CNPJ"].str.contains(cnpj or "", case=False, na=False) &
        data["Bairro"].str.contains(bairro or "", case=False, na=False) &
        data["Atividade"].str.contains(atividade or "", case=False, na=False)
    ]

    # Cria a mensagem com base nos filtros aplicados
    count = len(filtered_data)
    plural = "s" if count != 1 else ""
    filters = []

    if cnpj:
        filters.append(f"para o CNPJ '{cnpj}'")
    if bairro:
        filters.append(f"para o bairro '{bairro}'")
    if atividade:
        filters.append(f"para a atividade '{atividade}'")

    filter_text = " e ".join(filters) if filters else ""
    
    if filter_text:
        count_message = f"{count} resultado{plural} encontrado{plural} {filter_text}"
    else:
        count_message = f"{count} resultado{plural} encontrado{plural}"

    # Gera a tabela de resultados
    if count > 0:
        table = dbc.Table.from_dataframe(filtered_data, striped=True, bordered=True, hover=True)
    else:
        table = html.Div("Nenhum resultado encontrado.")  # Mensagem se não houver resultados

    return table, count_message

# Rodando o app
if __name__ == "__main__":
    app.run_server(debug=True)
