"""Recorta a imagem do dia (de scripts/imagens.png) e salva em docs/contagem.png, o link fixo da assinatura.
Linhas 1 a 200 = dias restantes; 201 = durante o evento; 202 = depois do evento."""
import datetime, pathlib
from PIL import Image

INICIO = datetime.date(2027, 5, 17)   # 1º dia da APAS Show 2027
FIM = datetime.date(2027, 5, 20)      # último dia
W, H = 240, 100

raiz = pathlib.Path(__file__).resolve().parent.parent
hoje = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=3)).date()   # Brasília

if hoje < INICIO:
    linha = min((INICIO - hoje).days, 200) - 1
elif hoje <= FIM:
    linha = 200
else:
    linha = 201

Image.open(raiz / "scripts" / "imagens.png").crop((0, linha * H, W, (linha + 1) * H)).save(raiz / "docs" / "contagem.png")
print(hoje, "-> linha", linha + 1)
