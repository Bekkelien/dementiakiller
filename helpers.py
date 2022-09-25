import pyaudio  
import pandas as pd

def extract_metadata(file_path):
    if 'LJSpeech-1.1' in str(file_path):
        df_metadata = pd.read_csv(str(file_path), delimiter = '|', header=None)
        df_metadata.columns = [str(x).replace(str(x),str(x)) for x in ['filenames','text','text2']]
        return df_metadata


def play_audio(f, chunk = 1024):
    """ Input a f from wave.open(file.wav,"rb")  """

    # Instantiate PyAudio  
    p = pyaudio.PyAudio()  

    # Open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                                                    channels = f.getnchannels(),  
                                                    rate = f.getframerate(),  
                                                    output = True)  
    # Read data  
    data = f.readframes(chunk)  

    # Play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  
        
    # Stop stream  
    stream.stop_stream()  
    stream.close()  

    # Close PyAudio  
    p.terminate()