from flask import Flask, jsonify, request, render_template


app = Flask(__name__, template_folder='templates')

cars = [
    {
        'modelo': 'Fusca',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1982',
        'preco': '15.000'
    },
    {
        'modelo': 'Monza',
        'motor': '1.6',
        'marca': 'Chevrolet',
        'ano': '1982',
        'preco': '10.000'
    },

    {
        'modelo': 'Mustang GT',
        'motor': '390 V8',
        'marca': 'Ford',
        'ano': '1966',
        'preco': '150.000'
    },
    {
        'modelo': 'Chevette',
        'motor': '1.6',
        'marca': 'Chevrolet',
        'ano': '1987',
        'preco': '10.000'

    },

    {
        'modelo': 'Gol',
        'motor': '1.8',
        'marca': 'Volkswagen',
        'ano': '1988',
        'preco': '25.000'
    },
    {
        'modelo': 'Uno Mille',
        'motor': '1.5',
        'marca': 'Fiat',
        'ano': '1984',
        'preco': '20.000'
    },
    {
        'modelo': 'Passat',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1982',
        'preco': '10.000'
    },

    {
        'modelo': 'Opala',
        'motor': '2.5',
        'marca': 'Chevrolet',
        'ano': '1981',
        'preco': '15.000'
    },

    {
        'modelo': 'Maverick',
        'motor': '4.9 V8',
        'marca': 'Ford',
        'ano': '1976',
        'preco': '60.000'
    },
    {
        'modelo': 'Kadett',
        'motor': '1.8',
        'marca': 'Chevrolet',
        'ano': '1989',
        'preco': '15.000'
    },

    {
        'modelo': 'Kombi',
        'motor': '1.4',
        'marca': 'Volkswagen',
        'ano': '1957',
        'preco': '25.000'
    },
    {
        'modelo': 'Santana',
        'motor': '1.6',
        'marca': 'Volkswagen',
        'ano': '1984',
        'preco': '10.000'
    },
]


@app.route("/generalInformations", methods=['GET'])
def general_informations():
    return render_template("general_informations.html", infos=cars)


@app.route("/filter", methods=['GET', 'POST'])
def filtering_cars():
    filtered = False
    filtered_cars = []
    if request.method == 'POST':
        for car_ in cars:
            print(request.form['engine'] == car_[
                  'motor'], request.form['year'] == car_['ano'])
            if (request.form['engine'] == car_['motor']) and (request.form['year'] == car_['ano']):
                filtered = True
                print("entra aqui")
                filtered_cars.append(car_)
    print(filtered_cars)
    return render_template("filtering.html", filt_cars=filtered_cars, filtered=filtered, infos=cars)


@app.route("/changeEngine", methods=['POST', 'GET'])
def change_car_engine():
    if request.method == 'POST':
        for car_ in cars:
            if request.form['model'] == car_['modelo']:
                car_['motor'] = request.form['engine']
    return render_template("change_engine.html", infos=cars)


@app.route("/remove", methods=['GET', 'POST'])
def remove_cars():
    if request.method == 'POST':
        for car_ in cars:
            if request.form['model'] == car_['modelo']:
                cars.remove(car_)
    return render_template("remove.html", infos=cars)


@app.route("/addNewModel", methods=['POST', 'GET'])
def add_cars():
    if request.method == 'POST':
        new_model = {
            'modelo': request.form['model'],
            'motor': request.form['engine'],
            'marca': request.form['brand'],
            'ano': request.form['year'],
            'preco': request.form['price']
        }
        cars.append(new_model)
    return render_template("add_car.html", infos=cars)


if __name__ == '__main__':
    app.run(debug=True)
