#!/usr/bin/env python3
"""
move_kindle_notes.py

Obsidian Vault 直下にある Markdown ファイルのうち、
本文またはFrontmatterに `kindle-sync` という文字列を含むものを検出し、
`kindle` フォルダへ移動するためのスクリプト。

デフォルトは dry-run（一覧表示のみ）で、`--apply` を付けたときだけ
実際にファイルを移動します。

Vault の場所を変更した場合は、`VAULT_PATH` を書き換えてください。
"""

import argparse
import datetime
import os
import shutil
import sys
from typing import Iterable, List


# Obsidian Vault の絶対パス
VAULT_PATH = "/Users/toshionoda/Documents/Obsidian Vault"

# Kindle ノートの格納フォルダ名
KINDLE_DIR_NAME = "kindle"


def iter_root_markdown_files(vault_path: str) -> Iterable[str]:
    """Vault 直下にある .md ファイルのフルパスを列挙する。"""
    try:
        entries = os.listdir(vault_path)
    except OSError as e:
        print(f"Failed to list vault directory: {vault_path}\n{e}", file=sys.stderr)
        return []

    for name in entries:
        full_path = os.path.join(vault_path, name)
        if os.path.isfile(full_path) and name.lower().endswith(".md"):
            yield full_path


def is_kindle_note(path: str) -> bool:
    """ファイル内容に 'kindle-sync' が含まれているかどうかで判定する。"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"Warning: failed to read file: {path}\n{e}", file=sys.stderr)
        return False

    return "kindle-sync" in content


def make_unique_destination(dest_dir: str, filename: str) -> str:
    """
    移動先フォルダ内で重複しないファイルパスを生成する。

    すでに同名ファイルが存在する場合は、
    `<元ファイル名>_YYYYMMDD-HHMMSS.md` のようにリネームする。
    それでも重複する場合は末尾に連番を付ける。
    """
    base, ext = os.path.splitext(filename)
    candidate = os.path.join(dest_dir, filename)

    if not os.path.exists(candidate):
        return candidate

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = os.path.join(dest_dir, f"{base}_{timestamp}{ext}")

    counter = 2
    while os.path.exists(candidate):
        candidate = os.path.join(dest_dir, f"{base}_{timestamp}_{counter}{ext}")
        counter += 1

    return candidate


def find_kindle_notes(vault_path: str) -> List[str]:
    """Vault 直下の .md のうち、`kindle-sync` を含むファイルだけを抽出する。"""
    matches: List[str] = []
    for path in iter_root_markdown_files(vault_path):
        if is_kindle_note(path):
            matches.append(path)
    return matches


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Move @kindle notes from Obsidian vault root to the 'kindle' folder."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="実際にファイルを移動する（指定しない場合は dry-run で一覧表示のみ）。",
    )

    args = parser.parse_args(argv)

    vault_path = VAULT_PATH
    kindle_dir = os.path.join(vault_path, KINDLE_DIR_NAME)

    # 移動先フォルダを作成（すでにある場合はそのまま）
    try:
        os.makedirs(kindle_dir, exist_ok=True)
    except OSError as e:
        print(f"Failed to create kindle directory: {kindle_dir}\n{e}", file=sys.stderr)
        return 1

    kindle_notes = find_kindle_notes(vault_path)

    if not kindle_notes:
        print("Vault直下に `@kindle` を含むノートは見つかりませんでした。")
        return 0

    mode = "本番移動モード (--apply 指定あり)" if args.apply else "dry-run モード (--apply なし)"
    print(f"検出された @kindle ノート: {len(kindle_notes)} 件 ({mode})")
    print()

    for src in sorted(kindle_notes):
        filename = os.path.basename(src)
        dest = make_unique_destination(kindle_dir, filename)
        rel_dest = os.path.relpath(dest, vault_path)
        print(f"- {filename} -> {rel_dest}")

        if args.apply:
            # 念のため、同一パスでの移動はスキップ
            if os.path.abspath(src) == os.path.abspath(dest):
                continue
            try:
                shutil.move(src, dest)
            except OSError as e:
                print(f"  移動失敗: {e}", file=sys.stderr)

    if args.apply:
        print()
        print("完了: 対象ファイルを kindle フォルダへ移動しました。")
    else:
        print()
        print("確認のみ: 実際の移動は行っていません。")
        print("問題なければ、同じコマンドに `--apply` を付けて実行してください。")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


