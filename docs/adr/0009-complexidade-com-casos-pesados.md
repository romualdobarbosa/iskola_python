# 0009. Complexidade cobrada com casos pesados

Status: aceito (2026-10-23). A marca `espera_tle` já funciona no `validar`; ainda não há problema que use.

## Decisão

A partir do 083, alguns casos têm `pesado = true` e são grandes o bastante pra uma solução O(n²) estourar os 2 s. O gabarito força bruta de cada um desses problemas declara `# iskola: espera_tle`, e o `iskola validar` exige que ele estoure o tempo em pelo menos um caso. Isso prova que o caso pesado de fato separa a força bruta da otimizada.

## Consequências

Os casos rodam em sequência, um por vez, pra que o tempo medido não dependa de quantos outros casos estão rodando junto.
