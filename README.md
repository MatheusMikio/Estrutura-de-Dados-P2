# Jogo de Combate contra Vampiros

## Descrição
Jogo de turnos onde heróis combatem vampiros e o poderoso Valdrak.

## Personagens
- Heróis: Aric, Liora, Thalric, Seraphina (padrão) ou personalizados
- Inimigos: Vampiros Comuns e Valdrak (chefe final)

## Habilidades
Os Heróis possuem 4 habilidades com custo de energia baseado no dano

## Como Jogar
1. Execute Jogo.py
2. Escolha entre:
   - 1: Jogar (requer 4 heróis)
   - 2: Criar herói
   - 3: Sair

## Mecânica de Combate

O jogo funciona em turnos alternados entre heróis e inimigos:

- **Sistema de Turnos**: Cada personagem age uma vez por rodada
- **Energia**: Recupera 1 ponto por turno quando passa a vez
- **Ataques**:
  - Heróis usam habilidades com custo de energia
  - Vampiros usam ataques básicos
  - Valdrak tem habilidades especiais
- **Vitória**: Derrotar todos os inimigos
- **Derrota**: Todos os heróis serem derrotados

**Fluxo do Combate**:
1. Escolha entre atacar ou passar o turno
2. Se atacar, selecione habilidade e alvo
3. Inimigos agem automaticamente
4. Rodada se repete até vitória ou derrota

### Estruturas de Dados Utilizadas

- **Fila (Queue)**: Utilizada para gerenciar os eventos dentro de cada capítulo, garantindo uma execução linear e ordenada conforme os eventos são processados e removidos da fila.

- **Pilha (Stack)**: Empregada para armazenar as cartas de habilidade, permitindo o acesso LIFO (Last In, First Out) que é ideal para o sistema de habilidades do jogo.

- **Tupla (Tuple)**: Utilizada para representar os capítulos da campanha, uma vez que se trata de uma história pré-definida que não requer mutabilidade, garantindo assim a imutabilidade dos dados.

- **Conjunto (Set)**: Utilizado para gerenciar o grupo de jogadores, assegurando que cada personagem seja único e evitando duplicações.

- **Dicionário (Dictionary)**: Escolhido para armazenar informações sobre as habilidades, proporcionando um acesso rápido e eficiente através de chaves, sem aumentar a complexidade do código.

- **Lista Encadeada (Linked List)**: Implementada para controlar a sequência de turnos no combate, garantindo uma ordem linear e sequencial das ações.

## Colaboradores
- Matheus Mikio Cisterna Takahashi - RA: 2005154
- Mateus Hideo Yamashita Santos - RA: 2005332
- Samara Adorno - RA: 2001639