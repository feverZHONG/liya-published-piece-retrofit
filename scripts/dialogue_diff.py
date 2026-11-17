#!/usr/bin/env python3
"""比对旧稿与新稿的台词（「」内文字），确认修订／重写没丢句、没改词。

用法:
    python3 dialogue_diff.py <旧稿.md> <新稿.md>

只抽「」（兼认 “”）内的台词逐条比，不比较叙述层——修订允许改动作、并段、
换起句、倒装归属，台词（人物说的话）必须一条不多一条不少、一字不改。

退出码: 0=台词完全一致 / 1=有差异（打印逐条 diff）/ 2=参数错
"""
import difflib
import re
import sys


def quotes(path: str) -> list[str]:
    text = open(path, encoding="utf-8").read()
    qs = re.findall(r"「[^」]*」|“[^”]*”", text)
    return [q.strip("「」“”") for q in qs]


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    a, b = quotes(sys.argv[1]), quotes(sys.argv[2])
    print(f"旧稿台词 {len(a)} 条｜新稿台词 {len(b)} 条")
    if a == b:
        print("✅ 台词逐条一致")
        return 0
    n = 0
    for line in difflib.unified_diff(a, b, fromfile="旧稿", tofile="新稿", lineterm="", n=0):
        if line.startswith(("---", "+++", "@@")):
            continue
        print(line[:120])
        n += 1
    print(f"❌ 差异 {n} 行——回原文核对是哪句丢了/改了；修订只许动归属与动作，台词不动")
    return 1


if __name__ == "__main__":
    sys.exit(main())
