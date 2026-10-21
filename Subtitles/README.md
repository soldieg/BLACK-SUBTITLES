# BLACK — legendas e guia de integração de idiomas

## Conteúdo e revisão deste diretório

O conjunto primário contém nove faixas de cutscene por idioma: inglês (`en`), português brasileiro (`pt-BR`), espanhol (`es`), francês (`fr`), alemão (`de`), italiano (`it`), indonésio (`id`) e russo (`ru`), totalizando 72 arquivos SRT. Os arquivos em inglês ficam em `Subtitles/en/<nome>.srt`; os demais ficam em `Subtitles/<locale>/<nome>.srt`.

O idioma de legenda deve acompanhar o idioma selecionado no jogo. Vídeos sem fala, incluindo `AK_N` e `MP5_N`, não têm SRT. As nove cutscenes faladas incluem identificação de falantes. Em `07_N` PT-BR, duas falas no mesmo cue têm identificação separada e o timing existente foi mantido. Algumas atribuições são estimativas de contexto; consulte `SPEAKER_ATTRIBUTION_REVIEW.csv`.

Espanhol, francês, alemão e italiano passaram por revisão editorial/assistida por IA; ainda pode faltar revisão de falante nativo e verificação cue a cue contra o áudio. As limitações de revisão do russo e indonésio também estão registradas nos READMEs de cada idioma. A presença de um SRT não significa transcrição oficial nem sincronização final confirmada.

Os SRTs experimentais de ASR e de retiming ficam separados em `../Test/Audio-Sync/`; não substitua as faixas primárias por eles sem revisão. Este repositório guarda os dados-fonte de legendas, não implementa o renderer do jogo nem contém dados do jogo.

## Guia de integração

Este guia compara o port **BlackDefinitiveHDPC** com a implementação de idiomas e legendas do **BLACK-XBERecomp**, para facilitar uma adaptação ao port sem misturar os formatos dos dois projetos.

> O guia descreve como adaptar as ideias; não afirma que o downloader ou o suporte aos oito idiomas já foram portados para o BlackDefinitiveHDPC. Código e arquivos precisam ser adaptados e testados no runtime correspondente.
## 1. Como o BlackDefinitiveHDPC organiza idioma e legenda

