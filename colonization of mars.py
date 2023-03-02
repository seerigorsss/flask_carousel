from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route('/promotion')
def promotion():
    text = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(text)


@app.route('/image_mars')
def image_mars():
    return '<h1>Жди нас, Марс!</h1>' \
           '<title>Привет, Марс!</title>' \
           '<figure>' \
           '<img src="static/img/mars.jpg" alt="missing" />' \
           '<figcaption>Красивый Марс</figcaption>' \
           '</figure>'


@app.route('/promotion_image')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href="static/css/style.css" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/img/mars.jpg" alt="missing" />
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"
                             />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control"
                                     id="lname" placeholder="Введите фамилию" name="lname">
                                    <input type="text" class="form-control"
                                     id="fname" placeholder="Введите имя" name="fname">
                                    <div class="form-group">
                                        <label for="classSelect"></label>
                                         <input type="email" class="form-control" id="email"
                                          aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                     </div>
                                     <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Послевузовское</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                     <label for="form-check">Какие у вас есть профессии?</label>
                                     <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="Check1" name="select" >
      <label class="form-check-label" for="Check1">Инженер-исследователь</label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="Check2" name="select" >
      <label class="form-check-label" for="Check2">Инженер-строитель</label>
    </div>
     <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="Check3" name="select" >
      <label class="form-check-label" for="Check3">Пилот</label>
    </div>
     <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="Check4" name="select" >
      <label class="form-check-label" for="Check4">Метеоролог</label>
    </div>
     <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="Check5" name="select" >
      <label class="form-check-label" for="Check5">Инженер по жизнеобеспечению</label>
    </div>
     <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="Check6" name="select" >
      <label class="form-check-label" for="Check6">Инженер по радиационной защите</label>
    </div>
     <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="Check7" name="select" >
      <label class="form-check-label" for="Check7">Врач</label>
    </div>
     <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="Check8" name="select" >
      <label class="form-check-label" for="Check8">Экзобиолог</label>
    </div>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                     <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    planets = {
        'Меркурий': ['Наименьшая планета в нашей солнечной системе;', 'На Меркурии очень горячо;',
                     'На Меркурии очень мало воды и атмосферы;', 'Поверхность Меркурия покрыта кратерами;',
                     'Поверхность Меркурия покрыта металлическими минералами.'],
        'Венера': ['Вторая планета Солнечной системы;', 'Имеет маленькую площадь поверхности;',
                   'На Венере очень много дыма и пыли;', 'На Венере очень мало воды;',
                   'Атмосфера состоит почти на 97% из углекислого газа.'],
        'Марс': ['Атмосфера на Марсе в 100 раз более разряженная, чем на Земле;',
                 'На Марсе существуют горы выше Эвереста;', 'Четвертая планете Солнечной системы;',
                 'У Марса есть 2 небольших луны – Деймос и Фобос;', 'Первым увидел Марс Галилео Галилей в 1609г.'],
        'Юпитер': [' У Юпитера самое сильное магнитное поле;', 'Юпитер самая быстрая планета солнечной системы;',
                   'Количество спутников Юпитера может меняться;', 'На Юпитере есть полярные сияния;',
                   'Большое красное пятно существует уже очень давно.'],
        'Сатурн': ['Сатурн обладает мощнейшим магнитным полем;', 'Сатурн не имеет твёрдой поверхности',
                   'На Сатурне бывает северное сияние', 'Скорость ветра на этой планете может достигать 1800 км/ч',
                   'На Сатурне неоднократно наблюдались облака странной шестиугольной формы'],
        'Уран': ['Уран делает оборот вокруг своей оси за 84 года;',
                 'Всего на сегодняшний день Уран насчитывает 27 спутников;',
                 'Атмосфера Урана признана самой холодной и приравнивается к -224 °C;',
                 'День на планете длится около 17 часов;',
                 'Через инфракрасные волны можно заметить облака на планете.'],
        'Нептун': ['Нептун является самой далекой планетой;', 'Нептун самый маленький из газовых гигантов;',
                   'Его поверхностная гравитация почти равна Земной;',
                   'Вокруг его открытия до сих пор не утихают споры',
                   'На планете самые сильные ветры в Солнечной системе'],
    }
    sentences = planets[planet_name]
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <div class="alert alert-light" role="alert">
                      <h2>{sentences[0]}</h2>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h2>{sentences[1]}</h2>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                     <h2>{sentences[2]}</h2> 
                    </div>
                    <div class="alert alert-warning" role="alert">
                     <h2>{sentences[3]}</h2> 
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h2>{sentences[4]}</h2>
                    </div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендента на участие {nickname}:</h2>
                            <div class="alert alert-success" role="alert">
                              <h2>Поздравляем! Ваш рейтинг после {level} этапа отбора</h2>
                            </div>
                            <h2>составляет {rating}!</h2>
                            <div class="alert alert-warning" role="alert">
                              <h2>Желаем удачи!</h2>
                            </div>
                          </body>
                        </html>'''


@app.route('/carousel')
def carousel():
    return '''<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
	<link rel="stylesheet" href="static/css/main.css">

	<title>Пейзажи Марса</title>
</head>
<body>
	<div class="container-fluid my-carousel">
		<div id="carouselExampleIndicators" class="carousel slide carousel-fade" data-bs-ride="carousel" data-bs-interval="5000">
			<div class="carousel-indicators">
				<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
				<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
				<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
				<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
			</div>
			<div class="carousel-inner">
				<div class="carousel-item active">
					<img src="static/img/1.jpg" class="d-block w-100" alt="...">
				</div>
				<div class="carousel-item">
					<img src="static/img/2.jpg" class="d-block w-100" alt="...">
				</div>
				<div class="carousel-item">
					<img src="static/img/3.jpg" class="d-block w-100" alt="...">
				</div>
				<div class="carousel-item">
					<img src="static/img/4.jpg" class="d-block w-100" alt="...">
				</div>
			</div>
			<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
				<span class="carousel-control-prev-icon" aria-hidden="true"></span>
				<span class="visually-hidden">Previous</span>
			</button>
			<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
				<span class="carousel-control-next-icon" aria-hidden="true"></span>
				<span class="visually-hidden">Next</span>
			</button>
		</div>
	</div>

	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
</body>
</html>

    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
