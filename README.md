# ENTEC — As built externo

Portal documental de ENTEC SERVIÇOS E LOCAÇÕES DE EQUIPAMENTOS LTDA.

Site: https://charles-igeotecnologia.github.io/ENTEC/

## Conteúdo

- 8 pranchas PDF com prévias ampliáveis e acesso aos originais.
- 5 desenhos DWG para download.
- 7 imagens com miniaturas, visualização ampliada e download dos JPEGs originais.
- Busca, filtros, catálogo CSV e resumo para impressão.

## Edição web 1.1

O index.html contém a interface e os metadados. Os arquivos em assets/ carregam conforme o uso: abertura responsiva em WebP; prévias ao consultar pranchas; miniaturas ao abrir a galeria; PDFs, DWGs e JPEGs originais somente quando acessados. Os originais são cópias integrais, com SHA-256 no catálogo.

A edição web depende dos arquivos de assets/ e de conexão para acessos ainda não armazenados pelo navegador. A versão anterior em HTML único, independente da internet, está preservada no projeto local e no histórico do commit 9bd648f.

## Atualização e verificação

Publique index.html e seus arquivos de assets/ juntos na branch main. Não renomeie recursos sem atualizar seus URLs. Os nomes incluem hashes para evitar mistura de versões em cache.

Execute python tests/check_assets.py antes do envio. A mesma verificação roda no GitHub Actions: confere integridade, referências e orçamento inicial de tamanho. Consulte PERFORMANCE.md para medições e validação em navegador. O GitHub Pages publica a raiz de main, sem compilação.

## Referências

Projeto legal as built R02/2024 e projeto executivo de ampliação R01/2026. Divergências documentais estão indicadas no portal. O acervo não atesta execução atual, aprovação ou situação de licenciamento. A condição executada depende de conferência de campo e validação técnica.
