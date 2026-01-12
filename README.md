# Construindo um Projeto Ágil no GitHub

## 📌 Objetivo do Projeto
Este projeto simula o desenvolvimento de um sistema de gerenciamento de tarefas
utilizando metodologias ágeis, com foco em organização, rastreabilidade,
controle de qualidade e adaptação a mudanças.

O sistema foi desenvolvido para uma empresa fictícia chamada TechFlow Solutions,
atendendo uma startup do setor de logística.

---

## 📋 Escopo Inicial
- Criar um sistema básico de gerenciamento de tarefas
- Permitir criar, listar, atualizar e remover tarefas (CRUD)
- Organizar o desenvolvimento utilizando Kanban
- Implementar testes automatizados
- Configurar integração contínua com GitHub Actions

---

## 🔁 Metodologia Ágil Utilizada
Foi adotado o **Kanban**, utilizando o GitHub Projects, com as colunas:

- A Fazer   
- Em Progresso
- Concluído

Essa abordagem permite visualização clara do fluxo de trabalho
e adaptação rápida a mudanças de escopo.

---

## 🛠️ Tecnologias Utilizadas
- Python
- Flask
- Pytest
- GitHub Actions

---

## ▶️ Como Executar o Projeto

```bash
pip install -r requirements.txt
python src/app.py
```

---

## 🔁 Gestão de Mudanças de Escopo

Durante o desenvolvimento do projeto, foi identificada a necessidade de melhorar o acompanhamento do fluxo de trabalho das tarefas. Inicialmente, o sistema permitia apenas o cadastro e a listagem das tarefas, sem controle explícito de status.

Como melhoria, foi adicionada a funcionalidade de status das tarefas, permitindo classificá-las como pendente, em andamento ou concluída. Essa alteração tornou o sistema mais aderente à realidade de equipes operacionais, especialmente no contexto de uma startup de logística, onde o acompanhamento do progresso é essencial.

A mudança de escopo foi registrada no quadro Kanban do GitHub Projects, com criação de nova tarefa, movimentação entre as colunas e posterior conclusão, seguindo os princípios da metodologia ágil Kanban.

