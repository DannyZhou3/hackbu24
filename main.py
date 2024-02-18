from flask import Flask, render_template, request

app = Flask('app')


@app.route('/')
def cooking():
  return render_template('homepage.html')

@app.route('/question1')
def q1():  
    return render_template('question1.html')
  
@app.route('/question2', methods=['POST'])
def q2():
  global crave
  crave = request.form["craving"]
  global x
  x = f'You want to eat {crave}'
  return render_template('question2.html')

@app.route('/question3', methods=['POST'])
def q3():
  global restrict
  restrictions = request.form["restrictions"]
  return render_template('question3.html', restrict=restrictions)
  
@app.route('/question4', methods=['POST'])
def q4():
  global money
  money = request.form["budget"]
  return render_template('question4.html')

@app.route('/results', methods=['POST'])
def results():
  global health
  health = request.form["healthRating"]
  return render_template('results.html')
  
@app.route('/chinese')
def chinese():
  if crave == 'Chinese':
    return render_template('chinese.html')
  else:
    str(x)
    return render_template('unfinished.html')
  
@app.route('/unfinished')
def unfinished():
  str(x)
  return render_template('unfinished', crave=crave)


app.run(host='0.0.0.0', port=8080)
