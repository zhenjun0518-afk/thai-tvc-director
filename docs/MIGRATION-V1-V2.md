# 从 V1 升级到 V2

V1：`thai-tvc-prompt-director.skill.md` 是单文件提示词型 Skill。

V2：`thai-tvc-director` 是仓库级 Skill。

## 主要变化

1. `SKILL.md` 只负责路由和核心规则。
2. 产品分析、泰式叙事、分镜、Prompt、声音和 QC 拆入 `references/`。
3. 新增 `quick / concepts / director / production` 四种交付模式。
4. 新增 Product Lock / Character Lock / 状态连续性。
5. 新增模型适配层。
6. 新增本地结构、故事和分镜校验脚本。
7. 保留 `spec/thai-tvc-director.skill.md` 作为 DZS-SDF 2.2 机器清单。
8. 明确“未真实生成并验证 MP4，不得声称成片完成”。

## ID 变化

旧：`thai-tvc-prompt-director`

新：`thai-tvc-director`

如已有旧 Skill，建议保留备份后用 V2 目录替换，不要让两个版本同时自动触发相同请求。
