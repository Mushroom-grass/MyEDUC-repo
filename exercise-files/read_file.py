import re
from pathlib import Path

# === 1) 配置你的输入文件路径（到仓库里确认真实文件名后替换） ===
INPUT_FILE = Path("romeo_full.txt")  # 示例名；请改成仓库里的实际文件名
OUTPUT_FILE = Path("output.txt")

# === 2) 行首角色名匹配：如 "ROMEO:", "Romeo.", "  JULIET " 等都算 ===
def is_speaker_line(line: str, name: str) -> bool:
    """
    判断该行是否为指定角色的对白：
    - 行首（可有空白）紧跟角色名（忽略大小写）
    - 角色名后面接边界或常见分隔符(: . , ; 空格)
    """
    pattern = rf"^\s*{re.escape(name)}\b[ :\.,;]?"
    return re.search(pattern, line, flags=re.IGNORECASE) is not None

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"未找到输入文件：{INPUT_FILE.resolve()}")

    total_lines = 0
    romeo_count = 0
    juliet_count = 0

    with INPUT_FILE.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            total_lines += 1
            line = raw.rstrip("\n")

            if is_speaker_line(line, "Romeo"):
                romeo_count += 1
            elif is_speaker_line(line, "Juliet"):
                juliet_count += 1

    # === 3) 写出结果到 output.txt（按题目格式） ===
    with OUTPUT_FILE.open("w", encoding="utf-8") as out:
        out.write(f"Lines of text: {total_lines}\n")
        out.write(f"Romeo: {romeo_count}\n")
        out.write(f"Juliet: {juliet_count}\n")

    print(f"统计完成，结果已写入 {OUTPUT_FILE.resolve()}")

if __name__ == "__main__":
    main()
