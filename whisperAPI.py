import whisper
file = open('reuniao.mp3', 'rb')
model = whisper.load_model("base")
result = model.transcribe('reuniao.mp3', fp16=False)
print(result["text"])
