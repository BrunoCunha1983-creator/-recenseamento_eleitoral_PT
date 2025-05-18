# Mesa de Voto para Home Assistant

Esta integração permite consultar a mesa de voto de um cidadão português usando o número do Cartão de Cidadão e data de nascimento.

### Instalação manual

1. Copiar a pasta `custom_components/mesa_de_voto` para o teu `config/custom_components/` no Home Assistant.
2. Adicionar ao `configuration.yaml`:

```yaml
sensor:
  - platform: mesa_de_voto
    cartao_cidadao: "00000000"
    data_nascimento: "1990-01-01"
    name: "Mesa de Voto Bruno"
```

### Via HACS

1. Adiciona este repositório como *Custom Repository* no HACS (tipo: integration).
2. Instala e reinicia o Home Assistant.

### Exemplo de resultado:

O sensor criará um estado "Disponível" ou "Erro", com os detalhes da mesa de voto nos atributos.