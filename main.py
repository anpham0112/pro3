import streamlit as st


st.title("Dien thong tin gioi thieu ban than")
quiz = ["Ho ten","Nam sinh","Lop"]
len_quiz = len(quiz)
answers = []
my_bar = st.progress(0)

for i in range(len_quiz):
  answer = st.text_input(quiz[i],"")
  if answer != "":
    answers.append(answer)
if st.button("Confirm"):
  if len(answers) == len_quiz:
    st.balloons()
    my_bar.progress(100)
  else:
      my_bar.progress(len(answers)/len_quiz)
      st.write("ban chua nhap day du thong tin")


