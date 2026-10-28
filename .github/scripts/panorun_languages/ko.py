"""Korean."""
from . import MAC_LINUX_KEYS, VIDEO_KEYS, blocks


def date(day, month, year):
    return f"{year}년 {month}월 {day}일"


WORDS = {
    "windows": "Windows용 Panorun {version} 다운로드",
    "android": "Android용 Panorun {version} 다운로드",
    "small": "설치하면서 Panorun을 내려받습니다",
    "full": '또는 <a href="{url}">전체 설치 프로그램</a>({size}): 모든 것이 들어 있어 인터넷 연결 없이 설치됩니다.',
    "mac": 'Mac용 Panorun {version} 다운로드',
    "linux": 'Linux용 Panorun {version} 다운로드',
    "locale": "ko-KR",
}

BLOCKS = blocks([
    "Panorun - 스테이지 전체가 한눈에 | TIE-Games",
    "스테이지 전체가 한눈에, 친구들이 바로 옆에서 달립니다.",
    "Panorun은 스테이지 전체를 보여 주는 고전 8비트 게임기 게임용 에뮬레이터입니다. 스크롤해서 지나온 모든 곳이 게임 주변 화면에 남습니다. 온라인으로 함께 플레이하면 친구들이 내 게임 안에서 나란히 달립니다. Panorun은 독일 드레스덴의 인디 스튜디오 TIE-Games가 만듭니다.",
    'Android 휴대폰이 있나요? <a href="#test">Google Play에서 Panorun 테스트를 도와주세요</a>.',
    "다운로드",
    "WINDOWS 10 및 11, 64비트",
    "설치 프로그램은 설치 위치와 바탕 화면 바로 가기를 만들지 묻습니다. 관리자 권한은 필요 없습니다.",
    "설치 프로그램은 아직 코드 서명이 되어 있지 않습니다. Windows에 <em>Windows의 PC 보호</em>가 나오면 <em>추가 정보</em>를 클릭한 다음 <em>실행</em>을 클릭하세요.",
    "그 뒤로는 Panorun이 스스로 업데이트합니다. 새 버전이 나왔다고 하면 <em>Update</em>를 클릭하세요.",
    "Panorun 제거: Windows 설정 &rarr; 앱 &rarr; 설치된 앱 &rarr; Panorun &rarr; 제거. 게임과 녹화는 <em>문서\\Panorun</em>에 남습니다.",
    "ANDROID 7 이상, 64비트",
    "<strong>먼저 이 페이지를 Chrome에서 여세요.</strong> 지금은 파일을 내려받을 수 없는 다른 앱(Telegram, WhatsApp, Gmail…) 안에서 열려 있어서 아래 버튼이 아무것도 하지 않습니다.",
    '<a class="button" id="open-in-chrome" href="https://tie-games.com/panorun/">Chrome에서 열기</a>',
    "아무 일도 없으면: 위쪽의 <strong>&#8942;</strong> 또는 <strong>&#8943;</strong>를 탭한 다음 <em>Chrome에서 열기</em> 또는 <em>브라우저에서 열기</em>를 탭하세요.",
    "<strong>앞서 해보기: Panorun은 모두에게 공개되기 전에 Google Play에서 테스트 중이며</strong>, 누구나 테스트에 참여할 수 있습니다:",
    'Google 계정으로 <a href="https://groups.google.com/g/panorun-testers">Panorun testers</a> 그룹에 가입하세요: <em>그룹 가입</em>.',
    '<a href="https://play.google.com/apps/testing/com.tiegames.panorun">Google Play의 Panorun 테스트</a>를 열고 <em>테스터 되기</em>를 탭하세요.',
    "위의 Google Play 버튼으로 Panorun을 설치하세요.",
    '2주 동안 설치해 두고 가끔 플레이해 주세요 - <em>데모 해 보기</em>, 가진 게임, 다른 사람과의 방 - 그리고 잘되는 것과 안 되는 것을 그룹이나 <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>으로 알려 주세요. 충분한 테스터가 2주 동안 플레이하면 Google Play에서 Panorun이 모두에게 공개됩니다.',
    "또는 여기서 다운로드:",
    '<strong><span id="android-file">Panorun</span> 다운로드 중&hellip;</strong> 1분쯤 걸립니다.',
    "다 되면 Chrome 아래쪽 메시지에서 <em>열기</em>를 탭하세요.",
    "<em>열기</em>가 없거나 메시지가 사라졌나요? Chrome 오른쪽 위의 <strong>&#8942;</strong>를 탭하고 <em>다운로드</em>에서 파일을 탭하세요. 또는 <em>파일</em> 앱(Xiaomi 휴대폰은 <em>파일 관리자</em>)을 열고 <em>다운로드</em>에서 파일을 탭하세요.",
    "<em>설치</em>를 탭하세요.",
    "휴대폰 브라우저(다른 앱 안이 아닌 Chrome)에서 이 페이지를 열고 버튼을 탭하세요. 다운로드가 끝나면 아래쪽 메시지에서 <em>열기</em>, 그다음 <em>설치</em>를 탭하세요. 놓쳤나요? Chrome의 <strong>&#8942;</strong> &rarr; <em>다운로드</em>에 파일이 있습니다. 거기서 탭하세요.",
    "처음에는 Android가 브라우저의 앱 설치를 허용할지 묻습니다. 허용하고 돌아가서 <em>설치</em>를 다시 탭하세요.",
    "여기서 내려받은 Panorun은 Play 스토어에서 온 것이 아니라서 Google Play 프로텍트가 모를 수 있습니다. <em>세부정보 더보기</em>를 탭한 다음 <em>무시하고 설치</em>를 탭하세요.",
    "Google Play의 Panorun과 이 페이지의 Panorun은 서로 덮어 설치할 수 없습니다. 바꾸려면 먼저 지금 있는 것을 제거하세요. 그 안에 저장한 게임도 함께 지워집니다.",
    "새 버전도 같은 방법으로 지금 있는 것 위에 설치합니다. 게임은 그대로 남습니다.",
    "할 수 있는 것",
    "<strong>스테이지를 한눈에.</strong> 게임기는 한 번에 한 화면만 그리고 나머지는 잊습니다. Panorun은 그린 모든 화면을 기억해 게임 주변 원래 자리에 스테이지를 그립니다. 지나온 지형이 왼쪽, 위, 아래에 그대로 남습니다.",
    "<strong>플레이하면서 지도를 그립니다.</strong> 게임 아래 띠에 지금까지의 스테이지와 내 위치가 보입니다.",
    "<strong>함께 플레이.</strong> 방을 열고 코드를 보내거나, 방 서버 목록의 방에 참가하세요. 참가한 사람은 각자 같은 게임의 자기 사본을 플레이하고, 모두의 캐릭터가 다른 모든 사람의 게임 안을 달립니다. 각자 자기 색으로, 지도에는 자기 선이 그려집니다. 너무 앞서간 게임은 다른 사람을 기다려 모두 함께 갑니다. 방마다 최대 12명.",
    "<strong>플레이하며 대화.</strong> 방에서 마이크 버튼(컴퓨터에서는 V)을 누르고 있는 동안 말하거나, 탭해서 켜 둘 수 있습니다. 내 게임 소리와 주변 소음은 걸러져서 다른 사람에게는 내 목소리만 들립니다.",
    "<strong>방 서버, 또는 없이.</strong> 온라인 플레이는 웹에 있는 Panorun 방 서버에 방을 열어 친구들이 참가할 수 있게 목록에 올립니다. 또는 로컬로 플레이하세요. 방은 연 사람의 창에서 돌아가고 친구들이 바로 참가합니다. Windows용 Panorun에는 누구나 실행할 수 있는 방 서버가 들어 있습니다.",
    "<strong>진짜 대결.</strong> 게임이 체력을 어디에 저장하는지 Panorun이 알게 되면 다른 사람이 내 캐릭터를 공격할 수 있고, 게임 속 적에게 맞을 때처럼 아픕니다. 뒤로 밀려나고 체력이 깎입니다. 모두의 체력이 이름 위에 보입니다.",
    "<strong>게임을 스스로 익힙니다.</strong> 플레이하는 동안 Panorun은 내 캐릭터가 어떻게 생겼는지, 어떤 버튼이 점프나 공격인지 배우고, 방의 플레이어들은 각자의 Panorun이 게임에 대해 아는 것을 나눕니다.",
    "<strong>플레이를 녹화합니다.</strong> 녹화는 누른 모든 버튼을 기록하고, 다시 보기는 처음부터 다시 재생합니다.",
    "<strong>가진 것으로 플레이.</strong> 키보드나 게임패드, 모든 키와 버튼을 원하는 대로 설정할 수 있습니다. 휴대폰에서는 왼쪽에 방향 키, 오른쪽에 A, B, 터보 A, 터보 B.",
    "<strong>휴대폰에서도 부드럽게.</strong> 게임기의 프로세서와 화면·소리 칩이 네이티브 코드로 돌아가서, 방에 친구가 있어도 휴대폰에서 부드럽게 플레이됩니다.",
    "<strong>게임은 들어 있지 않습니다.</strong> Panorun은 고전 8비트 게임기용 게임을 실행합니다. 인디 개발자들은 지금도 이 게임기용 새 게임을 만들고 많은 게임을 무료로 공개합니다. 웹에서 <em>8-bit homebrew games</em>를 검색해 보세요. 또는 가지고 있는 게임의 사본을 사용하세요. <em>게임 추가</em>로 추가하거나 창에 끌어다 놓으세요. Panorun은 <em>문서\\Panorun</em>에 보관합니다. 휴대폰에서는 <em>게임 추가</em>와 <em>폴더 선택</em>이 휴대폰의 파일 선택기를 엽니다. 또는 <em>데모 해 보기</em>: Panorun에 들어 있는 작은 게임 두 개, 밤의 옥상에서 벌이는 격투와 푸른 언덕을 달리는 게임입니다.",
    "개인정보",
    'Panorun에는 계정도, 분석도, 광고도 없습니다. 게임, 설정, 녹화는 내 컴퓨터나 휴대폰에 남습니다. Panorun이 연결하는 곳은 새 버전을 확인하는 GitHub(Windows), 게임 파일을 공개한 게임 목록과 목록의 게임을 시작할 때 그 파일을 위한 우리의 방 서버와 이 웹사이트, 그리고 온라인으로 플레이할 때 방 서버나 참가한 방의 컴퓨터뿐입니다. 이때 내 이름, 캐릭터, 체력, 있는 스테이지가 그 방의 플레이어와 공유되고, 방 서버나 방의 컴퓨터는 내 인터넷 주소를 봅니다. 방에서 마이크 버튼을 누르거나 켜면 내 목소리가 그 방의 플레이어에게 실시간으로 전달되며, 어디에도 녹음되거나 저장되지 않습니다. 자세한 내용은 <a href="/panorun/privacy">개인정보처리방침</a>(영어)을 보세요.',
    "오픈 소스 라이선스",
    'Panorun은 오픈 소스 소프트웨어로 만들어졌습니다. Python, pygame과 SDL, NumPy, 그리고 음성용 Xiph.Org의 Opus, RNNoise, speexdsp 등입니다. 각각 자체 라이선스로 사용됩니다. 모든 라이선스 본문이 담긴 전체 목록은 Panorun 안(설정 &rarr; 라이선스), Windows에서는 프로그램 옆, 그리고 여기에 있습니다: <a href="/panorun/third-party-notices.txt">타사 고지</a>.',
    "링크",
    '<a href="/panorun/privacy">개인정보처리방침</a>',
    '<a href="/panorun/terms">이용약관</a>',
    '<a href="/panorun/third-party-notices.txt">오픈 소스 라이선스</a>',
    '문의: <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>',
    "&copy; 2026 TIE-Games. All rights reserved.",
    'Panorun에는 게임이 들어 있지 않습니다. 게임 제목은 각 소유자의 상표이며, Panorun은 그들과 제휴하거나 보증받지 않았습니다. 우리가 게임에 대해 공개하는 것은 Panorun이 아는 것(캐릭터 체력의 저장 위치, 공격 버튼)뿐이며 게임 자체는 전혀 포함하지 않습니다. 삭제를 원하면 <a href="mailto:tie.games.info@gmail.com">tie.games.info@gmail.com</a>으로 연락하세요.',
    "Panorun은 스테이지 전체를 보여 주는 고전 8비트 게임기 게임용 에뮬레이터로, 친구들과 나란히 온라인으로 플레이할 수 있습니다.",
    "Panorun - 스테이지 전체가 한눈에",
    "Panorun 아이콘",
    "Google Play에서 Panorun 받기",
    "다운로드하기",
])

