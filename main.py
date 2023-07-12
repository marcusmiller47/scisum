#import openai
#import streamlit as st

from streamlit_chat import message

openai.api_key = st.secrets["pass"]

article_text = st.text_area("Enter scientific text to summarise")

output_size = st.radio(label = "What kind of output do you want?", 
                       options=["To-The-Point","Concise", "Detailed"]
                       )

# Set a token to determine output size 

if output_size == "To-The-Point":
    out_token = 50
elif output_size == "Concise":
    out_token = 128 
else: 
    out_token = 516

# ensure text is long enough to summarise 

if len(article_text)>100:
    
    # generate summary
    if st.button("Generate Summarey", type='primary'):

        # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt = "Please summarise this scientific article for me:"+article_text,
            max_tokens = out_token,
            temperature = 0.5
            )
    
    # print the summary
    res = response["choices"][0]["text"]
    st.success(res)

    # Allow user to save article to device
    st.download_button('Download result', res)

else:
    st.warning("Please supply a longer article!")
