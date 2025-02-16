from chatbot import chatbot_response
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/send")
def get_bot_response():
  userText = request.args.get('msg')
  history =[
    {
      "role" : "user",
      "parts" : [
        {
          "text" : "Do q é formada a Lua?"
        }
      ],
    },
    {
      "role" : "model",
      "parts" : [
        {
          "text" : "A Lua é formada principalmente por **rocha**, similar à composição do manto terrestre. Essa rocha é rica em minerais silicatos, como: * **Plagioclásio:** O mineral mais abundante na Lua. * **Piroxênio:** Outro mineral silicático comum. * **Olivina:** Menos abundante que plagioclásio e piroxênio. * **Ilmenita:** Um óxido de ferro e titânio, concentrado em algumas áreas, os 'mares' lunares. Além dos minerais principais, a Lua contém traços de outros elementos, como titânio, alumínio, ferro, magnésio, cálcio, sódio, potássio e fósforo. É importante destacar que a composição da Lua não é uniforme. A crosta, o manto e o (possível pequeno) núcleo possuem diferentes concentrações desses materiais. A superfície lunar também é coberta por uma camada de **regolito**, uma mistura de poeira fina, fragmentos de rocha, e material vítreo formado por impactos de meteoroides."
        }
      ]
    }
  ] 
   
  return chatbot_response(userText, history)

if __name__ == "__main__":
  app.run(debug=True)