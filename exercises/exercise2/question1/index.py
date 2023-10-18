from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database="arduino")
    cursor = connection.cursor()

    query = "SELECT * FROM datas"

    cursor.execute(query)

    temp_value = []
    humidity_value = []
    year_value = []
    date_value = []

    for (datas) in cursor.fetchall():
        # temp.append(temp)
        id, temp, humidity, date = datas
        temp_value.append(int(temp))
        humidity_value.append(int(humidity))
        year_value.append(date.strftime('%Y'))
        date_value.append(date.strftime('%Y-%m-%d %H:%M'))

    # return f"<p>Temp: {temp_value} | Humidity: {humidity_value}</p>"
    print(temp_value)
    print(humidity_value)
    print(year_value)
    return render_template('dashboard.html', temp_value=temp_value, humidity_value=humidity_value, year_value=year_value, date_value=date_value)

# if __name__ == '__main__':
app.run(host='0.0.0.0')