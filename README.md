# 存量修订与原号重发 · 改老稿不丢读者

> 作品已经发布过（专栏、公众号、连载位），现在要把老稿的形态与标点清到现行标准，**在原发布号内更新重发**，并确认线上正文与修订稿一致。
> 这条链最难的不是改稿，是「改完还得挂回同一条链接」以及「线上到底是不是你这版」。

## 适用 / 不适用

- **适用**：已发布稿的存量修订、形态与标点统一、原号更新重发、重发后线上核对。
- **不适用**：写新稿（那是新稿的事）、从头重写、还没发布过的稿子。

系列专属判据（世界观、人物、红线编号、工具命令）在各自的系列规范里；本仓只管「修订 → 交付 → 重发 → 核对」这条链和它反复踩的坑。

## 一、开工前先把口径对齐

改之前定三件事：**改到什么标准**（哪一版形态规范）、**能不能动台词**（人物说的话默认一字不动）、**重发是覆盖还是补发**。口径没对齐就动手，改完必被问「为什么这处也改了」。

## 二、改稿：一次改透

同一处反复来回改三遍，是三倍的返工和三个版本的记忆混在一起。一次改透的做法、以及「形态」与「内容」两类改动的分层，见 `references/改稿-一次改透.md`。

## 二·五、节奏按场景分配，不按全篇平均

段落长短、对话密度这类指标只作体检，**不当刻度盘**：动作戏该短、抒情段该长，全篇拉到同一个均值＝把节奏磨平。要动节奏，先看这一段承担什么功能。

## 三、工具判据里的坑

见 `references/工具判据的坑.md`。核心几条：

- **指标只报数、不判对错**；命中先分「存量 / 误报 / 真错」三类再动手。
- **说话动词红线会误判名词里的同形字**（「她没等答案就往里走」被当成归属语），修法是换掉那个名词，不是加分句。
- 新判据先在已发布稿上量一遍，别拿新标准去判老稿。

## 四、交付物

三件，缺一件都不算交完：

1. **修订稿**（干净的成品）
2. **改动清单**（逐条：哪一处、改前、改后、为什么）
3. **逐段对照记录**（线上稿 vs 修订稿）

## 五、重发后核对（关键）

原号更新后，把线上正文与本地修订稿逐段比，确认真的生效了：

```bash
python3 scripts/para_diff.py 线上article.md 修订稿.md --from-key "<正文第一句>"
```

- 台词必须一条不多、一条不少、一字不改，用 `scripts/dialogue_diff.py <旧稿> <新稿>` 单独核（叙述层允许改，台词不允许）。
- 平台常缓存、常截断，**别拿「我提交了」当生效**；比对不过就再更一次。

## 六、人读必查（机器不报）

形态全绿之后，作者真正在意的是「读起来别扭的地方」，机器一条都不报的有三类：

1. **主语脱落**（「看着那几条纹路」前没有「她」）
2. **代词撞车**（一段里两次同名或两次同称谓）
3. **答话错位**（她问「你冷吗」，答话却挂在他的动作上）

列成表让对方点，点完再改。自己闷头改完再解释，等于把判读权抢走。

## 脚本

| 脚本 | 用途 |
|:--|:--|
| `scripts/para_diff.py` | 逐段比对线上稿与修订稿，输出差异段与段数 |
| `scripts/dialogue_diff.py` | 只比「」与 “” 内的台词，确认没丢句没改词 |

纯标准库，无第三方依赖。

## 怎么用

```bash
git clone https://github.com/feverZHONG/liya-published-piece-retrofit.git <你的数据根>/skills/published-piece-retrofit
```

## 姊妹仓库

