# Solução do 015 · Painel binário

```python
base, valor = input().split()
n = int(valor, int(base))

print(f"decimal: {n}")
print(f"binário: {n:08b}")
print(f"octal: {n:o}")
print(f"hexadecimal: {n:02X}")
```

O int(texto, base) lê o texto na base que você mandar. int("1011", 2) dá 11 e int("ff", 16) dá 255, com maiúsculas ou minúsculas. Por isso não converti a base e o valor juntos com map. O valor tem que continuar texto até o int saber a base dele.

Na saída, cada base tem uma letra na especificação de formato. O b é binário, o o é octal, o x é hexadecimal minúsculo e o X maiúsculo. Antes da letra vai a largura com zero, igual ao :02d do 010. Então :08b é binário com pelo menos 8 dígitos completando com zero.

As funções bin, oct e hex também convertem, mas devolvem com prefixo. bin(11) dá "0b1011" e hex(255) dá "0xff". Pra usar aqui teria que cortar o prefixo e ainda completar os zeros, e a f-string já faz tudo.

## Complexidade

Tempo O(1) e espaço O(1), já que o número não passa de 255.
