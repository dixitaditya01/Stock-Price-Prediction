from flask import Flask, render_template, request, url_for
from flask.templating import Environment
import base64
import io
from PIL import Image
app = Flask(__name__)


@app.route('/')
def index():
    im = Image.open("static/Capture.jpg")
    data = io.BytesIO()
    im.save(data, "JPEG")
    encode_img_data = base64.b64encode(data.getvalue())
    return render_template('index.html', image_data = encode_img_data.decode('utf-8'))

@app.route('/predict', methods=['GET','POST'])
def predict():
    company = request.form['Company']
    if company == "TCS":
        im = Image.open("static/tcs.jpg")
        data = io.BytesIO()
        im.save(data, "JPEG")
        encode_img_data = base64.b64encode(data.getvalue())
        text = "The above graph is a prediction of the TCS Close price for the next 30 days."
        company_name = "TCS"
    elif company == "Infosys":
        im = Image.open("static/Infosys.jpg")
        data = io.BytesIO()
        im.save(data, "JPEG")
        encode_img_data = base64.b64encode(data.getvalue())
        text = "The above graph is a prediction of the Infosys Close price for the next 30 days."
        company_name = "Infosys"
    elif company == "HDFC":
        im = Image.open("static/HDFC.jpg")
        data = io.BytesIO()
        im.save(data, "JPEG")
        encode_img_data = base64.b64encode(data.getvalue())
        text = "The above graph is a prediction of the HDFC Close price for the next 30 days."
        company_name = "HDFC"
    else:
        im = Image.open("static/Wipro.jpg")
        data = io.BytesIO()
        im.save(data, "JPEG")
        encode_img_data = base64.b64encode(data.getvalue())
        text = "The above graph is a prediction of the Wipro Close price for the next 30 days."
        company_name = "Wipro"
    return render_template("index.html", image_data = encode_img_data.decode('utf-8'), text = text, Company_name = company_name)


if __name__=='__main__':
    app.run()