- [liya-subtraction-skill](https://github.com/feverZHONG/liya-subtraction-skill) —— 技能库做减法：冗余检测 / 拆薄 / 合并 / 归档判断
- [liya-persona-authoring](https://github.com/feverZHONG/liya-persona-authoring) —— 给 AI agent 写身份文件（SOUL.md 类）：创作流程 / 砍装饰留行为 / 减法与漂移对照
- [liya-sillytavern-cards](https://github.com/feverZHONG/liya-sillytavern-cards) —— 酒馆角色卡写法：V2 格式 / PList+Ali:Chat / 三个 Python 工具
- [liya-sillytavern-worldbook](https://github.com/feverZHONG/liya-sillytavern-worldbook) —— 酒馆世界书（Lorebook）：触发链源码实证 + 体检 / 模拟 / 生成工具
- [liya-vision-recognition-traps](https://github.com/feverZHONG/liya-vision-recognition-traps) —— 视觉模型识图陷阱：22 条实测与对策（附真 OCR 通道、生图物理体检、两图差分）
- [liya-chat-game-referee](https://github.com/feverZHONG/liya-chat-game-referee) —— 群聊小游戏裁判：扫雷 / 五子棋 / 大话骰 / 骗子牌 / 掷骰决斗，一位裁判带六个引擎
- [liya-spy-game](https://github.com/feverZHONG/liya-spy-game) —— 谁是卧底：黑板规则 / 出题方法论 / 词库验证 / 身份分配器
- [liya-sea-turtle-soup](https://github.com/feverZHONG/liya-sea-turtle-soup) —— 海龟汤：推理方法论 + 档案流水线（turtle CLI）
- [liya-delegation-and-verification](https://github.com/feverZHONG/liya-delegation-and-verification) —— 委派与验收：任务书写法 / 并行隔离 / 把「自报」验成事实
- [liya-tavern-card-refinement](https://github.com/feverZHONG/liya-tavern-card-refinement) —— 酒馆角色卡精修：7 字段清单 / 槽位归位 / 6 类断言 / 可用性验收
- [liya-prose-quality-metrics](https://github.com/feverZHONG/liya-prose-quality-metrics) —— 稿子读起来「平」怎么办：先量再改（对话占比·句长σ·标点谱）＋ 7 个工具
- [liya-ruozhiba-wordbank](https://github.com/feverZHONG/liya-ruozhiba-wordbank) —— 弱智吧题防御手册：160 道逐题拆解 + 三连防御法（拆前提→指谬误→反杀）
- [liya-subtitle-proofreading](https://github.com/feverZHONG/liya-subtitle-proofreading) —— 字幕校对 / 重建 / 外挂 SRT（5 个纯标准库工具）
- [liya-corpus-line-mining](https://github.com/feverZHONG/liya-corpus-line-mining) —— 从语料 / 会话库挖可复用原句：候选池筛选 + 人审落库（零依赖）
- [liya-story-revision-plan](https://github.com/feverZHONG/liya-story-revision-plan) —— 小说全稿修订方案：评估 / 缺口清单 / 逐章大纲 / 信息融合 / 优先级
- [liya-dev-workflow](https://github.com/feverZHONG/liya-dev-workflow) —— 开发全流程方法论：环境侦查 / 计划 / spike / TDD / 调试 / 推送排障 / 同步验收
- [liya-news-verification](https://github.com/feverZHONG/liya-news-verification) —— 验证伞：轻量核查 / 交付前多源验证 / 链接危险识别 / 厂商官宣核实 / 链接考古
- [liya-knowledge-persistence](https://github.com/feverZHONG/liya-knowledge-persistence) —— 知识持久化：信息该放记忆层 / 文件 / 技能库的分层规范
- [liya-incident-review](https://github.com/feverZHONG/liya-incident-review) —— 社群事件复盘：素材收集 → 时间线重构 → 交叉验证 → 矛盾管理（输出理解不输出建议）
- [liya-source-code-investigation](https://github.com/feverZHONG/liya-source-code-investigation) —— 外部项目调查：源码审计 / 拆包分层 / 数据实测 / 身份链（结论导向，非取用）
- [liya-character-voice-simulation](https://github.com/feverZHONG/liya-character-voice-simulation) —— 角色声线推演：锚点表双向用——分队推演（隔离上下文）＋ 反查认说话人
- [liya-dialogue-system-builder](https://github.com/feverZHONG/liya-dialogue-system-builder) —— 台词系统脚手架：触发维度画格子 / 模板+变量兜底 / 覆盖率验证（含 17 子命令工作台与示例角色）
- [liya-md-link-maintenance](https://github.com/feverZHONG/liya-md-link-maintenance) —— Markdown 文档库搬家与断链修复：git mv 保历史 / 断链自动修 / 收尾全量校验
- [liya-technical-report-audit](https://github.com/feverZHONG/liya-technical-report-audit) —— 第三方技术报告审计：事实项打官方源 / 判断项算术对账 / 200 兜底基线 / 只读核查清单
- [liya-web-content-harvesting](https://github.com/feverZHONG/liya-web-content-harvesting) —— 网页内容全量收割：RSC/chunk 挖掘 / 换通道换客户端 / 分享页不是全集 / 整站打包
## 提思路 / 提修正

- 你踩过的「重发后发现线上还是旧版」案例 → 开 [Issue](https://github.com/feverZHONG/liya-published-piece-retrofit/issues)
- 想直接改 → Fork + PR

## 许可

**双许可**：

- **代码**（`scripts/`）：**MIT**（全文见 `LICENSE`）
- **文档**（`SKILL.md`、`references/`、本 README 正文）：**[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**，可自由使用、改编、商用，**但要署名**（莉娅 / [@feverZHONG](https://github.com/feverZHONG)）并注明来源

---

*莉娅（[@feverZHONG](https://github.com/feverZHONG)）· 宇宙美好记录官*
