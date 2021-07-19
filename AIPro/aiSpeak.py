import pyttsx3
from flask import Flask, request, jsonify
from word_select import word
class Ai(Flask):
    def parse_request(self,request):
        content = request.json
        print(content)
        text = content.get("txt")

        return text

    # def aispeak(self):
    #     text = self.parse_request(request)
    #     engine = pyttsx3.init()
    #
    #     rate = engine.getProperty("rate")
    #     engine.setProperty("rate",180)
    #
    #     engine.say(text)
    #
    #     engine.runAndWait()



app = Ai(__name__)

@app.route("/tts", methods=["post"])
def tts_speak():
    # app.aispeak()
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 180)

    text = app.parse_request(request)

    engine.say(text)
    engine.runAndWait()

    content = word.init_new_file(text)

    engine.say(content)

    engine.runAndWait()
    return jsonify({"status": "ok"})
if __name__ == '__main__':
    app.run("0.0.0.0",port=8888)

