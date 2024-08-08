# Metacaracteres, Quantificadores e Grupos em Expressões Regulares

## Metacaracteres

- **`.`**: Corresponde a qualquer caractere, exceto uma nova linha.
- **`^`**: Corresponde ao início de uma linha ou string.
- **`$`**: Corresponde ao final de uma linha ou string.
- **`[]`**: Define uma classe de caracteres. Exemplo: `[abc]` corresponde a 'a', 'b' ou 'c'.
- **`[^]`**: Define uma classe de caracteres negada. Exemplo: `[^abc]` corresponde a qualquer caractere exceto 'a', 'b' ou 'c'.
- **`\d`**: Corresponde a qualquer dígito (equivalente a `[0-9]`).
- **`\D`**: Corresponde a qualquer caractere que não seja um dígito.
- **`\w`**: Corresponde a qualquer caractere alfanumérico (letras e dígitos) e o caractere de sublinhado (`_`).
- **`\W`**: Corresponde a qualquer caractere que não seja alfanumérico ou sublinhado.
- **`\s`**: Corresponde a qualquer caractere de espaço em branco (espaço, tabulação, quebra de linha, etc.).
- **`\S`**: Corresponde a qualquer caractere que não seja um espaço em branco.
- **`\b`**: Corresponde a uma borda de palavra (início ou fim de uma palavra).
- **`\B`**: Corresponde a uma posição que não é uma borda de palavra.

## Quantificadores

- **`*`**: Corresponde a zero ou mais ocorrências do padrão anterior.
- **`+`**: Corresponde a uma ou mais ocorrências do padrão anterior.
- **`?`**: Corresponde a zero ou uma ocorrência do padrão anterior.
- **`{n}`**: Corresponde exatamente a `n` ocorrências do padrão anterior.
- **`{n,}`**: Corresponde a `n` ou mais ocorrências do padrão anterior.
- **`{n,m}`**: Corresponde entre `n` e `m` ocorrências do padrão anterior.
- **`*?`**: Corresponde a zero ou mais ocorrências do padrão anterior, mas de forma não gulosa (minimalista).
- **`+?`**: Corresponde a uma ou mais ocorrências do padrão anterior, mas de forma não gulosa.
- **`??`**: Corresponde a zero ou uma ocorrência do padrão anterior, mas de forma não gulosa.
- **`{n,m}?`**: Corresponde entre `n` e `m` ocorrências do padrão anterior, mas de forma não gulosa.

## Grupos e Alternância

- **`()`**: Define um grupo. Pode ser usado para capturar partes da string.
- **`|`**: Alternância (ou). Corresponde ao padrão à esquerda ou ao padrão à direita.
- **`(?P<nome>...)`**: Define um grupo de captura nomeado. Exemplo: `(?P<dia>\d{2})` captura dois dígitos como um grupo nomeado `dia`.
- **`(?:...)`**: Define um grupo não capturante. Utilizado quando o agrupamento é necessário, mas a captura não.
- **`(?<!...)`**: Define uma negação lookbehind (olhar atrás). Exemplo: `(?<!\d)\d{2}` corresponde a dois dígitos que não são precedidos por um dígito.
- **`(?<=...)`**: Define uma afirmação lookbehind (olhar atrás). Exemplo: `(?<=\d)\d{2}` corresponde a dois dígitos que são precedidos por um dígito.
- **`(?!...)`**: Define uma negação lookahead (olhar à frente). Exemplo: `\d(?!\d)` corresponde a um dígito que não é seguido por outro dígito.
- **`(?=...)`**: Define uma afirmação lookahead (olhar à frente). Exemplo: `\d(?=\d)` corresponde a um dígito que é seguido por outro dígito.


## Funções Principais da Biblioteca `re`

- **`re.match()`**: Verifica se o padrão corresponde ao início da string.
  ```python
  import re
  resultado = re.match(r'\d+', '123abc')
  print(resultado.group())  # Output: 123

- **`re.search()`**: Procura o padrão em qualquer parte da string e retorna o primeiro match encontrado.
    ``` python
    import re
    resultado = re.search(r'\d+', 'abc123def')
    print(resultado.group())  # Output: 123

- **`re.findall()`**: Retorna todas as ocorrências do padrão na string como uma lista.
    ``` python
    import re
    resultados = re.findall(r'\d+', 'abc123def456')
    print(resultados)  # Output: ['123', '456']

- **`re.finditer()`**: Retorna um iterador de todos os matches encontrados.
    ``` python
    import re
    matches = re.finditer(r'\d+', 'abc123def456')
    for match in matches:
        print(match.group())  # Output: 123 \n 456


- **`re.sub()`**: Substitui todas as ocorrências do padrão na string com um substituto.
    ``` python
    import re
    nova_string = re.sub(r'\d+', 'X', 'abc123def456')
    print(nova_string)  # Output: abcXdefX