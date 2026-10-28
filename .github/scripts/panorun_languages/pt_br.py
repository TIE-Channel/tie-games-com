"""Portuguese (Brazil)."""
from . import MAC_LINUX_KEYS, VIDEO_KEYS, blocks

MONTHS = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
          "outubro", "novembro", "dezembro")


def date(day, month, year):
    return f"{day} de {MONTHS[month - 1]} de {year}"


WORDS = {
    "windows": "Baixar o Panorun {version} para Windows",
    "android": "Baixar o Panorun {version} para Android",
    "small": "baixa o Panorun enquanto instala",
    "full": 'Ou o <a href="{url}">instalador completo</a> ({size}), com tudo dentro: instala sem conexão.',
    "mac": 'Baixar o Panorun {version} para Mac',
    "linux": 'Baixar o Panorun {version} para Linux',
    "locale": "pt-BR",
}

BLOCKS = blocks([
    "Panorun - a fase inteira à vista | TIE-Games",
    "A fase inteira à vista, seus amigos correndo ao seu lado.",
    "O Panorun é um emulador de jogos clássicos de console 8 bits que mantém a fase inteira à vista: tudo o que você já percorreu continua na tela ao redor do jogo. Joguem juntos online, e seus amigos correm ao seu lado dentro do seu próprio jogo. O Panorun é feito pela TIE-Games, um estúdio independente de Dresden, na Alemanha.",
    'Tem um celular Android? <a href="#test">Ajude a testar o Panorun no Google Play</a>.',
    "Baixar",
    "WINDOWS 10 E 11, 64 BITS",
    "O instalador pergunta onde instalar e se deve criar um atalho na área de trabalho. Não precisa de permissão de administrador.",
    "O instalador ainda não é assinado: se o Windows disser <em>O Windows protegeu o computador</em>, clique em <em>Mais informações</em> e depois em <em>Executar assim mesmo</em>.",
    "Depois o Panorun se atualiza sozinho: clique em <em>Update</em> quando ele avisar de uma versão nova.",
    "Para remover o Panorun: Configurações do Windows &rarr; Aplicativos &rarr; Aplicativos instalados &rarr; Panorun &rarr; Desinstalar. Seus jogos e gravações ficam em <em>Documentos\\Panorun</em>.",
    "ANDROID 7 OU MAIS NOVO, 64 BITS",
    "<strong>Abra esta página no Chrome primeiro.</strong> Ela está aberta dentro de outro app (Telegram, WhatsApp, Gmail…), que não consegue baixar arquivos: lá o botão abaixo não faz nada.",
    '<a class="button" id="open-in-chrome" href="https://tie-games.com/panorun/">Abrir no Chrome</a>',
    "Se nada acontecer: toque em <strong>&#8942;</strong> ou <strong>&#8943;</strong> no topo e depois em <em>Abrir no Chrome</em> ou <em>Abrir no navegador</em>.",
    "<strong>Acesso antecipado: o Panorun está em teste no Google Play</strong> antes de abrir para todos, e qualquer pessoa pode entrar no teste:",
    'Entre no grupo <a href="https://groups.google.com/g/panorun-testers">Panorun testers</a> com sua conta do Google: <em>Participar do grupo</em>.',
    'Abra <a href="https://play.google.com/apps/testing/com.tiegames.panorun">o teste do Panorun no Google Play</a> e toque em <em>Tornar-se testador</em>.',
    "Instale o Panorun com o botão do Google Play acima.",
    'Fique com ele por duas semanas e jogue de vez em quando - <em>EXPERIMENTAR A DEMO</em>, um jogo seu, uma sala com outras pessoas - e conte o que funciona e o que não funciona, no grupo ou em <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>. O Google Play abre o Panorun para todos quando testadores suficientes jogarem por duas semanas.',
    "Ou baixe aqui:",
    '<strong>Baixando o <span id="android-file">Panorun</span>&hellip;</strong> Leva um minuto.',
    "Quando terminar, toque em <em>Abrir</em> na mensagem na parte de baixo do Chrome.",
    "Sem <em>Abrir</em>, ou a mensagem sumiu? Toque em <strong>&#8942;</strong> no canto superior direito do Chrome, depois em <em>Downloads</em>, e toque no arquivo. Ou abra o app <em>Arquivos</em> (nos celulares Xiaomi <em>Gerenciador de arquivos</em>), depois <em>Downloads</em>, e toque no arquivo.",
    "Toque em <em>Instalar</em>.",
    "Abra esta página no navegador do celular (o Chrome, não dentro de outro app) e toque no botão. Quando o download terminar, toque em <em>Abrir</em> na mensagem embaixo e depois em <em>Instalar</em>. Perdeu? Em <strong>&#8942;</strong> &rarr; <em>Downloads</em> do Chrome está o arquivo: toque nele lá.",
    "Na primeira vez, o Android pergunta se seu navegador pode instalar apps: permita, volte e toque em <em>Instalar</em> de novo.",
    "Baixado aqui, o Panorun não vem da Play Store, então o Google Play Protect pode não conhecê-lo: toque em <em>Mais detalhes</em> e depois em <em>Instalar mesmo assim</em>.",
    "O Panorun do Google Play e o Panorun desta página não podem ser instalados um por cima do outro: para trocar, desinstale primeiro o que você tem - isso apaga os jogos guardados nele.",
    "Uma versão nova é instalada do mesmo jeito, por cima da que você tem: seus jogos ficam.",
    "O que ele faz",
    "<strong>Mantém a fase à vista.</strong> Um console desenha uma tela por vez e esquece o resto. O Panorun guarda cada tela desenhada e pinta a fase ao redor do jogo, no lugar certo: o chão que você atravessou continua na tela à esquerda, acima e abaixo.",
    "<strong>Desenha um mapa enquanto você joga.</strong> Uma faixa embaixo do jogo mostra a fase até agora, com você nela.",
    "<strong>Deixa vocês jogarem juntos.</strong> Abra uma sala e envie o código, ou entre em uma das salas listadas no servidor de salas; quem entra joga sua própria cópia do mesmo jogo, e o personagem de cada um corre pelo jogo de todos os outros, cada um com sua cor, com sua linha no mapa. Um jogo muito à frente espera os outros, para todo mundo ficar junto. Até doze jogadores por sala.",
    "<strong>Converse enquanto joga.</strong> Em uma sala, segure o botão do microfone (V no computador) para falar, ou toque nele para deixá-lo ligado. O som do seu jogo e o barulho ao redor são removidos, então os outros ouvem sua voz, e não seu jogo nem seu quarto.",
    "<strong>Um servidor de salas, ou nenhum.</strong> JOGAR ONLINE abre salas no servidor de salas do Panorun na web, listadas lá para seus amigos entrarem. Ou jogue LOCAL: a sala roda na janela de quem a abre, e os amigos entram direto. O Panorun para Windows vem com um servidor de salas que qualquer um pode rodar.",
    "<strong>Lutas de verdade.</strong> Assim que o Panorun sabe onde um jogo guarda sua vida, os outros podem atingir seu personagem, e dói como com os inimigos do próprio jogo: você é empurrado para trás e sua vida cai. A vida de todos aparece sobre o nome.",
    "<strong>Aprende cada jogo sozinho.</strong> Enquanto você joga, o Panorun aprende como é seu personagem e qual botão pula ou ataca, e os jogadores de uma sala compartilham o que o Panorun deles sabe de um jogo.",
    "<strong>Grava suas partidas.</strong> GRAVAR guarda cada botão que você aperta, e REPLAY joga a partida de novo desde o começo.",
    "<strong>Joga com o que você tem.</strong> Teclado ou controle, com cada tecla e botão do seu jeito. No celular, um direcional à esquerda e A, B, TURBO A e TURBO B à direita.",
    "<strong>Fluido no celular.</strong> O processador e os chips de imagem e som do console rodam como código nativo, então o Panorun roda fluido no celular, mesmo com amigos na sala.",
    "<strong>Nenhum jogo incluído.</strong> O Panorun roda jogos feitos para o clássico console de 8 bits. Desenvolvedores independentes ainda criam jogos novos para esse console, e muitos os distribuem de graça - pesquise na web por <em>8-bit homebrew games</em>. Ou use cópias de jogos que você tem. Adicione-os com <em>ADICIONAR JOGOS</em> ou solte-os na janela; o Panorun os guarda em <em>Documentos\\Panorun</em>. No celular, <em>ADICIONAR JOGOS</em> e <em>ESCOLHER PASTA</em> abrem o seletor de arquivos do celular. Ou <em>EXPERIMENTAR A DEMO</em>: dois joguinhos do próprio Panorun, uma briga nos telhados à noite e uma corrida por colinas verdes.",
    "Sua privacidade",
    'O Panorun não tem contas, análises nem anúncios. Seus jogos, configurações e gravações ficam no seu computador ou celular. O Panorun só se conecta ao GitHub, para procurar uma versão mais nova (no Windows); ao nosso servidor de salas e a este site, para a lista de jogos de que publicamos um arquivo de jogo, e o arquivo de um jogo da lista quando você o inicia; e, quando você joga online, ao servidor de salas ou ao computador em cuja sala você entra: ele compartilha então seu nome, seu personagem, a vida dele e a fase em que você está com os jogadores daquela sala, e o servidor de salas ou o computador da sala vê seu endereço de internet. Quando você segura ou liga o botão do microfone em uma sala, sua voz vai ao vivo para os jogadores daquela sala; ela não é gravada nem guardada em lugar nenhum. Os detalhes estão na <a href="/panorun/privacy">Política de Privacidade</a> (em inglês).',
    "Licenças de código aberto",
    'O Panorun é feito com software de código aberto: entre outros Python, pygame e SDL, NumPy, e Opus, RNNoise e speexdsp da Xiph.Org para a voz. Cada um é usado sob sua própria licença. A lista completa, com o texto de cada licença, está no próprio Panorun (CONFIGURAÇÕES &rarr; LICENÇAS), ao lado do programa no Windows, e aqui: <a href="/panorun/third-party-notices.txt">avisos de terceiros</a>.',
    "Links",
    '<a href="/panorun/privacy">Política de Privacidade</a>',
    '<a href="/panorun/terms">Termos de Uso</a>',
    '<a href="/panorun/third-party-notices.txt">Licenças de código aberto</a>',
    'Contato: <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>',
    "&copy; 2026 TIE-Games. Todos os direitos reservados.",
    'O Panorun não vem com jogos. Os nomes dos jogos são marcas de seus donos; o Panorun não é afiliado a eles nem endossado por eles. O que publicamos de um jogo é só o que o Panorun sabe dele - onde ele guarda a vida de um personagem, quais botões atacam -, nunca nada do jogo em si. Para pedir que algo seja retirado, escreva para <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>.',
    "O Panorun é um emulador de jogos clássicos de console 8 bits que mantém a fase inteira à vista e deixa você jogar online com seus amigos correndo ao seu lado.",
    "Panorun - a fase inteira à vista",
    "Ícone do Panorun",
    "Baixe o Panorun no Google Play",
    "Disponível no",
])

