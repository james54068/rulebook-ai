# Cursor AI 編程助手使用指南

## 🚀 快速開始

### 方法一：使用快速開始腳本（推薦）

```bash
python quick_start.py
```

按照提示輸入您的項目路徑和選擇規則集即可。

### 方法二：手動安裝

```bash
# 1. 查看可用規則集
python src/manage_cursor_rules.py list-rules

# 2. 安裝規則到您的項目
python src/manage_cursor_rules.py install ~/path/to/your/project --rule-set light-spec

# 3. 將 .cursor/rules/ 添加到 .gitignore
echo ".cursor/rules/" >> ~/path/to/your/project/.gitignore
```

## 📁 安裝後的文件結構

```
your-project/
├── .cursor/rules/           # Cursor 規則文件（自動生成）
│   ├── 01-memory.mdc       # 項目記憶
│   ├── 02-error-documentation.mdc
│   ├── 03-lessons-learned.mdc
│   ├── 04-archiecture-understanding.mdc
│   ├── 05-directory-structure.mdc
│   ├── 06-rules_v1.mdc     # 主要規則
│   ├── 07-plan_v1.mdc      # 規劃工作流程
│   ├── 08-code_v1.mdc      # 編碼工作流程
│   └── 09-debug_v1.mdc     # 調試工作流程
├── project_rules/           # 項目規則源文件
├── memory/                  # 項目記憶庫
│   ├── docs/               # 項目文檔
│   └── tasks/              # 任務管理
└── .gitignore              # 已更新
```

## 💡 使用示例

### 1. 初始化項目記憶

在 Cursor 中輸入：
```
基於項目的自定義規則，初始化記憶庫文件 (docs/, tasks/)，根據項目的當前狀態或初始需求。
```

### 2. 規劃新功能

```
使用 @.cursor/rules/plan_v1.mdc 中定義的工作流程，為新的用戶配置文件功能制定計劃。
```

### 3. 實現功能

```
使用 @.cursor/rules/code_v1.mdc 中定義的工作流程，開發 updateUserProfile 函數。
```

### 4. 調試問題

```
使用 @.cursor/rules/debug_v1.mdc 中定義的工作流程，調試登錄功能中的錯誤。
```

## 🔧 自定義規則

### 修改規則

1. 編輯 `project_rules/` 目錄中的文件
2. 運行同步命令：
   ```bash
   python src/manage_cursor_rules.py sync ~/path/to/your/project
   ```

### 更新記憶庫

直接編輯 `memory/` 目錄中的文件：
- `memory/docs/product_requirement_docs.md` - 產品需求
- `memory/docs/architecture.md` - 系統架構
- `memory/docs/technical.md` - 技術規格
- `memory/tasks/tasks_plan.md` - 任務計劃
- `memory/tasks/active_context.md` - 當前上下文

## 📋 規則集說明

### Light-Spec (輕量級)
- ✅ 基本的開發工作流程
- ✅ 簡化的文檔結構
- ✅ 適合小型項目和快速原型

### Medium-Spec (中等)
- ✅ 更詳細的工作流程
- ✅ 完整的文檔系統
- ✅ 適合中型項目和團隊協作

### Heavy-Spec (完整)
- ✅ 最全面的工作流程
- ✅ 企業級文檔系統
- ✅ 適合大型複雜項目

## 🛠️ 管理命令

```bash
# 列出可用規則集
python src/manage_cursor_rules.py list-rules

# 安裝規則
python src/manage_cursor_rules.py install <項目路徑> --rule-set <規則集>

# 同步規則（重新生成）
python src/manage_cursor_rules.py sync <項目路徑>

# 清理規則（保留記憶庫）
python src/manage_cursor_rules.py clean-rules <項目路徑>

# 完全清理
python src/manage_cursor_rules.py clean-all <項目路徑>
```

## 🎯 最佳實踐

### 1. 項目記憶管理
- 定期更新 `memory/docs/` 中的文檔
- 在 `memory/tasks/active_context.md` 中記錄當前工作重點
- 使用 `memory/tasks/tasks_plan.md` 追蹤項目進度

### 2. 規則自定義
- 根據項目需求調整 `project_rules/` 中的規則
- 修改後記得運行 `sync` 命令
- 保持規則的簡潔和實用性

### 3. 版本控制
- 將 `memory/` 目錄提交到版本控制
- 將 `.cursor/rules/` 添加到 `.gitignore`
- 定期備份 `project_rules/` 目錄

## 🔍 故障排除

### 問題：Cursor 沒有使用新規則
**解決方案：**
1. 確認 `.cursor/rules/` 目錄存在
2. 重新啟動 Cursor
3. 檢查規則文件是否為 `.mdc` 格式

### 問題：規則同步失敗
**解決方案：**
1. 確認 `project_rules/` 目錄存在
2. 檢查文件權限
3. 重新運行 `install` 命令

### 問題：記憶庫文件丟失
**解決方案：**
1. 從版本控制恢復 `memory/` 目錄
2. 重新運行 `install` 命令
3. 手動恢復自定義內容

## 📚 更多資源

- 查看 `rule_sets/` 目錄了解不同規則集的詳細內容
- 查看 `memory_starters/` 目錄了解文檔模板
- 查看原始 README.md 了解完整功能

## 🤝 貢獻

如果您發現問題或有改進建議，請：
1. 檢查現有問題
2. 創建新的問題報告
3. 提交拉取請求

---

**享受使用 Cursor AI 編程助手！** 🎉




