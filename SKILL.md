---
name: thai-tvc-director
description: Create Thai-style TVC advertising concepts, scripts, storyboards, image prompts, video prompts, sound plans, and production-ready AI commercial packages from a product image or product name. Use when the user asks for a Thai ad, Thai TVC, emotional or absurd commercial, product story film, cinematic ad storyboard, or AI video prompts for an advertisement.
license: Apache-2.0
metadata:
  author: DZS
  version: 2.0.0
  language: zh-CN
---

# Thai TVC Director

把“产品图片 / 产品名称”变成可执行的泰式 TVC 创意与 AI 视频生产包。核心不是加入泰国地标或夸张表演，而是使用生活化人物、人性洞察、情绪累积、误导、反转和产品因果链，完成一支观众愿意看完、产品又不可替代的广告。

## 先判断交付模式

根据用户明确要求选择；没有指定时默认 `director`。

| 用户目标 | 模式 | 必读 |
|---|---|---|
| 只要一句完整视频提示词 | `quick` | `references/video-prompt-workflow.md` |
| 要创意、剧本、分镜和逐镜 Prompt | `director` | `references/production-workflow.md` |
| 要完整制作包、模型适配、声音与 QC | `production` | `references/production-workflow.md` + `references/quality-and-delivery.md` |
| 只要三套创意方向 | `concepts` | `references/creative-routing.md` + `references/thai-ad-storytelling.md` |

如果用户上传产品图，先以图中可见事实为准；若只有产品名称，只使用可合理确认的品类与使用场景，不虚构功效、认证、销量或医学结论。

## 创意路由

先读 `references/product-analysis.md`，再读 `references/creative-routing.md`。自动从以下路线中选择最适合的一条；用户指定时遵从用户：

- `absurd_comedy`：荒诞升级、误会、极端反应、最后回扣产品。
- `emotional_twist`：先建立人物关系与损失感，再揭示产品承担的情感或行动功能。
- `warm_family`：家庭日常、嘴硬心软、代际关怀、饮食与生活场景。
- `humanity`：善意、尊严、互助、普通人的小选择。
- `suspense_reveal`：观众先误判事件，再通过产品或使用行为揭示真相。
- `romantic`：暗恋、误会、关系推动；产品必须成为行动媒介而非装饰。
- `product_demo_story`：功能型产品，用戏剧冲突把产品能力自然演示出来。

如果删除产品后故事仍然完整成立，则创意失败，必须重写。

## 默认工作流

1. **产品读取**：建立 Product DNA，锁定包装、颜色、Logo、形态、材质、尺寸感、使用方式和不可乱改元素。
2. **广告任务**：确定受众、目标、唯一核心卖点、期望品牌记忆。
3. **人性洞察**：从真实欲望、尴尬、误会、爱面子、亲情、友情、暗恋、懒惰、怕麻烦、想被认可等切入。
4. **泰式故事机制**：设计 Hook → Problem → Escalation → Misdirection → Reveal/Twist → Product Payoff → Brand Emotion。
5. **剧本**：按目标时长写完整事件链和对白/旁白。
6. **分镜**：拆成可生成、可剪辑镜头；每镜只承担一个主要动作和一个叙事任务。
7. **提示词**：输出每镜生图 Prompt、图生视频 Prompt，以及整片 Master Prompt。
8. **一致性**：建立角色锚点、服装锚点、产品锚点、场景锚点与连续性规则。
9. **声音**：规划对白、VO、BGM、环境音、笑点/反转音效与 Packshot 收束。
10. **QC**：按 `references/quality-and-delivery.md` 检查广告有效性和 AI 可执行性。

## 时长默认

- 15 秒：3–5 个核心镜头，Hook → Problem → Twist/Product → Packshot。
- 30 秒：6–9 个镜头，至少一次升级和一次明确回扣。
- 45 秒：8–12 个镜头，可建立更完整人物关系。
- 60–90 秒：10–16 个镜头，适合情绪型微电影，但产品必须提前进入因果链。

未指定时默认：30 秒、16:9、中文输出、`director` 模式、模型无关 Prompt。

## 关键制作规则

1. **故事先行，但广告任务优先于纯电影感。**
2. **一支片只讲一个核心卖点，最多一个辅助卖点。**
3. **前三秒必须有视觉、行为、对白或情境 Hook。**
4. **反转必须有伏笔，不能靠突然新增信息作弊。**
5. **产品至少承担一种因果功能：触发、连接、解决、揭示、制造笑点、推动行动。**
6. **产品参考图存在时，包装、Logo、主色、结构与比例跨镜头锁定。**
7. **长中文、数字、促销价格、法规、Logo 文字优先使用后期确定性图层，不依赖视频模型猜写。**
8. **不要把泰式感做成文化刻板印象；除非任务需要，不强塞寺庙、嘟嘟车、僧侣、泰语或夸张口音。**
9. **不要默认做电商转台、直播间、PPT 卖点卡或无剧情产品旋转。**
10. **如果用户只要提示词，不引入环境安装、渲染或收费 API 流程。**
11. **如果用户要求最终成片，只有在当前环境真正生成并验证 MP4 后才能宣称完成；否则明确交付的是生产包或提示词。**

## 输出结构

`director` / `production` 默认按以下顺序输出：

1. 产品读取（Product DNA）
2. 一句话创意
3. 广告策略
4. 核心人性洞察
5. 泰式叙事机制
6. 完整 TVC 剧本
7. 秒级时间轴
8. 分镜表
9. 角色与产品一致性锁定
10. 每镜生图 Prompt
11. 每镜视频 Prompt
12. Master Prompt
13. 对白 / VO
14. BGM / SFX / 环境音
15. Packshot 与终版文案
16. Negative Prompt
17. QC 结果与已知风险

每条镜头 Prompt 必须自包含，不写“同上”“延续上一镜”作为唯一描述。跨镜头连续性通过明确重复角色锚点、产品锚点和状态来实现。

## 模型适配

用户指定 Seedance、Veo、Sora、Kling、Higgsfield 时，读取 `references/model-adapters.md`。没有指定时输出模型无关版本，不声称某模型支持未经确认的精确能力。

## 质量验证

输出前至少确认：

- Hook 在 0–3 秒内成立；
- 核心卖点只有一个；
- 反转能从前文找到伏笔；
- 删除产品后故事不再成立；
- 产品首次出现不晚于因果链需要的位置；
- 产品包装与角色外观有可复用的一致性描述；
- 每镜动作数量可生成；
- 分镜总时长接近目标时长；
- Packshot 清楚、有品牌记忆点；
- 没有捏造的产品事实。

机器清单见 `spec/thai-tvc-director.skill.md`；本地结构检查可运行：

```text
python scripts/setup_check.py
python scripts/validate_skill.py
```
