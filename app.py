import streamlit as st
import os
import pandas as pd
import pdfplumber

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Resume Screener",page_icon="📄",layout="wide")

st.markdown("""
<style>

.stApp { background:#0E1117;}

.block-container{ padding-top:2rem;}

.title{ font-size:45px; font-weight:bold; text-align:center; color:#00FFD5;}

[data-testid="stMetric"]{ 
background:#171717;
padding:10px;
border-radius:15px;
}

.card{
background:#171717;
padding:15px;
border-radius:16px;
border:1px solid #2A2A2A;
transition:0.3s;
text-align:center;
}


.card:hover{
transform:translateY(-6px);
box-shadow: 0px 0px 25px rgba(0,255,200,0.5);
}


.small{
font-size:16px;
color:#AAAAAA;
}


.big{
font-size:35px;
font-weight:bold;
}

</style>

""",
unsafe_allow_html=True)


st.markdown(

"""

<div class='title'>

<h1>📄AI Resume Ranking Dashboard</h1>

</div>

""",

unsafe_allow_html=True)


def extract_text(path):

    text=""

    try:

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:

                t = page.extract_text()

                if t:
                    text+=t

    except:
         pass

    return text


RESUME_FOLDER="data/resumes"
JOB_FILE="data/job_description.txt"


with open(JOB_FILE,"r",encoding="utf-8") as f:
    job=f.read()


resume_names=[]
resume_text=[]


for file in os.listdir(RESUME_FOLDER):

    if file.endswith(".pdf"):

        path=os.path.join(RESUME_FOLDER,file)

        text = extract_text(path)

        resume_names.append(file )

        resume_text.append(text)

if resume_text:

    docs=[job.lower()]+[r.lower() for r in resume_text ]

    tfidf=TfidfVectorizer(stop_words="english")

    matrix=tfidf.fit_transform(docs)

    scores=cosine_similarity(matrix[0:1],matrix[1:])[0]

    result=pd.DataFrame({

        "Resume":   resume_names,

        "Match %": (scores*100).round(2)

    })


    result=result.sort_values(

        "Match %", ascending=False

    )


    result.index=range(1,len(result)+1)

    c1,c2=st.columns(2)


    with c1:

        st.metric("📂 Total Resumes",len(result))


    with c2:

        st.metric("🏆 Highest Match",
               str( result.iloc[0]["Match %"])+" %" )

    st.divider()


    st.subheader("🏆 Resume Ranking")


    st.dataframe(

        result,
        use_container_width=True

    )

    st.divider()

    st.subheader("✨ Match Dashboard")

    total=len(result)


    for start in range(0,total,3):


        cols=st.columns(3,gap="large")

        for i in range(3):

            pos=start+i

            if pos<total:
                row=result.iloc[pos]

                score=row["Match %"]

                if pos<total*0.3:
                    emoji="🟢"
                    label="Strong"

                elif pos<total*0.7:
                    emoji="🟡"
                    label="Medium"

                else:
                    emoji="🔴"
                    label="Low"

                with cols[i]:

                    st.markdown(

f"""

<div class="card">

<h4>📄

<br>

{row["Resume"]}

</h4>

<div class="big">

{score:.1f}%

</div>

<div class="small">

{emoji}

{label}

</div>

</div>

""",

unsafe_allow_html=True
)
                    st.progress(int(score))

        st.markdown(

"""

<div
style='height:50px'>
</div>

""",

unsafe_allow_html=True
)

    st.divider()


    st.subheader("📊 Ranking Chart")


    st.bar_chart( result.set_index("Resume"))