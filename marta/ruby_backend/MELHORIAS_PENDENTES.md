# MARTA-Ruby — trabalho em aberto

O ciclo de correções de engenharia de novembro de 2026 está concluído.
A [lista original](../../docs/archive/ruby-improvements-before-2026-10-04.md)
preserva os apontamentos anteriores.

- **Grafo e tipos (A6–A8, B1).** Medir precisão, alcance e custo em projetos
  reais, cruzando evidência estática e traces. Incluir casos de retorno dinâmico
  e comparar critérios de escolha do chamador para a propagação de intenção.
- **Seleção de contexto (A1, A10, B3).** Calibrar a seleção e a abstenção do judge
  em dados próprios. Medir separadamente o contexto do Planner, as sugestões
  de tipos e o retrieval de reparação, com qualidade, tokens e tempo por tarefa.
- **Concorrência (A5).** Comparar 1, 2 e 4 workers com a mesma política de barreira.
  Registar throughput, memória, custo e validade das suites.
- **Investigação de tese.** Recolher dados de reparação e avaliar estratégias de
  seleção de contexto sob orçamento. Feedback humano, geração guiada por
  mutação e unificação com o backend Python são linhas independentes.
