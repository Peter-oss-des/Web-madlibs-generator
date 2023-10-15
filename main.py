from flask import Flask, render_template, request

app = Flask(__name__)

# Define routes and functions
@app.route('/')
def index():
    with open("story.txt","r") as f:
      story = f.read()

    words = set()
    start_of_word = -1
    start_word = "<"
    end_word = ">"
    word = ""
    for i, char in enumerate(story):
      if char == start_word:
        start_of_word = i

      if char == end_word and start_of_word != -1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1
    html_content = words
    return render_template('index.html', table_content=html_content)


@app.route('/process', methods=['POST'])
def process():
    
    with open("story.txt","r") as f:
      story = f.read()

    words = set()
    start_of_word = -1
    start_word = "<"
    end_word = ">"
    word = ""
    for i, char in enumerate(story):
      if char == start_word:
        start_of_word = i

      if char == end_word and start_of_word != -1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1
        
    
    answers = {}
    answer = [request.form[f'input{word}'] for word in words]
    i = 0
    for word in words:
      answers[word] = answer[i]
      i = i+1
    for word in words:
        story = story.replace(word,answers[word])
    
    return render_template('results.html', processed_data=story)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)


