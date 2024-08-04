# Estilos e Cores de Texto com Códigos ANSI

Os códigos ANSI permitem a formatação de texto em terminais que suportam sequências de controle ANSI. Aqui estão os principais códigos para estilizar o texto, alterar a cor do texto e definir a cor de fundo.

## Estilos de Texto

- **`0`**: Texto normal
- **`1`**: Texto em negrito
- **`4`**: Texto sublinhado
- **`7`**: Texto invertido (fundo e texto trocados)

## Cores do Texto

- **`30`**: Branco
- **`31`**: Vermelho
- **`32`**: Verde
- **`33`**: Amarelo
- **`34`**: Azul
- **`35`**: Roxo
- **`36`**: Azul esverdeado
- **`37`**: Cinza

## Cores de Fundo

- **`40`**: Fundo branco
- **`41`**: Fundo vermelho
- **`42`**: Fundo verde
- **`43`**: Fundo amarelo
- **`44`**: Fundo azul
- **`45`**: Fundo roxo
- **`46`**: Fundo azul esverdeado
- **`47`**: Fundo cinza

### Exemplos de Uso

Para aplicar uma combinação de estilos e cores, use a seguinte sintaxe em seu código:

```python
print(f'\033[{style_code};{text_color_code};{background_color_code}mSeu texto aqui\033[m')
