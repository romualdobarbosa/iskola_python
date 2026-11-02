"""Todo texto que aparece pro aluno. Traduzir o iskola é traduzir este arquivo."""

FASES = [
    "Tutorial",
    "Números, operadores e formatação",
    "Condicionais e laços",
    "Strings",
    "Listas e tuplas",
    "Dicionários e sets",
    "Funções e classes",
    "Algoritmos",
]

# Chaves iguais aos valores de iskola.correcao.Veredito.
VEREDITOS = {
    "aceito": "Aceito",
    "resposta_errada": "Resposta Errada",
    "erro_apresentacao": "Erro de Apresentação",
    "tempo_limite": "Tempo Limite Excedido",
    "erro_execucao": "Erro de Execução",
}

EXPLICACOES = {
    "resposta_errada": "A saída do seu programa não bate com a esperada.",
    "erro_apresentacao": (
        "A resposta está certa, mas sobrou ou faltou espaço ou linha em branco. "
        "Cada · é um espaço e cada ⏎ é uma quebra de linha."
    ),
    "tempo_limite": (
        "O programa passou de {limite} segundos sem terminar. "
        "Tem um loop que nunca termina?"
    ),
    "erro_execucao": "O programa quebrou no meio do caminho.",
}

EXCECOES = {
    "TypeError": (
        "Você misturou tipos que não combinam, como comparar texto com número. "
        "Lembre que input() sempre devolve texto (str). Faltou converter com int() ou float()?"
    ),
    "ValueError": (
        "O tipo está certo, mas o valor não serve. Acontece, por exemplo, com int('3.5') "
        "ou int('abc')."
    ),
    "NameError": (
        "Você usou um nome que o Python não conhece. Confira se escreveu igual em todo lugar "
        "(maiúscula conta) e se a variável foi criada antes de ser usada."
    ),
    "UnboundLocalError": (
        "Você usou uma variável dentro da função antes de dar um valor a ela ali dentro."
    ),
    "EOFError": (
        "O programa tentou ler mais linhas do que a entrada tem. "
        "Confira quantas vezes você chama input()."
    ),
    "ZeroDivisionError": "Divisão por zero. Algum divisor chegou a zero nesse caso.",
    "IndexError": (
        "Você acessou uma posição que não existe. Lembre que a contagem começa em 0 "
        "e que o último índice é len() - 1."
    ),
    "KeyError": "Você buscou no dicionário uma chave que ele não tem.",
    "AttributeError": "Você usou um método ou atributo que esse tipo não tem.",
    "RecursionError": "A função chamou a si mesma vezes demais. Falta o caso base?",
}
SAIU_COM_CODIGO = "O programa terminou com o código {codigo} sem levantar exceção. Tem um exit() perdido?"
EXCECAO_GENERICA = "O Python levantou {tipo}. Vale procurar esse nome na documentação."

TITULO_PROBLEMA = "{codigo} · {titulo}"
PLACAR = "{aceitos}/{total} casos"
RODANDO = "Rodando o caso {i} de {total}..."
CASO = "Caso {i} de {total}"
ENTRADA = "Entrada"
ESPERADO = "Esperado"
OBTIDO = "Obtido"
VAZIA = "(vazia)"
NADA = "(nada)"
LINHAS_OCULTAS = "... {n} linha(s) a mais"
TRAVOU = "Travou? Veja {caminho}"

TEMPO = "Caso mais lento levou {tempo} s"
PROXIMO = "Próximo: {codigo} · {titulo}"
COMANDO_RODAR = "uv run treino/{nome}.py"
FIM_DOS_PROBLEMAS = "Você passou em todos os problemas que existem até agora."
FASE_CONCLUIDA = "Você fechou a fase {nome}"
FASE_CONCLUIDA_DETALHE = "{total} de {total} problemas aceitos."

AVISO_TEMPLATE_TITULO = "⚠ Arquivo errado"
AVISO_TEMPLATE = (
    "Esse é o template em problemas/, não o seu arquivo de treino.\n"
    "Esse resultado não conta no progresso.\n\n"
    "Rode [bold]uv run iskola[/bold] (ele cria o treino/ que faltar) e trabalhe em:\n"
    "  [bold]uv run treino/{arquivo}[/bold]"
)
SEM_RAIZ = "Não achei as pastas problemas/ e testes/ a partir de {pasta}."
SEM_TESTES = "Não achei os testes de {arquivo}. O nome começa com o número do problema?"
MODO_NAO_SUPORTADO = "O modo '{modo}' ainda não existe no corretor."

# CLI
MAPA_TITULO = "iskola · {aceitos} de {total}"
EM_BREVE = "em breve"
COPIADOS = "{n} arquivo(s) novo(s) em treino/."
ICONES = {"aceito": "✅", "falhou": "❌", "pendente": "⬜"}
LEGENDA = "✅ passou   ❌ tentou e falhou   ⬜ pendente"
RESETADO = "Restaurei treino/{arquivo} a partir do template."
RESETADO_BACKUP = "A versão anterior ficou em .iskola/lixeira/{backup}."
PROBLEMA_INEXISTENTE = "Não existe problema {codigo}."
USO = """\
Uso:
  iskola                 mostra o mapa e copia os templates novos pra treino/
  iskola resetar NNN     restaura treino/NNN_*.py a partir do template
  iskola validar         roda todos os gabaritos contra os testes"""

# validar
VALIDAR_OK = "ok"
VALIDAR_FALHOU = "falhou"
VALIDAR_ESPERA_TLE = "estourou o tempo, como esperado"
VALIDAR_NAO_ESTOUROU = "devia estourar o tempo e não estourou"
VALIDAR_FALTA = "falta {arquivo}"
VALIDAR_SEM_GABARITO = "nenhum gabarito"
VALIDAR_RESUMO_OK = "Todos os {n} gabaritos passaram."
VALIDAR_RESUMO_FALHOU = "{n} problema(s) na validação."
