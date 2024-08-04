# Métodos e Operações em Python

Este documento cobre os principais métodos e operações para strings, números, listas, dicionários e tuplas em Python.

## Métodos de String

- **`str.capitalize()`**: Retorna a string com o primeiro caractere em maiúsculo e o restante em minúsculo.
- **`str.casefold()`**: Converte a string para minúsculas de uma maneira que seja mais agressiva para comparação.
- **`str.center(width, fillchar)`**: Retorna a string centralizada em um campo de largura `width`, preenchida com `fillchar`.
- **`str.count(substring)`**: Conta o número de ocorrências de `substring` na string.
- **`str.encode(encoding='utf-8', errors='strict')`**: Retorna uma versão codificada da string usando a codificação especificada.
- **`str.endswith(suffix, start=0, end=len(string))`**: Retorna `True` se a string terminar com o sufixo especificado.
- **`str.expandtabs(tabsize=8)`**: Substitui todos os caracteres de tabulação na string por espaços.
- **`str.find(substring, start=0, end=len(string))`**: Retorna o índice da primeira ocorrência de `substring`, ou -1 se não for encontrado.
- **`str.format(*args, **kwargs)`**: Formata a string substituindo os placeholders com os argumentos fornecidos.
- **`str.isalnum()`**: Retorna `True` se todos os caracteres da string forem alfanuméricos.
- **`str.isalpha()`**: Retorna `True` se todos os caracteres da string forem letras.
- **`str.isdigit()`**: Retorna `True` se todos os caracteres da string forem dígitos.
- **`str.islower()`**: Retorna `True` se todos os caracteres da string estiverem em minúsculas.
- **`str.isupper()`**: Retorna `True` se todos os caracteres da string estiverem em maiúsculas.
- **`str.join(iterable)`**: Junta os elementos de um iterável (como uma lista) em uma única string, separados pelo string original.
- **`str.ljust(width, fillchar)`**: Retorna a string justificada à esquerda em um campo de largura `width`, preenchida com `fillchar`.
- **`str.rjust(width, fillchar)`**: Retorna a string justificada à direita em um campo de largura `width`, preenchida com `fillchar`.
- **`str.lower()`**: Retorna a string em minúsculas.
- **`str.upper()`**: Retorna a string em maiúsculas.
- **`str.replace(old, new)`**: Substitui todas as ocorrências de `old` por `new`.
- **`str.split(sep=None, maxsplit=-1)`**: Divide a string em uma lista de substrings usando `sep` como delimitador.
- **`str.strip(chars=None)`**: Remove os caracteres especificados (ou espaços em branco por padrão) do início e fim da string.

## Métodos e Funções de Números

- **`int.bit_length()`**: Retorna o número de bits necessários para representar o número em binário.
- **`int.to_bytes(length, byteorder)`**: Retorna o número como uma sequência de bytes.
- **`float.as_integer_ratio()`**: Retorna uma tupla que representa o número como uma fração.
- **`float.is_integer()`**: Retorna `True` se o número for um inteiro.
- **`complex.conjugate()`**: Retorna o conjugado do número complexo.
- **`abs(x)`**: Retorna o valor absoluto de `x`.
- **`divmod(a, b)`**: Retorna uma tupla com o quociente e o resto da divisão de `a` por `b`.
- **`round(number, ndigits=None)`**: Arredonda o número para o número especificado de dígitos após o ponto decimal.
- **`pow(base, exp, mod=None)`**: Retorna `base` elevado à `exp`, opcionalmente modulo `mod`.

## Métodos de Listas

- **`list.append(item)`**: Adiciona um item ao final da lista.
- **`list.extend(iterable)`**: Adiciona todos os itens de um iterável ao final da lista.
- **`list.insert(index, item)`**: Insere um item na posição especificada.
- **`list.remove(item)`**: Remove a primeira ocorrência do item na lista.
- **`list.pop(index)`**: Remove e retorna o item na posição especificada. Se nenhum índice for fornecido, remove o último item.
- **`list.sort(key=None, reverse=False)`**: Ordena os itens da lista no local.
- **`list.reverse()`**: Reverte a ordem dos itens na lista.
- **`list.copy()`**: Retorna uma cópia superficial da lista.

## Métodos e Funções de Dicionários

- **`dict.clear()`**: Remove todos os itens do dicionário.
- **`dict.copy()`**: Retorna uma cópia superficial do dicionário.
- **`dict.fromkeys(seq, value=None)`**: Cria um novo dicionário com chaves de `seq` e valores definidos como `value`.
- **`dict.get(key, default=None)`**: Retorna o valor para `key` se `key` estiver no dicionário. Caso contrário, retorna `default`.
- **`dict.items()`**: Retorna uma visão dos itens (chave-valor) do dicionário.
- **`dict.keys()`**: Retorna uma visão das chaves do dicionário.
- **`dict.pop(key, default=None)`**: Remove e retorna o valor associado a `key`. Se `key` não estiver presente, retorna `default`.
- **`dict.popitem()`**: Remove e retorna um par chave-valor arbitrário do dicionário.
- **`dict.setdefault(key, default=None)`**: Retorna o valor para `key`. Se `key` não estiver no dicionário, insere `key` com o valor `default`.
- **`dict.update([other])`**: Atualiza o dicionário com pares chave-valor de `other`.
- **`dict.values()`**: Retorna uma visão dos valores do dicionário.

## Métodos de Tuplas

- **`tuple.count(value)`**: Retorna o número de vezes que `value` aparece na tupla.
- **`tuple.index(value, start=0, end=len(tuple))`**: Retorna o índice da primeira ocorrência de `value` na tupla. Levanta um `ValueError` se `value` não estiver presente.

## Funções Nativas de Python

- **`len(obj)`**: Retorna o número de itens em um objeto.
- **`type(obj)`**: Retorna o tipo do objeto.
- **`id(obj)`**: Retorna o identificador único do objeto.
- **`dir(obj)`**: Retorna uma lista dos atributos e métodos de um objeto.
- **`help(obj)`**: Invoca o sistema de ajuda integrado.
- **`repr(obj)`**: Retorna uma representação de string do objeto, útil para debugging.
- **`eval(expression)`**: Avalia uma expressão Python dinâmica a partir de uma string.
- **`exec(code)`**: Executa um código Python dinâmico passado como string.
- **`input(prompt)`**: Lê uma linha da entrada padrão (usuário).
- **`print(*objects, sep=' ', end='\n', file=sys.stdout)`**: Imprime os objetos no fluxo de saída padrão.
- **`range(start, stop, step)`**: Retorna um iterador que gera números em uma faixa.
- **`sorted(iterable, key=None, reverse=False)`**: Retorna uma lista dos itens em `iterable` ordenados.
- **`sum(iterable, start=0)`**: Retorna a soma dos itens de `iterable`, iniciando com `start`.
- **`zip(*iterables)`**: Agrega itens de múltiplos iteráveis em tuplas.
