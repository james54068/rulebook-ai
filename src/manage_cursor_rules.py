#!/usr/bin/env python3
"""
Cursor Rules Manager - 簡化版本
專門用於管理 Cursor AI 編程助手的規則
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

# 常量定義
# 獲取腳本所在目錄的絕對路徑
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

SOURCE_RULE_SETS_DIR = os.path.join(PROJECT_ROOT, "rule_sets")
SOURCE_MEMORY_STARTERS_DIR = os.path.join(PROJECT_ROOT, "memory_starters")
TARGET_PROJECT_RULES_DIR = "project_rules"
TARGET_MEMORY_DIR = "memory"
CURSOR_RULES_DIR = ".cursor/rules"

def print_banner():
    """打印歡迎橫幅"""
    print("=" * 60)
    print("Cursor Rules Manager - 簡化版本")
    print("=" * 60)

def list_available_rules():
    """列出可用的規則集"""
    print("\n可用的規則集:")
    print("-" * 30)
    
    if not os.path.exists(SOURCE_RULE_SETS_DIR):
        print("錯誤: rule_sets 目錄不存在")
        return 1
    
    rule_sets = [d for d in os.listdir(SOURCE_RULE_SETS_DIR) 
                 if os.path.isdir(os.path.join(SOURCE_RULE_SETS_DIR, d))]
    
    if not rule_sets:
        print("沒有找到規則集")
        return 1
    
    for i, rule_set in enumerate(sorted(rule_sets), 1):
        print(f"{i}. {rule_set}")
    
    print(f"\n使用命令安裝: python src/manage_cursor_rules.py install <項目路徑> --rule-set <規則集名稱>")
    return 0

def copy_and_number_files(source_dir, target_dir, extension_mode='add_mdc'):
    """複製並編號文件到目標目錄"""
    if not os.path.exists(source_dir):
        print(f"源目錄不存在: {source_dir}")
        return
    
    os.makedirs(target_dir, exist_ok=True)
    
    # 收集所有 .md 文件
    md_files = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    # 按文件名排序
    md_files.sort()
    
    # 複製並重命名文件
    for i, source_file in enumerate(md_files, 1):
        filename = os.path.basename(source_file)
        name_without_ext = os.path.splitext(filename)[0]
        
        if extension_mode == 'add_mdc':
            new_filename = f"{i:02d}-{name_without_ext}.mdc"
        else:
            new_filename = f"{i:02d}-{name_without_ext}.md"
        
        target_file = os.path.join(target_dir, new_filename)
        
        # 讀取源文件內容
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 寫入目標文件
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  創建: {new_filename}")

def copy_memory_starters(source_dir, target_dir):
    """複製記憶庫起始文件"""
    if not os.path.exists(source_dir):
        print(f"記憶庫起始目錄不存在: {source_dir}")
        return
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 複製所有文件和子目錄
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)
        
        if os.path.isdir(source_item):
            if not os.path.exists(target_item):
                shutil.copytree(source_item, target_item)
                print(f"  創建目錄: {item}/")
        else:
            if not os.path.exists(target_item):
                shutil.copy2(source_item, target_item)
                print(f"  複製文件: {item}")

def install_rules(target_repo_path, rule_set_name="light-spec"):
    """安裝規則到目標項目"""
    # 清理路徑，移除可能的引號和額外參數
    target_repo_path = target_repo_path.strip().strip('"').strip("'")
    # 移除路徑中可能包含的額外參數
    if ' --' in target_repo_path:
        target_repo_path = target_repo_path.split(' --')[0]
    target_repo_path = os.path.abspath(target_repo_path)
    print(f"\n安裝規則到: {target_repo_path}")
    print(f"使用規則集: {rule_set_name}")
    
    # 檢查源規則集是否存在
    source_rule_set_dir = os.path.join(SOURCE_RULE_SETS_DIR, rule_set_name)
    if not os.path.exists(source_rule_set_dir):
        print(f"錯誤: 規則集 '{rule_set_name}' 不存在")
        return 1
    
    # 創建目標目錄
    project_rules_dir = os.path.join(target_repo_path, TARGET_PROJECT_RULES_DIR)
    memory_dir = os.path.join(target_repo_path, TARGET_MEMORY_DIR)
    cursor_rules_dir = os.path.join(target_repo_path, CURSOR_RULES_DIR)
    
    # 清理並創建 project_rules 目錄
    if os.path.exists(project_rules_dir):
        print(f"警告: {TARGET_PROJECT_RULES_DIR} 目錄已存在，將被覆蓋")
        shutil.rmtree(project_rules_dir)
    
    os.makedirs(project_rules_dir)
    
    # 複製規則集到 project_rules
    print(f"\n複製規則集...")
    copy_and_number_files(source_rule_set_dir, project_rules_dir, extension_mode='add_mdc')
    
    # 複製記憶庫起始文件
    print(f"\n設置記憶庫...")
    copy_memory_starters(SOURCE_MEMORY_STARTERS_DIR, memory_dir)
    
    # 生成 Cursor 規則
    print(f"\n生成 Cursor 規則...")
    os.makedirs(os.path.dirname(cursor_rules_dir), exist_ok=True)
    if os.path.exists(cursor_rules_dir):
        shutil.rmtree(cursor_rules_dir)
    
    copy_and_number_files(project_rules_dir, cursor_rules_dir, extension_mode='add_mdc')
    
    print(f"\n安裝完成!")
    print(f"Cursor 規則位置: {cursor_rules_dir}")
    print(f"項目規則位置: {project_rules_dir}")
    print(f"記憶庫位置: {memory_dir}")
    
    print(f"\n下一步:")
    print(f"1. 將 {CURSOR_RULES_DIR} 添加到 .gitignore")
    print(f"2. 提交 memory/ 目錄到版本控制")
    print(f"3. 開始使用 Cursor 進行開發!")
    
    return 0

def sync_rules(target_repo_path):
    """同步規則（重新生成 Cursor 規則）"""
    # 清理路徑，移除可能的引號和額外參數
    target_repo_path = target_repo_path.strip().strip('"').strip("'")
    # 移除路徑中可能包含的額外參數
    if ' --' in target_repo_path:
        target_repo_path = target_repo_path.split(' --')[0]
    target_repo_path = os.path.abspath(target_repo_path)
    project_rules_dir = os.path.join(target_repo_path, TARGET_PROJECT_RULES_DIR)
    cursor_rules_dir = os.path.join(target_repo_path, CURSOR_RULES_DIR)
    
    print(f"\n同步規則...")
    print(f"源目錄: {project_rules_dir}")
    print(f"目標目錄: {cursor_rules_dir}")
    
    if not os.path.exists(project_rules_dir):
        print(f"錯誤: {TARGET_PROJECT_RULES_DIR} 目錄不存在")
        print("請先運行 install 命令")
        return 1
    
    # 清理並重新生成 Cursor 規則
    if os.path.exists(cursor_rules_dir):
        shutil.rmtree(cursor_rules_dir)
    
    os.makedirs(cursor_rules_dir)
    copy_and_number_files(project_rules_dir, cursor_rules_dir, extension_mode='add_mdc')
    
    print(f"同步完成!")
    return 0

def clean_rules(target_repo_path):
    """清理規則（保留記憶庫）"""
    # 清理路徑，移除可能的引號和額外參數
    target_repo_path = target_repo_path.strip().strip('"').strip("'")
    # 移除路徑中可能包含的額外參數
    if ' --' in target_repo_path:
        target_repo_path = target_repo_path.split(' --')[0]
    target_repo_path = os.path.abspath(target_repo_path)
    project_rules_dir = os.path.join(target_repo_path, TARGET_PROJECT_RULES_DIR)
    cursor_rules_dir = os.path.join(target_repo_path, CURSOR_RULES_DIR)
    
    print(f"\n清理規則...")
    
    cleaned = False
    
    if os.path.exists(project_rules_dir):
        shutil.rmtree(project_rules_dir)
        print(f"已刪除: {TARGET_PROJECT_RULES_DIR}")
        cleaned = True
    
    if os.path.exists(cursor_rules_dir):
        shutil.rmtree(cursor_rules_dir)
        print(f"已刪除: {CURSOR_RULES_DIR}")
        cleaned = True
    
    if not cleaned:
        print("沒有找到需要清理的規則文件")
    else:
        print(f"清理完成! 記憶庫 ({TARGET_MEMORY_DIR}) 已保留")
    
    return 0

def clean_all(target_repo_path):
    """完全清理（包括記憶庫）"""
    # 清理路徑，移除可能的引號和額外參數
    target_repo_path = target_repo_path.strip().strip('"').strip("'")
    # 移除路徑中可能包含的額外參數
    if ' --' in target_repo_path:
        target_repo_path = target_repo_path.split(' --')[0]
    target_repo_path = os.path.abspath(target_repo_path)
    project_rules_dir = os.path.join(target_repo_path, TARGET_PROJECT_RULES_DIR)
    cursor_rules_dir = os.path.join(target_repo_path, CURSOR_RULES_DIR)
    memory_dir = os.path.join(target_repo_path, TARGET_MEMORY_DIR)
    
    print(f"\n完全清理所有組件...")
    print(f"這將刪除所有規則文件和記憶庫!")
    
    # 確認
    confirm = input("確定要繼續嗎? (y/N): ").strip().lower()
    if confirm != 'y':
        print("操作已取消")
        return 0
    
    cleaned = False
    
    if os.path.exists(project_rules_dir):
        shutil.rmtree(project_rules_dir)
        print(f"已刪除: {TARGET_PROJECT_RULES_DIR}")
        cleaned = True
    
    if os.path.exists(cursor_rules_dir):
        shutil.rmtree(cursor_rules_dir)
        print(f"已刪除: {CURSOR_RULES_DIR}")
        cleaned = True
    
    if os.path.exists(memory_dir):
        shutil.rmtree(memory_dir)
        print(f"已刪除: {TARGET_MEMORY_DIR}")
        cleaned = True
    
    if not cleaned:
        print("沒有找到需要清理的文件")
    else:
        print(f"完全清理完成!")
    
    return 0

def main():
    """主函數"""
    parser = argparse.ArgumentParser(
        description="Cursor Rules Manager - 簡化版本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python src/manage_cursor_rules.py list-rules
  python src/manage_cursor_rules.py install ~/my-project
  python src/manage_cursor_rules.py install ~/my-project --rule-set heavy-spec
  python src/manage_cursor_rules.py sync ~/my-project
  python src/manage_cursor_rules.py clean-rules ~/my-project
  python src/manage_cursor_rules.py clean-all ~/my-project
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # list-rules 命令
    subparsers.add_parser('list-rules', help='列出可用的規則集')
    
    # install 命令
    install_parser = subparsers.add_parser('install', help='安裝規則到項目')
    install_parser.add_argument('target_repo_path', help='目標項目路徑')
    install_parser.add_argument('--rule-set', default='light-spec', 
                               help='規則集名稱 (預設: light-spec)')
    
    # sync 命令
    sync_parser = subparsers.add_parser('sync', help='同步規則')
    sync_parser.add_argument('target_repo_path', help='目標項目路徑')
    
    # clean-rules 命令
    clean_rules_parser = subparsers.add_parser('clean-rules', help='清理規則（保留記憶庫）')
    clean_rules_parser.add_argument('target_repo_path', help='目標項目路徑')
    
    # clean-all 命令
    clean_all_parser = subparsers.add_parser('clean-all', help='完全清理所有組件')
    clean_all_parser.add_argument('target_repo_path', help='目標項目路徑')
    
    args = parser.parse_args()
    
    if not args.command:
        print_banner()
        parser.print_help()
        return 1
    
    # 執行對應命令
    if args.command == 'list-rules':
        return list_available_rules()
    elif args.command == 'install':
        return install_rules(args.target_repo_path, args.rule_set)
    elif args.command == 'sync':
        return sync_rules(args.target_repo_path)
    elif args.command == 'clean-rules':
        return clean_rules(args.target_repo_path)
    elif args.command == 'clean-all':
        return clean_all(args.target_repo_path)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
