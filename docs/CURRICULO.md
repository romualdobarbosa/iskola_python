# Currículo

Os 100 problemas em ordem. Cada um traz um conceito **novo** e solda um conceito que algum anterior já ensinou (o número entre parênteses diz qual). O último problema de cada fase junta o que a fase ensinou.

Rascunho em revisão. Os títulos e slugs viram os nomes de arquivo (`NNN_slug`).

## Tutorial (001–006)

| # | Slug | Título | Novo | Soldado |
|---|---|---|---|---|
| 001 | ola_mundo | Olá, mundo | `print`, ler o diff | (início) |
| 002 | lendo_entrada | Lendo a entrada | `input()`, vários casos, placar | `print` (001) |
| 003 | cracha | Crachá | f-string, `sep`, `end`, Erro de Apresentação | `input()` (002) |
| 004 | voto | Voto | `if`/`elif`/`else`, `int()`, Erro de Execução | f-string (003) |
| 005 | contagem_regressiva | Contagem regressiva | `for`, `range` com passo negativo, mapa | `int()` (004) |
| 006 | collatz | Collatz | `while`, `//`, `%`, Tempo Limite Excedido | `if` (004) |

## Números, operadores e formatação (007–022)

| # | Slug | Título | Novo | Soldado |
|---|---|---|---|---|
| 007 | media | Média de duas notas | `float()`, `/` sempre dá float, `:.2f` | f-string (003) |
| 008 | mesma_linha | Dois na mesma linha | `input().split()`, `map(int, ...)`, desempacotar `a, b = ...` | `int()` (004) |
| 009 | figurinhas | Pacotes de figurinhas | `//`, `%` e `divmod` juntos | `split` (008), `//` (006) |
| 010 | relogio_digital | Relógio digital | `divmod` encadeado, zero à esquerda com `:02d` | `divmod` (009) |
| 011 | plantao | Plantão | `%` com negativo dá positivo no Python, volta do relógio sem `if` | `:02d` (010) |
| 012 | tabuleiro | Grãos no tabuleiro | `**`, inteiro sem limite de tamanho | aritmética inteira (009) |
| 013 | conta_restaurante | Conta do restaurante | imprecisão de float, `round` e o arredondamento bancário | `:.2f` (007) |
| 014 | bissexto | Ano bissexto | `and`/`or`/`not` como expressão, precedência | `%` (009) |
| 015 | bases | Painel binário | `int(s, base)`, `bin`, `hex`, formatos `b`/`o`/`x` | format spec (010) |
| 016 | quantos_positivos | Quantos positivos | `bool` é `int` (`True + True`), comparação encadeada | expressão booleana (014) |
| 017 | distancia | Ponto de ônibus | `import math`, `sqrt`, `hypot`, `isqrt` | formatação de float (013) |
| 018 | excursao | Ônibus da excursão | `math.ceil` e divisão pra cima com inteiros | `math` (017), `//` (009) |
| 019 | tres_em_ordem | Três em ordem | troca `a, b = b, a`, `min`, `max` | comparações (016) |
| 020 | recibo | Recibo | largura e alinhamento na f-string (`:<10`, `:>8`) | `for` (005), `split` (008) |
| 021 | censo | Censo | separador de milhar `:,` e troca pro padrão brasileiro | format spec (020) |
| 022 | troco | Troco | trabalhar em centavos inteiros, `for` sobre valores fixos | `divmod` (009), `round` (013), alinhamento (020) |

## Condicionais e laços (023–035)

| # | Slug | Título | Novo | Soldado |
|---|---|---|---|---|
| 023 | quadrante | Quadrante | condições compostas com casos de borda (eixos, origem) | `elif` (004), `float` (007) |
| 024 | positivos | Positivos | contador e acumulador num laço | `bool` como número (016) |
| 025 | par_impar_sinal | Par, ímpar e sinal | vários contadores com `if` independentes | contador (024) |
| 026 | impares_ate | Ímpares até X | passo no `range` e limite inclusivo | `range` (005), `%` (009) |
| 027 | seis_impares | Seis ímpares | calcular o início e contar N itens | passo no `range` (026) |
| 028 | quadrados_pares | Quadrados dos pares | expressão por item e saída formatada por linha | `**` (012), passo (026) |
| 029 | maior_menor | Maior e menor | acompanhar máximo e mínimo no laço | `min`/`max` (019), contador (024) |
| 030 | ate_zero | Até o zero | `while True` com `break`, leitura até sentinela | `while` (006), acumulador (024) |
| 031 | nota_valida | Nota válida | laço de validação, `continue` | `break` (030) |
| 032 | primos | Primos | `for`/`else`, testar só até a raiz | `math.isqrt` (017), `break` (030) |
| 033 | tabuada | Tabuada completa | laços aninhados | alinhamento (020) |
| 034 | triangulo | Triângulo de asteriscos | `str * n` pra desenhar padrões | laços aninhados (033) |
| 035 | extrato | Extrato | operações até `FIM`, saldo, saque recusado | tudo da fase |

