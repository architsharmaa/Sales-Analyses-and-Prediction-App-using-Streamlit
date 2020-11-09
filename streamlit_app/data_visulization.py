import streamlit as st
import pandas as pd
import seaborn as sns

from config import quarter_1, quarter_2,quarter_3, quarter_4, quarter_1_datasales, quarter_2_datasales, quarter_3_datasales, quarter_4_datasales

# catplot
def cat(x, y, df, k):
    sns.catplot(x=x, y=y, data=df, kind=k,height=7, aspect=11.7/7)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


# catplot of larger size
def big_cat(x, y, df, k):
    sns.catplot(x=x, y=y, data=df, kind=k,height=7, aspect=11.7/8.27)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


# date specific plotting
def dateplot(x, y, df, k):
    sns.catplot(x=x, y=y, data=df, kind=k,height=7, aspect=11.7/7)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

#plotting the Sales vs StoreType
def salesvsstoretype():
    col1, col2 = st.beta_columns(2)
    type_chart = col1.selectbox("Select the Chart type", ('Strip', 'Boxen', 'Box'))
    data1 = col2.selectbox("Select the financial quarter", ('quarter 1', 'quarter 2', 'quarter 3', 'quarter 4'))
    if (type_chart == 'Strip'):
        if (data1 == 'quarter 1'):
            cat("StoreType", "Sales", quarter1, 'strip')
        elif (data1 == 'quarter 2'):
            cat("StoreType", "Sales", quarter2, 'strip')
        elif (data1 == 'quarter 3'):
            cat("StoreType", "Sales", quarter3, 'strip')
        else:
            cat("StoreType", "Sales", quarter3, 'strip')
    elif (type_chart  == 'Boxen'):
        if (data1 == 'quarter 1'):
            cat("StoreType", "Sales", quarter1, 'boxen')
        elif (data1 == 'quarter 2'):
            cat("StoreType", "Sales", quarter2, 'boxen')
        elif (data1 == 'quarter 3'):
            cat("StoreType", "Sales", quarter3, 'boxen')
        else:
            cat("StoreType", "Sales", quarter3, 'boxen')
    else:
        if (data1 == 'quarter 1'):
            cat("StoreType", "Sales", quarter1, 'box')
        elif (data1 == 'quarter 2'):
            cat("StoreType", "Sales", quarter2, 'box')
        elif (data1 == 'quarter 3'):
            cat("StoreType", "Sales", quarter3, 'box')
        else:
            cat("StoreType", "Sales", quarter3, 'box')

#plotting the WeekDay vs Sales
def weekdayvssales():
    col1, col2 = st.beta_columns(2)
    type1 = col1.selectbox("Select the Chart type", ('Bar', 'Strip', 'Time Series Chart'))
    data1 = col2.selectbox("Select the financial quarter", ('quarter 1', 'quarter 2', 'quarter 3', 'quarter 4'))
    if (type1 == 'Bar'):
        if (data1 == 'quarter 1'):
            big_cat("DayOfWeekName","Sales", quarter1, "bar")
        elif (data1 == 'quarter 2'):
            big_cat("DayOfWeekName","Sales", quarter2, "bar")
        elif (data1 == 'quarter 3'):
            big_cat("DayOfWeekName","Sales", quarter3, "bar")
        else:
            big_cat("DayOfWeekName","Sales", quarter4, "bar")
    elif (type1 == 'Strip'):
        if (data1 == 'quarter 1'):
            big_cat("DayOfWeekName", "Sales", quarter1, 'strip')
        elif (data1 == 'quarter 2'):
            big_cat("DayOfWeekName", "Sales", quarter2, 'strip')
        elif (data1 == 'quarter 3'):
            big_cat("DayOfWeekName", "Sales", quarter3, 'strip')
        else:
            big_cat("DayOfWeekName", "Sales", quarter3, 'strip')
    else:
        if (data1 == 'quarter 1'):
            big_cat("DayOfWeekName", "Sales", quarter1, 'point')
        elif (data1 == 'quarter 2'):
            big_cat("DayOfWeekName", "Sales", quarter2, 'point')
        elif (data1 == 'quarter 3'):
            big_cat("DayOfWeekName", "Sales", quarter3, 'point')
        else:
            big_cat("DayOfWeekName", "Sales", quarter3, 'point')

