"""French."""
from . import MAC_LINUX_KEYS, VIDEO_KEYS, blocks

MONTHS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre",
          "octobre", "novembre", "décembre")


def date(day, month, year):
    return f"{day} {MONTHS[month - 1]} {year}"


WORDS = {
    "windows": "Télécharger Panorun {version} pour Windows",
    "android": "Télécharger Panorun {version} pour Android",
    "small": "télécharge Panorun pendant l'installation",
    "full": 'Ou le <a href="{url}">programme d\'installation complet</a> ({size}), avec tout dedans : il s\'installe sans connexion.',
    "mac": 'Télécharger Panorun {version} pour Mac',
    "linux": 'Télécharger Panorun {version} pour Linux',
    "locale": "fr-FR",
}

BLOCKS = blocks([
    "Panorun - le niveau entier en vue | TIE-Games",
    "Le niveau entier en vue, vos amis qui courent à côté de vous.",
    "Panorun est un émulateur de jeux de console 8 bits classiques qui garde le niveau entier en vue : tout ce que vous avez fait défiler reste à l'écran autour du jeu. Jouez ensemble en ligne, et vos amis courent à côté de vous dans votre propre jeu. Panorun est créé par TIE-Games, un studio indépendant de Dresde, en Allemagne.",
    'Vous avez un téléphone Android ? <a href="#test">Aidez à tester Panorun sur Google Play</a>.',
    "Télécharger",
    "WINDOWS 10 ET 11, 64 BITS",
    "Le programme d'installation demande où installer et s'il faut un raccourci sur le bureau. Aucun droit d'administrateur n'est nécessaire.",
    "Le programme d'installation n'est pas encore signé : si Windows affiche <em>Windows a protégé votre ordinateur</em>, cliquez sur <em>Informations complémentaires</em>, puis sur <em>Exécuter quand même</em>.",
    "Ensuite Panorun se met à jour tout seul : cliquez sur <em>Update</em> quand il annonce une nouvelle version.",
    "Pour supprimer Panorun : Paramètres Windows &rarr; Applications &rarr; Applications installées &rarr; Panorun &rarr; Désinstaller. Vos jeux et enregistrements restent dans <em>Documents\\Panorun</em>.",
    "ANDROID 7 OU PLUS RÉCENT, 64 BITS",
    "<strong>Ouvrez d'abord cette page dans Chrome.</strong> Elle est ouverte dans une autre application (Telegram, WhatsApp, Gmail…), qui ne peut pas télécharger de fichiers : le bouton ci-dessous n'y fait rien.",
    '<a class="button" id="open-in-chrome" href="https://tie-games.com/panorun/">Ouvrir dans Chrome</a>',
    "S'il ne se passe rien : touchez <strong>&#8942;</strong> ou <strong>&#8943;</strong> en haut, puis <em>Ouvrir dans Chrome</em> ou <em>Ouvrir dans le navigateur</em>.",
    "<strong>Accès anticipé : Panorun est en test sur Google Play</strong> avant de s'ouvrir à tous, et tout le monde peut rejoindre le test :",
    'Rejoignez le groupe <a href="https://groups.google.com/g/panorun-testers">Panorun testers</a> avec votre compte Google : <em>Rejoindre le groupe</em>.',
    'Ouvrez <a href="https://play.google.com/apps/testing/com.tiegames.panorun">le test de Panorun sur Google Play</a> et touchez <em>Devenir testeur</em>.',
    "Installez Panorun avec le bouton Google Play ci-dessus.",
    'Gardez-le deux semaines et jouez de temps en temps - <em>ESSAYER LA DÉMO</em>, un jeu à vous, un salon avec d\'autres - et dites-nous ce qui marche et ce qui ne marche pas, dans le groupe ou à <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>. Google Play ouvre Panorun à tous une fois qu\'assez de testeurs y ont joué pendant deux semaines.',
    "Ou téléchargez-le ici :",
    '<strong>Téléchargement de <span id="android-file">Panorun</span>&hellip;</strong> Comptez une minute.',
    "Une fois terminé, touchez <em>Ouvrir</em> dans le message en bas de Chrome.",
    "Pas d'<em>Ouvrir</em>, ou le message a disparu ? Touchez <strong>&#8942;</strong> en haut à droite de Chrome, puis <em>Téléchargements</em>, et touchez le fichier. Ou ouvrez l'application <em>Fichiers</em> (sur les téléphones Xiaomi <em>Gestionnaire de fichiers</em>), puis <em>Téléchargements</em>, et touchez le fichier.",
    "Touchez <em>Installer</em>.",
    "Ouvrez cette page dans le navigateur de votre téléphone (Chrome, pas dans une autre application) et touchez le bouton. Une fois le téléchargement terminé, touchez <em>Ouvrir</em> dans le message en bas, puis <em>Installer</em>. Raté ? Dans Chrome, <strong>&#8942;</strong> &rarr; <em>Téléchargements</em> contient le fichier : touchez-le.",
    "La première fois, Android demande si votre navigateur peut installer des applications : autorisez-le, revenez en arrière et touchez de nouveau <em>Installer</em>.",
    "Téléchargé ici, Panorun ne vient pas du Play Store, donc Google Play Protect peut ne pas le connaître : touchez <em>Plus de détails</em>, puis <em>Installer quand même</em>.",
    "Panorun de Google Play et Panorun de cette page ne s'installent pas l'un par-dessus l'autre : pour changer, désinstallez d'abord celui que vous avez - cela supprime les jeux qu'il contient.",
    "Une nouvelle version s'installe de la même façon, par-dessus celle que vous avez : vos jeux restent.",
    "Ce qu'il fait",
    "<strong>Garde le niveau en vue.</strong> Une console dessine un écran à la fois et oublie le reste. Panorun garde chaque écran dessiné et peint le niveau autour du jeu, là où il se trouve : le terrain parcouru reste à l'écran, à gauche, au-dessus et en dessous.",
    "<strong>Dessine une carte pendant que vous jouez.</strong> Une bande sous le jeu montre le niveau jusqu'ici, avec vous dessus.",
    "<strong>Vous fait jouer ensemble.</strong> Ouvrez un salon et envoyez son code, ou rejoignez un des salons listés sur le serveur de salons ; chacun joue sa propre copie du même jeu, et le personnage de chacun court dans le jeu de tous les autres, chacun de sa couleur, avec sa ligne sur la carte. Un jeu très en avance attend les autres, pour que tout le monde reste ensemble. Jusqu'à douze joueurs par salon.",
    "<strong>Parlez en jouant.</strong> Dans un salon, maintenez le bouton du micro (V sur un ordinateur) pour parler, ou touchez-le pour le laisser allumé. Le son de votre jeu et les bruits autour de vous sont retirés : les autres entendent votre voix, pas votre jeu ni votre pièce.",
    "<strong>Un serveur de salons, ou aucun.</strong> JOUER EN LIGNE ouvre des salons sur le serveur de salons de Panorun sur le web, listés là pour que vos amis les rejoignent. Ou jouez en LOCAL : le salon tourne dans la fenêtre de celui qui l'ouvre, et les amis le rejoignent directement. Panorun pour Windows est livré avec un serveur de salons que tout le monde peut lancer.",
    "<strong>De vrais combats.</strong> Dès que Panorun sait où un jeu garde votre santé, les autres peuvent frapper votre personnage, et ça fait mal comme avec les ennemis du jeu : vous êtes repoussé et votre santé baisse. La santé de chacun s'affiche au-dessus de son nom.",
    "<strong>Apprend chaque jeu tout seul.</strong> Pendant que vous jouez, Panorun apprend à quoi ressemble votre personnage et quel bouton saute ou frappe, et les joueurs d'un salon partagent ce que leur Panorun sait d'un jeu.",
    "<strong>Enregistre vos parties.</strong> ENREGISTRER garde chaque bouton pressé, et REVOIR rejoue la partie depuis son début.",
    "<strong>Joue avec ce que vous avez.</strong> Clavier ou manette, chaque touche et chaque bouton réglables. Sur téléphone, une croix à gauche et A, B, TURBO A et TURBO B à droite.",
    "<strong>Fluide sur téléphone.</strong> Le processeur et les puces d'image et de son de la console tournent en code natif : Panorun est fluide sur un téléphone, même avec des amis dans le salon.",
    "<strong>Aucun jeu n'est inclus.</strong> Panorun fait tourner des jeux conçus pour la console 8 bits classique. Des développeurs indépendants écrivent encore de nouveaux jeux pour cette console, et beaucoup les offrent : cherchez <em>8-bit homebrew games</em> sur le web. Ou utilisez des copies de jeux que vous possédez. Ajoutez-les avec <em>AJOUTER DES JEUX</em>, ou déposez-les sur la fenêtre ; Panorun les garde dans <em>Documents\\Panorun</em>. Sur téléphone, <em>AJOUTER DES JEUX</em> et <em>CHOISIR UN DOSSIER</em> ouvrent le sélecteur de fichiers du téléphone. Ou <em>ESSAYER LA DÉMO</em> : deux petits jeux à Panorun, une bagarre sur les toits la nuit et une course à travers des collines vertes.",
    "Votre vie privée",
    'Panorun n\'a ni comptes, ni statistiques, ni publicité. Vos jeux, réglages et enregistrements restent sur votre ordinateur ou téléphone. Panorun ne contacte que GitHub, pour chercher une version plus récente (sous Windows) ; notre serveur de salons et ce site, pour la liste des jeux dont nous avons publié un fichier de jeu, et le fichier d\'un jeu listé quand vous le lancez ; et, quand vous jouez en ligne, le serveur de salons ou l\'ordinateur dont vous rejoignez le salon : il partage alors votre nom, votre personnage, sa santé et le niveau où vous êtes avec les joueurs de ce salon, et le serveur de salons ou l\'ordinateur du salon voit votre adresse internet. Quand vous maintenez ou allumez le bouton du micro dans un salon, votre voix part en direct vers les joueurs de ce salon ; elle n\'est enregistrée ni stockée nulle part. Les détails sont dans la <a href="/panorun/privacy">politique de confidentialité</a> (en anglais).',
    "Licences open source",
    'Panorun est fait avec des logiciels open source : entre autres Python, pygame et SDL, NumPy, ainsi qu\'Opus, RNNoise et speexdsp de Xiph.Org pour la voix. Chacun est utilisé sous sa propre licence. La liste complète, avec le texte de chaque licence, est dans Panorun lui-même (RÉGLAGES &rarr; LICENCES), à côté du programme sous Windows, et ici : <a href="/panorun/third-party-notices.txt">mentions des tiers</a>.',
    "Liens",
    '<a href="/panorun/privacy">Politique de confidentialité</a>',
    '<a href="/panorun/terms">Conditions d\'utilisation</a>',
    '<a href="/panorun/third-party-notices.txt">Licences open source</a>',
    'Contact : <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>',
    "&copy; 2026 TIE-Games. Tous droits réservés.",
    'Panorun ne contient aucun jeu. Les titres de jeux sont des marques de leurs propriétaires ; Panorun n\'est ni affilié à eux ni approuvé par eux. Ce que nous publions d\'un jeu n\'est que ce que Panorun en sait - où il garde la santé d\'un personnage, quels boutons frappent -, jamais rien du jeu lui-même. Pour faire retirer quelque chose, écrivez à <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>.',
    "Panorun est un émulateur de jeux de console 8 bits classiques qui garde le niveau entier en vue et vous fait jouer en ligne avec vos amis qui courent à côté de vous.",
    "Panorun - le niveau entier en vue",
    "Icône de Panorun",
    "Disponible sur Google Play",
    "Disponible sur",
])

