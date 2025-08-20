import json
import re

# Load mappings
with open("data/gurmukhi_to_shahmukhi.json", "r", encoding="utf-8") as f:
    G2S_MAP = json.load(f)

with open("data/shahmukhi_to_gurmukhi.json", "r", encoding="utf-8") as f:
    S2G_MAP = json.load(f)

def transliterate(text: str, direction: str = "g2s") -> str:
    """
    Transliterate Punjabi text between Gurmukhi and Shahmukhi.
    direction: 'g2s' or 's2g'
    """
    map_dict = G2S_MAP if direction == "g2s" else S2G_MAP
    output = []

    for char in text:
        if char in map_dict:
            output.append(map_dict[char])
        else:
            output.append(char)  # fallback: preserve unknown chars

    return "".join(output)

def transliterate_word(word: str, direction: str = "g2s") -> str:
    # Optional: handle compound phonemes or diacritics
    return transliterate(word, direction)

def transliterate_sentence(sentence: str, direction: str = "g2s") -> str:
    words = re.split(r'(\s+)', sentence)
    return "".join([transliterate_word(w, direction) for w in words])
