from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello World!"

@app.route("/<error>")
def error(error):
  return "Sorry. No response, try again!"

@app.route("/dojo")
def dojo():
  return "Dojo!"

@app.route("/say/<word>")
def say(word):
  return "Hi, {}!".format(word)

@app.route("/repeat/<num>/<var>")
def repeat(num, var):
  i = 1
  str = ""
  while i <= int(num):
    str += var
    str += " "
    i += 1
  return str

if __name__ == "__main__":
  app.run(debug=True)