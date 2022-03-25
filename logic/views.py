from django.shortcuts import render
import pandas as pd

# Create your views here.

dataset=None
index=-1


def read_csv(request):
    global index,dataset
    if request.POST and request.FILES:
        print(request.FILES['dataset'])
        dataset=pd.read_excel(request.FILES['dataset'])
        #request.session['dataset']=dataset
        #request.session['index']=0
        index=-1
    context={
        'text':''
    }
    return next(request)


def label(request,label):
    try:
        dataset.loc[index,'Label'] = label
        print("Labelled")
        return next(request)
    except Exception as e:
        print(e)
        return render(request,'logic/error_happened.html')


def next(request):
    global index
    try:
        if index<len(dataset):
            index+=1
        if index%7==0:
            dataset.to_excel("results_sexism.xlsx",index=False,encoding='utf8')#constantly saving
        context={
            'text':dataset.iloc[index].tweet,
            'label':dataset.iloc[index].Label
        }
        return render(request,'logic/label_it.html',context)
    except Exception as e:
        print(e)
        return render(request,'logic/error_happened.html')
    finally:
        dataset.to_excel("results_sexism.xlsx",index=False,encoding='utf8')

def prec(request):
    global index
    try:
        if index>0:
            index-=1
        context={
            'text':dataset.iloc[index].tweet,
            'label':dataset.iloc[index].Label
        }
        return render(request,'logic/label_it.html',context)
    except Exception as e:
        print(e)
        return render(request,'logic/error_happened.html')
    finally:
        dataset.to_excel("results_sexism.xlsx",index=False,encoding='utf8')

def load(request):
    return render(request,'logic/load_dataset.html')




    