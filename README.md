# InterPixPy

This library provides developers with a simple way to interact with the Banco Inter's Pix API.

## Requirements

Python 3 or higher

## Installation

```bash
pip install interpixpy
```

## Usage

```python
import interpixpy

sdk = interpixpy.SDK(
    client_id="your_app_client_id",
    client_secret="your_app_client_secret",
    grant_type="grant_type",
    scope="your_app_scope",
)

cob_payload = {
    "calendario": {
        "expiracao": 3600
    },
    "devedor": {
        "cpf": "00000000000",
        "nome": "Fulano de Tal"
    },
    "valor": {
        "original": "100.00"
    },
    "chave": "00000000000", # Chave Pix do recebedor
    "solicitacaoPagador": "Pagamento dos serviços prestados."
}

result = sdk.cob().create(cob_payload)
```
