import numpy as np
from flask import Flask, request, render_template
from joblib import load


app = Flask(__name__)
model = load('SeulBike_model.joblib')


@ app.route('/')
def home():
    # return 'Hello World'
    return render_template('home.html')
    # return render_template('index.html')


@ app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # output = round(prediction[0], 2)
    return render_template(
        'home.html', prediction_text="Your prediction is {}".format(
            np.round(np.round(np.expm1(prediction[0]))))
    )


if __name__ == '__main__':
    app.run(debug=True, port=8080)

