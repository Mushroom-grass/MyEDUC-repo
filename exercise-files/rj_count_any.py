from pathlib import Path
from typing import Iterable, Dict

CANDIDATES = Path("romeo-full.txt")
INPUT_FILE = next((p for p in CANDIDATES if p.exists()), None)
if INPUT_FILE is None:
    raise FileNotFoundError("未找到 romeo_full.txt（或 romeo-full.txt），请确认文件在当前目录。")

OUTPUT_FILE = Path("output_any.txt")

def count_speeches_any(file_path: Path, speakers: Iterable[str]) -> Dict[str, int]:
    counts = {s: 0 for s in speakers}
    with file_path.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            # 只在“整行等于说话者标记”时计数，可避免匹配到舞台提示等
            if line in counts:
                counts[line] += 1
    return counts

# 你要统计的任意角色标记（需与文本中的标记大小写一致）
SPEAKERS = ["ROMEO", "JULIET", "Nurse"]  # 可自由增删

# 先计算总行数
with INPUT_FILE.open("r", encoding="utf-8", errors="ignore") as f:
    total_lines = sum(1 for _ in f)

# 统计说话次数
counts = count_speeches_any(INPUT_FILE, SPEAKERS)

# 写出
with OUTPUT_FILE.open("w", encoding="utf-8") as out:
    out.write(f"Lines of text: {total_lines}\n")
    for s in SPEAKERS:
        out.write(f"{s}: {counts[s]}\n")

print(f"完成：统计 {', '.join(SPEAKERS)}，结果已写入 {OUTPUT_FILE.resolve()}")
