import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt



st.set_page_config(layout="wide",page_title="Startup Analysis")

data=pd.read_csv("cleaned_data_of_startups.csv")
# dete=data
# dete["date"]=pd.to_datetime(data['date'], errors='coerce')







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
    st.title("OverAll Analysis (in crores)")


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
    # top sectors
    st.title("Top Sectors")
    col14,col15=st.columns(2)
    
    with col14:
        st.header("Table")
        top=data.groupby("vertical")["amount"].sum().sort_values(ascending=False).head().round()
        st.dataframe(top)
   
    st.divider()
    
    with col15:
        st.header("Bar Chart")
        fig10,ax10=plt.subplots()
        ax10.bar(top.index,top.values)
        st.pyplot(fig10)


        


#    top type of funding

    st.title("Top Investment Rounds")
    col16,col17=st.columns(2)
    
    with col16:
        st.header("Table")
        top_round=data.groupby("round")["amount"].sum().sort_values(ascending=False).head().round()
        st.dataframe(top_round)

    with col17:
        st.header("Bar Chart")
        fig11,ax11=plt.subplots()
        ax11.bar(top_round.index,top_round.values)
        st.pyplot(fig11)


    st.divider()
# top cities funding
    st.title("Top Invested Cities")
    col18,col19=st.columns(2)
    
    with col18:
        st.header("Table")
        top_city=data.groupby("city")["amount"].sum().sort_values(ascending=False).head(6 ).round()
        st.dataframe(top_city)

    with col19:
        st.header("Pie Chart")
        fig12,ax12=plt.subplots()
        ax12.pie(top_city,labels=top_city.index,autopct="%0.01f%%")
        st.pyplot(fig12)


        

# top startups
    st.title("Top Rising Startup")
    col20,col21=st.columns(2)
    
    with col20:
        st.header("Table")
        top_startups=data.groupby("startup")["amount"].sum().sort_values(ascending=False).head().round()
        st.dataframe(top_startups)

    with col21:
        st.header("Barchart")
        fig13,ax13=plt.subplots()
        ax13.bar(top_startups.index,top_startups.values)
        st.pyplot(fig13)


    st.divider()
    st.title("Leading Investors Analysis")
    col22,col23=st.columns(2)

    with col22:
        st.header("Table ")
        top_investor=data.groupby("investor")["amount"].sum().sort_values(ascending=False).head(10)
        st.dataframe(top_investor)

    with col23:
        st.header("Pie Chart")
        fig14,ax14=plt.subplots()
        ax14.pie(top_investor,labels=top_investor.index,autopct="%0.1f%%")
        st.pyplot(fig14)
    


def Startup_Analysis(startup):
    st.title(startup)

    col20,col21=st.columns(2)
    with col20:
        st.header("Investor")
        startup_investors = data[data['startup'].str.contains("Flipkart", case=False)]
        investors_startup = startup_investors['investor'].str.split(',', expand=True).stack().reset_index(drop=True)
        st.dataframe(investors_startup)

    st.divider()

    col22,col23=st.columns(2)

    with col22:
        st.title("Industry Vertical")
        startup_industry=data[data["startup"].str.contains(startup, case=False)]
        industry_startup=startup_industry["vertical"].str.split(",", expand=True).stack().reset_index(drop=True).drop_duplicates()
        st.dataframe(industry_startup)

    with col23:
        st.title("SubIndustres")
        startup_subindustry=data[data["startup"].str.contains(startup, case=False)]
        subindustry_startup=startup_subindustry["subvertical"].str.split(",", expand=True).stack().reset_index(drop=True).drop_duplicates()
        st.dataframe(subindustry_startup)


    st.divider()
        
    
    col24,col25=st.columns(2)
    with col24:
        st.title("Location")
        startup_location=data[data["startup"].str.contains(startup, case=False)]
        location=startup_location["city"].str.split(",", expand=True).stack().reset_index(drop=True).drop_duplicates()
        st.dataframe(location)

    with col25:
        st.title("Funding Stage")
        startup_round=data[data["startup"].str.contains(startup, case=False)]
        round=startup_round["round"].str.split(",", expand=True).stack().reset_index(drop=True).drop_duplicates()
        st.dataframe(round)

    st.divider()

    st.title("Funding Journey Insights")
    insights=data[data["startup"].str.contains("Flipkart")][["date","vertical","city","investor","amount"]]
    st.dataframe(insights)











st.sidebar.header("Startup Funding Analysis")
option=st.sidebar.selectbox("select one ",['OverAll Analysis', "Investor Analysis", "Startups Anaylis" ])

if option=="OverAll Analysis":
    btn0=st.sidebar.button("OverAll Analysis")
    if btn0:
        general_analysis()

if option=="Investor Analysis":
    investor=st.sidebar.selectbox("Choose Investor",sorted(set(data["investor"].str.split(",").sum())))
    btn2=st.sidebar.button("Investor Analysis")
    if btn2:
        investor_page(investor)
        

if option=="Startups Anaylis":
    startup=st.sidebar.selectbox("Startup Name ",(data["startup"].unique().tolist()) )
    btn1=st.sidebar.button("Startup Analysis")
    if btn1:
        Startup_Analysis(startup)