#plotting the month vs sales
def monthvssales():
    col1, col2 = st.beta_columns(2)
    type1 = col1.selectbox("Select the Chart type", ('Bar',))
    data1 = col2.selectbox("Select the financial quarter", ('quarter 1', 'quarter 2', 'quarter 3', 'quarter 4'))
    if (type1 == 'Bar'):
        if (data1 == 'quarter 1'):
            cat("MonthName", "Sales", quarter1, "bar")
        elif (data1 == 'quarter 2'):
            cat("MonthName", "Sales", quarter2, "bar")
        elif (data1 == 'quarter 3'):
            cat("MonthName", "Sales", quarter3, "bar")
        else:
            cat("MonthName", "Sales", quarter4, "bar")

#plotting customer vs storetype
def customervsstoretype():
    col1, col2 = st.beta_columns(2)
    type1 = col1.selectbox("Select the Chart type", ('Bar',))
    data1 = col2.selectbox("Select the financial quarter", ('quarter 1', 'quarter 2', 'quarter 3', 'quarter 4'))
    if (type1 == 'Bar'):
        if (data1 == 'quarter 1'):
            cat("StoreType", "Customers", quarter1, "bar")
        elif (data1 == 'quarter 2'):
            cat("StoreType", "Customers", quarter2, "bar")
        elif (data1 == 'quarter 3'):
            cat("StoreType", "Customers", quarter3, "bar")
        else:
            cat("StoreType", "Customers", quarter4, "bar")

#plotting the datevsales
def datevssales():
    col1, col2 = st.beta_columns(2)
    type1 = col1.selectbox("Select the Chart type", ('Time Series Chart',))
    data1 = col2.selectbox("Select the financial quarter", ('quarter 1', 'quarter 2', 'quarter 3', 'quarter 4'))
    if (type1 == 'Time Series Chart'):
        if (data1 == 'quarter 1'):
            dateplot("Date", "Sales", quarter1_datasales, "point")
        elif (data1 == 'quarter 2'):
            dateplot("Date", "Sales", quarter2_datasales, "point")
        elif (data1 == 'quarter 3'):
            dateplot("Date", "Sales", quarter3_datasales, "point")
        else:
            dateplot("Date", "Sales", quarter4_datasales, "point")

#page functioning
def app():
    html1 = '''
            <style>
            #heading{
              color: #E65142;
              text-align:top-left;
              font-size: 45px;
            }
            </style>
            <h1 id = "heading"> Sales Data Analyses</h1>
        '''
    st.markdown(html1, unsafe_allow_html=True)

    #button functionality for data points
    b1 = st.selectbox("Select the Analyses Point",('StoreType vs Sales','WeekDay vs Sales','Month vs Sales','Customer vs StoreType','Date vs Sales'))
    if(b1 == 'StoreType vs Sales'):
        salesvsstoretype()
    elif(b1 == 'WeekDay vs Sales'):
        weekdayvssales()
    elif(b1 == 'Month vs Sales'):
        monthvssales()
    elif(b1 == 'Customer vs StoreType'):
        customervsstoretype()
    elif(b1 == 'Date vs Sales'):
        datevssales()

#data imports
quarter1 = pd.read_csv(quarter_1)
quarter2 = pd.read_csv(quarter_2)
quarter3 = pd.read_csv(quarter_3)
quarter4 = pd.read_csv(quarter_4)

quarter1_datasales = pd.read_csv(quarter_1_datasales)
quarter2_datasales = pd.read_csv(quarter_2_datasales)
quarter3_datasales = pd.read_csv(quarter_3_datasales)
quarter4_datasales = pd.read_csv(quarter_4_datasales)




