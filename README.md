# 📘 Sistema Acadêmico

O **Sistema Acadêmico** é uma aplicação desenvolvida em **Python**, utilizando **Programação Orientada a Objetos (POO)** e **SQLite**, com o objetivo de simular o gerenciamento de uma instituição de ensino.  
O sistema possui três áreas principais — **Aluno**, **Professor** e **Administrativo** —, permitindo o acesso a funcionalidades específicas de acordo com o tipo de usuário.

---

## 🚀 Funcionalidades Principais

### 👨‍🎓 Área do Aluno
- Visualização de notas e faltas.  
- Atualização de informações pessoais.  
- Acesso simplificado por login.

### 👩‍🏫 Área do Professor
- Lançamento de notas e faltas.  
- Consulta de informações sobre turmas.  
- Alteração de dados pessoais.  

### 🏢 Área Administrativa
- Cadastro e gerenciamento de alunos e professores.  
- Controle de turmas e disciplinas.  
- Visualização geral dos registros do sistema.  

---

## 🧱 Tecnologias Utilizadas
- **Linguagem:** Python 3  
- **Banco de Dados:** SQLite (integrado via `sqlite3`)  
- **Estrutura:** Programação Orientada a Objetos (POO)  
- **Armazenamento adicional:** JSON (para simulação de dados complementares)  

---

## ⚙️ Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior instalado no sistema.  
- Nenhuma dependência externa é necessária além das bibliotecas padrão do Python.

### Passos para execução
1. Baixe ou clone o repositório:
   ```bash
   git clone https://github.com/usuario/sistema-academico.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd sistema-academico
   ```
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```
4. Use as **contas de teste** já disponíveis no código para explorar o sistema.

---

## 🧪 Contas de Teste (Pré-cadastradas)

| Tipo de Usuário | ID/Login | Senha | Descrição |
|------------------|----------|--------|------------|
| Aluno | `CW50T1A` | `123` | Exemplo de conta de aluno |
| Professor | `7UC3OGP` | `123` | Exemplo de conta de professor |
| Administrativo | `YNB1JNC` | `123` | Conta administrativa completa |

*(Esses dados podem variar de acordo com o conteúdo do arquivo `main.py`.)*

---

## 🧩 Estrutura de Pastas (Exemplo)

```
Sistema_Academico/
│
├── main.py                  # Ponto de entrada do sistema
├── banco_dados.db           # Banco de dados SQLite
├── modulos/                 # Classes e funções do sistema
│   ├── aluno.py
│   ├── professor.py
│   ├── administrativo.py
│   └── verificacao.py
└── dados/                   # Arquivos JSON de apoio
```

---

## 🧠 Conceitos Aplicados
- Encapsulamento, herança e polimorfismo em Python.  
- Interação com banco de dados SQLite usando SQL básico.  
- Manipulação de arquivos JSON.  
- Estrutura modular e reutilização de código.  
- Interface via prompt de comando (CLI).

---

## 🔮 Possíveis Melhorias Futuras
- Implementação de **interface gráfica (GUI)** utilizando Tkinter ou PyQt.  
- Criação de **API REST** para integração com sistemas externos.  
- Integração com **banco de dados remoto** (MySQL/PostgreSQL).  
- Adição de **autenticação segura** com hashing de senhas.  
- Desenvolvimento de **relatórios automatizados** em PDF.  
- Criação de uma **versão web** do sistema utilizando Flask ou Django.  

---

## 🧑‍💻 Autor
**Isaac Medeiros**  
Estudante de **Análise e Desenvolvimento de Sistemas (UNIP)**  
Foco em **desenvolvimento full-stack** e **automação com Python**.
