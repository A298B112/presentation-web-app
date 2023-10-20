import streamlit as st

st.set_page_config(layout="wide")
tab1, tab2, tab3 = st.tabs(["Home", "Clubs", "Trophies"])

with tab1:
   st.title("Early Life")
   content = """Cristiano Ronaldo dos Santos Aveiro was born the 5 February 1985 in the São Pedro parish of Funchal, 
   the capital of the Portuguese island of Madeira, and grew up in the nearby parish of Santo António. He is the 
   fourth and youngest child of Maria Dolores dos Santos Viveiros da Aveiro(his mother) who was a cook, 
   and José Dinis Aveiro(his father) who was a municipal gardener and part-time kit man. His great-grandmother on his 
   father's side, Isabel da Piedade, was from the island of São Vicente, Cape Verde. He has one older brother, Hugo, 
   and two older sisters, Elma and Liliana Cátia. He was named after actor and U.S. President Ronald Reagan, 
   whom his father was a fan of. His mother revealed that she wanted to abort him due to poverty, his father's 
   alcoholism, and having too many children already, but her doctor refused to perform the procedure, as abortions 
   were illegal in Portugal at that time. Ronaldo grew up in an impoverished Roman Catholic home, sharing a room with 
   all his siblings. As a child, Ronaldo played for Andorinha from 1992 to 1995, where his father was the kit man, 
   and later spent two years with Nacional. In 1997, aged 12, he went on a three-day trial with Sporting CP, 
   who signed him for a fee of £1,500. He subsequently moved from Madeira to Alcochete, near Lisbon, 
   to join Sporting's youth academy. By age 14, Ronaldo believed he had the ability to play semi-professionally and 
   agreed with his mother to cease his education to focus entirely on football. With a troubled life as a student and 
   living in Lisbon area away from his Madeiran family, he did not complete schooling beyond the 6th grade. While 
   popular with other students at school, he had been expelled after throwing a chair at his teacher, who he said had 
   "disrespected" him. One year later, he was diagnosed with tachycardia, a condition that could have forced him to 
   give up playing football. Ronaldo underwent heart surgery where a laser was used to cauterise multiple cardiac 
   pathways into one, altering his resting heart rate. He was discharged from the hospital hours after the procedure 
   and resumed training a few days later."""
   st.info(content)
   st.header("Old photo of Ronaldo with his family.")
   st.image("images/KidCR7.jpg")


with tab2:
   st.title("Club Career")
   content = """
   Ronaldo has played for a total of 5 clubs in his career. He played for Sporting CP, a Portuguese club, for Manchester
   United, an English club, Real Madrid CF, a Spanish club, Juventus, an Italian club then he returned to Manchester
   United and now, present, he's playing for an Arab club called Al Nassr. Below you'll see an image about all the
   clubs he played for.
   """
   st.info(content)

with tab3:
   st.title("This page is about the trophies Ronaldo won.")
