import os
from flask import request, render_template
from werkzeug.utils import secure_filename
from prajwal.core import Handler

def dataRoute(app):
    coreHandler = Handler()

    @app.route('/data/paneldata', methods = ['POST','GET'])
    def fetchPanelData():
        if request.method == 'POST':
            ratedPower = request.form['rated-power']
            ratedEfficiency = request.form['rated-efficiency']
            nominalCellTemp = request.form['nominal-cell-temp']
            panelArea = request.form['panel-area']
            cellCount = request.form['cell-count']
            panelCount = request.form['panel-count']
            coreHandler.setPanel(ratedPower,ratedEfficiency,nominalCellTemp,panelArea,cellCount,panelCount)
        return render_template('enviroment.html')


    @app.route('/data/location', methods = ['POST'])
    def getLocation():
        data = request.json
        location = data['location']
        (lat,lon) = tuple(map(float,location.split(',')))
        coreHandler.setLocation(lat,lon)
        return {
            'message':'location co-ordinates is recieved'
        }

    @app.route('/data/radiation', methods = ['POST'])
    def getRadiation():
        data = request.json
        radiation = data['radiation']
        rad = float(radiation)
        coreHandler.setRadiation(rad)
        return {
            'message':'radiation value is recieved'
        }
        

    @app.route('/data/envimage', methods = ['POST','GET'])
    def getEnvImage():
        if request.method == 'POST':
            image = request.files['image']
            # saving image in envImages
            envImages = os.path.join(app.instance_path, 'envImages')
            image.save(envImages + '/' + secure_filename(image.filename))
            return render_template('output.html')
        else:
            render_template('data.html')

    @app.route('/data/output')
    def getOutput():
        return {
            'electricPower': coreHandler.getElectricPower(),
            'efficiency' : coreHandler.getEfficiency()
        }