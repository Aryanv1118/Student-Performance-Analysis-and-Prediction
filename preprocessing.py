import pandas as pd

def encode_data(df):

    df["gender"] = df["gender"].map({
        "Male":1,
        "Female":0
    })

    df["parent_education"] = df["parent_education"].map({
        "Middle School":0,
        "High School":1,
        "Bachelor":2,
        "Master":3,
        "PhD":4
    })

    df["internet_access"] = df["internet_access"].map({
        "Yes":1,
        "No":0
    })

    df["extracurricular"] = df["extracurricular"].map({
        "Yes":1,
        "No":0
    })
    df["passed"] = df["passed"].map({
        "Yes":1,
        "No":0
    })

    return df