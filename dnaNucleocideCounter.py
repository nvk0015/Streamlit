##Importing the libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#Page title
image = Image.open('nucleotide.png')
st.image(image,use_column_width=True)
st.write("""
# DNA Nucleotide Count Web Application

This app counts the nucleotide composition quiery DNA
***
""")

#Input Textbox
st.header('Enter DNA sequence')
sequence_input = "Input DNA sequence\nNewLine\nNewline2"
#taking input of the dna sequence as an input and preprocessing the data
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence=sequence[1:] #considering first line is a heading, and the input of dna data starts from second line
sequence = ''.join(sequence) #joining all the lines of dna sequence to form a single list.


st.write("""
***
""")
st.header('Input (DNA Query)')
sequence #prints the sequence

#DNA nucleotide count
st.header('Output (DNA Nucleotide Count)')

#1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d
X = DNA_nucleotide_count(seq=sequence)
#X_label = list(X)
#X_values = list(X.values())
X # prints the dictionary

#2. Print the text
st.subheader('2. Print text')
st.write('There are '+str(X['A'])+' adenine(A)')
st.write('There are '+str(X['T'])+' thymine(T)')
st.write('There are '+str(X['G'])+' guanine(G)')
st.write('There are '+str(X['C'])+' cytosine(C)')

##3. Displaying a Dataframe
st.subheader('3. Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis= 'columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

##4. Plot Bar chart
st.subheader('4. Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p=p.properties(
    width=alt.Step(80)
)
st.write(p)