import tiktoken

class Tokenizer():
    
    
    def __init__(self,user_input):
        self.user_input=user_input
        self.encoding =  tiktoken.encoding_for_model("gpt-4o-mini")
    def Encoder(self):
           text =self.user_input
          
           
           tokens = self.encoding.encode(text)
           return tokens
       
    def Decoder(self,tokens):
        
        decoded_text = self.encoding.decode(tokens)
        return decoded_text
        
           
            
        