from statistics import mode
from django.shortcuts import render
import pickle
import pandas as pd

# load the model
model = pickle.load(open('heartapp/model/heart_pipe.sav', 'rb'))

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def predict(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        chest_pain = request.POST.get('chest_pain')
        rest_blood = float(request.POST.get('rest_blood'))
        choles = float(request.POST.get('choles'))
        fast_sugar = request.POST.get('fast_sugar')
        ecg = request.POST.get('ecg')
        heart_rate = int(request.POST.get('heart_rate'))
        angina = request.POST.get('angina')
        peak = float(request.POST.get('peak'))
        slope = request.POST.get('slope')

        # Predict
        list = [age, gender, chest_pain, rest_blood, choles, fast_sugar, ecg, heart_rate, angina, peak, slope]
        print(list)
        data = pd.DataFrame([list], columns = ['age', 'sex', 'chest_pain_type', 'resting_bp_s',
         'cholesterol', 'fasting_blood_sugar', 'resting_ecg', 'max_heart_rate', 
         'exercise_angina', 'oldpeak', 'ST_slope'])
        pred = model.predict(data)
        x = pred[0]

        context = {
            'data':list,
            'pred': x
        }

        return render(request, 'index.html', context)