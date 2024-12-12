from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

def generate_summary(genre):
    input_text = f"Generate an anime plot in the genre: {genre}"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    summary_ids = model.generate(input_ids)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
