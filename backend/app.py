from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import os
import gdown


app = Flask(__name__)
CORS(app)

# cargar modelo LED de hugging face
model_name = "allenai/led-base-16384-ms2"
token = "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"
tokenizer =  AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
summarizer =pipeline("summarization", model=model_name)

# cargar modelo BioBART
model_name_bioBART = os.path.join(os.path.dirname(__file__), 'modelosPLN/BioBART')
tokenizerBioBART =  AutoTokenizer.from_pretrained(model_name_bioBART)
summarizerBioBART =pipeline("summarization", model=model_name_bioBART)


@app.route('/api/data', methods=['POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        print(f"Received data: {data}")
        articulo = data['articulo']
        lonResumen = int(data['longitud'])
        maxLon = lonResumen + 50
        minLon = lonResumen - 50

        longitud_articulo = len(articulo.split())  # Contamos las palabras
        print(f"Longitud del artículo original: {longitud_articulo} palabras")

        if longitud_articulo < lonResumen:   
            return jsonify({
                "error": f"El artículo es demasiado corto ({longitud_articulo} palabras) para generar un resumen de {lonResumen} palabras. Por favor, aumenta el tamaño del artículo o reduce la longitud del resumen solicitada."
            }), 400
        
        tokensTextLED = tokenizer.tokenize(articulo)
        if len(tokensTextLED) > 1024:
            reconstructed_text_LED = tokenizer.convert_tokens_to_string(tokensTextLED)
            print("texto recostruido")
            resumenLED = summarizer(reconstructed_text_LED, max_length=maxLon, min_length=minLon, do_sample=False)
            print("resumen LED completo")
            resumenGenerado = resumenLED[0]['summary_text']
        else:
            print("Utilizamos el modelo BioBART")
            tokensBART = tokenizerBioBART.tokenize(articulo)
            reconstructed_text_BART = tokenizerBioBART.convert_tokens_to_string(tokensBART)
            print("texto recostruido")
            resumenBART = summarizerBioBART(reconstructed_text_BART, max_length=maxLon, min_length=minLon, do_sample=False)
            print("resumen BioBART completo")
            resumenGenerado = resumenBART[0]['summary_text']
       
        return jsonify({"articulo": articulo, "resumen": resumenGenerado, "longitud": lonResumen}), 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
