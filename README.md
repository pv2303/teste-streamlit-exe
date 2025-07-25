# teste-streamlit-exe
Teste de criação de um aplicativo de Streamlit usando `npm` e `electron`

## Passo a Passo
1. Este projeto é gerenciado por `uv` então primeiro passo é sincronizar

```powershell
uv sync
```

2. Ative o .venv criado (comando no powershell)
```powershell
.venv\Scripts\activate
```

3. A partir das informações já colocadas no `package.json` rode os seguintes comandos:

- Instalar o npm que vai criar a pasta `node_modules`
```powershell
npm install
```

- Estabelecer variável de ambiente (Apenas importante no windows)
```powershell
set NODE_ENV=production
```

- Cria a pasta `build` que é construída a partir dos *scripts* e requisitos necessários
```powershell
npm run dump
```

- Apenas se você quiser ver um preview do programa em um "ambiente controlado". Deverá cancelar a ação após para rodar o próximo comando.
```powershell
npm run servewindows
```

- Cria a aplicação *.exe* em uma nova pasta chamada `dist`
```powershell
npm run app:dist
```

Ao final, seu projeto deve ficar assim:
```text
teste-streamlit-exe
├── .gitattributes
├── .gitignore
├── .python-version
├── README.md
├── app
│   ├── app.py
│   ├── grafico.py
│   ├── requirements.txt
│   ├── tabela.py
│   └── utils.py
├── build                             <- RESULTADO do `npm run dump`
├── data
│   ├── Nerlove1963.xlsx
│   └── Nerlove1963_description.pdf
├── dist                              <- RESULTADO do `npm run app:dist`
├── node_modules                      <- RESULTADO De `npm install`
├── package-lock.json
├── package.json
├── pyproject.toml
└── uv.lock
```