"""Demonstração acadêmica de análise de dados com registros inteiramente fictícios."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "dados_exemplo_ficticios.csv"
RESULTS_DIR = BASE_DIR / "results"


def limpar_colunas(df):
    df = df.copy()
    df.columns = (df.columns.str.strip().str.lower().str.replace("\\n", " ", regex=False))
    return df


def encontrar_coluna(df, termo):
    return next((col for col in df.columns if termo in col), None)


def pontuar_registro(linha, col_exp, col_agilidade, col_disp, col_motivacao):
    """Avalia o registro com base em critérios heurísticos."""
    pontos = 0
    experiencia = str(linha[col_exp]).lower()
    agilidade = str(linha[col_agilidade]).lower()
    disponibilidade = str(linha[col_disp]).lower()
    motivacao = str(linha[col_motivacao]).strip()

    if any(p in experiencia for p in ["lanchonete", "atendimento", "restaurante", "cozinha", "vendas"]):
        pontos += 3
    elif experiencia.strip():
        pontos += 1

    if any(p in agilidade for p in ["ágil", "agil", "ráp", "dinâmic", "eficiente"]):
        pontos += 3
    elif len(agilidade.strip()) > 10:
        pontos += 2
    elif agilidade.strip():
        pontos += 1

    if any(p in disponibilidade for p in ["integral", "manhã", "manha"]):
        pontos += 2
    elif disponibilidade.strip():
        pontos += 1

    if len(motivacao) > 40:
        pontos += 2
    elif motivacao:
        pontos += 1
    return pontos


def salvar_grafico(serie, titulo, arquivo, pizza=False):
    plt.figure(figsize=(7, 5), dpi=180)
    if pizza:
        serie.plot(kind="pie", autopct="%1.1f%%", startangle=90)
        plt.ylabel("")
    else:
        serie.plot(kind="bar")
        plt.ylabel("Quantidade")
        plt.xticks(rotation=20, ha="right")
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / arquivo)
    plt.close()


def main():
    RESULTS_DIR.mkdir(exist_ok=True)
    dados = limpar_colunas(pd.read_csv(DATA_FILE)).fillna("")
    col_exp = encontrar_coluna(dados, "experiência")
    col_disp = encontrar_coluna(dados, "disponibilidade")
    col_esc = encontrar_coluna(dados, "ensino médio")
    col_agil = encontrar_coluna(dados, "agilidade")
    col_motiv = encontrar_coluna(dados, "por que")
    required = [col_exp, col_disp, col_esc, col_agil, col_motiv]
    if any(col is None for col in required):
        raise ValueError("A base não contém todas as colunas esperadas para a demonstração.")

    experiencia = dados[col_exp].apply(
        lambda valor: "Com experiência" if str(valor).strip() else "Sem experiência"
    ).value_counts()
    disponibilidade = dados[col_disp].value_counts()
    escolaridade = dados[col_esc].astype(str).str.strip().str.lower().value_counts()

    salvar_grafico(experiencia, "Experiência anterior", "grafico_experiencia.png", pizza=True)
    salvar_grafico(disponibilidade, "Disponibilidade de horário", "grafico_disponibilidade.png")
    salvar_grafico(escolaridade, "Escolaridade", "grafico_escolaridade.png")

    dados["pontuacao demonstrativa"] = dados.apply(
        lambda linha: pontuar_registro(linha, col_exp, col_agil, col_disp, col_motiv), axis=1
    )
    resumo = pd.DataFrame({
        "Total de registros": [len(dados)],
        "Com experiência": [int(experiencia.get("Com experiência", 0))],
        "Sem experiência": [int(experiencia.get("Sem experiência", 0))],
    })
    resumo.to_csv(RESULTS_DIR / "resumo.csv", index=False, encoding="utf-8-sig")
    with pd.ExcelWriter(RESULTS_DIR / "relatorio_demonstrativo.xlsx") as writer:
        dados.to_excel(writer, sheet_name="Dados fictícios", index=False)
        resumo.to_excel(writer, sheet_name="Resumo", index=False)

    print(f"Registros fictícios analisados: {len(dados)}")

    print("\nExperiência:\n", experiencia.to_string())
    print("\nDisponibilidade:\n", disponibilidade.to_string())
    print("\nEscolaridade:\n", escolaridade.to_string())

    print(f"\nRelatórios e gráficos salvos em: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
