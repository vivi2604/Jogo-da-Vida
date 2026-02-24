# 🧬 Jogo da Vida (Game of Life)

## 📌 Descrição
Este projeto é uma implementação do Jogo da Vida de Conway, desenvolvido em Python. O sistema simula a evolução de células em uma matriz bidimensional com base em regras específicas de sobrevivência e reprodução.

O usuário pode definir manualmente quais células começam vivas, e o programa executa automaticamente as gerações até que todas as células estejam mortas.


## 🎯 Objetivo
Aplicar conceitos fundamentais de programação, como:

- Estruturas de repetição (while e for)
- Estruturas condicionais (if/else)
- Matrizes (listas bidimensionais)
- Modularização com múltiplos arquivos
- Validação de entrada de dados
- Simulação de sistemas


## 🧠 Como funciona

O jogo ocorre em uma grade 10x10, onde cada célula pode estar:

- Viva (O)
- Morta (X)

A cada geração, o estado das células é atualizado com base nas seguintes regras:

- Uma célula viva com menos de 2 vizinhos vivos → morre (solidão)
- Uma célula viva com mais de 3 vizinhos vivos → morre (superpopulação)
- Uma célula morta com exatamente 3 vizinhos vivos → nasce
- Caso contrário → permanece no mesmo estado


## ⚙️ Funcionalidades

- 🧩 Inicialização de células vivas pelo usuário  
- 🔄 Atualização automática das gerações  
- 📊 Exibição da matriz no terminal  
- ⏱ Intervalo entre gerações (simulação visual)  
- 🛑 Encerramento automático quando todas as células morrem  


## 🗂 Estrutura do projeto

- `principal.py` → arquivo principal com a execução do jogo  
- `defvariavel.py` → definição de variáveis e funções auxiliares  


## 🛠 Tecnologias utilizadas

- Python

## ▶️ Como executar

1. Certifique-se de ter o Python instalado  
2. Baixe ou clone este repositório  
3. Execute o arquivo principal:

```bash
python principal.py

## 📚 Contexto

Projeto desenvolvido para a disciplina MI - Algoritmos, com foco na prática de lógica de programação e construção de sistemas interativos.

## 📄 Relatório completo

Para mais detalhes sobre o desenvolvimento do projeto, acesse o relatório completo.
