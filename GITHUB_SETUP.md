# GitHub 仓库设置指南

## 快速开始

本项目已创建本地Git仓库，要发布到GitHub，请按以下步骤操作：

### 1. 在GitHub创建新仓库

访问 https://github.com/new 创建新仓库：
- 仓库名：`xiyouhouji` (西游后记的拼音)
- 描述：取经归来五百年，三界风云再起。师徒重聚踏新程，再续西游传奇。
- 选择 "Public" (公开)
- 不要初始化README（本地已有）

### 2. 连接本地仓库到GitHub

```bash
# 添加远程仓库（将YOUR_USERNAME替换为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/xiyouhouji.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 3. 验证发布

访问 `https://github.com/YOUR_USERNAME/xiyouhouji` 查看仓库是否成功发布。

---

## 自动更新设置

本项目配置了GitHub Actions，每天晚上8点自动更新：

### 启用GitHub Actions

1. 在GitHub仓库页面，点击 "Actions" 标签
2. 如果看到提示 "Workflows aren't being run on this forked repository"，点击 "I understand my workflows, go ahead and enable them"
3. 工作流已启用，每天晚上8点会自动运行

### 手动触发更新

也可以手动触发更新：
1. 进入GitHub仓库的 "Actions" 标签
2. 选择 "Daily Chapter Update" 工作流
3. 点击 "Run workflow" 按钮

---

## 项目结构

```
西游后记/
├── README.md              # 项目说明
├── GITHUB_SETUP.md        # GitHub设置指南（本文件）
├── .github/
│   └── workflows/
│       └── daily-update.yml  # 自动更新工作流
└── chapters/              # 章节目录
    ├── chapter01.md       # 第一回
    ├── chapter02.md       # 第二回（待更新）
    └── ...
```

---

## 更新计划

- ✅ 第一回：已发布
- ⏳ 第二回：待更新
- ⏳ 第三回：待更新
- ...

每天晚上8点更新一回新章节！

---

## 参与贡献

欢迎提出建议、讨论剧情走向，或者提交PR修复错别字！

---

*最后更新：2026年2月3日*
