from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_PATH = "./punjabi_translit_model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

def transliterate(text: str, direction: str = "g2s") -> str:
    lang_tag = "<2ur>" if direction == "g2s" else "<2pa>"
    input_text = f"{text} </s> {lang_tag}"
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
