import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px

# SETTING PAGE CONFIGURATIONS
icon = Image.open(r"C:\Users\sunil\OneDrive\Desktop\python guvi\airbnb\4494647.png")
st.set_page_config(page_title= "Airbnb analysis| By SUNIL RAGAV",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded")
st.markdown("<h1 style='text-align: center; color:red;'>Airbnb Analysis</h1>", unsafe_allow_html=True)

df=pd.read_csv(r"C:\Users\sunil\OneDrive\Desktop\python guvi\airbnb\Airbnb (2).csv")
col=df[["host_id","host_url","host_name","host_location","host_response_time","host_thumbnail_url","host_neighbourhood","host_response_rate","host_is_superhost","host_has_profile_pic","host_identity_verified","host_total_listings_count","host_verifications"]]

# CREATING OPTION MENU
with st.sidebar:
    co,co1=st.columns([1,4])
    with co:
        st.image(icon)
    with co1:
        #  st.write(" ")
         st.header("Airbnb")
    selected = option_menu(None, ["Home","Explore","User selection"], 
                       icons=["house","book","pencil-square"],
                       default_index=0,
                       orientation="vertical",
                       styles={"nav-link": {"font-size": "15px", "text-align": "centre", "margin": "0px", "--hover-color": "red"},
                               "icon": {"font-size": "25px"},
                               "container" : {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "red"}})



roomtype=df["room_type"].unique()
bed_type=df["bed_type"].unique()
property_type=df["property_type"].unique()
cancellation_policy=df["cancellation_policy"].unique()
name=df["name"].unique
country=df["country"].unique()
market=df["market"].unique()



# HOME MENU
def home():
    if selected == "Home":

        col1,col2,col3 = st.columns([3,2,4])
        col1.markdown("## :red[Domain] : Travel Industry, Property Management and Tourism")
        col1.markdown("## :red[Technologies used] : Python, Pandas, Plotly, Streamlit, MongoDB")
        col1.markdown("## :red[Overview] : To analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. ")
        col2.markdown("#   ")
        col2.markdown("#   ")
        ic=Image.open(r"C:\Users\sunil\OneDrive\Desktop\python guvi\airbnb\4494647.png")
        col3.image(ic)
        
home()     
# UPLOAD AND EXTRACT MENU
if selected == "Explore":
        st.write()
        # RAW DATA
        col1,col2 = st.columns([2,2])
        if st.button("Click to view dataframe"):
            with col1:
                st.markdown("Host data's Dataframe")
                st.write(col)

            with col2:
                st.markdown("Overall data's Dataframe")
                st.write(df)
        column1,column2,column3=st.columns(3)
        st.markdown("<h1 style='text-align: left; color:red;'>Data Visualisation:</h1>", unsafe_allow_html=True)
        st.subheader(":red[Find average price of property dynamically :]")
        col1,col2=st.columns([4,4])
        with col1:
            selected_roomtype=st.selectbox(label="Selected room type",options=roomtype,index=0,help="Choose the type of room you're interested in.")
        with col2:
            selected_bedtype=st.selectbox(label="Selected bed type",options=bed_type,index=0,help="Choose the type of bed you're interested in.")
        column1,column2=st.columns(2)
        with column1:
             filtered=df[(df["bed_type"]==selected_bedtype)&(df["room_type"]==selected_roomtype)]
             grouping=filtered.groupby(["bed_type","room_type","property_type"]).price.mean().reset_index()
             group=grouping.sort_values(by="price",ascending=False)
             
             bar=px.bar(group,x='property_type',y="price",hover_data="price",color="property_type")
        co1,col3=st.columns([4,2])
        with co1:
             st.plotly_chart(bar,use_container_width=True)
        with col3:
             st.info("""Heres is the information of average price of property type""")
             st.write(grouping)
        

        st.markdown("<h3 style='text-align: left; color:red;'>Top 10 property type bar chart by size:</h3>", unsafe_allow_html=True)
        filtered_df = df
        grouping=filtered_df.groupby("property_type").size().reset_index(name='Listings')
        sorted1=grouping.sort_values(by="Listings",ascending=False)[:10]
        bar1=px.bar(sorted1,x="property_type",y="Listings",color="property_type")
        col1,col2=st.columns([5,1])
        col1.plotly_chart(bar1,use_container_width=True)
        col2.write(" ")
        col2.write(" ")
        col2.write(" ")
        col2.info("""-Here the bar chart denotes the top 10 property type. X-axis indicates property type.
                  Y-axis indicates listings of property type.
                  listings here means how many are or size of individual property type""")


        st.markdown("<h3 style='text-align: left; color:red;'>Top 10 Hosts bar chart by size:</h3>", unsafe_allow_html=True)
        filtered_df = df
        grouping=filtered_df.groupby("host_name").size().reset_index(name='Listings')
        sorted1=grouping.sort_values(by="Listings",ascending=False)[:10]
        bar1=px.bar(sorted1,x="host_name",y="Listings",color="host_name")
        col1,col2=st.columns([5,1])
        col1.plotly_chart(bar1,use_container_width=True)
        col2.write(" ")
        col2.write(" ")
        col2.write(" ")
        col2.info("""-Here the bar chart denotes the top 10 hosts on the basics of the repeatation.X-axis indicates host name.
                  Y-axis indicates listings of the host.
                  listings here means how many times are or size of individual host repeatation""")


        st.markdown("<h3 style='text-align: left; color:red;'>Listings in Each Room Type Pie chart by size:</h3>", unsafe_allow_html=True)
        filtered_df = df
        grouping=filtered_df.groupby("room_type").size().reset_index(name='Listings')
        sorted1=grouping.sort_values(by="Listings",ascending=False)[:10]
        bar1=px.pie(sorted1,names="room_type",values="Listings")
        col1,col2=st.columns([5,1])
        col1.plotly_chart(bar1,use_container_width=True)
        col2.write(" ")
        col2.write(" ")
        col2.write(" ")
        col2.info("""-Here the pie chart denotes the listings of Each Room Type by Size.
                  names denote Room Types.values denotes listings or count of each Room Type.
                  Hover on the pie chart and see the count of each Room Type and their Percentage.
                   """)

        st.markdown("<h3 style='text-align: left; color:red;'>Average price details of each countries in Geo Chart:</h3>", unsafe_allow_html=True)
        country_df = df.groupby(['country'])['price'].mean().reset_index()
        fig = px.choropleth(country_df,
                                locations='country',
                                locationmode='country names',
                                color='country',
                                hover_data=["price"],
                                color_continuous_scale=px.colors.sequential.Plasma
                               )
        col1,col2=st.columns([5,1])
        col1.plotly_chart(fig,use_container_width=True)
        col2.write(" ")
        col2.write(" ")
        col2.write(" ")
        col2.info("""-Here the choropleth chart denotes the Average price spent on staying.
                  Each color indicates different countries.
                  Hover over the countries to see the average price of staying.""")

        st.markdown("<h3 style='text-align: left; color:red;'>Average price of Each Room Type in Bar chart:</h3>", unsafe_allow_html=True)
        filtered_df = df
        grouping=filtered_df.groupby("room_type")["price"].mean().reset_index()
        sorted1=grouping.sort_values(by="price",ascending=False)
        bar1=px.bar(sorted1,x="price",y="room_type",color="room_type")
        col1,col2=st.columns([5,1])
        col1.plotly_chart(bar1,use_container_width=True)
        col2.write(" ")
        col2.write(" ")
        col2.write(" ")
        col2.info("""-Here the bar chart denotes the Average price of Each Room Type.
                  X-axis indiactes Average Price.Y-axis indicates Room Types.
                  Hover over the Bar's to see the Average price of Each Room Type. """)

        st.markdown("<h3 style='text-align: left; color:red;'>Average price of Property type in Bar chart:</h3>", unsafe_allow_html=True)
        filtered_df = df
        grouping=filtered_df.groupby("property_type")["price"].mean().reset_index()
        sorted1=grouping.sort_values(by="price",ascending=False)
        bar1=px.bar(sorted1,x="property_type",y="price",color="property_type")
        col1,col2=st.columns([5,1])
        col1.plotly_chart(bar1,use_container_width=True)
        col2.write(" ")
        col2.write(" ")
        col2.write(" ")
        col2.info("""-Here the bar chart denotes the Average price of Each Property Type.
                  X-axis indiactes Property Type.Y-axis indicates Average Price.
                  Hover over the Bar's to see the Average price of Each Room Type. """)

        st.markdown("<h3 style='text-align: left; color:red;'>Availibality checking in Bar chart by size:</h3>", unsafe_allow_html=True)
        c1,c2=st.columns(2)
        with c1:
            selected_country=st.selectbox("Selected country",country,index=0,help="Choose the country you're interested in.")
        with c2:
            selected_market=st.selectbox("Selected property",property_type,index=0,help="Choose the type of property you're interested in.")
        filtered_df=df[(df["country"]==selected_country)&(df["property_type"]==selected_market)]
        grouping=filtered_df.groupby(["country","market","name","property_type","availability_365"])["availability_365"].size().reset_index(name="Listings")
        bar1=px.bar(grouping,x="name",y="availability_365",color="market")
        col1,col2=st.columns([5,1])
        col1.plotly_chart(bar1,use_container_width=True)
        col2.write(" ")
        col2.write(" ")
        col2.write(" ")
        col2.info("""-Here the bar chart denotes the Availabilty checking.
                  X-axis indiactes name.Y-axis indicates Availabilty in 365 days.
                  You can Dynamically select the Country and Property Type.
                  Hover over the Bar's to see the Availabilty of Each property by Name. """)


        
        country_df=df.groupby(["country",'room_type',"property_type"])["price"].mean().reset_index()
        fig = px.scatter_geo(country_df,
                                       locations='country',
                                       color= 'property_type', 
                                       hover_data=['price',"room_type","property_type"],
                                       locationmode='country names',
                                       size='price',
                                       color_continuous_scale='agsunset'
                            )
        co1,co2=st.columns(2)
        with co1:
            st.markdown("<h3 style='text-align:left; color:red ;'>Average price in countries by scattergeo graph:</h3>",unsafe_allow_html=True)
            st.plotly_chart(fig,use_container_width=True)

        country_df=df.groupby(["country",'room_type',"property_type"])["availability_365"].mean().reset_index()
        fig = px.scatter_geo(data_frame=country_df,
                                       locations='country',
                                       color= 'room_type', 
                                       hover_data=['availability_365',"room_type","property_type"],
                                       locationmode='country names',
                                       size='availability_365',
                                       color_continuous_scale='jet'
                            )
        with co2:
                st.markdown("<h3 style='text-align:left; color:red ;'>Average availability in countries by scattergeo graph:</h3>",unsafe_allow_html=True)
                st.plotly_chart(fig,use_container_width=True)
        # linechartdf=df.groupby(["country",'room_type',"property_type","bed_type"])["price"].mean().reset_index()
        # line=px.line(linechartdf,x="property_type",y="bed_type",color="room_type")
        # st.plotly_chart(line,use_container_width=True)
    


if selected=="User selection":
     st.markdown("<h3 style='text-align:left; color:red ;'>Here user can select their need and find what they want:</h3>",unsafe_allow_html=True)
     coo1,coo2=st.columns(2)
     with coo1:
        userselect_market=st.selectbox("Select the market you are in",market,index=0)
     with coo2:
        userselect_property_type=st.selectbox("Select the property type you want:",property_type,index=0)
     if st.button("Search"):
          filtered_df = df[(df["market"] == userselect_market) & (df["property_type"] == userselect_property_type)]
          st.dataframe(filtered_df)
          st.write("Total number of places are ",len(filtered_df))

     st.markdown("<h3 style='text-align:left; color:red ;'>Advanced Search:</h3>",unsafe_allow_html=True)
     cooo1,cooo2=st.columns(2)
     with cooo1:
          userselect_roomtype=st.selectbox("Select the room type you want:",roomtype,index=0)
     with cooo2: 
          userselect_cancellation=st.selectbox("Select the cancellation policy prefer",cancellation_policy,index=0)
     if st.button("Advance search"):
          display=df[(df["market"] == userselect_market) & (df["property_type"] == userselect_property_type)&(df["room_type"]==userselect_roomtype)&(df["cancellation_policy"]==userselect_cancellation)]
          st.dataframe(display)
          st.write("Total number of places are ",len(display))
     display = df[(df["market"] == userselect_market) & (df["property_type"] == userselect_property_type) & (
                df["room_type"] == userselect_roomtype) & (df["cancellation_policy"] == userselect_cancellation)]
     st.markdown("<h3 style='text-align:left; color:red ;'>User Select Name:</h3>",unsafe_allow_html=True)
     selc = st.selectbox("Select name that you selected from the sorted data:", display["name"], index=False)
     
     if st.button("check"):
        c1,c2=st.columns(2)
        if selc:
            end = df[(df["name"] == selc)]

            namee = end["name"].iloc[0] 
            listing_url = end["listing_url"].iloc[0]
            property_type = end["property_type"].iloc[0]
            room_type = end["room_type"].iloc[0]
            bed_type = end["bed_type"].iloc[0]
            minimum_nights = end["minimum_nights"].iloc[0]
            maximum_nights = end["maximum_nights"].iloc[0]
            cancellation_policy = end["cancellation_policy"].iloc[0]
            accommodates = end["accommodates"].iloc[0]
            bedrooms = end["bedrooms"].iloc[0]
            beds = end["beds"].iloc[0]
            bathrooms = end["bathrooms"].iloc[0]
            number_of_reviews = end["number_of_reviews"].iloc[0]
            price = end["price"].iloc[0]
            extra_people = end["extra_people"].iloc[0]
            guests_included = end["guests_included"].iloc[0]
            review_scores = end["review_scores"].iloc[0]
            cleaning_fee = end["cleaning_fee"].iloc[0]
            street = end["street"].iloc[0]
            is_location_exact = end["is_location_exact"].iloc[0]
            amenities = end["amenities"].iloc[0]
            image=end["images"].iloc[0]
            with c1:
                st.write("Name:", namee)
                st.write("Listing URL:", listing_url)
                st.write("Property Type:", property_type)
                st.write("Room Type:", room_type)
                st.write("Bed Type:", bed_type)
                st.write("Minimum Nights:", minimum_nights)
                st.write("Maximum Nights:", maximum_nights)
                st.write("Cancellation Policy:", cancellation_policy)
                st.write("Accommodates:", accommodates)
                st.write("Bedrooms:", bedrooms)
                st.write("Beds:", beds)
                st.write("Bathrooms:", bathrooms)
                st.write("Number of Reviews:", number_of_reviews)
                st.write("Price:", price)
                st.write("Extra People:", extra_people)
                st.write("Guests Included:", guests_included)
                st.write("Review Scores:", review_scores)
                st.write("Cleaning Fee:", cleaning_fee)
            with c2:
                
                st.write("Street:", street)
                st.write("Is Location Exact:", is_location_exact)
                st.write("Amenities:", amenities)
                st.image(image)
     s1,s2,s3,s4,s5,s6=st.columns(6)
     l=4
     with s3:
        if st.button("Yes user got the information"):
            l=0
     with s4:
        if st.button("No user didn't"):
           l=1 
     if l==0:
        st.success("We Received good feedback")
     if l==1:
         st.warning("We Received bad feedback")