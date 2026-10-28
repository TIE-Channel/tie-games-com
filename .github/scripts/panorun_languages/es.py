"""Spanish."""
from . import MAC_LINUX_KEYS, blocks

MONTHS = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
          "octubre", "noviembre", "diciembre")


def date(day, month, year):
    return f"{day} de {MONTHS[month - 1]} de {year}"


WORDS = {
    "windows": "Descargar Panorun {version} para Windows",
    "android": "Descargar Panorun {version} para Android",
    "small": "descarga Panorun mientras lo instala",
    "full": 'O el <a href="{url}">instalador completo</a> ({size}), con todo dentro: instala sin conexión.',
    "mac": 'Descargar Panorun {version} para Mac',
    "linux": 'Descargar Panorun {version} para Linux',
    "locale": "es-ES",
}

BLOCKS = blocks([
    "Panorun - el nivel entero a la vista | TIE-Games",
    "El nivel entero a la vista, tus amigos corriendo a tu lado.",
    "Panorun es un emulador de juegos clásicos de consola de 8 bits que mantiene el nivel entero a la vista: todo lo que has recorrido sigue en pantalla alrededor del juego. Jugad juntos en línea, y tus amigos corren a tu lado dentro de tu propio juego. Panorun está hecho por TIE-Games, un estudio independiente de Dresde, Alemania.",
    '¿Tienes un móvil Android? <a href="#test">Ayuda a probar Panorun en Google Play</a>.',
    "Descargar",
    "WINDOWS 10 Y 11, 64 BITS",
    "El instalador pregunta dónde instalar y si poner un acceso directo en el escritorio. No hacen falta permisos de administrador.",
    "El instalador aún no está firmado: si Windows dice <em>Windows protegió su PC</em>, haz clic en <em>Más información</em> y luego en <em>Ejecutar de todas formas</em>.",
    "Después Panorun se actualiza solo: haz clic en <em>Update</em> cuando avise de una versión nueva.",
    "Para quitar Panorun: Configuración de Windows &rarr; Aplicaciones &rarr; Aplicaciones instaladas &rarr; Panorun &rarr; Desinstalar. Tus juegos y grabaciones se quedan en <em>Documentos\\Panorun</em>.",
    "ANDROID 7 O POSTERIOR, 64 BITS",
    "<strong>Abre primero esta página en Chrome.</strong> Está abierta dentro de otra app (Telegram, WhatsApp, Gmail…), que no puede descargar archivos: ahí el botón de abajo no hace nada.",
    '<a class="button" id="open-in-chrome" href="https://tie-games.com/panorun/">Abrir en Chrome</a>',
    "Si no pasa nada: toca <strong>&#8942;</strong> o <strong>&#8943;</strong> arriba y luego <em>Abrir en Chrome</em> o <em>Abrir en el navegador</em>.",
    "<strong>Acceso anticipado: Panorun está en pruebas en Google Play</strong> antes de abrirse a todos, y cualquiera puede unirse a la prueba:",
    'Únete al grupo <a href="https://groups.google.com/g/panorun-testers">Panorun testers</a> con tu cuenta de Google: <em>Unirse al grupo</em>.',
    'Abre <a href="https://play.google.com/apps/testing/com.tiegames.panorun">la prueba de Panorun en Google Play</a> y toca <em>Convertirse en tester</em>.',
    "Instala Panorun con el botón de Google Play de arriba.",
    'Consérvalo dos semanas y juega de vez en cuando - <em>PROBAR LA DEMO</em>, un juego tuyo, una sala con otros - y cuéntanos qué funciona y qué no, en el grupo o en <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>. Google Play abre Panorun a todos cuando suficientes testers lo han jugado dos semanas.',
    "O descárgalo aquí:",
    '<strong>Descargando <span id="android-file">Panorun</span>&hellip;</strong> Tarda un minuto.',
    "Cuando termine, toca <em>Abrir</em> en el mensaje de abajo de Chrome.",
    "¿No sale <em>Abrir</em>, o el mensaje ya no está? Toca <strong>&#8942;</strong> arriba a la derecha en Chrome, luego <em>Descargas</em>, y toca el archivo. O abre la app <em>Archivos</em> (en móviles Xiaomi <em>Gestor de archivos</em>), luego <em>Descargas</em>, y toca el archivo.",
    "Toca <em>Instalar</em>.",
    "Abre esta página en el navegador del móvil (Chrome, no dentro de otra app) y toca el botón. Cuando termine la descarga, toca <em>Abrir</em> en el mensaje de abajo y luego <em>Instalar</em>. ¿Se te pasó? En Chrome, <strong>&#8942;</strong> &rarr; <em>Descargas</em> tiene el archivo: tócalo ahí.",
    "La primera vez, Android pregunta si tu navegador puede instalar apps: permítelo, vuelve atrás y toca <em>Instalar</em> otra vez.",
    "Descargado aquí, Panorun no viene de Play Store, así que Google Play Protect puede no conocerlo: toca <em>Más detalles</em> y luego <em>Instalar de todos modos</em>.",
    "Panorun de Google Play y Panorun de esta página no se pueden instalar uno encima del otro: para cambiar, desinstala primero el que tienes; eso borra los juegos guardados en él.",
    "Una versión nueva se instala igual, encima de la que tienes: tus juegos se quedan.",
    "Qué hace",
    "<strong>Mantiene el nivel a la vista.</strong> Una consola dibuja una pantalla cada vez y olvida el resto. Panorun guarda cada pantalla dibujada y pinta el nivel alrededor del juego donde corresponde, así el terreno que has cruzado sigue en pantalla a la izquierda, arriba y abajo.",
    "<strong>Dibuja un mapa mientras juegas.</strong> Una franja bajo el juego muestra el nivel hasta ahora, contigo en él.",
    "<strong>Os deja jugar juntos.</strong> Abre una sala y envía su código, o entra en una de las salas del servidor de salas; quien entra juega su propia copia del mismo juego, y el personaje de cada uno corre por el juego de todos los demás, cada uno de su color, con su línea en el mapa. Un juego que va muy adelantado espera a los demás, para que sigáis juntos. Hasta doce jugadores por sala.",
    "<strong>Hablad mientras jugáis.</strong> En una sala, mantén pulsado el botón del micrófono (V en el ordenador) para hablar, o tócalo para dejarlo encendido. Tu propio sonido y el ruido de tu alrededor se eliminan, así los demás oyen tu voz y no tu juego ni tu habitación.",
    "<strong>Un servidor de salas, o ninguno.</strong> JUGAR EN LÍNEA abre salas en el servidor de salas de Panorun en la web, listadas allí para que tus amigos entren. O juega en LOCAL: la sala funciona en la ventana de quien la abre, y los amigos entran directamente. Panorun para Windows trae un servidor de salas que cualquiera puede ejecutar.",
    "<strong>Peleas de verdad.</strong> En cuanto Panorun sabe dónde guarda un juego tu salud, los demás pueden golpear a tu personaje, y duele como con los enemigos del propio juego: te empujan hacia atrás y tu salud baja. La salud de todos se ve sobre su nombre.",
    "<strong>Aprende cada juego por sí mismo.</strong> Mientras juegas, Panorun aprende cómo es tu personaje y qué botón salta o golpea, y los jugadores de una sala comparten lo que su Panorun sabe de un juego.",
    "<strong>Graba tus partidas.</strong> GRABAR guarda cada botón que pulsas, y REPETICIÓN vuelve a jugar la partida desde donde empezó.",
    "<strong>Juega con lo que tienes.</strong> Teclado o mando, con cada tecla y botón a tu gusto. En el móvil, una cruceta a la izquierda y A, B, TURBO A y TURBO B a la derecha.",
    "<strong>Fluido en el móvil.</strong> El procesador y los chips de imagen y sonido de la consola funcionan como código nativo, así Panorun va fluido en el móvil, también con amigos en la sala.",
    "<strong>No incluye juegos.</strong> Panorun ejecuta juegos hechos para la clásica consola de 8 bits. Desarrolladores independientes siguen escribiendo juegos nuevos para esta consola, y muchos los regalan: busca en la web <em>8-bit homebrew games</em>. O usa copias de juegos que tengas. Añádelos con <em>AÑADIR JUEGOS</em> o suéltalos en la ventana; Panorun los guarda en <em>Documentos\\Panorun</em>. En el móvil, <em>AÑADIR JUEGOS</em> y <em>ELEGIR CARPETA</em> abren el selector de archivos del móvil. O <em>PROBAR LA DEMO</em>: dos pequeños juegos propios de Panorun, una pelea en las azoteas de noche y una carrera por colinas verdes.",
    "Tu privacidad",
    'Panorun no tiene cuentas, ni analíticas ni publicidad. Tus juegos, ajustes y grabaciones se quedan en tu ordenador o móvil. Panorun solo contacta con GitHub, para buscar una versión más nueva (en Windows); con nuestro servidor de salas y esta web, para la lista de juegos de los que hemos publicado un archivo de juego, y el archivo de un juego de la lista cuando lo inicias; y, cuando juegas en línea, con el servidor de salas o el ordenador cuya sala te une: entonces comparte tu nombre, tu personaje, su salud y el nivel en el que estás con los jugadores de esa sala, y el servidor de salas o el ordenador de la sala ve tu dirección de internet. Cuando mantienes o enciendes el botón del micrófono en una sala, tu voz va en directo a los jugadores de esa sala; no se graba ni se guarda en ningún sitio. Los detalles están en la <a href="/panorun/privacy">Política de privacidad</a> (en inglés).',
    "Licencias de código abierto",
    'Panorun está hecho con software de código abierto: entre otros Python, pygame y SDL, NumPy, y Opus, RNNoise y speexdsp de Xiph.Org para la voz. Cada uno se usa bajo su propia licencia. La lista completa, con el texto de cada licencia, está en el propio Panorun (AJUSTES &rarr; LICENCIAS), junto al programa en Windows, y aquí: <a href="/panorun/third-party-notices.txt">avisos de terceros</a>.',
    "Enlaces",
    '<a href="/panorun/privacy">Política de privacidad</a>',
    '<a href="/panorun/terms">Condiciones de uso</a>',
    '<a href="/panorun/third-party-notices.txt">Licencias de código abierto</a>',
    'Contacto: <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>',
    "&copy; 2026 TIE-Games. Todos los derechos reservados.",
    'Panorun no incluye juegos. Los títulos de los juegos son marcas de sus propietarios; Panorun no está afiliado a ellos ni respaldado por ellos. Lo que publicamos de un juego es solo lo que Panorun sabe de él - dónde guarda la salud de un personaje, qué botones golpean -, nunca nada del juego en sí. Para que retiremos algo, escribe a <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>.',
    "Panorun es un emulador de juegos clásicos de consola de 8 bits que mantiene el nivel entero a la vista y te deja jugar en línea con tus amigos corriendo a tu lado.",
    "Panorun - el nivel entero a la vista",
    "Icono de Panorun",
    "Consigue Panorun en Google Play",
    "Disponible en",
])

#: Mac and Linux (2026-10-28).
BLOCKS.update(dict(zip(MAC_LINUX_KEYS, [
    'MACOS 11 O POSTERIOR, APPLE SILICON (M1 Y POSTERIORES)',
    '<a class="button" href="https://github.com/TIE-Channel/tie-games-com/releases">Descargar Panorun para Mac</a>',
    'Abre la imagen de disco y arrastra <em>Panorun</em> a <em>Aplicaciones</em>.',
    'Panorun aún no está notarizado por Apple: la primera vez, macOS dice que no puede comprobarlo. Abre <em>Ajustes del Sistema</em> &rarr; <em>Privacidad y seguridad</em>, desplázate hacia abajo y haz clic en <em>Abrir igualmente</em> junto a Panorun.',
    'Tus juegos y grabaciones se guardan en <em>Documentos/Panorun</em>.',
    'LINUX, 64 BITS (UBUNTU 22.04 O POSTERIOR Y SIMILARES)',
    '<a class="button" href="https://github.com/TIE-Channel/tie-games-com/releases">Descargar Panorun para Linux</a>',
    'Un solo archivo, un AppImage: permite que se ejecute como programa (en sus Propiedades, o con <code>chmod +x</code>) y ábrelo.',
])))
