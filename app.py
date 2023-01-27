#!/usr/bin/env python
# coding: utf-8

# In[4]:


from flask import Flask, render_template, request


# In[5]:


import joblib


# In[6]:


app = Flask(__name__) 


# In[7]:


def priority(kmeans_pred):
    if kmeans_pred[0] == 1:
        output = "Low Priority"
    elif kmeans_pred[0] == 2:
        output = "High Priority"
    else:
        output = "Medium Priority"
    return output


# In[8]:


@app.route("/", methods = ["GET", "POST"])
#adalah decorator harus dipake sebelum function.

def index():
    if request.method == "POST":
        satis = float(request.form.get("Satisfaction Level"))
        evaluation = float(request.form.get("Evaluation Score"))
        data = [[satis, evaluation]]
        model = joblib.load("cluster") 
        pred = priority(model.predict(data))
        
        return(render_template("index.html", result = pred))
    else:
        return(render_template("index.html", result = "Waiting"))


# In[9]:


if __name__ == "__main__":
    app.run()


# In[ ]:




