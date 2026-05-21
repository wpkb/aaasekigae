from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    seats = []
    rows = 5
    cols = 6
    names_text = ""

    if request.method == 'POST':
        names_text = request.form.get('names', '')
        rows = int(request.form.get('rows', 5))
        cols = int(request.form.get('cols', 6))
        
        # 名前をリスト化（空行を削除）
        names = [name.strip() for name in names_text.split('\n') if name.strip()]
        total_seats = rows * cols
        
        # 席数より名前が少ない場合は「空席」で埋める
        while len(names) < total_seats:
            names.append("空席")
        
        # 席数より名前が多い場合はカット（エラー防止）
        names = names[:total_seats]
        
        # シャッフル
        random.shuffle(names)
        
        # 2次元配列（縦×横）に分割
        seats = [names[i * cols:(i + 1) * cols] for i in range(rows)]
        
    return render_template('index.html', seats=seats, rows=rows, cols=cols, names_text=names_text)

# UptimeRobotからのアクセスを受け止める用のエンドポイント
@app.route('/ping')
def ping():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
