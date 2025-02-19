import streamlit as st
st.title("Tu gioi thieu ve ban than")
bar = st.progress(0)
quiz = ["Ho va ten:","Ngay sinh nhat:","So thich:"]
answers = []
len_quiz = len(quiz)
for i in range(len_quiz):
  answer = st.text_input(quiz[i], "")
  if answer != "":
    answers.append(answer)
if st.button("Confirm"):
  if len(answers) == len_quiz:
    bar.progress(100)
    st.write("Ban da dien day du thong tin")
    st.balloons()
  else:
      bar.progress(len(answers)/len(quiz))
      st.write("Ban chua dien day du thong tin")
for i in range(len(answers)):
  st.write(quiz[i], answers[i])
