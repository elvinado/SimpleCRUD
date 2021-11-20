from flask import Flask, render_template, request, redirect
from flask_pure import Pure
from datetime import datetime

app = Flask(__name__)
app.config['PURECSS_RESPONSIVE_GRIDS'] = True
app.config['PURECSS_USE_CDN'] = True
app.config['PURECSS_USE_MINIFIED'] = True
Pure(app)

members_dict = {}
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        id = request.form['id']
        # if not id:
        #     return redirect('/')

        try:
            members_dict[id] = {}
            members_dict[id]['first_name'] = request.form['first_name']
            members_dict[id]['last_name'] = request.form['last_name']
            members_dict[id]['date_join'] = datetime.utcnow()
            return redirect('/')
        except:
            return 'There was an issue adding task'
    else:
        return render_template('index.html',members=members_dict)

@app.route('/delete/<string:id>')
def delete(id):
    try:
        members_dict.pop(id)
        return redirect('/')
    except:
        return 'Problem delete'

@app.route('/update/<string:id>',methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        try:
            members_dict[id]['first_name'] = request.form['first_name']
            members_dict[id]['last_name'] = request.form['last_name']
            return redirect('/')
        except:
            return 'problem updating'
    else:
        return render_template('update.html', members=members_dict,id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)