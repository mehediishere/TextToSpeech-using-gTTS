#!/usr/bin/env python
# coding: utf-8

# ## TextToSpeech using gTTS(Google Text-to-Speech)

# In[36]:


from gtts import gTTS  #This required module for text to speech conversion
import PyPDF2   # This will be used to extract text from pdf file


# TextToSpeech -- From **pdf** file

# In[37]:


book = open('story2.pdf', 'rb') #So, first we open pdf file
pdfReader = PyPDF2.PdfFileReader(book) # reading the pdf file
pages = pdfReader.numPages # count number of pages, which will help to read a specific or in a range pages


# The process for Specific or Individual page

# In[38]:


page = pdfReader.getPage(0) #Selecting page we want to read. For multiple page reading we'll need to use loop.Check below
textInPage = page.extractText() #Extract text from pdf page


# In[39]:


tts = gTTS(text=textInPage, lang='en', slow=False) # Passing the text and language to the engine

###### _Parameters:_  
# * `text` - String - Text to be spoken.  
# * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in.  
# * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).  

tts.save('story_en.mp3') #Saving the converted audio in a mp3 file. Name give as you wish just add .mp3 at the last.


# The process for full pdf or in a range

# In[40]:


textList=[]
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    textList.append(text)
    
#Converting multiline text to single line text
textString = " ".join(textList)
# print(textString)

tts = gTTS(text=textString, lang='en', slow=False)
tts.save('story_en_101.mp3')


# TextToSpeech -- From **text** file

# In[41]:


# # read text file
# f = open('th.txt','r', encoding="utf8")
# message = f.read()

# print("Message from text file:")
# print(message)
# f.close()

# # message = message.decode('utf-8')

# tts = gTTS(text=message, lang='th', slow=False)
# tts.save('story_th.mp3')

