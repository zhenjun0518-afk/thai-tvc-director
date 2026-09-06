# Thai TVC Director

一个面向 AI 视频生产的泰国广告片 Skill。输入产品图片或产品名称，自动完成产品理解、人性洞察、泰式广告创意、剧本、时间轴、分镜、生图提示词、视频提示词、声音设计、产品一致性锁定与质量检查。

## 核心原则

- 泰式广告感来自普通人物、人性洞察、升级、误导与合理反转，而不是地标、口音或文化符号堆砌。
- 产品必须进入故事因果链。删除产品后故事若仍完全成立，则创意必须重写。
- 一支广告默认只讲一个核心卖点。
- 产品参考图存在时，包装结构、主色、Logo位置、比例和关键文字必须跨镜头锁定。
- 先做能执行的广告，再追求复杂电影感。

## 使用方式

最简单的输入：

```text
使用 $thai-tvc-director，用这张饮料产品图做一支30秒泰式搞笑反转广告，16:9，输出Seedance逐镜视频提示词。
```

或者：

```text
使用 $thai-tvc-director，产品是护手霜，做45秒泰式温情反转TVC。先给3套创意，选最佳方案后输出剧本、分镜、生图Prompt和视频Prompt。
```

## 输出模式

- `quick`：一句话创意 + 完整视频提示词。
- `concepts`：3套明显不同的广告创意方向。
- `director`：产品分析 → 策略 → 创意 → 剧本 → 分镜 → 生图/视频提示词。
- `production`：在 director 基础上增加模型适配、产品锁定、声音设计、Packshot、Negative Prompt 与 QC。

## 项目结构

```text
thai-tvc-director/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── LICENSE
├── config/
├── docs/
├── examples/
├── legacy/
├── references/
├── scripts/
└── spec/
```

## 安装

### Codex / Skills 目录

```bash
git clone https://github.com/zhenjun0518-afk/thai-tvc-director.git ~/.codex/skills/thai-tvc-director
python ~/.codex/skills/thai-tvc-director/scripts/setup_check.py
```

Windows PowerShell：

```powershell
git clone https://github.com/zhenjun0518-afk/thai-tvc-director.git "$env:USERPROFILE/.codex/skills/thai-tvc-director"
python "$env:USERPROFILE/.codex/skills/thai-tvc-director/scripts/setup_check.py"
```

## DZS-SDF

`spec/thai-tvc-director.skill.md` 提供 DZS-SDF 2.2 机器定义，用于参数、执行图和质量策略解析。

## 版本

当前：**2.0.0**

详见 `CHANGELOG.md`。
