import re


def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)

    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    return sentences


print("Введите текст:")
text = input()

sentences_list = split_sentences(text)

print("\nПредложения:")
for i, sentence in enumerate(sentences_list, 1):
    print(f"{sentence}")

print(f"\nПредложений в тексте: {len(sentences_list)}")