# Geographic Documentary Master Photography

一个面向 Codex / AI 图像提示词工作流的原创“世界级地理纪实摄影”Skill。

它吸收了高水平纪实摄影、地理摄影、自然摄影、野生动物摄影、人文地理与旅行报道的共同方法，同时借鉴了 `vibeshot-candid-photography` 中非常有效的变量池、锁定条件、批次差异和自然语言 Prompt 生成机制，并融合了成年虚构角色真人化、公开空间观察式抓拍、长焦/手机/反射/遮挡机位与“被发现镜头”等系统。

> 本项目不代表、隶属于或复制 National Geographic。这里的“国家地理级”仅描述专业目标：强烈地方感、现场真实性、叙事性、自然光、地理/生态逻辑与编辑级摄影质量。

## 默认行为

- 不指定数量时默认生成 10 组专题摄影提示词。
- 指定数量时严格按用户数量输出。
- 只输入地点、动物、人物或角色名也可以自动补全。

## 核心能力

- 风光与地貌
- 野生动物
- 人文地理
- 旅行纪实
- 探险与科考
- 城市地理
- 航拍
- 水下
- 微距与生态细节
- 夜间与极端天气
- 公开空间中的自然抓拍/观察式人物摄影

## 与普通摄影 Prompt 的区别

普通 Prompt 常常追求：漂亮、壮观、黄金时刻、完美主体。

本 Skill 优先追求：

1. 地点是否可信、可辨识
2. 主体与环境是否有关系
3. 画面是否包含一个清晰故事
4. 镜头和机位是否服务于故事
5. 光线和天气是否真实
6. 是否有足够的空间层次
7. 是否避免 AI 模板感

## 安装

```bash
mkdir -p ~/.codex/skills
cp -R geographic-documentary-master-photography ~/.codex/skills/
```

新的 Codex 对话中调用：

```text
使用 $geographic-documentary-master-photography，冰岛火山公路 n=10，3:2。
```

## 常用输入

```text
使用 $geographic-documentary-master-photography，喜马拉雅牧民 n=10，3:2。
```

```text
使用 $geographic-documentary-master-photography，亚马逊雨林美洲豹，600mm，暴雨后，低机位，只给提示词。
```

```text
使用 $geographic-documentary-master-photography，冰岛黑沙滩，风暴，16:9，人物小比例大环境。
```

```text
使用 $geographic-documentary-master-photography，东京雨夜通勤人群，35mm纪实摄影，n=6。
```

## n=10

`n=10` 不会只是换背景。Skill 会主动拉开：

- 焦段
- 机位
- 景别
- 前景
- 动作
- 光线
- 空间尺度
- 天气表现
- 叙事重点

最终像一个摄影师完成的 10 张专题组照。

## 设计来源

结构上参考了 Vibeshot Candid Photography 的几个成熟机制：

- 可锁定用户条件
- 其余变量继续设计/随机
- 多组输出主动去重
- 用完整自然语言 Prompt 而非机械字段输出
- 强调非常规机位、空间遮挡和真实摄影状态

在此基础上扩展为完整的地理摄影体系，并增加：地理真实性、生态合理性、人文伦理、天气系统、野生动物行为、探险叙事、航拍地图关系与反AI模板规则。
