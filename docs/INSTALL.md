# 安装

## Codex

将整个目录复制到：

```text
~/.codex/skills/thai-tvc-director/
```

Windows 示例：

```powershell
Copy-Item -Recurse .\thai-tvc-director "$env:USERPROFILE/.codex/skills/thai-tvc-director"
python "$env:USERPROFILE/.codex/skills/thai-tvc-director/scripts/setup_check.py"
python "$env:USERPROFILE/.codex/skills/thai-tvc-director/scripts/validate_skill.py"
```

## 依赖

提示词、创意、剧本和分镜模式仅需要 Python 3.10+ 用于本地校验；Skill 本身不依赖第三方视频 API。

真正渲染视频属于运行环境能力。没有视频生成/剪辑工具时，应交付生产包，不假装已有成片。
