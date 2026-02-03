#!/bin/bash
# 推送到GitHub脚本

GITHUB_REPO="https://github.com/zhanglunet/xiyouhouji.git"

echo "========================================"
echo "🚀 推送到GitHub: zhanglunet/xiyouhouji"
echo "========================================"
echo ""

# 检查git
cd /root/.openclaw/workspace/西游后记

# 设置远程仓库
git remote remove origin 2>/dev/null
git remote add origin $GITHUB_REPO

# 检查状态
echo "📋 当前状态:"
git status

echo ""
echo "========================================"
echo "📤 准备推送..."
echo "========================================"

# 推送
git branch -M main
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "✅ 推送成功!"
    echo "========================================"
    echo ""
    echo "📍 仓库地址: https://github.com/zhanglunet/xiyouhouji"
    echo ""
else
    echo ""
    echo "========================================"
    echo "❌ 推送失败!"
    echo "========================================"
    echo ""
    echo "可能需要GitHub Token认证"
fi
