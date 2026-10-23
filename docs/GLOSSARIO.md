# Glossário

Termos do iskola, na forma em que aparecem no código e nos textos.

**Caso (de teste)**. Uma entrada e a saída esperada pra ela. Fica em `testes/NNN_slug.toml`, num bloco `[[casos]]`.

**Caso pesado**. Caso com `pesado = true`, grande o bastante pra uma solução O(n²) estourar o tempo. Só a partir do 083.

**Corretor** (ou harness). A parte do pacote `iskola` que roda o arquivo do aluno contra os casos e mostra o veredito.

**Dica**. `dicas/NNN_slug.md`. Termos pra pesquisar e links da documentação oficial, sem código, uma por problema.

**Entrada**. O texto que o programa recebe no stdin, lido com `input()`.

**Fase**. Faixa de problemas com um tema (Tutorial, Strings, Algoritmos...). As faixas ficam em `iskola/catalogo.py` e os nomes em `iskola/mensagens.py`.

**Gabarito**. Uma solução que passa nos testes, em `gabaritos/`. É o que o `iskola validar` roda.

**Variante**. Um gabarito alternativo do mesmo problema, com o nome `NNN_slug.<variante>.py` (`.sep_end`, `.forca_bruta`, `.otimizada`).

**Linha mágica**. `from iskola import verificar; verificar(__file__)`, logo depois do enunciado. Liga o corretor (ver ADR 0002).

**Mapa**. O que `uv run iskola` mostra. Os problemas por fase com ✅ passou, ❌ tentou e falhou, ⬜ pendente.

**Modo**. Como o problema é corrigido. `stdio` compara texto de saída, `funcao` chama uma função e compara o retorno (076+).

**Placar**. Um ✓ ou ✗ por caso e a contagem x/y, no topo de todo resultado.

**Problema**. Um dos 100 drills, identificado pelo número de três dígitos e pelo slug (`004_voto`).

**Progresso**. `.iskola/progresso.json`. Tentativas e datas de aprovação de cada problema.

**Solda**. O princípio da progressão. Cada problema reaproveita o que o anterior ensinou e avança só um passo.

**Solução**. `solucoes/NNN_slug.md`. Explicação dos gabaritos, da força bruta à otimizada, com Big-O.

**Template**. O arquivo original do problema em `problemas/`. Nunca é editado pelo aluno.

**Treino**. A pasta `treino/`, onde ficam as cópias dos templates que o aluno edita.

**Veredito**. O resultado de uma correção. Aceito, Resposta Errada, Erro de Apresentação, Tempo Limite Excedido ou Erro de Execução.
