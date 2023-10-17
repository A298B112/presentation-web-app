import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Logo.jpg", width=426)
    st.title("About the club:")
    content = """
    Real Madrid Club de Fútbol, commonly referred to as Real Madrid
    is a Spanish football club based in the capital Madrid. They are
    considered as one of the most successful clubs in the whole world
    The club competes in La Liga, the top league of Spain. The club was 
    founded in March 6, 1902. Since then, Real Madrid have won a total
    of 14 Champions League, 35 La Liga, 19 Copa del Rey and many more...
    The legends who played for Real Madrid are the likes of Cristiano Ronaldo,
    Karim Benzema, Alfredo di Stefano, David Beckham and Roberto Carlos.
    """
    st.info(content)
    st.title("Legends:")
    images = ["images/Ronaldo.jpg", "images/Carlos.jpg"]
    st.image(images)
    st.image("images/Benzema.jpg")

with col2:
    st.title("Real Madrid CF")
    st.title("Major Trophies:")
    st.info("14x Champions League winner")
    st.image("images/UCL.jpg")
    st.info("35x La Liga winner")
    st.image("images/LaLiga.jpg")
    st.info("19x Copa del Rey winner")
    st.image("images/CopadelRey.jpg")
    content = """
    Real Madrid have won the Champions League 14 times, the La Liga 35 times and the Copa del Rey 19 times.
    These are record breaking numbers in the trophies section of clubs. Real Madrid is arguably one of the best
    clubs in the world if not THE best. The trophies shown here are just a small part of Real Madrid's collection
    of trophies. Other kinds of trophies that they won are 8 Club World Cups, 5 European Super Cups, 2 UEFA Cups,
    12 Spanish Super Cups, 1 League Cup, 2 Small World Cups, 2 Latin Cups, The Best Club of the 20th Century and
    so on... Real Madrid have won the most ever Champions Leagues in football history! In 2nd place there's
    AC Milan with a total of 7 Champions Leagues and in 3rd place we have Liverpool with a total of 6
    Champions Leagues. 
    """
    st.info(content)



