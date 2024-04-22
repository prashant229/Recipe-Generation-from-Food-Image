from flask import render_template ,url_for,flash,redirect,request
from Foodimg2Ing import app
from Foodimg2Ing.output import output
import os


@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/', methods=['POST', 'GET'])
def predict():
    imagefile = request.files['imagefile']
    image_dir = os.path.join(app.root_path, 'static/images/demo_imgs')
    
    # Create the directory if it doesn't exist
    os.makedirs(image_dir, exist_ok=True)
    
    image_path = os.path.join(image_dir, imagefile.filename)
    imagefile.save(image_path)
    img = "/images/demo_imgs/" + imagefile.filename
    title, ingredients, recipe = output(image_path)
    return render_template('predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img)

@app.route('/<samplefoodname>')
def predictsample(samplefoodname):
    imagefile=os.path.join(app.root_path,'static/images',str(samplefoodname)+".jpg")
    img="/images/"+str(samplefoodname)+".jpg"
    title,ingredients,recipe = output(imagefile)
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)


# /Users/prashanttiwari/Downloads/recepie/Recipe-Generation-from-Food-Image-main/Foodimg2Ing/static/demo_imgs