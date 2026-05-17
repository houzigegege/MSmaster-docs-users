# Manual.docx 网站生成

本目录提供一个脚本：把 `Manual.docx` 自动转换成 `mkdocs` 可直接发布的文档网站（包含章节页、目录页，并尽量抽取图片）。

**线上地址：** [https://houzigegege.github.io/MSmaster-docs-users/](https://houzigegege.github.io/MSmaster-docs-users/)

## 生成

在项目根目录（本 README 所在目录）运行：

```powershell
python scripts/generate_manual_site.py --clean-manual
```

生成后会得到：

- `docs/manual/`：自动生成的 markdown 页面和图片资源
- `mkdocs.yml`：默认不会被脚本覆盖（建议你手工维护导航）

> 不要手改 `docs/manual/` 里的内容；下次运行 `--clean-manual` 会被覆盖。首页、样式等请改 `docs/index.md`、`overrides.css` 等。

## 预览（可选）

```powershell
python -m mkdocs serve
```

用浏览器打开终端里提示的本地地址，确认章节与图片无误后再发布。

本地仅构建、不上传时：

```powershell
python -m mkdocs build
```

构建产物在 `site/` 目录（GitHub Pages 由 Actions 自动构建，一般不必手动上传 `site/`）。

---

## 更新 Manual.docx 后，如何重新发布到线上

每次改完 Word 手册并希望 [https://houzigegege.github.io/MSmaster-docs-users/](https://houzigegege.github.io/MSmaster-docs-users/) 同步更新时，按下面做即可。

### 1. 保存 Word 并重新生成网页内容

1. 将更新后的 **`Manual.docx`** 放在项目根目录（覆盖旧文件）。
2. 在项目根目录打开 PowerShell，执行：

   ```powershell
   cd "D:\1_DATA\博士后资料\18 MSMaster\05 website"
   python scripts/generate_manual_site.py --clean-manual
   ```

### 2. 用 GitHub Desktop 推到 GitHub

1. 打开 **GitHub Desktop**，选中本仓库 **`MSmaster-docs-users`**。
2. 左侧 **Changes** 中应出现 `docs/manual/` 等变更。
3. 左下角 **Summary** 填写说明（例如 `update manual from Manual.docx`）。
4. 点击 **Commit to main**，再点击 **Push origin**（或 **Fetch origin** 旁的推送按钮）。

### 3. 等待自动部署完成

1. 浏览器打开仓库：**https://github.com/houzigegege/MSmaster-docs-users**
2. 进入 **Actions**，等待 **Deploy MkDocs to GitHub Pages** 出现 **绿色勾**（通常 1～3 分钟）。
3. 部署成功后，刷新线上站点：  
   **https://houzigegege.github.io/MSmaster-docs-users/**  
   （若未立刻更新，可等 1～2 分钟或强制刷新浏览器缓存。）

### 说明

- 线上网站由 **GitHub Actions** 根据 `main` 分支自动构建，无需把 `site/` 文件夹手动上传到 GitHub。
- 若还修改了 **`mkdocs.yml`**（例如 `site_url`、导航），同样需要 **Commit + Push** 后才会生效。
- 仓库需为 **Public**，且 **Settings → Pages** 已选择 **`gh-pages`** 分支、`/(root)`（首次部署时配置一次即可）。
