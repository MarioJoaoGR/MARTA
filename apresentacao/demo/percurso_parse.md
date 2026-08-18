# Percurso completo: o metodo `Formatador#parse`

Todos os blocos abaixo sao dados reais, extraidos da execucao guardada em
`sondagens/runs/formatador/`. Nada foi escrito a mao.

## 1. O projeto: 3 ficheiros

- `formatador.rb` — 1 classes, 13 metodos
- `formatador/progressbar.rb` — 2 classes, 5 metodos
- `formatador/table.rb` — 1 classes, 4 metodos

## 2. O codigo do metodo
```ruby
  def parse(string)
    if color_support
      string.gsub(PARSE_REGEX) { "\e[#{STYLES[::Regexp.last_match(1).to_sym]}m" }.gsub(INDENT_REGEX) { indentation }
    else
      strip(string)
    end
  end
```

## 3. O que o Prism devolve para este metodo
```json
{
 "name": "parse",
 "owner": "Formatador",
 "start_line": 86,
 "end_line": 92,
 "params": [
  {
   "name": "string",
   "kind": "req"
  }
 ],
 "calls": [
  {
   "name": "color_support",
   "recv": "none",
   "recv_name": null,
   "line": 87
  },
  {
   "name": "gsub",
   "recv": "other",
   "recv_name": null,
   "line": 88
  },
  {
   "name": "gsub",
   "recv": "lvar",
   "recv_name": "string",
   "line": 88
  },
  {
   "name": "[]",
   "recv": "const",
   "recv_name": "STYLES",
   "line": 88
  },
  {
   "name": "to_sym",
   "recv": "other",
   "recv_name": null,
   "line": 88
  },
  {
   "name": "last_match",
   "recv": "const",
   "recv_name": "::Regexp",
   "line": 88
  },
  {
   "name": "indentation",
   "recv": "none",
   "recv_name": null,
   "line": 88
  },
  {
   "name": "strip",
   "recv": "none",
   "recv_name": null,
   "line": 90
  }
 ]
}
```

## 4. O que o resolver decidiu

Das 8 chamadas registadas, 3 resolveram para metodos do projeto:

- `Formatador#parse` -> `Formatador#color_support`  (linha 87, forma `none`)
- `Formatador#parse` -> `Formatador#indentation`  (linha 88, forma `none`)
- `Formatador#parse` -> `Formatador#strip`  (linha 90, forma `none`)

As outras 5 sairam para fora do projeto (`gsub`, `to_sym`, `Regexp.last_match`,
`STYLES[]`) e por isso nao geram aresta: so indexamos o codigo do proprio projeto.

## 5. O contexto que foi para o Planner

```
Method Name: Formatador#parse
Require target: formatador

SOURCE CODE:
  def parse(string)
    if color_support
      string.gsub(PARSE_REGEX) { "\e[#{STYLES[::Regexp.last_match(1).to_sym]}m" }.gsub(INDENT_REGEX) { indentation }
    else
      strip(string)
    end
  end

SUMMARY:
The `Formatador` class provides a set of methods designed to facilitate formatted text output with various ANSI escape codes for color and style attributes. Here's a summary of its key functionalities:

### Class Methods
- **`display(*args, &block)`**: Outputs formatted text to the standard output, [...]

INFERRED PARAMETER TYPES:
- `string` responds to [gsub]

COVERAGE FEEDBACK:
First pass: Try to achieve maximum coverage.
```

## 6. O spec gerado
```ruby
require "formatador"

RSpec.describe Formatador do
  it "handles valid inputs correctly" do
    formatador = Formatador.new
    expect(formatador.display("Hello, World!")).to eq nil
    expect(formatador.new_line).to eq nil
  end

end
```

(ficheiro `formatador__Formatador__parse_r1_spec.rb`; existem 1 versoes deste metodo, uma por ronda)

