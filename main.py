from flask import Flask, render_template, request, redirect

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
  x = f'You want to eat {crave}\n'
  return render_template('question2.html')

@app.route('/question3', methods=['POST'])
def q3():
  global restrict
  restrict = request.form["restrictions"]
  global y 
  y = f'You cannot eat {restrict}\n'
  return render_template('question3.html')
  
@app.route('/question4', methods=['POST'])
def q4():
  global money
  money = request.form["budget"]
  global z
  z = f'You have a {money}\n'
  return render_template('question4.html')

@app.route('/results', methods=['POST'])
def results():
  global health
  health = request.form["healthRating"]
  global h
  h = f'Health-wise: {health}\n'
  return render_template('results.html')
  
@app.route('/chinese')
def chinese():
  if crave == 'Chinese':
    return render_template('chinese.html')
  else:
    return render_template('unfinished.html', x=f'You want to eat {crave}\n', y = f'You cannot eat {restrict}\n'
                           , z = f'You have a {money}\n', h = f'Health-wise: {health}\n')
  
@app.route('/unfinished')
def unfinished():
  return render_template('unfinished.html')


app.run(host='0.0.0.0', port=8080)
