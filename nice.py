from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """

    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
      Hi! This is the home page. <a href="/hello">Hello</a>
      </body>
    </html>

    """

     


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""



    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="POST">
          <label>What's your name? <input type="text" name="person"></label>
          <label>Select a compliment:

            <select name="compliment">
              <option value="%s">%s</option>
              <option value="%s">%s</option>
              <option value="%s">%s</option>
              <option value="%s">%s</option>
              <option value="%s">%s</option>
              <option value="%s">%s</option>
              <option value="%s">%s</option>
            </select>
          </label>
          <input type="submit">
        </form>
      </body>
    </html>
    """  % (AWESOMENESS[0], AWESOMENESS[0], AWESOMENESS[1], AWESOMENESS[1], AWESOMENESS[2], AWESOMENESS[2], AWESOMENESS[3], AWESOMENESS[3], 
      AWESOMENESS[4], AWESOMENESS[4], AWESOMENESS[5], AWESOMENESS[5], AWESOMENESS[6], AWESOMENESS[6])


@app.route('/greet', methods=["POST"])
def greet_person():
    """Get user by name."""

    player = request.form.get("person")

    compliment = request.form.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
