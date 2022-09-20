import pyaudio  
import pandas as pd


def extract_metadata():
    df_metadata = pd.read_csv('data/LJSpeech-1.1/metadata.csv', delimiter = '|', header=None)
    df_metadata.columns = [str(x).replace(str(x),str(x)) for x in ['filenames','text','text2']]
    return df_metadata

def play_audio(f, chunk = 1024):
    """ Input a f from wave.open(file.wav,"rb")  """

    #instantiate PyAudio  
    p = pyaudio.PyAudio()  

    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                                                    channels = f.getnchannels(),  
                                                    rate = f.getframerate(),  
                                                    output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  
        
    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()