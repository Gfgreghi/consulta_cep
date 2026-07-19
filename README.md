# Consulta CEP

Projeto simples desenvolvido em Python para consultar informações de um CEP utilizando a API do ViaCEP. A interface gráfica foi criada com Tkinter.

## Como funciona

O usuário digita um CEP com 8 números e clica em **Consultar**.

- Se o CEP for válido, o programa exibe as informações do endereço.
- Se o CEP não existir, é exibida uma mensagem informando que ele não foi encontrado.
- Se o formato estiver incorreto, o programa solicita que o CEP seja digitado no padrão correto.

## Tecnologias utilizadas

- Python
- Tkinter
- Requests
- API ViaCEP

## Exemplo

**Entrada:**

```text
01001000
```

**Saída:**

```text
CEP: 01001-000
Logradouro: Praça da Sé
Bairro: Sé
Localidade: São Paulo
Estado: SP
```

## Objetivo

Praticar o consumo de APIs em Python, criação de interfaces gráficas com Tkinter e validação de dados fornecidos pelo usuário.