A referência consultada foi a branch `main` do [BlackDefinitiveHDPC](https://github.com/euspring1/BlackDefinitiveHDPC), commit [`d9594f0`](https://github.com/euspring1/BlackDefinitiveHDPC/commit/d9594f03eabb5138a7a481b0ce83e477fd84e844), em 20/10/2026.

Esse projeto é um port nativo para Windows que carrega o `default.xbe` original e executa o código x86 do jogo. Ele substitui partes do Xbox por implementações de PC. O XBE Recomp tem outra arquitetura e outro renderer; por isso, os conceitos podem ser reaproveitados, mas as funções não devem ser copiadas sem adaptação.

### Idioma do jogo e da interface do port

O port possui atualmente duas opções: inglês (`en`) e português brasileiro (`ptbr`). O inglês usa os textos originais do jogo. O português usa arquivos próprios e também traduz as páginas e opções do menu do PC.

- A opção fica em **PC SETTINGS > MODS > LANGUAGE**.
- O valor é persistido em `black.ini` como `language = en` ou `language = ptbr`; a linha de comando também aceita `--language`.
- Como o jogo carrega sua tabela de textos durante a inicialização, a troca é aplicada no próximo início.
- `lang::tr(...)` traduz os textos próprios do port. Isso é separado dos arquivos de texto do jogo.
- `lang::root()` aponta para `mods/language/ptbr`. O interceptor de arquivos do kernel procura ali os arquivos pedidos pelo jogo e deixa o jogo original atender quando não há substituição.
- O pacote de idioma do jogo usa a estrutura esperada pelos arquivos originais, por exemplo `strings/MainUS.bin` e `fonts/*.bin`.
- O código do port converte `ã/õ/Ã/Õ` para os glifos `ä/ö/Ä/Ö` quando a fonte do jogo não possui os caracteres com til. O texto de origem continua legível e a conversão é feita na apresentação.

A seleção do idioma também é usada pelos mods: `mod.ini` pode declarar `lang = en` ou `lang = ptbr`. Um mod de outro idioma fica bloqueado, evitando que arquivos em inglês e português sejam misturados. Mod sem idioma declarado continua elegível, sujeito à prioridade normal dos mods.

### Legendas dos filmes

O port desenha a legenda por cima do vídeo. Ele não altera o arquivo `.xmv` do jogo. A opção `subtitles = 0/1` em `black.ini` ou **MOVIE SUBTITLES** no menu controla a exibição; ela começa desligada por padrão. `--no-subtitles` também pode desativá-la.

O carregador procura arquivos `.srt` nas pastas `subtitles` dos mods habilitados. O nome do arquivo identifica o filme, sem a extensão, por exemplo:

```text
game/
└── mods/
    └── subtitles_ptbr/
        ├── mod.ini                 # name = Legendas PT-BR; lang = ptbr
        └── subtitles/
            ├── 03_N.srt
            └── 05_N.srt
```

Os tempos do SRT selecionam a fala enquanto o filme está em reprodução. O código identifica o filme pelo nome usado pelo player e conta o tempo da sessão; quando o filme reinicia, o contador da legenda também reinicia. Desabilitar o mod desabilita os SRTs que ele fornece.

**Diferença visual importante:** no BlackDefinitiveHDPC, o texto da legenda é rasterizado em uma textura com GDI+ e a fonte Segoe UI. Isso não é a fonte `Small.bin` do jogo. O XBE Recomp, por sua vez, desenha as legendas com a fonte de legenda do próprio jogo. Para preservar o aspecto do jogo no port, seria necessário adaptar o renderer e sua medição de glifos; simplesmente transferir o desenho GDI+ não produz a mesma tipografia.

## 2. Como o XBE Recomp implementa esses recursos

Os caminhos abaixo descrevem o código de referência do XBE Recomp consultado em 20/10/2026. O checkout analisado continha alterações locais ainda não commitadas; compare estas notas com o release que você estiver usando.

### 2.1 Seleção e detecção de idioma

- `src/common/options.h`: define os códigos do idioma ativo e as opções de legenda que são guardadas nas configurações.
- `src/common/game_info.cpp`: consulta os idiomas de interface preferidos do Windows, mapeia o idioma do sistema para um idioma suportado na primeira inicialização e usa inglês como fallback. Salva o idioma selecionado. Também solicita o pacote do idioma e coordena a reinicialização automática quando a seleção inicial foi detectada pelo sistema e o download terminou.
- `src/game/language.cpp`: seleciona a tabela de textos que o jogo original usará no boot e mantém inglês como fallback se o arquivo de texto esperado não estiver disponível.
- `src/common/translations.cpp`: traduz os textos dos menus e recursos próprios da recompilação. Essa camada não é a mesma coisa que traduzir todos os textos originais do jogo.
- `src/game/options_menu.cpp`: integra o seletor e as opções de legenda ao menu e posiciona a prévia.

Códigos usados pela interface/configuração e suas pastas de pacote:

| Idioma | Código na recompilação | Pasta dos recursos |
|---|---|---|
| Inglês | `int` | `en-US` |
| Francês | `fra` | `fr` |
| Alemão | `deu` | `de` |
| Italiano | `ita` | `it` |
| Espanhol | `esp` | `es` |
| Português brasileiro | `pt-BR` | `pt-BR` |
| Indonésio | `id` | `id` |
| Russo | `ru` | `ru` |

**Atenção:** oito idiomas selecionáveis/pacotes não significam automaticamente oito tabelas completas de texto original do XBE. `src/game/language.cpp` precisa encontrar o arquivo de texto compatível; sem ele, o jogo pode permanecer em inglês. Legendas, textos do menu da recompilação, arquivos de fonte e textos originais do jogo são categorias distintas e devem ser conferidas separadamente.

### 2.2 Distribuição e atualização dos pacotes

- `src/common/language_download.h/.cpp`: recebe o pedido do menu, executa o trabalho em segundo plano, baixa o manifesto e os arquivos do repositório de localização, instala um idioma individual e oferece atualização dos idiomas listados no manifesto.
- A seleção de um idioma pede o pacote correspondente. **Update Translations** consulta a versão atual do manifesto e atualiza os pacotes disponíveis.
- Os arquivos são instalados ao lado do executável, em `language/<pasta-do-idioma>/...`.
- O downloader valida versão e repositório do manifesto, aceita somente caminhos relativos seguros, limita o tamanho dos arquivos, verifica SHA-256 e grava primeiro em arquivo temporário antes de substituir o destino.
- O SHA-256 detecta arquivo ausente ou diferente do manifesto; como manifesto e arquivos vêm do mesmo repositório, isso é uma verificação de integridade, não uma assinatura independente do publicador.
- Se o pacote do idioma selecionado ainda não estiver instalado, o menu mostra o estado do download e pede reinicialização quando necessário.

O repositório de conteúdo [`BLACK-SUBTITLES`](https://github.com/soldieg/BLACK-SUBTITLES) separa SRTs, catálogos de menu, fontes e dados experimentais. O manifesto lista arquivos de conteúdo por idioma, caminho, formato, tamanho e hash. Um item marcado como experimental ou ausente do catálogo de distribuição não deve ser tratado como pronto para o jogo.

### 2.3 Leitura e apresentação de SRT no XBE Recomp

- `src/common/subtitles_data.cpp`: interpreta blocos SRT, timestamps e texto UTF-8. O cabeçalho BOM UTF-8 é removido quando existe.
- `src/common/subtitles.h/.cpp`: identifica o filme em reprodução, escolhe o SRT pelo nome do filme e pelo idioma do boot, acompanha o tempo da sessão e retorna a fala ativa. Se o SRT do idioma não existir ou não tiver cues válidas, tenta o SRT inglês.
- Caminho instalado: `language/<locale>/Subtitles/<nome-do-filme>.srt`. Por exemplo: `language/pt-BR/Subtitles/03_N.srt`.
- `src/game/fps_counter.cpp` desenha a legenda e a prévia no overlay 2D usando a fonte pequena do BLACK (`Small.bin`), centraliza e quebra as linhas, e aplica tamanho, negrito, cor, sombra e fundo. `src/game/options_menu.cpp` ancora a prévia logo abaixo da opção “Prévia”; `src/d3d/d3d8.cpp` fornece o retângulo translúcido do fundo.
- `src/common/subtitle_layout.cpp` contém o cálculo de centralização e a substituição de glifos portugueses. Em fontes PT-BR sem til, `ã/Ã` são exibidos usando `ä/Ä`, e `õ/Õ` usando `ö/Ö`.

As opções atuais de legenda são persistidas junto às configurações: ativar/desativar, escala de 80% a 160%, negrito, branco/amarelo, sombra desligada/suave/forte e fundo ligado/desligado. O SRT em si continua guardando caracteres Unicode; o remapeamento da fonte acontece só ao renderizar.

## 3. Como adaptar a ideia ao BlackDefinitiveHDPC

A forma mais simples de integrar sem misturar responsabilidades é manter três camadas separadas:

1. **Textos da interface do port:** tabela de tradução do próprio menu e valores do PC SETTINGS.
2. **Arquivos de idioma do jogo:** arquivos originais substituídos pelo overlay de `mods/language/<código>/`, com fallback para o XBE quando o arquivo não existe.
3. **Legendas dos filmes:** SRTs externos na pasta `subtitles` de um mod habilitado, associados ao nome do filme.

### Sequência sugerida

1. **Definir códigos canônicos.** Use um código estável por idioma (`en`, `ptbr`, `fr`, `de`, `it`, `es`, `id`, `ru`) e uma única função para normalizar nomes como `pt-BR` para `ptbr`. Não misture código de menu, código de pacote e nome de pasta implicitamente.
2. **Ampliar configuração e menu.** Troque o seletor de duas opções por uma lista de idiomas disponíveis; grave o código em `black.ini`. Mantenha a escolha em `language_next` até o próximo início, pois o XBE lê textos durante o boot.
3. **Adicionar detecção automática de idioma do Windows.** Só defina idioma automaticamente na primeira inicialização, respeitando escolha explícita já salva. Se o idioma do sistema não tiver pacote, mantenha inglês. Não reinicie o jogo antes de o pacote escolhido estar instalado.
4. **Preparar recursos do jogo por idioma.** Para cada língua, entregue os arquivos de texto e fonte no formato que o XBE/port realmente consome. Os SRTs do nosso repositório, por si só, não traduzem os menus nem os textos do jogo.
5. **Criar um mod por pacote ou uma estrutura equivalente.** Use `mod.ini` com o código de idioma e bloqueie mods de outro idioma. Preserve a regra de fallback e a prioridade existente dos mods.
6. **Distribuir SRTs por idioma.** Converta o catálogo do repositório para a estrutura do port. No BlackDefinitiveHDPC, o carregador atual espera `mods/<mod>/subtitles/<filme>.srt`; ele não procura automaticamente `language/<locale>/Subtitles/` como o XBE Recomp.
7. **Manter nomes de filme estáveis.** O nome-base do `.srt` precisa corresponder ao nome lido pelo player. Validar todos os nomes de vídeo e os respectivos SRTs antes de publicar o pacote.
8. **Adicionar downloader somente se desejado.** Um manifesto deve indicar idioma, arquivo de origem, destino, formato, tamanho e SHA-256. Baixar para temporário, validar caminho/tamanho/hash e só então substituir. Falha de rede ou pacote inválido deve manter os arquivos antigos e registrar erro no log.
9. **Manter saves independentes do idioma.** O port já trata nomes de perfil entre idiomas (`Profile`/`Perfil`) durante a importação. A troca de legenda/idioma não deve apagar, recriar ou alterar progresso; validar a compatibilidade do nome de perfil e manter backup antes de qualquer migração.
10. **Validar no jogo.** Testar um SRT curto, uma fala com acentos, um arquivo ausente, troca de idioma com reinício, mod desativado, mod de idioma incorreto e um save existente. Log de “SRT carregado” comprova leitura, mas a imagem em uma cutscene é necessária para confirmar posição, tempo, fonte e contraste.

### Exemplo de pacote separado de legendas para o port

```text
mods/
├── subtitles_en/
│   ├── mod.ini                 # name = English subtitles; lang = en
│   └── subtitles/
│       ├── 03_N.srt
│       └── 05_N.srt
└── subtitles_ptbr/
    ├── mod.ini                 # name = Legendas PT-BR; lang = ptbr
    └── subtitles/
        ├── 03_N.srt
        └── 05_N.srt
```

A tradução do texto do jogo ficaria separada em `mods/language/<código>/strings` e `mods/language/<código>/fonts`, seguindo o formato que o port intercepta. A implementação atual do BlackDefinitiveHDPC só inclui o conteúdo de idioma inglês e português brasileiro; os outros idiomas exigem arquivos compatíveis e validação próprios.

## 4. O que não copiar literalmente

- Não apontar o BlackDefinitiveHDPC para `language/<locale>/Subtitles` sem alterar o carregador: o port atual varre `subtitles` dentro dos mods habilitados.
- Não reutilizar `strings/MainUS.bin` de PT-BR para outros idiomas; cada língua precisa de texto, mapeamento de glifos e fonte que correspondam.
- Não confundir `lang::tr()` (textos da interface do port) com a tabela `MainUS.bin` (textos originais do jogo).
- Não usar `Segoe UI` como se fosse a `Small.bin` do BLACK. O primeiro é o renderer de legenda atual do port; o segundo é usado pela recompilação.
- Não considerar transcrições experimentais de voz como legendas finais. Use os SRTs primários e mantenha revisão de texto, timing e idioma nativo.
- Não alterar ou regenerar save ao trocar o idioma. O nome do perfil e a leitura do perfil precisam continuar compatíveis.

## 5. Arquivos de referência

### BlackDefinitiveHDPC

- [README e opções](https://github.com/euspring1/BlackDefinitiveHDPC/blob/d9594f03eabb5138a7a481b0ce83e477fd84e844/README.md)
- [Tradução da interface e seleção de idioma](https://github.com/euspring1/BlackDefinitiveHDPC/blob/d9594f03eabb5138a7a481b0ce83e477fd84e844/loader/src/lang.cpp)
- [Configuração `black.ini`](https://github.com/euspring1/BlackDefinitiveHDPC/blob/d9594f03eabb5138a7a481b0ce83e477fd84e844/loader/src/settings.cpp)
- [Filtro de mods por idioma](https://github.com/euspring1/BlackDefinitiveHDPC/blob/d9594f03eabb5138a7a481b0ce83e477fd84e844/loader/src/mods.cpp)
- [Overlay de arquivos do jogo](https://github.com/euspring1/BlackDefinitiveHDPC/blob/d9594f03eabb5138a7a481b0ce83e477fd84e844/loader/src/kernel/k_file.cpp)
- [Leitura e desenho das legendas](https://github.com/euspring1/BlackDefinitiveHDPC/blob/d9594f03eabb5138a7a481b0ce83e477fd84e844/loader/src/d3d/subtitles.cpp)
- [Opção de legenda e idioma no menu](https://github.com/euspring1/BlackDefinitiveHDPC/blob/d9594f03eabb5138a7a481b0ce83e477fd84e844/loader/src/fe/pc_settings.cpp)

### BLACK-XBERecomp e conteúdo de localização

- Código: `src/common/game_info.cpp`, `src/common/language_download.cpp`, `src/common/subtitles.cpp`, `src/common/subtitles_data.cpp`, `src/common/subtitle_layout.cpp`, `src/common/translations.cpp`, `src/game/language.cpp`, `src/game/options_menu.cpp`, `src/game/fps_counter.cpp` e `src/d3d/d3d8.cpp`.
- Conteúdo e manifesto: [BLACK-SUBTITLES](https://github.com/soldieg/BLACK-SUBTITLES), especialmente `Subtitles/`, `Localization/Fonts/`, `Localization/Menu/` e `manifest.json`.

## Fontes e avisos

- O BlackDefinitiveHDPC é um port separado; este guia documenta a integração de idiomas/legendas e não inclui arquivos do jogo.
- Os SRTs e catálogos devem conservar autoria, revisão e proveniência. Uma tradução automática ou uma transcrição experimental precisa de revisão antes de ser distribuída como final.
- Este documento descreve interfaces observadas nos códigos consultados. Mudanças futuras nos dois repositórios podem exigir atualização do guia.






## Pacote BlackDefinitiveHDPC

Os catálogos e as nove legendas por idioma espelhados para o port estão em [`GitHubs/BlackDefinitiveHDPC/`](../GitHubs/BlackDefinitiveHDPC/README.md). O pacote é material de tradução; o port consultado ainda ativa somente inglês e português brasileiro.