#: Mac and Linux (2026-10-28).
BLOCKS.update(dict(zip(MAC_LINUX_KEYS, [
    'MACOS 11 OU PLUS RÉCENT, APPLE SILICON (M1 ET PLUS RÉCENTS)',
    "Ouvrez l'image disque et faites glisser <em>Panorun</em> sur <em>Applications</em>.",
    "Panorun n'est pas encore notarié par Apple : la première fois, macOS dit qu'il ne peut pas le vérifier. Ouvrez <em>Réglages Système</em> &rarr; <em>Confidentialité et sécurité</em>, faites défiler et cliquez sur <em>Ouvrir quand même</em> à côté de Panorun.",
    'Vos jeux et enregistrements sont gardés dans <em>Documents/Panorun</em>.',
    'LINUX, 64 BITS (UBUNTU 22.04 OU PLUS RÉCENT ET SIMILAIRES)',
    "Un seul fichier, un AppImage : autorisez-le à s'exécuter comme un programme (dans ses Propriétés, ou avec <code>chmod +x</code>) et ouvrez-le.",
])))

BLOCKS.update(dict(zip(VIDEO_KEYS, [
    'Lire la vidéo de Panorun (YouTube)',
    'Les deux petits jeux de Panorun, joués ensemble dans un salon',
    'Panorun en 40 secondes. Une fois cliquée, la vidéo est lue depuis YouTube.',
])))
