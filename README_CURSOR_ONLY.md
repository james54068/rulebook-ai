# Cursor AI 編程助手規則模板

這是一個專門為 Cursor AI 編程助手設計的規則模板，提供結構化的開發工作流程和項目記憶系統。

## 🎯 主要功能

1. **結構化工作流程** - 定義規劃、實現、調試的標準流程
2. **項目記憶系統** - 持久化的項目文檔和上下文
3. **最佳實踐整合** - 基於軟體工程原則的開發指導
4. **快速設置** - 預配置的規則和文檔模板

## 📁 項目結構

```
cursor-rules-template/
├── rule_sets/                    # 預定義規則集
│   ├── light-spec/              # 輕量級規則集
│   ├── medium-spec/             # 中等規則集
│   └── heavy-spec/              # 完整規則集
├── memory_starters/             # 記憶庫起始文檔
│   ├── docs/                    # 文檔模板
│   └── tasks/                   # 任務模板
├── src/                         # 管理腳本
│   └── manage_rules.py          # 規則管理工具
└── README_CURSOR_ONLY.md        # 本文件
```

## 🚀 快速開始

### 1. 環境設置

```bash
# 創建 Python 環境
conda create -n cursor_rules python=3.11 -y
conda activate cursor_rules

# 安裝依賴
pip install -r requirements.txt
```

### 2. 查看可用規則集

```bash
python src/manage_rules.py list-rules
```

### 3. 安裝規則到您的項目

```bash
# 使用預設的 light-spec 規則集
python src/manage_rules.py install ~/path/to/your/project

# 或指定特定規則集
python src/manage_rules.py install ~/path/to/your/project --rule-set heavy-spec
```

### 4. 同步規則（如果需要修改）

```bash
python src/manage_rules.py sync ~/path/to/your/project
```

## 📋 Cursor 規則文件結構

安裝後，您的項目將包含以下 Cursor 規則文件：

```
.cursor/rules/
├── 01-memory.mdc              # 項目記憶和文檔
├── 02-error-documentation.mdc # 錯誤文檔
├── 03-lessons-learned.mdc     # 經驗教訓
├── 04-archiecture-understanding.mdc # 架構理解
├── 05-directory-structure.mdc # 目錄結構
├── 06-rules_v1.mdc            # 主要規則
├── 07-plan_v1.mdc             # 規劃工作流程
├── 08-code_v1.mdc             # 編碼工作流程
└── 09-debug_v1.mdc            # 調試工作流程
```

## 🧠 記憶系統

項目記憶系統包含以下核心文件：

### 核心文檔 (memory/docs/)
- **product_requirement_docs.md** - 產品需求文檔
- **architecture.md** - 系統架構文檔
- **technical.md** - 技術規格文檔

### 任務管理 (memory/tasks/)
- **tasks_plan.md** - 任務計劃和進度追蹤
- **active_context.md** - 當前開發上下文

## 💡 使用示例

### 1. 初始化項目記憶

```
基於項目的自定義規則，初始化記憶庫文件 (docs/, tasks/)，根據項目的當前狀態或初始需求。遵循規則中定義的文檔結構和說明。
```

### 2. 規劃新功能

```
使用 @.cursor/rules/plan_v1.mdc 中定義的工作流程，為新的用戶配置文件功能制定計劃。詳細需求在 @memory/tasks/active_context.md 的"用戶配置文件更新"任務中指定。
```

### 3. 實現功能

```
使用 @.cursor/rules/code_v1.mdc 中定義的工作流程，開發 updateUserProfile 函數。確保實現符合 @memory/docs/technical.md 中的 API 設計指南。
```

## 🔧 規則集說明

### Light-Spec (輕量級)
- 基本的開發工作流程
- 簡化的文檔結構
- 適合小型項目

### Medium-Spec (中等)
- 更詳細的工作流程
- 完整的文檔系統
- 適合中型項目

### Heavy-Spec (完整)
- 最全面的工作流程
- 企業級文檔系統
- 適合大型複雜項目

## 📝 自定義規則

您可以通過修改 `project_rules/` 目錄中的文件來自定義規則：

1. 修改規則文件
2. 運行同步命令：`python src/manage_rules.py sync ~/path/to/your/project`
3. Cursor 將自動使用更新後的規則

## 🗂️ 清理規則

```bash
# 清理規則（保留記憶和工具）
python src/manage_rules.py clean-rules ~/path/to/your/project

# 完全清理所有組件
python src/manage_rules.py clean-all ~/path/to/your/project
```

## 🎯 適用場景

- 需要結構化 AI 輔助開發的項目
- 希望保持項目文檔和上下文一致性的團隊
- 尋求基於最佳實踐的開發工作流程的開發者
- 需要可重現和可維護的 AI 互動的項目

## 📚 更多信息

- 查看 `rule_sets/` 目錄了解不同規則集的詳細內容
- 查看 `memory_starters/` 目錄了解文檔模板
- 查看 `src/manage_rules.py` 了解管理工具的功能