## Strings (036–050)

| # | Slug | Título | Novo | Soldado |
|---|---|---|---|---|
| 036 | iniciais | Iniciais | índice `s[0]`, `s[-1]`, `len` | `split` (008) |
| 037 | palindromo | Palíndromo | fatias, `s[::-1]` | índices (036) |
| 038 | caixa | Maiúsculas e minúsculas | `upper`, `lower`, `title`, `casefold`, string é imutável | palíndromo (037) |
| 039 | vogais | Contar vogais | `for` sobre caracteres, operador `in` | contador (024) |
| 040 | espacos | Espaços demais | `split()` sem argumento, `join`, `strip` | métodos de string (038) |
| 041 | censura | Censura | `find`, `replace`, `startswith`, `endswith` | `split`/`join` (040) |
| 042 | cpf | Validar CPF | `isdigit`, dígito vira número, dígitos verificadores | `%` (009), `for` sobre caracteres (039) |
| 043 | cesar | Cifra de César | `ord`, `chr` | `%` com volta (011) |
| 044 | compactar | Compactar texto | comparar com o caractere anterior, montar string aos poucos | `for` sobre caracteres (039) |
| 045 | senha_forte | Senha forte | `isupper`, `islower`, flags booleanas | `isdigit` (042), `and`/`or` (014) |
| 046 | escapes | Escapes | `\n`, `\t`, aspas dentro de aspas, raw string | `print` (001) |
| 047 | sem_acento | Busca sem acento | `unicodedata.normalize`, filtrar acentos | `casefold` (038), `join` (040) |
| 048 | romano | Para romano | decomposição gulosa com pares (valor, símbolo) | troco (022) |
| 049 | de_romano | De romano | olhar o próximo caractere com `range(len(s))` | romano (048) |
| 050 | justificar | Quebrar linhas | quebrar texto numa largura máxima | tudo da fase |

## Listas e tuplas (051–065)

| # | Slug | Título | Novo | Soldado |
|---|---|---|---|---|
| 051 | notas | Lista de notas | lista, `append`, `sum`, `len` | acumulador (024) |
| 052 | acima_media | Acima da média | por que guardar os valores (duas passadas) | lista (051) |
| 053 | rotacionar | Rotacionar | fatias de lista, `%` no deslocamento | fatias de string (037), `%` (011) |
| 054 | ranking | Ranking | `sorted` e `.sort()`, `reverse`, `key` | lista (051) |
| 055 | fila_banco | Fila do banco | `pop`, `insert`, `remove`, lista é mutável | operações até `FIM` (035) |
| 056 | onde_esta | Onde está | `enumerate`, `index` | métodos de lista (055) |
| 057 | compreensao | Pares ao quadrado | compreensão de lista com `if` | quadrados dos pares (028) |
| 058 | boletim | Boletim | tuplas, ordenar por várias chaves | `key` (054) |
| 059 | gabarito_prova | Gabarito da prova | `zip` | `enumerate` (056) |
| 060 | copia | Cópia ou a mesma lista | referência e cópia, armadilha do `[[0] * n] * m` | mutabilidade (055) |
| 061 | matriz | Somas da matriz | lista de listas, linhas e colunas | laços aninhados (033), cópia (060) |
| 062 | transposta | Transposta | `zip(*m)`, diagonais | `zip` (059), matriz (061) |
| 063 | campo_minado | Campo minado | vizinhança e checagem de borda | matriz (061) |
| 064 | sudoku | Sudoku válido | blocos de uma matriz | transposta (062), `sorted` (054) |
| 065 | jogo_da_vida | Jogo da vida | uma geração do autômato de Conway | vizinhança (063), cópia (060) |

## Dicionários e sets (066–075)

