from pathlib import Path


CANDIDATES = Path("romeo-full.txt")
INPUT_FILE = next((p for p in CANDIDATES if p.exists()), None)
if INPUT_FILE is None:
    raise FileNotFoundError("未找到 romeo_full.txt（或 romeo-full.txt），请确认文件在当前目录。")

OUTPUT_FILE = Path("output.txt")

total_lines = 0
romeo_count = 0
juliet_count = 0

with INPUT_FILE.open("r", encoding="utf-8", errors="ignore") as f:
    for raw in f:
        total_lines += 1
        line = raw.strip()          # 去掉两侧空白，方便做“完全等于”判断
        if line == "ROMEO":
            romeo_count += 1
        elif line == "JULIET":
            juliet_count += 1

with OUTPUT_FILE.open("w", encoding="utf-8") as out:
    out.write(f"Lines of text: {total_lines}\n")
    out.write(f"Romeo: {romeo_count}\n")
    out.write(f"Juliet: {juliet_count}\n")

print(f"完成：结果已写入 {OUTPUT_FILE.resolve()}")
