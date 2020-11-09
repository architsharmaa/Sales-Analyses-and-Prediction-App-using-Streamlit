import pandas as pd
import streamlit as st

from config import datafields, home_image

#page functioning
def app():

    #heading and text information
    html1 = '''
    <style>
    #pred_image{
      
     }
    #heading{
      color: #E65142;
      text-align:top-left;
      font-size: 45px;
    }
    #sub_heading1{
    color: #E65142;
    text-align: right;
    font-size: 30px;
    }
    #sub_heading2{
    color: #E65142;
    text-align: left;
    font-size: 30px;
      }
    #usage_instruction{
    text-align: right;
    font-size : 15px;
    }
    #data_info{
    text-align : left;
    font-sixe : 15px;
    }
    /* Rounded border */
    hr.rounded {
        border-top: 6px solid #E65142;
        border-radius: 5px;
    }
    </style>
    <h1 id = "heading"> Rossman Sales Analysis </h1>
    <h3>Rossmann operates over 3,000 drug stores in 7 European countries.<br>
    This website works on the data extracted from the Kaggle Competition<br>
    <a href = "https://www.kaggle.com/c/rossmann-store-sales/overview" target="_blank"><i><b>'Rossmann Store Sales-Forecast sales using store, promotion, and competitor data'</i></b></a>
    </h3>
    '''
    st.markdown(html1, unsafe_allow_html=True)
    st.image(home_image, width=700, output_format="PNG")
    html2 = '''
    <hr class="rounded">
    <h3 id = "sub_heading1">Usage Description&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</h3>
    <p id = "usage_instruction">The UI/UX for the app glides using the <b>Sidebar</b> to the left.&emsp;&emsp;<br>
    Access all the features of the app using it.The web app comes&nbsp;<br>
    with the features including -&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; <br>
    <b>1. Sales Analyses using <i> Data Visulations</i> based on <i>Seaborn</i><br>
    <b>2. Future Sale Prediction using <i>Decision Tree Algorithm</i>&emsp;&emsp;<br>
    <h3 id ="sub_heading2">Data Description&emsp;&emsp;&emsp;</h3>
    <p id ="data_info">The data is the <i>sales data</i> for the <b>financial year 2014</b> from <i> 1155 Rossman<br> 
    Drug Stores</i> The data is divided and analysed into <b> financial quaters</b>  for&nbsp;&nbsp;&nbsp;<br>  
    better analyses and assesment of the sales.&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</p>
    '''
    st.markdown(html2, unsafe_allow_html=True)

    df = pd.read_csv(datafields)
    data = [["Quarter1", "Jan, 2014 - Mar, 2014"], ["Quarter2", "Apr, 2014 - Jun, 2014"],["Quarter3", "Jul, 2014 - Sep, 2014"], 
    ["Quarter4", "Oct, 2014 - Dec, 2014"]]
    df2 = pd.DataFrame(data, columns=["Quarters", "Range"])

    #data description
    col1, col2 = st.beta_columns(2)
    
    button1 = col1.button("Data Fields")
    if(button1):
        st.table(df)
    button2 = col2.button("Data Breakup")
    if(button2):
      st.table(df2)

    
