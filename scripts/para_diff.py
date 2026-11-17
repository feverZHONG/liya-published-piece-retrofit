#!/usr/bin/env python3
"""逐段比对「线上稿」与「修订稿」。

用法：
    python3 para_diff.py <线上 article.md> <修订稿 article.md> [--from-key 起始句]

--from-key 用来跳过线上稿的标题/元数据/前排说明，从正文第一句开始比。
不给 --from-key 时尝试自动跳过以 '#'、'**'、'---' 开头的头部行。

输出：段数、差异段（unified diff，按空行分段），退出码 0=一致 1=有差异 2=参数错。
"""
import sys
import difflib


def load_paras(path: str, from_key: str | None) -> list[str]:
    text = open(path, encoding="utf-8").read()
    if from_key:
        idx = text.find(from_key)
        if idx < 0:
            raise SystemExit(f"✗ 在 {path} 里找不到起始句：{from_key}")
        text = text[idx:]
    paras = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not from_key:
        paras = [p for p in paras if not p.startswith(("#", "**", "---", ">", "!["))]
    return paras


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    from_key = None
    if "--from-key" in sys.argv:
        i = sys.argv.index("--from-key")
        from_key = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        args = [a for a in args if a != from_key]
    if len(args) != 2:
        print(__doc__)
        return 2

    online = load_paras(args[0], from_key)
    draft = load_paras(args[1], from_key)
    print(f"线上 {len(online)} 段｜修订 {len(draft)} 段")

    diff = list(difflib.unified_diff(online, draft, "线上", "修订", lineterm="", n=0))
    if not diff:
        print("✅ 逐段一致")
        return 0
    print(f"❌ 有差异（{len(diff)} 行 diff）")
    for line in diff:
        print(line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
