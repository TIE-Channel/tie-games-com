"""German."""
from . import blocks

MONTHS = ("Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September",
          "Oktober", "November", "Dezember")


def date(day, month, year):
    return f"{day}. {MONTHS[month - 1]} {year}"


WORDS = {
    "windows": "Panorun {version} für Windows herunterladen",
    "android": "Panorun {version} für Android herunterladen",
    "small": "lädt Panorun beim Installieren herunter",
    "full": 'Oder das <a href="{url}">vollständige Installationsprogramm</a> ({size}) mit allem darin: es installiert ohne Verbindung.',
    "locale": "de-DE",
}

BLOCKS = blocks([
    "Panorun - das ganze Level im Blick | TIE-Games",
    "Das ganze Level im Blick, deine Freunde laufen neben dir.",
    "Panorun ist ein Emulator für klassische 8-Bit-Konsolenspiele, der das ganze Level im Blick behält: Alles, woran du vorbeigescrollt bist, bleibt rund um das Spiel auf dem Bildschirm. Spielt zusammen online, und deine Freunde laufen in deinem eigenen Spiel neben dir. Panorun wird von TIE-Games gemacht, einem unabhängigen Studio in Dresden.",
    'Du hast ein Android-Handy? <a href="#test">Hilf mit, Panorun auf Google Play zu testen</a>.',
    "Download",
    "WINDOWS 10 UND 11, 64 BIT",
    "Das Installationsprogramm fragt, wohin installiert wird und ob eine Verknüpfung auf den Desktop soll. Administratorrechte sind nicht nötig.",
    "Das Installationsprogramm ist noch nicht signiert: Wenn Windows <em>Der Computer wurde durch Windows geschützt</em> meldet, klicke auf <em>Weitere Informationen</em> und dann auf <em>Trotzdem ausführen</em>.",
    "Danach aktualisiert sich Panorun selbst: Klicke auf <em>Update</em>, wenn es eine neue Version meldet.",
    "Panorun entfernen: Windows-Einstellungen &rarr; Apps &rarr; Installierte Apps &rarr; Panorun &rarr; Deinstallieren. Deine Spiele und Aufnahmen bleiben in <em>Dokumente\\Panorun</em>.",
    "ANDROID 7 ODER NEUER, 64 BIT",
    "<strong>Öffne diese Seite zuerst in Chrome.</strong> Sie ist in einer anderen App geöffnet (Telegram, WhatsApp, Gmail…), die keine Dateien herunterladen kann: Dort tut die Schaltfläche unten nichts.",
    '<a class="button" id="open-in-chrome" href="https://tie-games.com/panorun/">In Chrome öffnen</a>',
    "Wenn nichts passiert: Tippe oben auf <strong>&#8942;</strong> oder <strong>&#8943;</strong>, dann auf <em>In Chrome öffnen</em> oder <em>Im Browser öffnen</em>.",
    "<strong>Früher Zugang: Panorun ist im Test auf Google Play</strong>, bevor es für alle erscheint, und jeder kann am Test teilnehmen:",
    'Tritt mit deinem Google-Konto der Gruppe <a href="https://groups.google.com/g/panorun-testers">Panorun testers</a> bei: <em>Gruppe beitreten</em>.',
    'Öffne <a href="https://play.google.com/apps/testing/com.tiegames.panorun">den Test von Panorun auf Google Play</a> und tippe auf <em>Tester werden</em>.',
    "Installiere Panorun mit der Google-Play-Schaltfläche oben.",
    'Behalte es zwei Wochen und spiele ab und zu - <em>DEMO AUSPROBIEREN</em>, ein eigenes Spiel, ein Raum mit anderen - und sag uns, was klappt und was nicht, in der Gruppe oder an <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>. Google Play gibt Panorun für alle frei, sobald genug Tester es zwei Wochen lang gespielt haben.',
    "Oder lade es hier herunter:",
    '<strong>Lade <span id="android-file">Panorun</span> herunter&hellip;</strong> Das dauert eine Minute.',
    "Wenn es fertig ist, tippe unten in Chrome in der Meldung auf <em>Öffnen</em>.",
    "Kein <em>Öffnen</em>, oder die Meldung ist weg? Tippe oben rechts in Chrome auf <strong>&#8942;</strong>, dann auf <em>Downloads</em>, und tippe dort auf die Datei. Oder öffne die App <em>Dateien</em> (auf Xiaomi-Handys <em>Dateimanager</em>), dann <em>Downloads</em>, und tippe auf die Datei.",
    "Tippe auf <em>Installieren</em>.",
    "Öffne diese Seite im Browser deines Handys (Chrome - nicht in einer anderen App) und tippe auf die Schaltfläche. Wenn der Download fertig ist, tippe unten in der Meldung auf <em>Öffnen</em>, dann auf <em>Installieren</em>. Verpasst? In Chrome unter <strong>&#8942;</strong> &rarr; <em>Downloads</em> liegt die Datei: Tippe dort darauf.",
    "Beim ersten Mal fragt Android, ob dein Browser Apps installieren darf: Erlaube es, geh zurück und tippe noch einmal auf <em>Installieren</em>.",
    "Hier heruntergeladen kommt Panorun nicht aus dem Play Store, daher kennt Google Play Protect es vielleicht nicht: Tippe auf <em>Weitere Details</em>, dann auf <em>Trotzdem installieren</em>.",
    "Panorun von Google Play und Panorun von dieser Seite lassen sich nicht übereinander installieren: Zum Wechseln deinstalliere zuerst das, was du hast - dabei gehen die darin gespeicherten Spiele verloren.",
    "Eine neue Version wird genauso über die vorhandene installiert: Deine Spiele bleiben.",
    "Was es kann",
    "<strong>Behält das Level im Blick.</strong> Eine Konsole zeichnet einen Bildschirm nach dem anderen und vergisst den Rest. Panorun behält jeden gezeichneten Bildschirm und malt das Level rund um das Spiel dorthin, wo es hingehört - der Boden, den du überquert hast, bleibt links, oben und unten auf dem Bildschirm.",
    "<strong>Zeichnet beim Spielen eine Karte.</strong> Ein Streifen unter dem Spiel zeigt das bisherige Level, und dich darauf.",
    "<strong>Lässt euch zusammen spielen.</strong> Öffne einen Raum und schick seinen Code, oder tritt einem der Räume auf dem Raumserver bei; jeder, der beitritt, spielt seine eigene Kopie desselben Spiels, und jede Figur läuft durch die Spiele aller anderen, jede in ihrer eigenen Farbe, mit ihrer Linie auf der Karte. Ein Spiel, das weit vorne ist, wartet auf die anderen, damit alle zusammenbleiben. Bis zu zwölf Spieler pro Raum.",
    "<strong>Redet beim Spielen.</strong> Halte in einem Raum die Mikrofon-Taste gedrückt (V am Computer), um zu sprechen, oder tippe darauf, damit sie an bleibt. Dein eigener Spielton und die Geräusche um dich herum werden herausgefiltert, sodass die anderen deine Stimme hören und nicht dein Spiel oder deinen Raum.",
    "<strong>Ein Raumserver, oder keiner.</strong> ONLINE SPIELEN öffnet Räume auf dem Raumserver von Panorun im Web, wo deine Freunde sie finden. Oder spiele LOKAL: Der Raum läuft im Fenster dessen, der ihn öffnet, und Freunde treten ihm direkt bei. Panorun für Windows bringt einen Raumserver mit, den jeder betreiben kann.",
    "<strong>Echte Kämpfe.</strong> Sobald Panorun weiß, wo ein Spiel dein Leben speichert, können die anderen deine Figur treffen, und es tut so weh wie bei den Gegnern des Spiels: Du wirst zurückgestoßen und dein Leben sinkt. Das Leben aller steht über ihrem Namen.",
    "<strong>Lernt jedes Spiel von selbst.</strong> Während du spielst, lernt Panorun, wie deine Figur aussieht und welcher Knopf springt oder schlägt, und Spieler in einem Raum teilen, was ihr Panorun über ein Spiel weiß.",
    "<strong>Nimmt deine Läufe auf.</strong> AUFNEHMEN speichert jeden Knopfdruck, und WIEDERGABE spielt den Lauf von seinem Anfang an noch einmal ab.",
    "<strong>Spielt mit dem, was du hast.</strong> Tastatur oder Gamepad, jede Taste und jeder Knopf frei belegbar. Auf dem Handy ein Kreuz links und A, B, TURBO A und TURBO B rechts.",
    "<strong>Flüssig auf dem Handy.</strong> Prozessor, Grafik- und Soundchips der Konsole laufen als nativer Code, so spielt Panorun auf dem Handy flüssig, auch mit Freunden im Raum.",
    "<strong>Es sind keine Spiele enthalten.</strong> Panorun spielt Spiele für die klassische 8-Bit-Konsole. Unabhängige Entwickler schreiben noch heute neue Spiele für diese Konsole, und viele verschenken sie - suche im Web nach <em>8-bit homebrew games</em>. Oder nutze Kopien von Spielen, die dir gehören. Füge sie mit <em>SPIELE HINZUFÜGEN</em> hinzu oder zieh sie auf das Fenster; Panorun bewahrt sie in <em>Dokumente\\Panorun</em> auf. Auf dem Handy öffnen <em>SPIELE HINZUFÜGEN</em> und <em>ORDNER WÄHLEN</em> die Dateiauswahl des Handys. Oder <em>DEMO AUSPROBIEREN</em>: ein kleines eigenes Spiel von Panorun.",
    "Deine Privatsphäre",
    'Panorun hat keine Konten, keine Analyse und keine Werbung. Deine Spiele, Einstellungen und Aufnahmen bleiben auf deinem Computer oder Handy. Panorun kontaktiert nur GitHub, um nach einer neueren Version zu suchen (unter Windows); unseren Raumserver und diese Website für die Liste der Spiele, für die wir eine Spieldatei veröffentlicht haben, und die Datei eines gelisteten Spiels, wenn du es startest; und, wenn du online spielst, den Raumserver oder den Computer, dessen Raum du beitrittst: Dann teilt es deinen Namen, deine Figur, ihr Leben und das Level, in dem du bist, mit den Spielern in diesem Raum, und der Raumserver oder der Computer des Raums sieht deine Internetadresse. Wenn du in einem Raum die Mikrofon-Taste hältst oder einschaltest, geht deine Stimme live an die Spieler in diesem Raum; sie wird nirgends aufgezeichnet oder gespeichert. Einzelheiten stehen in der <a href="/panorun/privacy">Datenschutzerklärung</a> (auf Englisch).',
    "Open-Source-Lizenzen",
    'Panorun ist mit Open-Source-Software gemacht: unter anderem Python, pygame und SDL, NumPy sowie Opus, RNNoise und speexdsp von Xiph.Org für die Stimme. Jede wird unter ihrer eigenen Lizenz genutzt. Die vollständige Liste mit dem Text jeder Lizenz steht in Panorun selbst (EINSTELLUNGEN &rarr; LIZENZEN), unter Windows neben dem Programm, und hier: <a href="/panorun/third-party-notices.txt">Hinweise zu Drittanbietern</a>.',
    "Links",
    '<a href="/panorun/privacy">Datenschutzerklärung</a>',
    '<a href="/panorun/terms">Nutzungsbedingungen</a>',
    '<a href="/panorun/third-party-notices.txt">Open-Source-Lizenzen</a>',
    'Kontakt: <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>',
    "&copy; 2026 TIE-Games. Alle Rechte vorbehalten.",
    'Panorun enthält keine Spiele. Spieletitel sind Marken ihrer Inhaber; Panorun ist nicht mit ihnen verbunden und wird nicht von ihnen unterstützt. Was wir über ein Spiel veröffentlichen, ist nur, was Panorun darüber weiß - wo es das Leben einer Figur speichert, welche Knöpfe schlagen - nie etwas vom Spiel selbst. Um etwas entfernen zu lassen, schreib an <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>.',
    "Panorun ist ein Emulator für klassische 8-Bit-Konsolenspiele, der das ganze Level im Blick behält und dich online mit deinen Freunden zusammen spielen lässt, die neben dir laufen.",
    "Panorun - das ganze Level im Blick",
    "Panorun-Symbol",
    "Panorun bei Google Play holen",
    "Jetzt bei",
])
