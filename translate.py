from transformers import MarianMTModel, MarianTokenizer

MODEL_NAME_MAP = {
    ("af", "en"): "Helsinki-NLP/opus-mt-af-en",
    ("en", "af"): "Helsinki-NLP/opus-mt-en-af",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("ha", "en"): "Helsinki-NLP/opus-mt-ha-en",
    ("en", "ha"): "Helsinki-NLP/opus-mt-en-ha"
}

models = {}

def load_model(src_lang, tgt_lang):
    key = (src_lang, tgt_lang)
    if key not in models:
        model_name = MODEL_NAME_MAP.get(key)
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        models[key] = (tokenizer, model)
    return models[key]

def translate_text(text, src_lang="af", tgt_lang="en"):
    tokenizer, model = load_model(src_lang, tgt_lang)
    input_tokens = tokenizer([text], return_tensors="pt", padding=True)
    translated = model.generate(**input_tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
