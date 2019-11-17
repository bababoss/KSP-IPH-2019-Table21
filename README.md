# KSP-IPH-2019-Table21
#Tool and Technologies
```
Programming language: Python, Javascript
Frameworks and Libs:  Pytorch, OpenCV, TensorFlow, Keras,Pandas, Scikit-learn, Plotly, W3.css, Inceptionv3
Technologies: NLP, Data analytics, State of art ML and DL  like:- UlmFIT fine tune model, VGG16 DL Network, RandomForestRegrassor,Sequence to sequuence model

```
# Dependencies install
```
pip install -r requirements.txt

```
# Insights from Data:
```
  1. Accidents in the month of January, May and December are comparatively more than other months.
  2. Accidents on Friday, Saturday and Sunday are relatively more than other weekdays.
  3. Correlation of features tells us:
      a. Accidents on bridges are more on narrow bridges and culverts.
      b. Bottleneck accident spots are arterial roads, asphalted road separation and roads which are crest of hill.
  4. Feature Relevance towards Road Accident
  
```

![alt text](http://34.206.109.62:8001/media/uploaded_model/feature_relevance.jpg)

# Dashboard:

![alt text](http://34.206.109.62:8001/media/uploaded_model/dashboard_home.png)

# Correlation analytics:

![alt text](http://34.206.109.62:8001/media/uploaded_model/correlation_graph.png)

# location_images_tensorboard
![alt text](http://34.206.109.62:8001/media/uploaded_model/location_images_tensorboard.png)


# accidents_prediction
![alt text](http://34.206.109.62:8001/media/uploaded_model/accidents_prediction.png)

# Architecture Diagram:
![alt text](http://34.206.109.62:8001/media/uploaded_model/MoRTH.png)

# HOW run service
## Analytics and prediction service
```
python heatmap_service.py

```
## Dashboard service

```
Run service from:
html/grid.html

```
