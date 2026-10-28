"""Japanese."""
from . import MAC_LINUX_KEYS, blocks


def date(day, month, year):
    return f"{year}年{month}月{day}日"


WORDS = {
    "windows": "Panorun {version} をダウンロード（Windows）",
    "android": "Panorun {version} をダウンロード（Android）",
    "small": "インストールしながらPanorunをダウンロードします",
    "full": 'または<a href="{url}">完全版インストーラー</a>（{size}）: すべて入っていて、接続なしでインストールできます。',
    "mac": 'Panorun {version} をダウンロード（Mac）',
    "linux": 'Panorun {version} をダウンロード（Linux）',
    "locale": "ja-JP",
}

BLOCKS = blocks([
    "Panorun - ステージ全体が見える | TIE-Games",
    "ステージ全体が見える。友達がすぐ横を走る。",
    "Panorunは、クラシックな8ビットゲーム機のゲームをステージ全体が見える状態で遊べるエミュレーターです。スクロールして通り過ぎた部分も、ゲームの周りの画面に残ります。オンラインで一緒に遊べば、友達があなた自身のゲームの中を並んで走ります。Panorunはドイツ・ドレスデンのインディースタジオ、TIE-Gamesが作っています。",
    'Androidスマートフォンをお持ちですか？ <a href="#test">Google PlayでPanorunのテストに協力してください</a>。',
    "ダウンロード",
    "WINDOWS 10 / 11（64ビット）",
    "インストーラーはインストール先と、デスクトップにショートカットを置くかを尋ねます。管理者権限は必要ありません。",
    "インストーラーはまだコード署名されていません。Windowsが<em>WindowsによってPCが保護されました</em>と表示したら、<em>詳細情報</em>をクリックし、<em>実行</em>をクリックしてください。",
    "その後、Panorunは自分で更新します。新しいバージョンが出たと表示されたら<em>Update</em>をクリックしてください。",
    "Panorunを削除するには: Windowsの設定 &rarr; アプリ &rarr; インストールされているアプリ &rarr; Panorun &rarr; アンインストール。ゲームと録画は<em>ドキュメント\\Panorun</em>に残ります。",
    "ANDROID 7 以降（64ビット）",
    "<strong>まずこのページをChromeで開いてください。</strong> 別のアプリ（Telegram、WhatsApp、Gmail…）の中で開かれていて、ファイルをダウンロードできません。そこでは下のボタンは何もしません。",
    '<a class="button" id="open-in-chrome" href="https://tie-games.com/panorun/">Chromeで開く</a>',
    "何も起きない場合: 上部の<strong>&#8942;</strong>または<strong>&#8943;</strong>をタップし、<em>Chromeで開く</em>または<em>ブラウザで開く</em>をタップしてください。",
    "<strong>早期アクセス: PanorunはGoogle Playでテスト中です。</strong>一般公開の前に、どなたでもテストに参加できます:",
    'Googleアカウントでグループ<a href="https://groups.google.com/g/panorun-testers">Panorun testers</a>に参加: <em>グループに参加</em>。',
    '<a href="https://play.google.com/apps/testing/com.tiegames.panorun">Google PlayのPanorunのテスト</a>を開き、<em>テスターになる</em>をタップします。',
    "上のGoogle PlayボタンからPanorunをインストールします。",
    '2週間インストールしたまま、ときどき遊んでください - <em>デモを試す</em>、お持ちのゲーム、ほかの人とのルーム。うまくいったこと、いかなかったことをグループか<a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>までお知らせください。十分な数のテスターが2週間遊ぶと、Google PlayでPanorunが一般公開されます。',
    "またはここからダウンロード:",
    '<strong><span id="android-file">Panorun</span>をダウンロード中&hellip;</strong> 1分ほどお待ちください。',
    "完了したら、Chromeの下部のメッセージで<em>開く</em>をタップします。",
    "<em>開く</em>がない、またはメッセージが消えた場合: Chromeの右上の<strong>&#8942;</strong>をタップし、<em>ダウンロード</em>でファイルをタップします。または<em>ファイル</em>アプリ（Xiaomiでは<em>ファイルマネージャー</em>）を開き、<em>ダウンロード</em>でファイルをタップします。",
    "<em>インストール</em>をタップします。",
    "スマートフォンのブラウザ（Chrome - ほかのアプリの中ではなく）でこのページを開き、ボタンをタップします。ダウンロードが終わったら、下部のメッセージで<em>開く</em>、続いて<em>インストール</em>をタップします。見逃した場合は、Chromeの<strong>&#8942;</strong> &rarr; <em>ダウンロード</em>にファイルがあります。そこでタップしてください。",
    "初回は、ブラウザにアプリのインストールを許可するかAndroidが尋ねます。許可して戻り、もう一度<em>インストール</em>をタップしてください。",
    "ここからダウンロードしたPanorunはPlayストア経由ではないため、Google Playプロテクトが認識しないことがあります。<em>詳細</em>をタップし、<em>インストールする</em>をタップしてください。",
    "Google PlayのPanorunとこのページのPanorunは上書きインストールできません。切り替えるには、まず今のものをアンインストールしてください。中に保存したゲームも削除されます。",
    "新しいバージョンも同じように、今のものに上書きしてインストールします。ゲームは残ります。",
    "できること",
    "<strong>ステージを見渡せる。</strong> ゲーム機は一度に1画面だけを描き、ほかは忘れてしまいます。Panorunは描いた画面をすべて覚え、ゲームの周りの本来の位置にステージを描きます。通り過ぎた地形が左にも上にも下にも残ります。",
    "<strong>遊びながらマップを描く。</strong> ゲームの下の帯に、これまでのステージとあなたの位置が表示されます。",
    "<strong>一緒に遊べる。</strong> ルームを開いてコードを送るか、ルームサーバーに並ぶルームに参加します。参加した人はそれぞれ同じゲームの自分のコピーを遊び、全員のキャラクターがほかの全員のゲームの中を走ります。それぞれ自分の色で、マップには自分の線が引かれます。大きく先に進んだゲームはほかの人を待つので、みんな一緒にいられます。1ルーム最大12人。",
    "<strong>遊びながら話せる。</strong> ルームでマイクボタン（コンピューターではV）を押している間話せます。タップするとオンのままになります。自分のゲーム音と周りの雑音は取り除かれ、相手にはあなたの声だけが聞こえます。",
    "<strong>ルームサーバーでも、なしでも。</strong> 「オンラインで遊ぶ」はウェブ上のPanorunのルームサーバーにルームを開き、友達が参加できるよう一覧に載せます。またはローカルで遊ぶこともできます。ルームは開いた人のウィンドウで動き、友達は直接参加します。Windows版Panorunには誰でも動かせるルームサーバーが付いています。",
    "<strong>本気の対戦。</strong> ゲームが体力をどこに保存しているかPanorunが知ると、ほかの人があなたのキャラクターを攻撃でき、ゲームの敵と同じようにダメージを受けます。弾き飛ばされ、体力が減ります。全員の体力が名前の上に表示されます。",
    "<strong>ゲームを自分で学ぶ。</strong> 遊んでいる間に、Panorunはあなたのキャラクターの見た目や、どのボタンでジャンプや攻撃をするかを学び、ルームのプレイヤーは各自のPanorunがそのゲームについて知っていることを共有します。",
    "<strong>プレイを録画。</strong> 「録画」は押したボタンをすべて記録し、「リプレイ」はそのプレイを最初から再生します。",
    "<strong>手持ちの機器で遊べる。</strong> キーボードでもゲームパッドでも、キーとボタンは自由に設定できます。スマートフォンでは左に十字キー、右にA、B、ターボA、ターボB。",
    "<strong>スマートフォンでもなめらか。</strong> ゲーム機のプロセッサー、画像と音のチップはネイティブコードで動くので、ルームに友達がいてもスマートフォンでなめらかに遊べます。",
    "<strong>ゲームは含まれていません。</strong> Panorunはクラシックな8ビットゲーム機用のゲームを遊べます。インディー開発者は今もこのゲーム機向けに新作を作り、その多くを無料で公開しています。ウェブで<em>8-bit homebrew games</em>を検索してください。またはお持ちのゲームのコピーを使ってください。<em>ゲームを追加</em>で追加するか、ウィンドウにドロップします。Panorunは<em>ドキュメント\\Panorun</em>に保存します。スマートフォンでは<em>ゲームを追加</em>と<em>フォルダーを選ぶ</em>がスマートフォンのファイル選択を開きます。または<em>デモを試す</em>: Panorun付属の小さなゲームです。",
    "プライバシー",
    'Panorunにはアカウントも解析も広告もありません。ゲーム、設定、録画はあなたのコンピューターやスマートフォンに残ります。Panorunが接続するのは、新しいバージョンを確認するGitHub（Windows）、ゲームファイルを公開しているゲームの一覧と、一覧のゲームを始めたときのそのファイルのための私たちのルームサーバーとこのウェブサイト、そしてオンラインで遊ぶときのルームサーバーまたは参加したルームのコンピューターだけです。そのとき、名前、キャラクター、その体力、いるステージがそのルームのプレイヤーと共有され、ルームサーバーまたはルームのコンピューターにはあなたのインターネットアドレスが見えます。ルームでマイクボタンを押すかオンにすると、声はそのルームのプレイヤーにライブで届きます。どこにも録音・保存されません。詳しくは<a href="/panorun/privacy">プライバシーポリシー</a>（英語）をご覧ください。',
    "オープンソースライセンス",
    'Panorunはオープンソースソフトウェアで作られています。Python、pygameとSDL、NumPy、そして音声用のXiph.OrgのOpus、RNNoise、speexdspなどです。それぞれ独自のライセンスで使用しています。全ライセンスの本文を含む一覧は、Panorun本体（設定 &rarr; ライセンス）、Windowsではプログラムの横、そしてこちらにあります: <a href="/panorun/third-party-notices.txt">サードパーティーの通知</a>。',
    "リンク",
    '<a href="/panorun/privacy">プライバシーポリシー</a>',
    '<a href="/panorun/terms">利用規約</a>',
    '<a href="/panorun/third-party-notices.txt">オープンソースライセンス</a>',
    'お問い合わせ: <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>',
    "&copy; 2026 TIE-Games. All rights reserved.",
    'Panorunにゲームは付属しません。ゲームのタイトルは各所有者の商標であり、Panorunはそれらと提携も承認もされていません。私たちがゲームについて公開するのは、Panorunがそのゲームについて知っていること（キャラクターの体力の保存場所、攻撃するボタン）だけで、ゲーム自体は一切含みません。削除のご依頼は<a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>までご連絡ください。',
    "Panorunは、クラシックな8ビットゲーム機のゲームをステージ全体が見える状態で遊べ、友達と並んでオンラインで遊べるエミュレーターです。",
    "Panorun - ステージ全体が見える",
    "Panorunのアイコン",
    "Google PlayでPanorunを入手",
    "手に入れよう",
])

#: Mac and Linux (2026-10-28).
BLOCKS.update(dict(zip(MAC_LINUX_KEYS, [
    'MACOS 11 以降、APPLE シリコン（M1 以降）',
    '<a class="button" href="https://github.com/TIE-Channel/tie-games-com/releases">Panorun をダウンロード（Mac）</a>',
    'ディスクイメージを開き、<em>Panorun</em>を<em>アプリケーション</em>にドラッグします。',
    'PanorunはまだAppleの公証を受けていません。初回はmacOSが確認できないと表示します。<em>システム設定</em> &rarr; <em>プライバシーとセキュリティ</em>を開き、下にスクロールしてPanorunの横の<em>このまま開く</em>をクリックしてください。',
    'ゲームと録画は<em>書類/Panorun</em>に保存されます。',
    'LINUX（64ビット、UBUNTU 22.04 以降など）',
    '<a class="button" href="https://github.com/TIE-Channel/tie-games-com/releases">Panorun をダウンロード（Linux）</a>',
    'AppImageの1ファイルです。プログラムとして実行できるようにして（プロパティ、または<code>chmod +x</code>）開いてください。',
])))
