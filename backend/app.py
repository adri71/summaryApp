from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import os
import gdown


app = Flask(__name__)
CORS(app)

#en local
#model_path_led = os.path.join(os.path.dirname(__file__), 'modelosPLN/LED')
#model_path_bioBart = os.path.join(os.path.dirname(__file__), 'modelosPLN/BioBART')
#print(f"---{model_path}")
#tokenizerBioBART = AutoTokenizer.from_pretrained(model_path_bioBart)
#summarizerBioBART = pipeline("summarization", model=model_path_bioBart)
#tokenizerLED = AutoTokenizer.from_pretrained(model_path_led)
#summarizerLED = pipeline("summarization", model=model_path_led)

"""
# de drive
model_dir = os.path.join(os.path.dirname(__file__), 'modelosPLN')
model_drive_path = os.path.join(model_dir, 'model_from_drive')

drive_file_id = "17ot5w0hH5uoG7UyAGCGrDyrse53DUHpU"
output_path = os.path.join(model_drive_path, 'model.zip')
#https://drive.google.com/drive/folders/17ot5w0hH5uoG7UyAGCGrDyrse53DUHpU?usp=sharing

tokenizer_drive = None
summarizer_drive = None
tokenizer_transformers = None
summarizer_transformers = None

print(model_drive_path)
print(output_path)

def download_model_from_drive():
    print("as")
    if not os.path.exists(model_drive_path):
        print("as1")
        os.makedirs(model_drive_path)
        print("as2")
    if not os.path.exists(output_path):  # Only download if not already downloaded
        print("as3")
        gdown.download(f"https://drive.google.com/drive/folders/{drive_file_id}?usp=sharing", output_path, quiet=False)
        print("descarga echa -------------")
        # Unzip the model if it's zipped
        os.system(f'unzip {output_path} -d {model_drive_path}')

def initialize_models():
    global tokenizer_drive, summarizer_drive, tokenizer_transformers, summarizer_transformers

    # Download and load the model from Google Drive
    print("Downloading and loading the model from Google Drive...")
    download_model_from_drive()
    print("modelo drive descargado correctamente")
    tokenizer_drive = AutoTokenizer.from_pretrained(model_drive_path)
    summarizer_drive = pipeline("summarization", model=model_drive_path)
    print("modelo drive cargado correctamente")

    # Load the second model directly from Huggingface Transformers
    print("Loading the Huggingface model...")
    model_name = "facebook/bart-large-cnn"  # Example: BART large pre-trained model from Huggingface
    tokenizer_transformers = AutoTokenizer.from_pretrained(model_name)
    summarizer_transformers = pipeline("summarization", model=model_name)

    print("Models successfully loaded.")

# Call the initialize_models function when the backend starts
initialize_models()

"""

# cargar de hugging face
model_name = "allenai/led-base-16384-ms2"
token = "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"
tokenizer =  AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
summarizer =pipeline("summarization", model=model_name)


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
        
        #inputs = tokenizer.encode("summarize: " + articulo, return_tensors="pt", max_length=512, truncation=True)
        #summary_ids = model.generate(inputs, max_length=maxLon, min_length=minLon, num_beams=4, early_stopping=True)
        #resumen = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        #tokensText = tokenizer.tokenize(articulo, max_length=1010, truncation=True)
        #reconstructed_text = tokenizer.convert_tokens_to_string(tokensText)
        #resumen = summarizer(reconstructed_text, max_length=maxLon, min_length=minLon, do_sample=False)
        
        #tokensTextLED = tokenizerLED.tokenize(articulo)
        #numTLed = len(tokensTextLED)
        #print(f"El texto tiene {numTLed} tokens del modelo LED")
        #tokensTextBioBART = tokenizerBioBART.tokenize(articulo)
        #numTBBART = len(tokensTextBioBART)
        #print(f"El texto tiene {numTBBART} tokens del modelo BioBART")
        print("comenzando resumen")
        
        """
        #LED + BioBART  
        tokensTextLED = tokenizerLED.tokenize(articulo)
        print(f"tokenizacion LED -- {len(tokensTextLED)}")

        if len(tokensTextLED) > 1020:
            reconstructed_text_LED = tokenizerLED.convert_tokens_to_string(tokensTextLED)
            resumenLED = summarizerLED(reconstructed_text_LED, max_length=700, min_length=600, do_sample=False)
            print("resumen led completo")

            if isinstance(resumenLED, list):
                resumenLED = resumenLED[0]['summary_text']
        else:
            resumenLED = articulo
            print("unicamente realizaremos el resumen con el modelo bioBART")

        tokensTextBioBART = tokenizerBioBART.tokenize(resumenLED)   
        reconstructed_text_BioB = tokenizerBioBART.convert_tokens_to_string(tokensTextBioBART)
        resumenBioB = summarizerBioBART(reconstructed_text_BioB, max_length=maxLon, min_length=minLon, do_sample=False)
        print("resumen BioBART completo")

        print(resumenBioB)
        print("Resumen completo")
        #print(f"{articulo} - {lonResumen}")
        return jsonify({"articulo": articulo, "resumen": resumenBioB[0]['summary_text'], "longitud": lonResumen}), 200
        """

        # modelo led solo
        tokensTextLED = tokenizer.tokenize(articulo)
        print("tokenizacion echa")
        reconstructed_text_LED = tokenizer.convert_tokens_to_string(tokensTextLED)
        print("texto recostruido")
        resumenLED = summarizer(reconstructed_text_LED, max_length=maxLon, min_length=minLon, do_sample=False)
        print("resumen completo")
        return jsonify({"articulo": articulo, "resumen": resumenLED[0]['summary_text'], "longitud": lonResumen}), 200

if __name__ == '__main__':
    app.run(debug=True)
