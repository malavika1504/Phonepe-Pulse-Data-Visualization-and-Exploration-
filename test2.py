import os
import json
import pandas as pd
import psycopg2
import requests
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go

#aggregated_insurance

path="C:/Users/DELL/Desktop/p2/pulse/data/aggregated/insurance/country/india/state/"
agg_insur_list=os.listdir(path)

columns={"States":[],"Years":[],"Quarter":[],"Insurance_type":[],"Insurance_count":[],"Insurance_amount":[]}

for s in agg_insur_list:
    states=path+s+"/"
    agg_yr_list=os.listdir(states)

    for y in agg_yr_list:
        years=states+y+"/"
        agg_jsfl_list=os.listdir(years)

        for f in agg_jsfl_list:
            files=years+f
            data=open(files,"r")
            A=json.load(data)
            
            for i in A["data"]["transactionData"]:
                Name = i["name"]
                Count = i["paymentInstruments"][0]["count"]
                Amount = i["paymentInstruments"][0]["amount"]
                columns["Insurance_type"].append(Name)
                columns["Insurance_count"].append(Count)
                columns["Insurance_amount"].append(Amount)
                columns["States"].append(s)
                columns["Years"].append(y)
                columns["Quarter"].append(int(f.strip(".json")))

agg_insur=pd.DataFrame(columns)
agg_insur["States"] = agg_insur["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
agg_insur["States"] = agg_insur["States"].str.replace("-"," ")
agg_insur["States"] = agg_insur["States"].str.title()
agg_insur['States'] = agg_insur['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#aggregated_transaction
path1="C:/Users/DELL/Desktop/p2/pulse/data/aggregated/transaction/country/india/state/"
agg_trans_list=os.listdir(path1)

columns1={'States':[],'Years':[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}

for s in agg_trans_list:
    states=path1+s+"/"
    agg_yr_list=os.listdir(states)
    
    for y in agg_yr_list:
        years=states+y+"/"
        agg_jsfl_list=os.listdir(years)
        
        for f in agg_jsfl_list:
            files=years+f
            data=open(files,"r")
            D=json.load(data)

            for i in D["data"]["transactionData"]:
                Name=i["name"]
                Count=i["paymentInstruments"][0]["count"]
                Amount=i["paymentInstruments"][0]["amount"]
                columns1["Transaction_type"].append(Name)
                columns1["Transaction_count"].append(Count)
                columns1["Transaction_amount"].append(Amount)
                columns1["States"].append(s)
                columns1["Years"].append(y)
                columns1["Quarter"].append(int(f.strip(".json")))

agg_trans=pd.DataFrame(columns1)
agg_trans["States"] = agg_trans["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
agg_trans["States"] = agg_trans["States"].str.replace("-"," ")
agg_trans["States"] = agg_trans["States"].str.title()
agg_trans['States'] = agg_trans['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#aggregated_users
path2="C:/Users/DELL/Desktop/p2/pulse/data/aggregated/user/country/india/state/"
agg_user_list=os.listdir(path2)

columns2={"States":[],"Years":[],"Quarter":[],"Brands":[],"Transaction_count":[],"Percentage":[]}

for s in agg_user_list:
    states=path2+s+"/"
    agg_yr_list=os.listdir(states)

    for y in agg_yr_list:
        years=states+y+"/"
        agg_jsfl_list=os.listdir(years)

        for f in agg_jsfl_list:
            files=years+f
            data=open(files,"r")
            B=json.load(data)

            try:
                for i in B["data"]["usersByDevice"]:
                    Brand=i["brand"]
                    Count=i["count"]
                    Percentage=i["percentage"]
                    columns2["Brands"].append(Brand)
                    columns2["Transaction_count"].append(Count)
                    columns2["Percentage"].append(Percentage)
                    columns2["States"].append(s)
                    columns2["Years"].append(y)
                    columns2["Quarter"].append(int(f.strip(".json")))
            except:
                pass

agg_user=pd.DataFrame(columns2)
agg_user["States"] = agg_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
agg_user["States"] = agg_user["States"].str.replace("-"," ")
agg_user["States"] = agg_user["States"].str.title()
agg_user['States'] = agg_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#map_insurance

path3="C:/Users/DELL/Desktop/p2/pulse/data/map/insurance/hover/country/india/state/"
map_insur_list=os.listdir(path3)

columns3={"States":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}

for s in map_insur_list:
    states=path3+s+"/"
    map_yr_list=os.listdir(states)

    for y in map_yr_list:
        years=states+y+"/"
        map_jsfl_list=os.listdir(years)

        for f in map_jsfl_list:
            files=years+f
            data=open(files,"r")
            A=json.load(data)
            
            for i in A["data"]["hoverDataList"]:
                Name = i["name"]
                Count = i["metric"][0]["count"]
                Amount = i["metric"][0]["amount"]
                columns3["Districts"].append(Name)
                columns3["Transaction_count"].append(Count)
                columns3["Transaction_amount"].append(Amount)
                columns3["States"].append(s)
                columns3["Years"].append(y)
                columns3["Quarter"].append(int(f.strip(".json")))

map_insur=pd.DataFrame(columns3)
map_insur["States"] = map_insur["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_insur["States"] = map_insur["States"].str.replace("-"," ")
map_insur["States"] = map_insur["States"].str.title()
map_insur['States'] = map_insur['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#map_trans

path4="C:/Users/DELL/Desktop/p2/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list=os.listdir(path4)

columns4={"States":[], "Years":[], "Quarter":[],"Districts":[], "Transaction_count":[],"Transaction_amount":[]}

for s in map_trans_list:
    states=path4+s+"/"
    map_yr_list=os.listdir(states)

    for y in map_yr_list:
        years=states+y+"/"
        map_jsfl_list=os.listdir(years)

        for f in map_jsfl_list:
            files=years+f
            data=open(files,"r")
            C=json.load(data)

            for i in C["data"]["hoverDataList"]:
                Name=i["name"]
                Count=i["metric"][0]["count"]
                Amount=i["metric"][0]["amount"]
                columns4["Districts"].append(Name)
                columns4["Transaction_count"].append(Count)
                columns4["Transaction_amount"].append(Amount)
                columns4["States"].append(s)
                columns4["Years"].append(y)
                columns4["Quarter"].append(int(f.strip(".json")))

map_trans=pd.DataFrame(columns4)
map_trans["States"] = map_trans["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_trans["States"] = map_trans["States"].str.replace("-"," ")
map_trans["States"] = map_trans["States"].str.title()
map_trans['States'] = map_trans['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#map_users

path5="C:/Users/DELL/Desktop/p2/pulse/data/map/user/hover/country/india/state/"
map_user_list=os.listdir(path5)

columns5={"States":[], "Years":[], "Quarter":[], "Districts":[], "RegisteredUser":[], "AppOpens":[]}

for s in map_user_list:
    states=path5+s+"/"
    map_yr_list=os.listdir(states)

    for y in map_yr_list:
        years=states+y+"/"
        map_jsfl_list=os.listdir(years)

        for f in map_jsfl_list:
            files=years+f
            data=open(files,"r")
            E=json.load(data)

            for i in E["data"]["hoverData"].items():
                District = i[0]
                Registereduser = i[1]["registeredUsers"]
                Appopens = i[1]["appOpens"]
                columns5["Districts"].append(District)
                columns5["RegisteredUser"].append(Registereduser)
                columns5["AppOpens"].append(Appopens)
                columns5["States"].append(s)
                columns5["Years"].append(y)
                columns5["Quarter"].append(int(f.strip(".json")))

map_user=pd.DataFrame(columns5)
map_user["States"] = map_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_user["States"] = map_user["States"].str.replace("-"," ")
map_user["States"] = map_user["States"].str.title()
map_user['States'] = map_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#Top_insurance

path6="C:/Users/DELL/Desktop/p2/pulse/data/top/insurance/country/india/state/"
top_insur_list=os.listdir(path6)

columns6={"States":[],"Years":[],"Quarter":[],"Pincodes":[],"Transaction_count":[],"Transaction_amount":[]}

for s in top_insur_list:
    states=path6+s+"/"
    top_yr_list=os.listdir(states)

    for y in top_yr_list:
        years=states+y+"/"
        top_jsfl_list=os.listdir(years)

        for f in top_jsfl_list:
            files=years+f
            data=open(files,"r")
            A=json.load(data)
            
            for i in A["data"]["pincodes"]:
                EntityName = i["entityName"]
                Count = i["metric"]["count"]
                Amount = i["metric"]["amount"]
                columns6["Pincodes"].append(EntityName)
                columns6["Transaction_count"].append(Count)
                columns6["Transaction_amount"].append(Amount)
                columns6["States"].append(s)
                columns6["Years"].append(y)
                columns6["Quarter"].append(int(f.strip(".json")))


Top_insur=pd.DataFrame(columns6)
Top_insur["States"] = Top_insur["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_insur["States"] = Top_insur["States"].str.replace("-"," ")
Top_insur["States"] = Top_insur["States"].str.title()
Top_insur['States'] = Top_insur['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

#top_trans
path7="C:/Users/DELL/Desktop/p2/pulse/data/top/transaction/country/india/state/"
top_trans_list=os.listdir(path7)

columns7={"States":[],"Years":[], "Quarter":[],"Pincodes":[],"Transaction_count":[],"Transaction_amount":[]}

for s in top_trans_list:
    states=path7+s+"/"
    top_yr_list=os.listdir(states)

    for y in top_yr_list:
        years=states+y+"/"
        top_jsfl_list=os.listdir(years)

        for f in top_jsfl_list:
            files=years+f
            data=open(files,"r")
            F=json.load(data)

            for i in F["data"]["pincodes"]:
                EntityName=i["entityName"]
                Count=i["metric"]["count"]
                Amount=i["metric"]["amount"]
                columns7["Pincodes"].append(EntityName)
                columns7["Transaction_count"].append(Count)
                columns7["Transaction_amount"].append(Amount)
                columns7["States"].append(s)
                columns7["Years"].append(y)
                columns7["Quarter"].append(int(f.strip(".json")))

Top_trans=pd.DataFrame(columns7)
Top_trans["States"] = Top_trans["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_trans["States"] = Top_trans["States"].str.replace("-"," ")
Top_trans["States"] = Top_trans["States"].str.title()
Top_trans['States'] = Top_trans['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


#top_user

path8="C:/Users/DELL/Desktop/p2/pulse/data/top/user/country/india/state/"
top_user_list=os.listdir(path8)

columns8={"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

for s in top_user_list:
    states=path8+s+"/"
    top_yr_list=os.listdir(states)

    for y in top_yr_list:
        years=states+y+"/"
        top_jsfl_list=os.listdir(years)

        for f in top_jsfl_list:
            files=years+f
            data=open(files,"r")
            G=json.load(data)

            for i in G["data"]["pincodes"]:
                Name = i["name"]
                Registereduser = i["registeredUsers"]
                columns8["Pincodes"].append(Name)
                columns8["RegisteredUser"].append(Registereduser)
                columns8["States"].append(s)
                columns8["Years"].append(y)
                columns8["Quarter"].append(int(f.strip(".json")))

Top_user=pd.DataFrame(columns8)
Top_user["States"] = Top_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_user["States"] = Top_user["States"].str.replace("-"," ")
Top_user["States"] = Top_user["States"].str.title()
Top_user['States'] = Top_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



#tb creation & sql connect
mydb=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="12345",
                      port="5432",
                      database="phonepe")
mycursor=mydb.cursor()

#aggregated_insurance_table
mycursor.execute("""Drop table if exists agg_insu""")
mydb.commit()

mycursor.execute("""create table if not exists agg_insu
                 (States varchar(150),
                 Years int,
                 Quarter int,
                 Insurance_type varchar(150),
                 Insurance_count bigint,
                 Insurance_amount bigint)""")
mydb.commit()

for index,row in agg_insur.iterrows():
    i="""insert into agg_insu(States,
                                Years,
                                Quarter,
                                Insurance_type,
                                Insurance_count,
                                Insurance_amount)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Insurance_type"],
            row["Insurance_count"],
            row["Insurance_amount"])
    mycursor.execute(i,values)
    mydb.commit()


#aggregated_transaction_Table
mycursor.execute("""Drop table if exists agg_tran""")
mydb.commit()

mycursor.execute("""create table if not exists agg_tran
                 (States varchar(150),
                 Years int,
                 Quarter int,
                 Transaction_type varchar(150),
                 Transaction_count bigint,
                 Transaction_amount bigint)""")
mydb.commit()

for index,row in agg_trans.iterrows():
    i="""insert into agg_tran(States,
                                Years,
                                Quarter,
                                Transaction_type,
                                Transaction_count,
                                Transaction_amount)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Transaction_type"],
            row["Transaction_count"],
            row["Transaction_amount"])
    mycursor.execute(i,values)
    mydb.commit()


#aggregated_user_table

mydb=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="12345",
                      port="5432",
                      database="phonepe")
mycursor=mydb.cursor()

mycursor.execute("""Drop table if exists agg_users""")
mydb.commit()

mycursor.execute("""create table if not exists agg_users
                 (States varchar(150),
                 Years int,
                 Quarter int,
                 Brands varchar(50),
                 Transaction_count bigint,
                 Percentage float)""")
mydb.commit()

for index,row in agg_user.iterrows():
    i="""insert into agg_users(States,
                                Years,
                                Quarter,
                                Brands,
                                Transaction_count,
                                Percentage)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Brands"],
            row["Transaction_count"],
            row["Percentage"])
    mycursor.execute(i,values)
    mydb.commit()


#map_insurance_table
mycursor.execute("""Drop table if exists map_insu""")
mydb.commit()

mycursor.execute("""create table if not exists map_insu
                 (States varchar(150),
                 Years int,
                 Quarter int,
                 Districts varchar(150),
                 Transaction_count bigint,
                 Transaction_amount float)""")
mydb.commit()

for index,row in map_insur.iterrows():
    i="""insert into map_insu(States,
                                Years,
                                Quarter,
                                Districts,
                                Transaction_count,
                                Transaction_amount)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Districts"],
            row["Transaction_count"],
            row["Transaction_amount"])
    mycursor.execute(i,values)
    mydb.commit()


#map_trans_table

mydb=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="12345",
                      port="5432",
                      database="phonepe")
mycursor=mydb.cursor()

mycursor.execute("""Drop table if exists map_tran""")
mydb.commit()

mycursor.execute("""create table if not exists map_tran
                 (States varchar(100),
                 Years int,
                 Quarter int,
                 Districts varchar(50),
                 Transaction_count bigint,
                 Transaction_amount float)""")
mydb.commit()

for index,row in map_trans.iterrows():
    i="""insert into map_tran(States,
                                Years,
                                Quarter,
                                Districts,
                                Transaction_count,
                                Transaction_amount)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Districts"],
            row["Transaction_count"],
            row["Transaction_amount"])
    mycursor.execute(i,values)
    mydb.commit()


#map_users_table

mydb=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="12345",
                      port="5432",
                      database="phonepe")
mycursor=mydb.cursor()

mycursor.execute("""Drop table if exists map_users""")
mydb.commit()

mycursor.execute("""create table if not exists map_users
                 (States varchar(100),
                 Years int,
                 Quarter int,
                 Districts varchar(50),
                 RegisteredUser bigint,
                 AppOpens bigint)""")
mydb.commit()

for index,row in map_user.iterrows():
    i="""insert into map_users(States,
                                Years,
                                Quarter,
                                Districts,
                                RegisteredUser,
                                AppOpens)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Districts"],
            row["RegisteredUser"],
            row["AppOpens"])
    mycursor.execute(i,values)
    mydb.commit()


#top_insurance_table
mycursor.execute("""Drop table if exists top_insu""")
mydb.commit()

mycursor.execute("""create table if not exists top_insu
                 (States varchar(150),
                 Years int,
                 Quarter int,
                 Pincodes int,
                 Transaction_count bigint,
                 Transaction_amount bigint)""")
mydb.commit()

for index,row in Top_insur.iterrows():
    i="""insert into top_insu(States,
                                Years,
                                Quarter,
                                Pincodes,
                                Transaction_count,
                                Transaction_amount)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Pincodes"],
            row["Transaction_count"],
            row["Transaction_amount"])
    mycursor.execute(i,values)
    mydb.commit()


#top_trans_table

mydb=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="12345",
                      port="5432",
                      database="phonepe")
mycursor=mydb.cursor()

mycursor.execute("""Drop table if exists top_tran""")
mydb.commit()

mycursor.execute("""create table if not exists top_tran
                 (States varchar(100),
                 Years int,
                 Quarter int,
                 Pincodes int,
                 Transaction_count bigint,
                 Transaction_amount bigint)""")
mydb.commit()

for index,row in Top_trans.iterrows():
    i="""insert into top_tran(States,
                                Years,
                                Quarter,
                                Pincodes,
                                Transaction_count,
                                Transaction_amount)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Pincodes"],
            row["Transaction_count"],
            row["Transaction_amount"])
    mycursor.execute(i,values)
    mydb.commit()


#top_user_table

mydb=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="12345",
                      port="5432",
                      database="phonepe")
mycursor=mydb.cursor()

mycursor.execute("""Drop table if exists top_users""")
mydb.commit()

mycursor.execute("""create table if not exists top_users
                 (States varchar(100),
                 Years int,
                 Quarter int,
                 Pincodes int,
                 RegisteredUser bigint)""")
mydb.commit()

for index,row in Top_user.iterrows():
    i="""insert into top_users(States,
                                Years,
                                Quarter,
                                Pincodes,
                                RegisteredUser)
                                VALUES(%s,%s,%s,%s,%s)"""
    
    values=(row["States"],
            row["Years"],
            row["Quarter"],
            row["Pincodes"],
            row["RegisteredUser"])
    mycursor.execute(i,values)
    mydb.commit()

#sql to dataframe
mydb=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="12345",
                      port="5432",
                      database="phonepe")
mycursor=mydb.cursor()

#aggregated_insurance
mycursor.execute("""select * from agg_insu""")
mydb.commit()
d0=mycursor.fetchall()
ag_insur=pd.DataFrame(d0,columns=("States","Years","Quarter","Transaction_type","Transaction_count","Transaction_amount"))

#aggregated_transaction
mycursor.execute("""select * from agg_tran""")
mydb.commit()
d1=mycursor.fetchall()
ag_trans=pd.DataFrame(d1,columns=("States","Years","Quarter","Transaction_type","Transaction_count","Transaction_amount"))

#aggregated_user
mycursor.execute("""select * from agg_users""")
mydb.commit()
d2=mycursor.fetchall()
ag_user=pd.DataFrame(d2,columns=("States","Years","Quarter","Brands","Transaction_count","Percentage"))

#map_insurance
mycursor.execute("""select * from map_insu""")
mydb.commit()
d3=mycursor.fetchall()
ma_insur=pd.DataFrame(d3,columns=("States","Years","Quarter","Districts","Transaction_count","Transaction_amount"))

#map_transaction
mycursor.execute("""select * from map_tran""")
mydb.commit()
d4=mycursor.fetchall()
ma_trans=pd.DataFrame(d4,columns=("States","Years","Quarter","Districts","Transaction_count","Transaction_amount"))

#map_user
mycursor.execute("""select * from map_users""")
mydb.commit()
d5=mycursor.fetchall()
ma_user=pd.DataFrame(d5,columns=("States","Years","Quarter","Districts","RegisteredUser","AppOpens"))

#top_insurance
mycursor.execute("""select * from top_insu""")
mydb.commit()
d6=mycursor.fetchall()
to_insur=pd.DataFrame(d6,columns=("States","Years","Quarter","Pincodes","Transaction_count","Transaction_amount"))

#top_transaction
mycursor.execute("""select * from top_tran""")
mydb.commit()
d7=mycursor.fetchall()
to_trans=pd.DataFrame(d7,columns=("States","Years","Quarter","Pincodes","Transaction_count","Transaction_amount"))

#top_user
mycursor.execute("""select * from top_users""")
mydb.commit()
d8=mycursor.fetchall()
to_user=pd.DataFrame(d8,columns=("States","Years","Quarter","Pincodes","RegisteredUser"))


def agg_insur_yr(df,yr):
    aiy=df[df["Years"]==yr]
    aiy.reset_index(drop=True,inplace=True)
    aiy_g=aiy.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
    aiy_g.reset_index(inplace=True)

    col1,col2=st.columns(2)
    with col1:
        fig_amt= px.bar(aiy_g, x="States", y= "Transaction_amount",title= f"{yr} TRANSACTION AMOUNT",
                            width=600, height= 600, color_discrete_sequence=px.colors.sequential.Plasma_r)
        st.plotly_chart(fig_amt)
    
    with col2:
        fig_count= px.bar(aiy_g, x="States", y= "Transaction_count",title= f"{yr} TRANSACTION COUNT",
                          width=600, height= 600, color_discrete_sequence=px.colors.sequential.Plasma)
        st.plotly_chart(fig_count)

    col1,col2=st.columns(2)
    with col1:
        url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data= json.loads(response.content)
        states_name_tra= [feature["properties"]["ST_NM"] for feature in data["features"]]
        states_name_tra.sort()
        

        fig_1= px.choropleth(aiy_g, geojson= data, locations= "States", featureidkey= "properties.ST_NM",
                                 color= "Transaction_amount", color_continuous_scale= "Bluered",
                                 range_color= (aiy_g["Transaction_amount"].min(),aiy_g["Transaction_amount"].max()),
                                 title = f"{yr} TRANSACTION AMOUNT",
                                 width =600, height= 650)
        fig_1.update_geos(fitbounds= "locations",visible =False)
        st.plotly_chart(fig_1)

    with col2:

        fig_2= px.choropleth(aiy_g, geojson= data, locations= "States", featureidkey= "properties.ST_NM",
                                 color= "Transaction_count", color_continuous_scale= "Agsunset",
                                 range_color= (aiy_g["Transaction_count"].min(),aiy_g["Transaction_count"].max()),
                                 hover_name= "States",title = f"{yr} TRANSACTION COUNT",
                                 width =600, height= 650)
        fig_2.update_geos(fitbounds= "locations",visible =False)
        
        st.plotly_chart(fig_2)


    return aiy


def agg_insur_YQ(df,quarter):
    aiyq=df[df["Quarter"]==quarter]
    aiyq.reset_index(drop=True,inplace=True)
    aiyq_g= aiyq.groupby("States")[["Transaction_count", "Transaction_amount"]].sum()
    aiyq_g.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_q_amount= px.bar(aiyq_g, x= "States", y= "Transaction_amount", 
                            title= f"{aiyq['Years'].min()} AND {quarter} TRANSACTION AMOUNT",width= 600, height=650,
                            color_discrete_sequence=px.colors.sequential.Burg_r)
        st.plotly_chart(fig_q_amount)

    with col2:
        fig_q_count= px.bar(aiyq_g, x= "States", y= "Transaction_count", 
                            title= f"{aiyq['Years'].min()} AND {quarter} TRANSACTION COUNT",width= 600, height=650,
                            color_discrete_sequence=px.colors.sequential.RdBu_r)
        st.plotly_chart(fig_q_count)

    col1,col2= st.columns(2)
    with col1:

        url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data2= json.loads(response.content)
        states_name_tra= [feature["properties"]["ST_NM"] for feature in data2["features"]]
        states_name_tra.sort()

        fig_india_1= px.choropleth(aiyq_g, geojson= data2, locations= "States", featureidkey= "properties.ST_NM",
                                 color= "Transaction_amount", color_continuous_scale= "Hot",
                                 range_color= (aiyq_g["Transaction_amount"].min(),aiyq_g["Transaction_amount"].max()),
                                 hover_name= "States",title = f"{aiyq['Years'].min()} AND {quarter} TRANSACTION AMOUNT",
                                 fitbounds= "locations",width =600, height= 600)
        fig_india_1.update_geos(visible =False)
        
        st.plotly_chart(fig_india_1)
    with col2:

        fig_india_2= px.choropleth(aiyq_g, geojson= data2, locations= "States", featureidkey= "properties.ST_NM",
                                 color= "Transaction_count", color_continuous_scale= "Blackbody",
                                 range_color= (aiyq_g["Transaction_count"].min(),aiyq_g["Transaction_count"].max()),
                                 hover_name= "States",title = f"{aiyq['Years'].min()} AND {quarter} TRANSACTION COUNT",
                                 fitbounds= "locations",width =600, height= 600)
        fig_india_2.update_geos(visible =False)
        
        st.plotly_chart(fig_india_2)
    
    return aiyq 

def agg_trans_type(df,state):
    state_1=df[df["States"]==state]
    state_1.reset_index(inplace=True)

    att_g=state_1.groupby("Transaction_type")[["Transaction_count","Transaction_amount"]].sum()
    att_g.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:

        fig_hbar_1= px.bar(att_g, x= "Transaction_count", y= "Transaction_type", orientation="h",
                        color_discrete_sequence=px.colors.sequential.Turbo_r, width= 600,height= 600, 
                        title= f"{state.upper()} TRANSACTION TYPES AND TRANSACTION COUNT")
        st.plotly_chart(fig_hbar_1)

    with col2:

        fig_hbar_2= px.bar(att_g, x= "Transaction_amount", y= "Transaction_type", orientation="h",
                        color_discrete_sequence=px.colors.sequential.Greens_r, width= 600,height= 600,
                        title= f"{state.upper()} TRANSACTION TYPES AND TRANSACTION AMOUNT")
        st.plotly_chart(fig_hbar_2)

def agg_user_plot1(df,year):
    auy= df[df["Years"] == year]
    auy.reset_index(drop= True, inplace= True)
    
    auy_g= pd.DataFrame(auy.groupby("Brands")["Transaction_count"].sum())
    auy_g.reset_index(inplace= True)

    fig_line= px.bar(auy_g, x="Brands",y= "Transaction_count", title=f"{year} BRANDS AND TRANSACTION COUNT",
                    width=800,color_discrete_sequence=px.colors.sequential.matter)
    st.plotly_chart(fig_line)

    return auy

def agg_user_plot2(df,quarter):
    auq= df[df["Quarter"] == quarter]
    auq.reset_index(drop= True, inplace= True)

    fig_pie= px.pie(data_frame=auq, names= "Brands", values="Transaction_count", hover_data= "Percentage",
                      width=800,title=f"{quarter} QUARTER TRANSACTION COUNT PERCENTAGE",hole=0.5, color_discrete_sequence= px.colors.sequential.haline_r)
    st.plotly_chart(fig_pie)

    return auq

def agg_user_plot3(df,state):
    aus= df[df["States"] == state]
    aus.reset_index(drop= True, inplace= True)

    aus_g= pd.DataFrame(aus.groupby("Brands")["Transaction_count"].sum())
    aus_g.reset_index(inplace= True)

    fig_scatter= px.line(aus_g, x= "Brands", y= "Transaction_count", markers= True,width=800,color_discrete_sequence= px.colors.sequential.RdBu_r)
    st.plotly_chart(fig_scatter)

def map_insure_plot1(df,state):
    mis= df[df["States"] == state]
    mis_g= mis.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
    mis_g.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_map_bar= px.bar(mis_g, x= "Districts", y= "Transaction_amount",
                              width=600, height=600, title= f"{state.upper()} DISTRICTS TRANSACTION AMOUNT",
                              color_discrete_sequence= px.colors.sequential.Purp_r)
        st.plotly_chart(fig_map_bar)

    with col2:
        fig_map_bar= px.bar(mis_g, x= "Districts", y= "Transaction_count",
                              width=600, height= 600, title= f"{state.upper()} DISTRICTS TRANSACTION COUNT",
                              color_discrete_sequence= px.colors.sequential.Mint)
        
        st.plotly_chart(fig_map_bar)

def map_insur_plot2(df,state):
    mis= df[df["States"] == state]
    mis_g= mis.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
    mis_g.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:
        fig_map_pie= px.pie(mis_g, names= "Districts", values= "Transaction_amount",
                              width=600, height=600, title= f"{state.upper()} DISTRICTS TRANSACTION AMOUNT",
                              hole=0.5,color_discrete_sequence= px.colors.sequential.Magenta_r)
        st.plotly_chart(fig_map_pie)

    with col2:
        fig_map_pie= px.pie(mis_g, names= "Districts", values= "Transaction_count",
                              width=600, height= 600, title= f"{state.upper()} DISTRICTS TRANSACTION COUNT",
                              hole=0.5,  color_discrete_sequence= px.colors.sequential.dense_r)
        
        st.plotly_chart(fig_map_pie)

def map_user_plot1(df,year):
    muy= df[df["Years"] == year]
    muy.reset_index(drop= True, inplace= True)
    muy_g= muy.groupby("States")[["RegisteredUser","AppOpens"]].sum()
    muy_g.reset_index(inplace= True)

    fig_map_user_plot= px.line(muy_g, x= "States", y= ["RegisteredUser","AppOpens"], markers= True,
                                width=1000,height=800,title= f"{year} REGISTERED USER AND APPOPENS", color_discrete_sequence= px.colors.sequential.Plotly3_r)
    st.plotly_chart(fig_map_user_plot)

    return muy

def map_user_plot2(df,quarter):
    muq= df[df["Quarter"] == quarter]
    muq.reset_index(drop= True, inplace= True)
    muq_g= muq.groupby("States")[["RegisteredUser", "AppOpens"]].sum()
    muq_g.reset_index(inplace= True)

    fig_map_user_plot_1= px.line(muq_g, x= "States", y= ["RegisteredUser","AppOpens"], markers= True,
                                title= f"{df['Years'].min()}, {quarter} QUARTER REGISTERED USER AND APPOPENS",
                                width= 1000,height=800,color_discrete_sequence= px.colors.sequential.Jet_r)
    st.plotly_chart(fig_map_user_plot_1)

    return muq

def map_user_plot3(df,state):
    mus= df[df["States"] == state]
    mus.reset_index(drop= True, inplace= True)
    mus_g= mus.groupby("Districts")[["RegisteredUser", "AppOpens"]].sum()
    mus_g.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_map_user_plot= px.bar(mus_g, x= "RegisteredUser",y= "Districts",orientation="h",
                                    title= f"{state.upper()} REGISTERED USER",height=800,
                                    color_discrete_sequence= px.colors.sequential.Rainbow_r)
        st.plotly_chart(fig_map_user_plot)

    with col2:
        fig_map_user_plot= px.bar(mus_g, x= "AppOpens", y= "Districts",orientation="h",
                                    title= f"{state.upper()} APPOPENS",height=800,
                                    color_discrete_sequence= px.colors.sequential.thermal)
        st.plotly_chart(fig_map_user_plot)

def top_user_plot1(df,year):
    tuy= df[df["Years"] == year]
    tuy.reset_index(drop= True, inplace= True)

    tuy_g= pd.DataFrame(tuy.groupby(["States","Quarter"])["RegisteredUser"].sum())
    tuy_g.reset_index(inplace= True)

    fig_top_plot_1= px.bar(tuy_g, x= "States", y= "RegisteredUser", barmode= "group", color= "Quarter",
                            width=1000, height= 800, color_continuous_scale= px.colors.sequential.Magenta)
    st.plotly_chart(fig_top_plot_1)

    return tuy

def top_user_plot2(df,state):
    tus= df[df["States"] == state]
    tus.reset_index(drop= True, inplace= True)

    tus_g= pd.DataFrame(tus.groupby("Quarter")["RegisteredUser"].sum())
    tus_g.reset_index(inplace= True)

    fig_top_plot= px.bar(tus, x= "Quarter", y= "RegisteredUser",barmode= "group",
                           width=1000, height= 800,color= "Pincodes",hover_data="Pincodes",
                            color_continuous_scale= px.colors.sequential.matter_r)
    st.plotly_chart(fig_top_plot)


#streamlit part
    
st.set_page_config(page_title="PhonePe Pluse")
title_style = """
    <style>
        .title-css {
            text-color:black;
            font-size:50px;
            text-align: center;
            font-size: 36px;
            font-family: 'Palatino Bold';
        }
    </style>
"""
# Render the title with the custom CSS
st.markdown(title_style, unsafe_allow_html=True)
st.markdown("<h1 class='title-css'>PHONEPE PLUSE DATA VISUALIZATION AND EXPLORATION</h1>", unsafe_allow_html=True)

with st.sidebar:
    a=option_menu("Main Menu",["Home","Data Visulation","Top Charts"])

if a=="Home":
    col1,col2=st.columns(2)
    with col1:
        st.markdown("<h2 style='font-family:Playfair Display; font-style: Bold 700; font-size: 28px;'>India's Top Payment App</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-family:Playfair Display; font-style: Medium 500; font-size:20px; color:#8E5737;'>PhonePe is a popular Indian digital payments and financial technology company.</p>", unsafe_allow_html=True)
        st.markdown("<h2 style='font-family:Playfair Display; font-style: Bold 700; font-size: 28px;'>Key Features:", unsafe_allow_html=True)
        st.markdown("<ul style='font-family:Roboto; font-style: Medium 500;font-size:45px; color: #F0EB93;'>"
                    "<li>Digital Payments</li>"
                    "<li>UPI Payments</li>"
                    "<li>Bill Payments and Recharges</li>"
                    "<li>Merchant Payments</li>"
                    "<li>Money Transfer</li>"
                    "<li>Investment</li>"
                    "<li>Rewards and Cashbacks</li>"
                    "<li>Split Bills</li>"
                    "<li>24/7 Customer Support</li>"
                    "</ul>", unsafe_allow_html=True)
        st.download_button("Download the App Now", "https://www.phonepe.com/app-download/")


    with col2:
        st.video("C:\\Users\\DELL\\Desktop\\p2\\phonepe\\Phonepe.mp4")

    col3,col4=st.columns(2)

    with col3:
        st.markdown("<h3 style='font-family:Playfair Display; font-style: Bold 700; font-size: 28px;'>Multiple Ways of Payment:</h3>", unsafe_allow_html=True)
        st.markdown("<ul style='color: #FF9100; font-size:16px;font-family:Roboto; font-style:Medium 500; font-size: 45px;'>"
                    "<li>UPI (Unified Payments Interface)</li>"
                    "<li>Credit/Debit Cards</li>"
                    "<li>Wallet Balance</li>"
                    "<li>Net Banking</li>"
                    "<li>QR Code Payments</li>"
                    "</ul>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='font-family:Playfair Display; font-style: Bold 700; font-size: 28px;'>Benefits of PhonePe Pulse:</h3>", unsafe_allow_html=True)
        st.markdown("<ul style='color: #FF9100; font-size:16px;font-family:Roboto; font-style: Medium 500; font-size: 45px;'>"
                    "<li>Quick bill payments</li>"
                    "<li>Instant money transfers</li>"
                    "<li>Effortless investments</li>"
                    "<li>Wide range of services</li>"
                    "<li>Easy navigation</li>"
                    "<li>Added convenience</li>"
                    "<li>Secure transactions</li>"
                    "<li>Valuable rewards</li>"
                    "</ul>", unsafe_allow_html=True)



    with col4:
        st.video("C:\\Users\\DELL\\Desktop\\p2\\phonepe\\Phonepe_1.mp4")


if a=="Data Visulation":
    tab1,tab2,tab3=st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])

    with tab1:
        b=st.radio("Select the Method",["Aggregated Insurance", "Aggregated Transaction", "Aggregated User"])

        if b=="Aggregated Insurance":
            col1,col2=st.columns(2)
            with col1:
                YEARS=st.slider("Select the Year",ag_insur["Years"].min(),ag_insur["Years"].max(),ag_insur["Years"].min())

            df1=agg_insur_yr(ag_insur,YEARS)

            col1,col2=st.columns(2)
            with col1:
                QUARTERS=st.slider("**Select the Quarter**",df1["Quarter"].min(),df1["Quarter"].max(),df1["Quarter"].min())
            
            agg_insur_YQ(df1,QUARTERS)

        elif b=="Aggregated Transaction":
            col1,col2=st.columns(2)
            with col1:
                YEARS_TR=st.slider("Select the Year", ag_trans["Years"].min(), ag_trans["Years"].max(),ag_trans["Years"].min())

            df3=agg_insur_yr(ag_trans,YEARS_TR)

            col1,col2=st.columns(2)
            with col1:
                QUARTER_TR=st.slider("Select the Quarter", df3["Quarter"].min(), df3["Quarter"].max(),df3["Quarter"].min())

            df4=agg_insur_YQ(df3,QUARTER_TR)

            STATE_TR=st.selectbox("Select the State",df4["States"].unique())
            agg_trans_type(df4,STATE_TR)

        elif b=="Aggregated User":
            YEAR_UR=st.selectbox("Select the Year",ag_user["Years"].unique())
            df_ur=agg_user_plot1(ag_user,YEAR_UR)

            QUARTER_UR=st.selectbox("Select the Quarter",df_ur["Quarter"].unique())
            df1_ur=agg_user_plot2(df_ur,QUARTER_UR)

            STATE_UR=st.selectbox("Select the State",df_ur["States"].unique())
            agg_user_plot3(df1_ur,STATE_UR)
            
    with tab2:
        c=st.radio("Select the Method",["Map Insurance","Map Transaction","Map User"])

        if c=="Map Insurance":
            col1,col2=st.columns(2)
            with col1:
                YEARS_M=st.slider("Select the Year_m",ma_insur["Years"].min(),ma_insur["Years"].max(),ma_insur["Years"].min())
            df1_y=agg_insur_yr(ma_insur,YEARS_M)

            col1,col2=st.columns(2)
            with col1:
                STATE_M=st.selectbox("Select the State_m",df1_y["States"].unique())
            map_insure_plot1(df1_y,STATE_M)

            col1,col2=st.columns(2)
            with col1:
                QUARTER_M=st.slider("Select the Quarter_m",df1_y["Quarter"].min(),df1_y["Quarter"].max(),df1_y["Quarter"].min())
            df1_yq=agg_insur_YQ(df1_y,QUARTER_M)

            col1,col2=st.columns(2)
            with col1:
                STATE_M1=st.selectbox("Select the State_m1",df1_yq["States"].unique())
            map_insur_plot2(df1_yq,STATE_M1)

        elif c=="Map Transaction":
            col1,col2=st.columns(2)
            with col1:
                YEARS_M1=st.slider("Select the Year_m1",ma_trans["Years"].min(), ma_trans["Years"].max(),ma_trans["Years"].min())
            df1_y1=agg_insur_yr(ma_trans,YEARS_M1)

            col1,col2=st.columns(2)
            with col1:
                STATE_M2=st.selectbox("Select the State_m2",df1_y1["States"].unique())
            map_insure_plot1(df1_y1,STATE_M2)

            col1,col2=st.columns(2)
            with col1:
                QUARTER_M1=st.slider("Select the Quarter_m1",df1_y1["Quarter"].min(),df1_y1["Quarter"].max(),df1_y1["Quarter"].min())
            df1_yq1=agg_insur_YQ(df1_y1,QUARTER_M1)

            col1,col2=st.columns(2)
            with col1:
                STATE_M3=st.selectbox("Select the State_m3", df1_yq1["States"].unique())
            map_insur_plot2(df1_yq1,STATE_M3)

        elif c=="Map User":
            col1,col2=st.columns(2)
            with col1:
                YEARS_M2=st.selectbox("Select the Year_m2",ma_user["Years"].unique())
            df1_y2=map_user_plot1(ma_user,YEARS_M2)

            col1,col2=st.columns(2)
            with col1:
                QUARTER_M2=st.selectbox("Select the Quarter_m2",df1_y2["Quarter"].unique())
            df1_yq2=map_user_plot2(df1_y2,QUARTER_M2)

            col1,col2=st.columns(2)
            with col1:
                STATE_M4=st.selectbox("Select the State_m4",df1_yq2["States"].unique())
            map_user_plot3(df1_yq2,STATE_M4)
    with tab3:
        d=st.radio("Select the Method",["Top Insurance","Top Transaction","Top User"])
        
        if d=="Top Insurance":
            col1,col2= st.columns(2)
            with col1:
                YEARS_T=st.slider("Select the Year_t",to_insur["Years"].min(),to_insur["Years"].max(),to_insur["Years"].min())
            df2_y=agg_insur_yr(to_insur,YEARS_T)

            col1,col2= st.columns(2)
            with col1:
                QUARTER_T=st.slider("Select the Quarter_t", df2_y["Quarter"].min(),df2_y["Quarter"].max(),df2_y["Quarter"].min())
            df2_yq=agg_insur_YQ(df2_y,QUARTER_T)

        elif d=="Top Transaction":
            col1,col2= st.columns(2)
            with col1:
                YEARS_T1=st.slider("Select the Year_t1",to_trans["Years"].min(),to_trans["Years"].max(),to_trans["Years"].min())
            df2_y1=agg_insur_yr(to_trans,YEARS_T1)

            col1,col2= st.columns(2)
            with col1:
                QUARTER_T1=st.slider("Select the Quarter_t1",df2_y1["Quarter"].min(),df2_y1["Quarter"].max(),df2_y1["Quarter"].min())
            df2_yq1=agg_insur_YQ(df2_y1,QUARTER_T1)

        elif d=="Top User":
            col1,col2= st.columns(2)
            with col1:
                YEARS_T2=st.selectbox("Select the Year_t2",to_user["Years"].unique())
            df2_y2=top_user_plot1(to_user,YEARS_T2)

            col1,col2= st.columns(2)
            with col1:
                STATE_T1=st.selectbox("Select the State_t",df2_y2["States"].unique())
            df2_s=top_user_plot2(df2_y2,STATE_T1)

if a == "Top Charts":

    ques = st.selectbox("Select the Question",(
    "1. Which mobile phone brands are most commonly used?",
    "2. Which states have the highest transaction amounts?",
    "3. Which states have the lowest transaction amounts?",
    "4. Which districts have the highest transaction amounts?",
    "5. What are the top 10 districts with the lowest transaction amounts?",
    "6. What are the top 10 states with the highest number of app opens?",
    "7. What are the least 10 states with the number of app opens?",
    "8. Which states have the lowest transaction count?",
    "9. Which states have the highest transaction count?",
    "10. What are the top 50 districts with the lowest transaction amounts?"))
    
    if ques == "1. Which mobile phone brands are most commonly used?":
        br= ag_user[["Brands","Transaction_count"]]
        br1= br.groupby("Brands")["Transaction_count"].sum().sort_values(ascending=False)
        br2= pd.DataFrame(br1).reset_index()

        fig1= px.pie(br2, values= "Transaction_count", names= "Brands", color_discrete_sequence=px.colors.sequential.dense_r,
                        title= "TOP MOBILE BRANDS")
        st.plotly_chart(fig1)

    elif ques == "2. Which states have the highest transaction amounts?":
        ht= ag_trans[["States", "Transaction_amount"]]
        ht1= ht.groupby("States")["Transaction_amount"].sum().sort_values(ascending= False)
        ht2= pd.DataFrame(ht1).reset_index().head(10)

        fig2= px.pie(ht2, values= "Transaction_amount", names= "States",title= "HIGHEST TRANSACTION AMOUNT WITH STATES",
                        color_discrete_sequence= px.colors.sequential.Oranges_r)
        st.plotly_chart(fig2)
    
    elif ques == "3. Which states have the lowest transaction amounts?":
        lt = ag_trans[["States", "Transaction_amount"]]
        lt1 = lt.groupby("States")["Transaction_amount"].sum().sort_values(ascending=True)
        lt2 = pd.DataFrame(lt1).reset_index().head(10)

        fig3 = px.line_polar(lt2, r='Transaction_amount', theta='States', line_close=False,title= "LOWEST TRANSACTION AMOUNT WITH STATES",
                                color_discrete_sequence= px.colors.qualitative.Vivid)
        st.plotly_chart(fig3)

    elif ques == "4. Which districts have the highest transaction amounts?":
        ht= ma_trans[["Districts", "Transaction_amount"]]
        ht1= ht.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=False)
        ht2= pd.DataFrame(ht1).head(10).reset_index()

        fig4 = px.sunburst(ht2, path=['Districts'], values='Transaction_amount',title="HIGHEST TRANSACTION AMOUNT WITH DISTRICTS",
            color='Districts', hover_data=['Districts', 'Transaction_amount'],color_discrete_sequence=px.colors.sequential.YlGn_r)
        st.plotly_chart(fig4)    

    elif ques == "5. What are the top 10 districts with the lowest transaction amounts?":
        lt= ma_trans[["Districts", "Transaction_amount"]]
        lt1= lt.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
        lt2= pd.DataFrame(lt1).head(10).reset_index()

        fig5 = px.scatter(lt2, x='Districts', y='Transaction_amount', size='Transaction_amount',
                 title='Top 10 Districts with Lowest Transaction Amounts',color=lt2['Transaction_amount'], color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig5)

    elif ques == "6. What are the top 10 states with the highest number of app opens?":
        ht= ma_user[["States", "AppOpens"]]
        ht1= ht.groupby("States")["AppOpens"].sum().sort_values(ascending=False)
        ht2= pd.DataFrame(ht1).reset_index().head(10)

        fig6 = px.bar_polar(ht2, r='AppOpens', theta='States', title='Top 10 States with App Opens',
                    color='AppOpens', color_continuous_scale=px.colors.sequential.Pinkyl)
        st.plotly_chart(fig6)

    elif ques == "7. What are the least 10 states with the number of app opens?":
        s= ma_user[["States", "AppOpens"]]
        s1= s.groupby("States")["AppOpens"].sum().sort_values(ascending=True)
        s2= pd.DataFrame(s1).reset_index().head(10)

        fig7 = px.bar(s2, x="AppOpens", y="States", title="Lowest 10 States With App Opens",
            pattern_shape_sequence=["/"], color_discrete_sequence=px.colors.qualitative.Set1,color="States")
        st.plotly_chart(fig7)

    elif ques == "8. Which states have the lowest transaction count?":
        sl= ag_trans[["States", "Transaction_count"]]
        sl1= sl.groupby("States")["Transaction_count"].sum().sort_values(ascending=True)
        sl2= pd.DataFrame(sl1).reset_index()

        fig8 = px.scatter(sl2, x="Transaction_count", y="States", title="Lowest Transaction Count with States",
            color_discrete_sequence=px.colors.sequential.Sunsetdark_r,color="States")
        fig8.update_traces(marker=dict(size=30,opacity=0.6))

        st.plotly_chart(fig8)        

    elif ques == "9. Which states have the highest transaction count?":
        sh= ag_trans[["States", "Transaction_count"]]
        sh1= sh.groupby("States")["Transaction_count"].sum().sort_values(ascending=False)
        sh2= pd.DataFrame(sh1).reset_index()

        fig9= px.bar(sh2, x= "States", y= "Transaction_count", title= "HIGHEST TRANSACTION COUNT WITH STATES",
                color_discrete_sequence= px.colors.qualitative.Vivid,color="States")
        st.plotly_chart(fig9)
        

    elif ques == "10. What are the top 50 districts with the lowest transaction amounts?":
        dt= ma_trans[["Districts", "Transaction_amount"]]
        dt1= dt.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
        dt2= pd.DataFrame(dt1).reset_index().head(50)

        fig10= px.bar(dt2, x= "Districts", y= "Transaction_amount", title= "LOWEST TRANSACTION AMOUNT WITH DISTRICTS",
            color_discrete_sequence= px.colors.qualitative.Dark24,color="Districts")
        st.plotly_chart(fig10)
