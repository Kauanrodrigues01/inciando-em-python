# Funções e Métodos das Bibliotecas `math` e `random`

Este documento cobre as principais funções e métodos das bibliotecas `math` e `random` em Python.

## Biblioteca `math`

A biblioteca `math` fornece funções matemáticas básicas.

- **`math.ceil(x)`**: Retorna o menor inteiro maior ou igual a `x`.
- **`math.floor(x)`**: Retorna o maior inteiro menor ou igual a `x`.
- **`math.sqrt(x)`**: Retorna a raiz quadrada de `x`.
- **`math.pow(x, y)`**: Retorna `x` elevado à potência `y`.
- **`math.exp(x)`**: Retorna o valor de `e` elevado à potência `x`.
- **`math.log(x, base)`**: Retorna o logaritmo de `x` na base especificada. Se a base não for fornecida, retorna o logaritmo natural.
- **`math.log10(x)`**: Retorna o logaritmo de `x` na base 10.
- **`math.sin(x)`**: Retorna o seno de `x`, onde `x` está em radianos.
- **`math.cos(x)`**: Retorna o cosseno de `x`, onde `x` está em radianos.
- **`math.tan(x)`**: Retorna a tangente de `x`, onde `x` está em radianos.
- **`math.degrees(x)`**: Converte `x` de radianos para graus.
- **`math.radians(x)`**: Converte `x` de graus para radianos.
- **`math.factorial(x)`**: Retorna o fatorial de `x`, onde `x` é um número inteiro não-negativo.
- **`math.gcd(a, b)`**: Retorna o maior divisor comum de `a` e `b`.

## Biblioteca `random`

A biblioteca `random` fornece funções para gerar números aleatórios e realizar operações relacionadas.

- **`random.random()`**: Retorna um número flutuante aleatório entre 0.0 e 1.0.
- **`random.uniform(a, b)`**: Retorna um número flutuante aleatório entre `a` e `b`.
- **`random.randint(a, b)`**: Retorna um inteiro aleatório entre `a` e `b`, inclusivo.
- **`random.choice(sequence)`**: Retorna um elemento aleatório de uma sequência não vazia.
- **`random.shuffle(x)`**: Embaralha a sequência `x` no local.
- **`random.sample(population, k)`**: Retorna uma lista de `k` elementos únicos escolhidos aleatoriamente da população.
- **`random.seed(a=None)`**: Inicializa o gerador de números aleatórios com a semente `a`. Se `a` for `None`, usa um valor de semente padrão.
- **`random.choices(population, weights=None, cum_weights=None, k=1)`**: Retorna uma lista com `k` elementos escolhidos aleatoriamente da população com base nas `weights`.

