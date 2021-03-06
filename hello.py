from flask import Flask, render_template, url_for   # Из пакета flask импортируем класс Flask

app = Flask(__name__)	# Создаем новое web-приложение
# app – имя переменной, в которой хранится ссылка на ЭКЗЕМПЛЯР класса Flask
# __name__ -  атрибут создаваемого экземпляра класса. Передает создаваемому экземпляру класса 
# имя модуля (пакета) в котором расположен   этот класс.
 	    # Иначе Flask не знает где искать шаблоны, статистические файлы и т.д.
@app.route("/")
def index():
#    return "Hello, world!"
    return render_template("index.html")

@app.route("/layout.html")
def layout():
#    return url_for('layout')
    return render_template("layout.html")

@app.route("/integrity.html")
def integrity():		#  эта функция вернет в тэг <body> браузера слова Hello World!
    return render_template("integrity.html")

@app.route("/terms.html")
def terms():		#  эта функция вернет в тэг <body> браузера слова Hello World!
    return render_template("terms.html")
#	return "Hello, world! "
#@app.route("/index")
# @ - декоратор - вызываем функцию (метод) route() расположенную в экземпляре app класса Flask. 
# Эта функция route()  анализирует строку браузера и, если она заканчивается на / (слэш),  
# то вызывается функция расположенная сразу под декоратором.
# Можно разместить  несколько декораторов подряд, тогда одно действие для нескольких путей.

#  Вариант запуска  flask 
if __name__ == "__main__":  #  Если вызвать этот файл из командной:  python hello.py
    app.run(debug=True)			#  То запустится  web приложение
