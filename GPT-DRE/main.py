import gpt2
from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel
# TOKEN NTtrBGGxNCffVDYRPPksCQsnZMKXYiQajMzSgnpiSZCEElOKItYtKILbcjelwkvhbvnrFfTdQsSNuCRbYPpudgxbFWGTrCSLPuiNeywjLDbtURKTTIijIpUSeRonEwwQ


#classifier = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment") #  PARTICULAR MODEL
#print(classifier('We are very happy to show you the 🤗 Transformers library.')) # FAR FASTER SENTIMENT ANAYLSIS

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')#gpt2-xl #for very powerful model
model = GPT2LMHeadModel.from_pretrained('gpt2', pad_token_id=tokenizer.eos_token_id)

text = "what is natural language processing?"
encoded_input = tokenizer.encode(text, return_tensors='pt')

print(tokenizer.decode((encoded_input[0][0])))

#output = model.generate(encoded_input,max_length=500, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)

