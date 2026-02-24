import streamlit as st



from Tokenizer import Tokenizer





st.title("🚀 How AI CONVERT TEXT INTO TOKEN USING  THEIR TOKENIZER")
st.header(" INPUT YOUR VALUE IN TEXT  ")








user_input = st.text_input("Your Input :")
tk=Tokenizer(user_input)

def EncodeInput():
    
    enc = tk.Encoder()
    print("your tokens are :",enc)
    return enc
    
def DecodeInput():
     enc_val=EncodeInput()
     
     return tk.Decoder(enc_val)
 
        

if st.button("see tokens "):
    if not user_input:
        st.error('user_input is empty ', icon="🚨")
    else:
         st.write(f"based on your input the token generated : ",EncodeInput())
    
    
    
    
if st.button("decode tokens "):
    if not user_input:
        st.error('user_input is empty ', icon="🚨")
    else:
        st.write(f"based on your tokens -> text  generated : ",DecodeInput())
    
        
        
    
     

    