# Desempenho da edição web 1.1

O HTML anterior incorporava os binários em base64. A abertura exigia receber todo o acervo, mesmo para consultar somente a página inicial.

| Medida | Antes | Depois |
| --- | ---: | ---: |
| HTML em disco | 30.624.536 bytes | 36.986 bytes |
| Corpo inicial recebido, incluindo imagem de abertura em desktop | ~30,6 MB | ~177 KB |
| Mediana até DOMContentLoaded, teste local controlado | 7.894 ms | 328 ms |
| Mediana até load, teste local controlado | 7.917 ms | 330 ms |

Redução de aproximadamente 99,4% no volume inicial. Tempos de laboratório não representam garantia para todas as conexões.

## Condições de medição

Três navegações por versão, Chrome headless instalado, viewport 1440 × 1000, cache desativado, latência simulada de 40 ms e download limitado a 4 MiB/s, ambas servidas por HTTP local. Os corpos medidos pelo navegador podem incluir a pequena instrumentação do antivírus local. O site não adiciona serviços de terceiros.

HTML e WebP de abertura são os únicos recursos da aplicação solicitados inicialmente. Em telas menores, o navegador pode selecionar a variante de 480 pixels (~41 KB). PDFs, DWGs, JPEGs originais, prévias e miniaturas não são transferidos na abertura da visão geral.

## Preservação e validação

- As 8 pranchas PDF, os 5 DWGs e os 7 JPEGs originais mantêm bytes e hashes das fontes.
- Prévias das pranchas usam WebP sem perdas a partir das renderizações PNG; o PDF original continua disponível para leitura integral.
- Fotos de exibição e miniaturas usam WebP; o download fornece o JPEG original.
- Validação Chrome: 8 prévias e zoom; abertura PDF; filtros e estado vazio; CSV; 20 downloads com nome e SHA-256; galeria e teclado; navegação em 320, 768, 1024 e 1440 pixels; links diretos para pranchas e galeria; impressão.
- Na verificação local: zero erros JavaScript e zero respostas HTTP com erro em recursos da aplicação.

## Orçamento e manutenção

`tests/check_assets.py` impede HTML acima de 45 KB, abertura desktop acima de 250 KB e abertura móvel acima de 100 KB; verifica integridade de todos os originais e suas referências. A verificação roda no GitHub Actions. Ela não substitui testes em navegador depois de mudanças de comportamento.

Para acompanhar o desempenho real, use o painel Network do navegador com cache desativado e filtro pelo domínio do portal. Compare a primeira abertura antes de consultar outras abas. Não se instalou rastreamento de visitantes.

## Reversão

Restaure o `index.html` do commit `9bd648f` em um novo commit e envie a `main`. O HTML anterior contém o acervo completo. A pasta `assets/` pode permanecer sem uso durante a reversão. A versão local em HTML único permanece preservada.
