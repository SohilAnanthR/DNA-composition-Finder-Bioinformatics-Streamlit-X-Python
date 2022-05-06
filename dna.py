import altair as alt
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np



_,col2, _ =st.columns([1,3,1])
with col2:
    st.header('DNA Composition Finder :')


sequence_input = ">DNA Query:\n"


sequence = st.text_area("Sequence input", sequence_input, height=150)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Skips the sequence name (first line)
sequence = ''.join(sequence)  # Concatenates list to string

st.write("""
***
""")





st.header('OUTPUT (DNA Nucleotide Count)')


st.subheader('1.Python Output:')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = DNA_nucleotide_count(sequence)

X








st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)


st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)


st.header("Find the percentage compositon of each nucleotide : ")

seq1 = st.text_input("Enter your Dna sequence :")
seq = st.text_area("sequence input",seq1, height=250)
seq = seq.splitlines()

st.write("""
***
""")

aCount=0
cCount=0
tCount=0
gCount=0

for d in seq1:
    if d == 'A':
        aCount = aCount+1
    elif d == 'C':
        cCount = cCount + 1
    elif d == 'T':
        tCount = tCount + 1
    elif d == 'G':
        gCount = gCount + 1

seqlength=len(seq1)

st.write("Percentage of A's in the given sequence:",(float(aCount)/seqlength) * 100)
st.write("Percentage of C's in the given sequence:",(float(cCount)/seqlength) * 100)
st.write("Percentage of T's in the given sequence:",(float(tCount)/seqlength) * 100)
st.write("Percentage of G's in the given sequence:",(float(gCount)/seqlength) * 100)


