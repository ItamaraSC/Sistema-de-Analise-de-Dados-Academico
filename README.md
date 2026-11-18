# Sistema de Análise de Dados — Tia da Coxinha

Projeto acadêmico de extensão desenvolvido na disciplina **Tópicos de Big Data em Python (Estácio)**. A solução original foi criada para apoiar a organização e a análise de respostas de um formulário, explorando integração de dados, tratamento, análise estatística, visualização e exportação de relatórios.

> **Privacidade:** este repositório contém somente uma base sintética (fictícia), criada para demonstrar a execução. Dados pessoais, respostas originais, planilhas reais, identificadores privados e credenciais de acesso não fazem parte desta publicação.

## Objetivo

Demonstrar um fluxo de análise de dados com Python: leitura de dados tabulares, padronização de colunas, cálculo de frequências, produção de gráficos e exportação de resultados para CSV e Excel.

## Funcionalidades demonstradas

- Leitura de uma base CSV de exemplo;
- Padronização dos nomes das colunas;
- Identificação das colunas de interesse;
- Contagem de categorias e cálculo de indicadores descritivos;
- Geração de gráficos de experiência, disponibilidade e escolaridade;
- Aplicação de uma regra heurística de pontuação demonstrativa;
- Exportação de resumo CSV e relatório Excel.

## Tecnologias

- **Python** — lógica e processamento;
- **Pandas** — manipulação e análise de dados;
- **Matplotlib** — visualização;
- **OpenPyXL** — suporte à exportação Excel.

A versão acadêmica original também utilizou Google Sheets API, Gspread e autenticação por Service Account para acessar a planilha de origem. Por segurança e para permitir a execução pública sem credenciais, essa integração não está ativa nesta versão demonstrativa. Nenhuma chave ou arquivo de autenticação deve ser enviado ao GitHub.

## Estrutura

```text
├── analise_tia_coxinha.py
├── requirements.txt
├── README.md
├── data/
│   └── dados_exemplo_ficticios.csv
└── results/
    ├── grafico_experiencia.png
    ├── grafico_disponibilidade.png
    ├── grafico_escolaridade.png
    ├── resumo.csv
    └── relatorio_demonstrativo.xlsx
```

## Como executar

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

Execute na pasta do projeto:

```bash
python analise_tia_coxinha.py
```

Os gráficos e relatórios serão gerados na pasta `results/`.

## Sobre os dados e a pontuação

A base incluída contém **35 registros inteiramente fictícios**. Os resultados gerados a partir dela são apenas ilustrativos e não representam os resultados originais do projeto ou pessoas reais.

A pontuação reproduz uma regra heurística desenvolvida no contexto acadêmico para demonstrar operações com dados. Ela não é um modelo validado, não mede objetivamente o potencial de pessoas e não deve ser utilizada para decisões reais de recrutamento.

## Aprendizados

O desenvolvimento proporcionou prática com integração de fontes de dados, limpeza e padronização, análise exploratória, criação de indicadores, visualização e geração automatizada de relatórios.

---

**Autoria:** Itamara Santos Cavalcanti  
**Contexto:** Projeto de extensão acadêmica — Estácio.
