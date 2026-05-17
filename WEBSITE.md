# 文档网站构建与发布（维护者说明）

本文件说明如何从 `Manual.docx` 生成 MkDocs 站点、发布到 GitHub Pages，以及如何通过 Releases 分发安装包。  
仓库首页面向用户的介绍见 **[README.md](README.md)**。

**线上文档：** [https://houzigegege.github.io/MSmaster-docs-users/](https://houzigegege.github.io/MSmaster-docs-users/)

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

---

## 在 MSmaster-docs-users 发布安装包（GitHub Releases）

安装包约 **1GB**，**不要**用 Git 提交进仓库（会超限、拖慢克隆）。应使用 **Releases** 单独托管安装文件，文档里只放下载链接。

仓库地址：**https://github.com/houzigegege/MSmaster-docs-users**

### 发布前准备

1. 安装包文件名建议带版本，例如：`MSmaster-1.0.0-win64.zip`（或 `.7z`、`.exe`）。
2. 单文件需 **小于 2GB**（GitHub Release 附件上限）。
3. 网络稳定；1GB 上传可能需要 **十几到几十分钟**。

### 第一次发布（网页操作，推荐小白）

#### 1. 打开 Releases 页面

浏览器打开：

**https://github.com/houzigegege/MSmaster-docs-users/releases**

点击 **「Create a new release」**（创建新发行版）。

#### 2. 填写版本信息

| 字段 | 建议填写 |
|------|----------|
| **Choose a tag** | 输入 `v1.0.0`，选 **「Create new tag: v1.0.0 on publish」** |
| **Target** | 保持 **`main`** |
| **Release title** | 例如 `MSmaster v1.0.0 (Windows)` |
| **Describe this release** | 写更新说明：系统要求、解压方式、已知问题等 |

#### 3. 上传安装包

在 **「Attach binaries by dropping them here or selecting them」** 区域：

- 把本地的 **安装包文件拖进去**，或点选文件；  
- 等待上传进度到 **100%**（不要关页面）。

可一次上传多个文件（例如 `.zip` + `SHA256.txt` 校验文件）。

#### 4. 发布

- **不要**勾选 **「Set as a pre-release」**（除非这是测试版）。  
- 点击 **「Publish release」**（发布发行版）。

#### 5. 复制直链（给手册用）

发布成功后，在 Release 页面 **Assets** 里，**右键**安装包文件名 → **复制链接地址**。

链接格式类似：

```text
https://github.com/houzigegege/MSmaster-docs-users/releases/download/v1.0.0/MSmaster-1.0.0-win64.zip
```

说明：

- `v1.0.0` 是 **标签名（tag）**  
- 最后一段是 **你上传时的文件名**（必须完全一致）

把该链接写进 **`Manual.docx` 的 Install 章节**（或首页），再运行 `generate_manual_site.py --clean-manual` 并 Push，用户即可从 [文档站](https://houzigegege.github.io/MSmaster-docs-users/) 点过去下载。

**Install 页 Markdown 示例（写在 Word 里，生成后会进 section_02）：**

```markdown
### Download (GitHub Release)

- **Version:** v1.0.0  
- **Size:** ~1.0 GB  
- **Windows:** [MSmaster-1.0.0-win64.zip](https://github.com/houzigegege/MSmaster-docs-users/releases/download/v1.0.0/MSmaster-1.0.0-win64.zip)
```

### 发布新版本（例如 v1.0.1）

1. 再次打开 **Releases** → **「Draft a new release」**。  
2. 新标签填 **`v1.0.1`**，上传新安装包。  
3. **Publish**。  
4. 更新 `Manual.docx` 里的版本号与链接，重新生成并 Push 文档。

旧版本 Release **可保留**，方便用户下载历史版本。

### 修改已发布版本（补传文件）

1. 打开对应 Release（例如 `v1.0.0`）。  
2. 右上角 **「Edit release」**。  
3. 在 Assets 区继续拖入文件，或删除错误文件后重传。  
4. **「Update release」** 保存。

### 可选：用命令行上传（网页太慢时）

需先安装 [GitHub CLI](https://cli.github.com/) 并登录 `gh auth login`。

```powershell
cd "D:\path\to\your\installer\folder"
gh release create v1.0.0 "D:\path\to\MSmaster-1.0.0-win64.zip" `
  --repo houzigegege/MSmaster-docs-users `
  --title "MSmaster v1.0.0 (Windows)" `
  --notes "Windows 10/11 64-bit. Extract and run MSmaster.exe"
```

### 常见问题

| 问题 | 处理 |
|------|------|
| 网页上传失败/中断 | 换网络重试，或用 `gh release create`；可先把包打成 `.7z` 略减小体积 |
| 链接 404 | 检查 tag 名、文件名是否与 Release 里完全一致 |
| 国内下载很慢 | 可额外提供网盘链接写在 Install 章，Release 作国际备用 |
| 不想把安装包放进 Git 历史 | 只用 Releases，**不要** `git add` 安装包 |

### 与文档站的关系

| 内容 | 放在哪 |
|------|--------|
| 安装包 ~1GB | **Releases → Assets** |
| 使用手册网页 | **main 分支** → Actions → GitHub Pages |
| 下载按钮/说明 | **`Manual.docx`** → 生成 `docs/manual/section_02.md` |
