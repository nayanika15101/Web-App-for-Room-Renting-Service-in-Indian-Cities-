from flask import Flask, jsonify, render_template, request
import urllib.request, json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index2.html')

@app.route('/result', methods=['GET', 'POST'])
def get_json():


    print("It's here")
    if request.method == 'POST':
        hsr = request.form['city_name']

    url = "https://www.oyolife.in/api/listing?city=" + hsr

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    vals = list(data.values())[0]

    print("Main Webiste Done")

    ids = []

    for i in vals:
        ids.append(i['id'])

    final_res = []
    final_res2 = []
    ctr = 0

    for i in ids:
        ctr += 1
        print("Loading hotel #" + str(ctr))

        try:

            url = "https://www.oyolife.in/api/propertyDetails?id=" + i
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            new_dic = {
            		"Property name":data['name'],
            		"id":data['id'],
            		"hsr layout":data['city_name'],
            		"co-ordinates":str(int(data['latitude'])) +"latitute"+ str(int(data['longitude']))+"longitude",
            		"location":data['address'], 
            		"Sharing room price":data['rooms']['sharing_price'],
            		"Private room price":data['rooms']['private_price']
            	}

            final_res.append(new_dic)

    		if new_dic.id==999:
    			final_res2.append(new_dic)


        except Exception as e:
            print(e)
       
    return jsonify(final_res2)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug = True)