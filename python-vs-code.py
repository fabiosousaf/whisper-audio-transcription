import whisper
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

# Caminho para os áudios
pasta_audios = Path(r"C:\Users\USER\Desktop\python\open-ai-whisper\audios") #Definir caminho de pasta
model = whisper.load_model("medium")  # Pode usar "base", "small", etc.

# Cria pasta para salvar os arquivos
pasta_resultados = pasta_audios / "transcricoes"
pasta_resultados.mkdir(exist_ok=True)

# Formatos aceitos
extensoes = (".mp3", ".wav", ".m4a", ".flac")
arquivos_audio = [f for f in pasta_audios.iterdir() if f.suffix.lower() in extensoes]

for arquivo in arquivos_audio:
    print(f"\n🎧 Transcrevendo: {arquivo.name}")
    result = model.transcribe(
        str(arquivo),
        verbose=True,       # Ativa exibição detalhada
        fp16=False,         # Necessário se estiver usando CPU
        language="pt"       # Força o modelo a usar português
    )
    
    texto = result["text"]

    # Salva a transcrição
    arquivo_saida = pasta_resultados / f"{arquivo.stem}.txt"
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(texto)
    
    print(f"✅ Transcrição salva: {arquivo_saida}")

print("\n🎯 Todas as transcrições foram concluídas.")
