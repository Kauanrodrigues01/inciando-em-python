# Métodos e Operações em Python

Este documento cobre os principais métodos e operações para strings, números, listas, dicionários e tuplas em Python.

## Métodos de String

- **`str.upper()`**: Retorna a string em maiúsculas.
- **`str.lower()`**: Retorna a string em minúsculas.
- **`str.strip()`**: Remove espaços desnecessários do início e fim da string.
- **`str.replace(old, new)`**: Substitui todas as ocorrências de `old` por `new`.
- **`str.split(sep=None)`**: Divide a string em uma lista de substrings usando `sep` como delimitador.
- **`str.find(substring)`**: Retorna o índice da primeira ocorrência de `substring`, ou -1 se não encontrado.

## Métodos e Funções de Números

- **`int()`**: Converte um valor para um número inteiro.
- **`float()`**: Converte um valor para um número de ponto flutuante.
- **`abs(x)`**: Retorna o valor absoluto de `x`.
- **`round(number, ndigits=None)`**: Arredonda o número para o número especificado de dígitos após o ponto decimal.

## Métodos de Listas

- **`list.append(item)`**: Adiciona um item ao final da lista.
- **`list.extend(iterable)`**: Adiciona todos os itens de um iterável ao final da lista.
- **`list.insert(index, item)`**: Insere um item na posição especificada.
- **`list.remove(item)`**: Remove a primeira ocorrência do item na lista.
- **`list.pop(index)`**: Remove e retorna o item na posição especificada. Se nenhum índice for fornecido, remove o último item.
- **`list.sort(key=None, reverse=False)`**: Ordena os itens da lista no local.

## Métodos e Funções de Dicionários

- **`dict.clear()`**: Remove todos os itens do dicionário.
- **`dict.get(key, default=None)`**: Retorna o valor para `key` se `key` estiver no dicionário. Caso contrário, retorna `default`.
- **`dict.items()`**: Retorna uma visão dos itens (chave-valor) do dicionário.
- **`dict.keys()`**: Retorna uma visão das chaves do dicionário.
- **`dict.values()`**: Retorna uma visão dos valores do dicionário.

## Métodos e Funções de Tuplas

- **`tuple.count(value)`**: Retorna o número de vezes que `value` aparece na tupla.
- **`tuple.index(value)`**: Retorna o índice da primeira ocorrência de `value` na tupla. Levanta um `ValueError` se `value` não estiver presente.

## Funções Nativas de Python

- **`len(obj)`**: Retorna o número de itens em um objeto.
- **`type(obj)`**: Retorna o tipo do objeto.
- **`dir(obj)`**: Retorna uma lista dos atributos e métodos de um objeto.
- **`input(prompt)`**: Lê uma linha da entrada padrão (usuário).
- **`print(*objects)`**: Imprime os objetos no fluxo de saída padrão.
- **`range(start, stop, step)`**: Retorna um iterador que gera números em uma faixa.
- **`sorted(iterable, key=None, reverse=False)`**: Retorna uma lista dos itens em `iterable` ordenados.
- **`sum(iterable, start=0)`**: Retorna a soma dos itens de `iterable`, iniciando com `start`.
- **`zip(*iterables)`**: Agrega itens de múltiplos iteráveis em tuplas.
