# Lemo-Opuscar

**40 种影片风格，每种都配一支完全用代码做出来的短片。** 选一个风格，带上你自己的主题，让你的编程 agent 来当导演。

[**▶ 看图鉴**](https://lemomo-ai.github.io/lemo-opuscar/) · [English](README.md)

![全部 40 个风格](docs/cover.jpg)

这里的每一支片子，都是 AI agent（Claude Opus 5.5）写代码导演、作画、配乐、混音的：Canvas 和 WebGL 页面逐帧渲染，用免费采样库写原创配乐，本地 TTS 配音。不用视频生成，也不用素材库画面。

## 怎么用

```sh
git clone https://github.com/lemomo-ai/lemo-opuscar.git
cd lemo-opuscar
claude            # 或 Codex、Cursor……任何会读 AGENTS.md 的 agent
```

然后直接说：

> 用 **watercolor** 风格做一支 45 秒的片子，讲我家经营的咖啡园，温暖的女声旁白。

agent 会读三份指南，像一个小工作室一样开工：

| 文件 | 给 agent 的东西 |
|---|---|
| [导演方法](docs/zh-CN/DIRECTOR.md) | 怎么导：故事、声音、节奏、镜头、表演、自检 |
| [技术方法](docs/zh-CN/TECHNIQUE.md) | 怎么做：逐帧渲染、配音、配乐、混音 |
| `styles/<风格>/STYLE.md` | 这个风格长什么样、听起来什么样，以及我们的样片是怎么做的 |

它会停下来找你两次：一次确认**故事和分镜**，一次确认**画面**。之后把成片做到 `films/<名字>/` 里。

想在自己的项目里做？把这三个文件交给你的 agent 就行。

**提前知道：** 一支片子 agent 大约要工作 30–60 分钟，token 用量不小。需要 Node 20+、Chrome、ffmpeg 和 Python 3.11+。配音模型、采样库这类大文件，用到的那一步才会下载。

## 风格清单

<!-- styles:start -->

**手绘与绘画 · Hand-drawn & Painting**

- [蜡笔儿童绘本 Crayon Picture Book](styles/crayon-book/STYLE.md) · 《The Moon Can't Sleep》: 月亮失眠了，小女孩爬上屋顶给它唱摇篮曲。
- [水彩笔刷 Watercolor Brush](styles/watercolor/STYLE.md) · 《Follow the Rain》: 跟着降雨从澳洲红色腹地一路画到绿色海岸，一镜到底。
- [中国水墨 Chinese Ink Wash](styles/ink-wash/STYLE.md) · 《The Swordsman and the River》: 侠客踏水过江，一剑断流。
- [油画厚涂 Impasto Oil Painting](styles/impasto/STYLE.md) · 《The Colour of Rain》: 灰色雨中广场，第一把红伞撑开，圆舞曲把整个广场刷上颜色。
- [一笔画 One-line Drawing](styles/one-line/STYLE.md) · 《The Line That Never Lifted》: 一根不离纸的线画完一个人的一生，再把笔交给孩子。
- [白板讲解 Whiteboard Explainer](styles/whiteboard/STYLE.md) · 《Einstein in Your Pocket》: 手机怎么知道你在哪：GPS、原子钟，和相对论每天多出的 38 微秒。
- [钢笔淡彩 Urban Sketch · Pen & Wash](styles/urban-sketch/STYLE.md) · 《Where the Wind Went》: 公园只是一张钢笔速写，风把草帽吹到哪里，哪里才有颜色。

**东方传统 · East Asian Traditions**

- [皮影戏 Shadow Puppetry](styles/shadow-puppet/STYLE.md) · 《Hou Yi Shoots the Suns》: 十日炙烤大地，后羿张弓射日。
- [浮世绘 Ukiyo-e](styles/ukiyoe/STYLE.md) · 《A Journey Toward the Mountain》: 旅人走向远山，每个镜头都是一幅版画，最后迎来一道巨浪。
- [红色窗花剪纸 Red Paper-cut](styles/papercut-red/STYLE.md) · 《Nian Comes to Town》: 除夕年兽进村，小女孩剪出的大窗花照亮全村，把它吓跑。
- [纸雕灯影 Paper-cut Lightbox](styles/paper-lantern/STYLE.md) · 《A Mooncake's Longing》: 一枚月饼讲中秋的团圆与思念，纸雕灯箱层层透光。

**印刷与版画 · Print & Printmaking**

- [Risograph 丝网印刷 Risograph Print](styles/risograph/STYLE.md) · 《Sunday Ride》: 周日早晨骑车穿过城市：面包店、公园、河边。
- [复古半调案卷 Halftone Dossier](styles/halftone-dossier/STYLE.md) · 《Case File: Chubby》: 橘猫胖橘被立案审查：测试重力、凌晨跑酷，最后无罪释放。
- [木刻版画 Woodcut Print](styles/woodcut/STYLE.md) · 《The Bell Founder》: 村子用一整个冬天铸一口钟，钟声第一次响起，雪停了。

**图形与排版 · Graphic & Type**

- [瑞士动态排版 Swiss Motion Graphics](styles/swiss-motion/STYLE.md) · 《Five Rules for a Poster》: 一张音乐会海报按瑞士设计的五条规则自己排版，第五条是只打破一条。
- [60s 间谍片头 60s Spy Title Sequence](styles/spy-titles/STYLE.md) · 《The Velvet Cipher》: 虚构 1964 年间谍片的片头：追一把被偷的钥匙，几何碎片最后拼成片名。
- [装饰艺术 Art Deco](styles/art-deco/STYLE.md) · 《Midnight at the Starlight Hotel》: 1930 年的大饭店，门童赶在午夜前把一封信送上顶楼。
- [蓝图 / 工程制图 Blueprint](styles/blueprint/STYLE.md) · 《Patent Pending: The Cloud Catcher》: 发明家的蓝图自己画出一台接云机器，修订云线变成了真的雨云。
- [彩色玻璃窗 Stained Glass](styles/stained-glass/STYLE.md) · 《The Dragon of the East Window》: 阳光从清晨移到黄昏，照到哪一格花窗，哪一格的故事就动起来。
- [象形运动图形 Pictogram Motion](styles/pictogram-motion/STYLE.md) · 《Aichi-Nagoya 2026 — All 43 Sports》: 2026 亚运会 43 个大项，几何象形人卡着节拍快闪。
- [ASCII / CRT 终端 ASCII / CRT Terminal](styles/ascii-crt/STYLE.md) · 《Tranquility.log》: 月球基地的 AI 沉睡 40 年后被唤醒，用字符画出“家”来回复。

**信息与发布 · Information & Keynote**

- [数据叙事 Data Storytelling](styles/dataviz/STYLE.md) · 《A Hundred Summers》: 一百年的夏季气温，图表本身就是故事。
- [等距信息图 Isometric Infographic](styles/iso-infographic/STYLE.md) · 《From Bean to Cup》: 一杯咖啡从种植园到你手里的旅程。
- [暗色科技发布 Dark Tech Keynote](styles/dark-keynote/STYLE.md) · 《Room to Think》: 虚构 app Tidy 的发布片：被埋掉的光标一键把几百个窗口归位。
- [活体实机录屏 Living Screencast](styles/living-screencast/STYLE.md) · 《Clawd Moves In》: 像素小人 Clawd 跳出终端、搬进 Claude 应用，在一镜到底的录屏里演示 Plan 模式、diff 评论和自检。

**卡通与动画 · Cartoon & Anime**

- [1930s 橡皮管卡通 1930s Rubber Hose Cartoon](styles/rubber-hose/STYLE.md) · 《Coffee Cup Chase》: 一只咖啡杯满厨房追一块逃跑的方糖。
- [80 年代赛璐璐动画 80s Cel Anime](styles/cel-anime-80s/STYLE.md) · 《City Lights, 1987》: 快递少女骑车穿过雨后霓虹都市，赶在黎明发射前送到一盘磁带。
- [科幻情景喜剧卡通 Sci-Fi Sitcom Toon](styles/scifi-toon/STYLE.md) · 《Coffee Run》: 厌世天才开传送门只想买杯咖啡，却穿过越来越离谱的平行宇宙。

**游戏 · Games**

- [16-bit 像素 RPG 16-bit Pixel RPG](styles/pixel-rpg/STYLE.md) · 《The Last Save Point》: 勇士在最终 Boss 门前存档，存档画面闪回一路冒险。
- [HD-2D](styles/hd-2d/STYLE.md) · 《The Lampbearer》: 灯塔熄灭，孙女提着最后一簇火穿过夜林、爬上风暴悬崖。
- [微游戏快闪（瓦里奥制造式） Microgame Frenzy](styles/microgame/STYLE.md) · 《Five-Second Astronaut》: 见习宇航员闯五秒训练营，越来越快，Boss 关亲手降落回地球。
- [综艺节奏扁平 Game Show Flat](styles/game-show/STYLE.md) · 《Rhythm of AI, 1997 → 2026》: 把 AI 发展史做成一局节奏游戏，模型踩着拍登场，最后发成绩单。

**电影与时代 · Cinema & Eras**

- [1920s 默片 1920s Silent Film](styles/silent-film/STYLE.md) · 《The Runaway Loaf》: 面包店学徒追一个滚走的面包，最后掰成两半分给饿肚子的小女孩。
- [后室 / 新怪谈 Liminal Found Footage](styles/backrooms/STYLE.md) · 《Night Shift Orientation》: 新夜班员工拍下入职第一晚：无尽的黄色办公空间，和墙上的员工守则。

**材质与 3D · Materials & 3D**

- [积木玩具 Brick Toy](styles/brick-toy/STYLE.md) · 《Rocket from Spare Parts》: 积木宇航员用零件拼出火箭，飞向积木月亮。
- [纸片立体书 Paper Pop-up Book](styles/paper-popup/STYLE.md) · 《Pip's Paper Adventure》: 立体书在书桌上打开，小精灵 Pip 在纸片世界冒险，最后跳出书外。
- [移轴微缩 Tilt-Shift Miniature](styles/tilt-shift/STYLE.md) · 《Toy Town Rush Hour》: 玩具城的早高峰，一切都像模型。
- [低多边形等距 Low-poly Isometric Island](styles/lowpoly-island/STYLE.md) · 《The Island That Grew》: 空海里一格格长出小岛和村庄，每放一块响一个音符，直到星空。
- [玻璃质感产品 Glass Product Render](styles/glass-product/STYLE.md) · 《Aura — Hear the Light》: 虚构玻璃耳机 Aura 的开箱与特写。
<!-- styles:end -->

## 署名与授权

**LemoLab × Claude Opus 5.5** 出品。代码采用 MIT；指南、`STYLE.md` 和成片采用 CC BY 4.0。第三方采样、字体、音乐沿用各自的授权（CC0、CC BY、OFL），逐条列在每个样片的 `CREDITS` 里。