#: Mac and Linux (2026-10-28).
BLOCKS.update(dict(zip(MAC_LINUX_KEYS, [
    'MACOS 11 OU MAIS NOVO, APPLE SILICON (M1 E MAIS NOVOS)',
    'Abra a imagem de disco e arraste o <em>Panorun</em> para <em>Aplicativos</em>.',
    'O Panorun ainda não é notarizado pela Apple: na primeira vez, o macOS diz que não pode verificá-lo. Abra <em>Ajustes do Sistema</em> &rarr; <em>Privacidade e Segurança</em>, role para baixo e clique em <em>Abrir Mesmo Assim</em> ao lado do Panorun.',
    'Seus jogos e gravações ficam em <em>Documentos/Panorun</em>.',
    'LINUX, 64 BITS (UBUNTU 22.04 OU MAIS NOVO E SEMELHANTES)',
    'Um só arquivo, um AppImage: permita que ele seja executado como programa (nas Propriedades, ou com <code>chmod +x</code>) e abra-o.',
])))

BLOCKS.update(dict(zip(VIDEO_KEYS, [
    'Assistir ao vídeo do Panorun (YouTube)',
    'Os dois joguinhos do Panorun, jogados juntos em uma sala',
    'O Panorun em 40 segundos. Ao clicar, o vídeo é reproduzido pelo YouTube.',
])))
