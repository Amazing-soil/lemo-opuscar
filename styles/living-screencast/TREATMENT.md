# Living Screencast（活体实机录屏）— 风格与分镜

> 2026-09-26 用户认可方案（要求更多动效与导演技术）→ 已出成片 `living-screencast.mp4`（59.4 s）。下文是开工前的讨论稿；成片在此基础上加了：logo 象限像素化身、片名当落点、弹窗/消息当移动地面、4× 快进 + 焦点转移、聚光冻结、甩镜动态模糊、暗色揭示吞掉整部片、会话分裂、逐词跳字片尾。声线最终用 am_michael（其它声线把 Claude 读成 Clod）。

> 题材：Claude 应用里的 Claude Code 基础用法，主角 Clawd（Claude Code 的像素吉祥物），约 60 秒，英文。

## 风格：和现有 44 个风格的区别

- 不是 25 Dark Tech Keynote：那支是黑色舞台、虚构产品、抽象 UI。这支是浅色暖调的真实应用，每个按钮、菜单和快捷键都真实存在，已按官方桌面版文档核对。
- 不是像素游戏（29/30）：画面主体是高清矢量界面，只有 Clawd 和它的道具是像素。低分辨率的小家伙住在高分辨率的界面里，两种分辨率的反差就是这个风格的视觉识别点。

## 六条规则

1. **实机感，但全是 2D 重绘**：界面用 DOM 和 CSS 1:1 重绘，不贴截图，文字全部清晰可读。字体用 Inter、Newsreader 和 JetBrains Mono，均为 OFL 授权。
2. **镜头用录屏软件的语法**：只在"屏幕"里推拉摇，缩放始终 ≥1，不会拍到屏幕外。运动用弹簧缓动，光标带运动模糊，点击时轻推一下。
3. **Clawd 的像素网格**：18×10 的网格，由 Claude Code 终端 logo `▐▛███▜▌` 的象限字符 1:1 展开。像素硬边，随镜头一起放大。尘土、火花、铅笔、感叹号也用同一套网格。
4. **重力等于 UI 的上边缘**：Clawd 只站在界面元素的顶边上，比如输入框、菜单、文件行、diff 行和按钮。站位按真实元素的位置测量，不靠手摆。
5. **因果诚实**：用户的操作只由光标完成，画面里没有手。Claude 做的事由 Clawd 演出来，而且每个动作都对应一次真实的界面变化，例如读文件时那一行高亮，点预览时页面变暗。
6. **信息层**：按键 HUD（KeyCastr 式）显示快捷键，章节标签 01–04，字幕放在毛玻璃药丸里。

## 对标（只学语法）

| 对标 | 学什么 | 不学什么 |
|---|---|---|
| Screen Studio 式产品录屏 | 自动推近光标、光标平滑、点击推镜 | 它的 UI 和品牌 |
| Apple Guided Tour 教程片 | 真实界面加平静旁白，一句话讲一个功能 | 画面和配乐 |
| Duolingo / Headspace 吉祥物动效 | 角色在界面里表演，挤压拉伸 | 角色造型 |
| Arc（The Browser Company）发布片 | 俏皮的产品语气和剪辑节奏 | 素材 |

## 分镜（约 60 秒，104 BPM）

| # | 时间 | 画面 / Clawd | 旁白 / 字幕 |
|---|---|---|---|
| 1 | 0:00 | 终端里敲下 `claude`，logo 的方块字符"活"了，跳出终端，原处只剩虚线空位 | Meet Clawd. It used to live in your terminal… |
| 2 | 0:05 | Claude 应用窗口展开，Clawd 落在窗口顶边，出片名 | …now it lives right inside the Claude app. |
| 3 | 0:09 | **01 Just say it**：打字，出 @ 文件弹窗，Clawd 站在输入框上看 | Say what you want in plain words, and point at a file with @. |
| 4 | 0:14 | 文件面板里 Clawd 沿文件行跑过，读到的行高亮 | It reads your project before it touches a thing. |
| 5 | 0:19 | **02 Plan first**：按 ⇧⌘M 打开模式菜单，Clawd 站在菜单顶上看着选 Plan | Not sure yet? Switch to Plan mode. |
| 6 | 0:23 | Plan 面板，Clawd 用像素铅笔写下第 4 条，标着 No files changed | You get a clear plan, and nothing changes until you say go. |
| 7 | 0:29 | **03 Review**：弹出 `+24 −3` 统计条，Clawd 站在上面欢呼，光标点 Review | Every edit shows up as a diff. |
| 8 | 0:32 | Diff 视图，点第 6 行写评论，按 ⌘↵ 提交，Clawd 趴在评论框上读 | Click any line, leave a note… |
| 9 | 0:37 | 该行被改写，Clawd 头顶冒出"!"，文件统计变成 +13 | …and Claude revises it. |
| 10 | 0:42 | **04 Checks its own work**：预览面板，Clawd 踩下切换按钮，暗色从按钮处圆形扩散开，弹出截图提示 | Then it runs your app in the preview and clicks through it. |
| 11 | 0:50 | 按 ⌘N 开新会话，分屏里三个 Clawd 各干各的：PR 的 CI 通过、测试 50/50、新会话刚进来 | Start another session. They work side by side. |
| 12 | 0:56 | 片尾：Clawd 欢呼加标语，署名写"Unofficial fan film" | Say it. Plan it. Review it. Ship it. |

## 声音

- **配乐**：用"两种分辨率"做音乐。高清层是毛毡钢琴、拨奏贝斯、刷鼓和拍手。像素层是 Clawd 的方波主题，5 个音，只在它动作时出现。片尾两层合奏。
- **拟音**：真实的键盘声和触控板点击，面板滑动带一点风声。Clawd 的脚步是 8-bit 噪声，落地"噗"一声，不说话。
- **旁白**：Kokoro TTS。候选：`af_heart`（美式女声，偏亲切），或 `bm_george`（英式男声，沿用白板片）。

## 待讨论

1. 选的功能是：@ 提及和读代码、Plan 模式、diff 行评论、预览自检，收尾讲并行会话。备选：斜杠命令和 Skills、CLAUDE.md 记忆、PR 自动修复和自动合并、检查点回退。
2. 画面用了官方吉祥物，界面也和 Claude 应用高度相似，片尾署名写"Unofficial fan film"。这样可以吗？
3. 用哪个旁白声线。
4. 这个风格要不要登记进 STYLES.md？目前是独立文件夹，没有动任何清单。