| # | Slug | Título | Novo | Soldado |
|---|---|---|---|---|
| 066 | frequencia | Frequência de palavras | `dict`, `get` com padrão | contador (024), `split` (040) |
| 067 | mais_frequentes | Mais frequentes | ordenar `items()` com desempate | várias chaves (058) |
| 068 | counter | Letras mais comuns | `Counter`, `most_common` | frequência (066) |
| 069 | turmas | Alunos por turma | `defaultdict(list)`, agrupar | `Counter` (068) |
| 070 | morse | Código Morse | compreensão de dicionário, inverter um `dict` | compreensão de lista (057) |
| 071 | pangrama | Pangrama | `set`, `in` em tempo constante | `in` em string (039) |
| 072 | em_comum | Amigos em comum | união, interseção e diferença | `set` (071) |
| 073 | anagramas | Anagramas agrupados | chave montada com `sorted` | agrupar (069) |
| 074 | estoque | Estoque | `dict` aninhado | agrupar (069), operações (055) |
| 075 | apuracao | Apuração | votos válidos, brancos e nulos, percentuais, regra de segundo turno | tudo da fase |

## Funções e classes (076–082)

Daqui em diante o corretor usa o modo `funcao` (ADR 0003).

| # | Slug | Título | Novo | Soldado |
|---|---|---|---|---|
| 076 | eh_bissexto | Função bissexto | `def`, `return`, anotação de tipo, modo `funcao` | bissexto (014) |
| 077 | moeda | Formatar moeda | parâmetro com padrão, argumento nomeado, armadilha do padrão mutável | padrão brasileiro (021) |
| 078 | estatisticas | Estatísticas | devolver uma tupla | tuplas (058), maior e menor (029) |
| 079 | achatar | Achatar listas | recursão, caso base, `isinstance` | lista de listas (061) |
| 080 | criterio | Ordenar por critério | função como valor, `lambda` | `key` (054) |
| 081 | ponto | Ponto | `@dataclass`, método | distância (017) |
| 082 | conta_bancaria | Conta bancária | classe com estado, `raise ValueError` | extrato (035) |

## Algoritmos (083–100)

A partir daqui entram os casos `pesado` e os gabaritos força bruta com `# iskola: espera_tle` (ADR 0009).

| # | Slug | Título | Novo | Soldado |
|---|---|---|---|---|
| 083 | dois_somam | Dois que somam | trocar O(n²) por um `dict`, primeiro caso pesado | `dict` (066) |
| 084 | dois_somam_ordenado | Dois que somam, ordenado | dois ponteiros | dois que somam (083) |
| 085 | sem_repetidos | Sem repetidos | ponteiro de leitura e de escrita, alterar no lugar | dois ponteiros (084) |
| 086 | palindromo_frase | Palíndromo de frase | dois ponteiros numa string | palíndromo (037), sem acento (047) |
| 087 | reservatorio | Maior reservatório | dois ponteiros com escolha gulosa | dois ponteiros (084) |
| 088 | janela_fixa | Melhor semana | janela deslizante de tamanho fixo | acumulador (024) |
| 089 | sem_repetir | Maior trecho sem repetir | janela de tamanho variável | `set` (071), janela (088) |
| 090 | menor_trecho | Menor trecho que soma | janela que encolhe | janela variável (089) |
| 091 | busca_binaria | Busca binária | busca binária, `bisect` | lista ordenada (084) |
| 092 | raiz_inteira | Raiz inteira | busca binária na resposta | `math.isqrt` (017), busca binária (091) |
| 093 | primeira_ultima | Primeira e última posição | `bisect_left` e `bisect_right` | busca binária (091) |
| 094 | capacidade | Capacidade mínima | busca binária na resposta com verificação | divisão pra cima (018), raiz inteira (092) |
| 095 | parenteses | Parênteses | pilha com `append` e `pop` | métodos de lista (055) |
| 096 | posfixa | Calculadora pós-fixa | avaliar expressão com pilha | pilha (095) |
| 097 | proximo_maior | Próximo maior | pilha monotônica | pilha (095) |
| 098 | inverter_lista | Inverter lista ligada | nó ligado, inverter iterativo | classe (081) |
| 099 | ciclo | Ciclo na lista | ponteiro lento e rápido (Floyd) | lista ligada (098), dois ponteiros (084) |
| 100 | lru | Cache LRU | `dict` mais lista duplamente ligada | `dict` (066), lista ligada (098), classe (082) |

## Pendências

- Lista ligada no modo `funcao` (098 a 100): o TOML não descreve nós. O corretor precisa converter lista em nós na entrada e nós em lista na saída, ou o teste chama uma sequência de operações.
- O 060 pode vir com o bug de aliasing no template, como os tutoriais fazem com os vereditos.
- O 100 testa uma sequência de chamadas de métodos, então o modo `funcao` precisa aceitar classe além de função.
