import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt



st.set_page_config(layout="wide",page_title="Startup Analysis")

data=pd.read_csv("cleaned_data_of_startups.csv")







def investor_page(investors):

    # name
    st.title(investor)

    # recent investment
    st.header("Recent Investments")
    recent_investment=data[data["investor"].str.contains(investors)].head()
    st.dataframe(recent_investment)

    col1,col2=st.columns(2)

    with col1:
    # biggest investment
        st.header("Biggest Investments")
        biggest_investment=data[data["investor"].str.contains(investors)].groupby("startup")["amount"].sum().sort_values(ascending=False).head()
        st.dataframe(biggest_investment)


    with col2:
        st.header("Sectors Invested In")
        fig,ax=plt.subplots(figsize=(3,3))
        ax.bar(biggest_investment.index,biggest_investment.values)

        st.pyplot(fig)



    
    
    st.divider() 
    

    col3,col4=st.columns(2)
    with col3:
        # sector pie

        st.title("Invested sectors ")
        sector=data[data["investor"].str.contains(investors)].groupby("vertical")["amount"].sum().head()
        st.dataframe(sector)
               
    with col4:
        st.header("Sectors Invested In")
        fig1,ax1=plt.subplots(figsize=(3,3))
        ax1.pie(sector,labels=sector.index,autopct="%0.01f%%")

        st.pyplot(fig1)

    st.divider()


    col5,col6=st.columns(2)
    with col5:
        # stage 

        st.title("Investment stage")
        stage=data[data["investor"].str.contains(investors)].groupby("round")["amount"].sum()
        st.dataframe(stage)

    with col6:

        # stage pie

        st.header("Investment Stage Pie Chart")
        fig2,ax2=plt.subplots(figsize=(3,3))
        ax2.pie(stage,labels=stage.index,autopct="%0.01f%%")
        st.pyplot(fig2)


    st.divider()
    
    # investment city
    st.title("Invested Cities")
    col7,col8=st.columns(2)

    with col7:
        st.header("Table for Cities")
        cities=data[data["investor"].str.contains(investors)].groupby("city")["amount"].sum()
        st.dataframe(cities)

    with col8:
        st.header("pie Chart for Cities")
        fig3,ax3=plt.subplots(figsize=(3,3))
        ax3.pie(cities,labels=cities.index,autopct="%0.01f%%")

        st.pyplot(fig3)
    
    st.divider()


# year on year investment
    st.title("Year by Year Investment")
    col9,col10=st.columns(2)
    
    
    with col9:
        st.header("Tabel")
        year=pd.to_datetime(data['date'], errors='coerce')
        data['year']=year.dt.year
        # note
        yoy=data[data["investor"].str.contains(investors)].groupby("year")["amount"].sum()
        st.dataframe(yoy)

    with col10:
        st.header("graph Chart")
        fig4,ax4=plt.subplots(figsize=(3,3))
        ax4.plot(yoy)

        st.pyplot(fig4)




def general_analysis():
    st.title("OverAll Analysis")


    st.divider()


    col11,col12,col13=st.columns(3)

    with col11:

        total=data["amount"].sum().round()
        st.metric("Total",str(total)+"cr")

    with col12:
        max=data.groupby("startup")["amount"].sum().sort_values(ascending=False).head(1).values[0].round()
        st.metric("maximum",str(max)+"cr")

    with col13:
        mean=data.groupby("startup")["amount"].mean().head(1).values[0]
        st.metric("Average",str(mean)+"cr")

    st.divider()
    # year by year chart
   

   














st.sidebar.header("Startup Funding Analysis")
option=st.sidebar.selectbox("select one ",['OverAll Analysis', "Investor Analysis", "Startups Anaylis" ])

if option=="OverAll Analysis":
    btn0=st.sidebar.button("Genral Analysis")
    if btn0:
        general_analysis()

if option=="Investor Analysis":
    investor=st.sidebar.selectbox("Choose Investor",sorted(set(data["investor"].str.split(",").sum())))
    btn2=st.sidebar.button("Investor Analysis")
    if btn2:
        # investor_page(investor)
        st.title("byy")

if option=="Startups Anaylis":
    startup=st.sidebar.selectbox("Startup Name ",(data["startup"].unique().tolist()) )
    btn1=st.sidebar.button("Startup Analysis")
    if btn1:
        st.header("back")