#: Mac and Linux (2026-10-28).
BLOCKS.update(dict(zip(MAC_LINUX_KEYS, [
    'MACOS 11 이상, APPLE 실리콘 (M1 이상)',
    '디스크 이미지를 열고 <em>Panorun</em>을 <em>응용 프로그램</em>으로 끌어다 놓으세요.',
    'Panorun은 아직 Apple의 공증을 받지 않았습니다. 처음에는 macOS가 확인할 수 없다고 합니다. <em>시스템 설정</em> &rarr; <em>개인정보 보호 및 보안</em>을 열고 아래로 스크롤해 Panorun 옆의 <em>그래도 열기</em>를 클릭하세요.',
    '게임과 녹화는 <em>문서/Panorun</em>에 보관됩니다.',
    'LINUX, 64비트 (UBUNTU 22.04 이상 등)',
    'AppImage 파일 하나입니다. 프로그램으로 실행할 수 있게 허용하고(속성 또는 <code>chmod +x</code>) 여세요.',
])))

BLOCKS.update(dict(zip(VIDEO_KEYS, [
    'Panorun 동영상 재생 (YouTube)',
    'Panorun의 작은 게임 두 개를 방에서 함께 플레이',
    '40초로 보는 Panorun. 클릭하면 YouTube에서 동영상이 재생됩니다.',
])))
