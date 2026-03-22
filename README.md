# Manual.docx 网站生成

本目录提供一个脚本：把 `Manual.docx` 自动转换成 `mkdocs` 可直接发布的文档网站（包含章节页、目录页，并尽量抽取图片）。

## 生成

在当前目录运行：

```powershell
python scripts/generate_manual_site.py --clean-manual
```

生成后会得到：

- `docs/manual/`：自动生成的 markdown 页面和图片资源
- `mkdocs.yml`：默认不会被脚本覆盖（建议你手工维护导航，符合方案 A）

## 预览

```powershell
python -m mkdocs serve
```

用浏览器打开输出的本地地址即可。

## 发布

```powershell
python -m mkdocs build
```

构建产物在 `site/` 目录。

