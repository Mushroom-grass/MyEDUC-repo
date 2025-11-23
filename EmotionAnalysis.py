import re
from collections import Counter

# === 加载文本（这里替换为你自己的文本文件路径） ===
file_path = "/Users/yuanqihu/Library/CloudStorage/OneDrive-PennO365/2025Fall/EDUC5913/MyEDUC-repo/romeo-full.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read().lower()

# === 定义一个简单的情绪词典（可扩展） ===
emotion_lexicon = {
    "love": ["love", "dear", "sweet", "beloved", "lovely"],
    "joy": ["joy", "happy", "delight", "glad", "smile"],
    "anger": ["anger", "hate", "rage", "enemy", "fury"],
    "fear": ["fear", "afraid", "peril", "danger", "death"],
    "sadness": ["sad", "sorrow", "weep", "grief", "heavy"],
    "surprise": ["wonder", "astonish", "marvel"]
}

# === 提取所有单词 ===
words = re.findall(r"[a-z']+", text)

# === 统计每类情绪的出现次数 ===
emotion_counts = {emotion: 0 for emotion in emotion_lexicon}

for word in words:
    for emotion, lex_words in emotion_lexicon.items():
        if word in lex_words:
            emotion_counts[emotion] += 1

# === 输出结果 ===
print("Emotion Word Counts:")
for emo, count in emotion_counts.items():
    print(f"{emo:10s} : {count}")

# 统计出现过的情绪词
emotion_words_found = []
for emotion, lex_words in emotion_lexicon.items():
    for w in lex_words:
        if w in words:
            emotion_words_found.append(w)

print("\nEmotion Words Found in Text:")
print(sorted(set(emotion_words_found)))
