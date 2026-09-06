# 产品与角色一致性

## Product Lock

从 Product DNA 生成固定字符串，所有关键产品镜头重复使用：

```text
PRODUCT LOCK:
[品类]，[包装形态]，[主色/辅色]，[材质]，[Logo/标签位置]，[瓶盖/开口/结构]，[尺寸感]。
Preserve exact package silhouette, color blocking, label placement, material, proportions and cap structure across every shot.
```

## Character Lock

```text
CHARACTER LOCK:
年龄段、性别呈现、脸型、发型、肤色、体型、服装上衣、下装、鞋、标志性配饰、表演气质。
```

角色锚点应稳定但不过度细化到容易让模型冲突的几十项小特征。

## 状态连续性

额外记录：

- 产品是否密封/打开；
- 液位或内容物状态；
- 是否已使用；
- 人物手里拿产品的左右手；
- 产品是否沾水/污渍/冷凝；
- 道具损坏或移动状态。

## 精确文字

品牌名、价格、促销、二维码、法规、长中文和关键数字若必须准确：

1. 生图/视频时保持标签区域干净或使用参考资产；
2. 后期用确定性文字/Logo 层叠加；
3. 不宣称视频模型能可靠生成像素级文字。
