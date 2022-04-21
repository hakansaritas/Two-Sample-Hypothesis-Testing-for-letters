# -*- coding: utf-8 -*-
"""

@author: Hakan
"""


def letters_of_songs(list_of_bands=["Rainbow"], num_of_song=2, api_key="", dataset_name="my_dataset"):
    
    """
    letter_of_songs_v1.1
    calculation of frequency of the unique letters in lyrics writing in english.

    Args:
        list_of_bands : Artist names you want to analyze, list
        num_of_song: number of songs requested for each artist, int 
        api_key: the api key for reaching Genius database, str
        dataset_name: output dataset name 
        
    Returns:
        df: with variable of ....
            artist_name: artist name,str
            artist_id: groups ID, int
            song_name: song name, str
            song_id: song ID, int
            song_lyric: song lyric without title, str
            A : frequency of A letter,int
            …
            Z: frequency of Z letter,int
        
    Note:
        This function outputs both an excel and a csv
        

    """
    import pandas as pd
    from lyricsgenius import Genius
    
    
    # Genius function with api key

    genius = Genius(api_key, timeout=120, remove_section_headers=True, verbose=False)
    
    df = pd.DataFrame()
    
    
    for band in list_of_bands:
    
        artist_all_lyrics = genius.search_artist(band, max_songs=num_of_song)
    
        for i in range(num_of_song):
            
    # getting songs,artists names and IDs                 
            try:
                lyric_before = artist_all_lyrics.songs[i].lyrics
                song_name = artist_all_lyrics.songs[i].title
                song_id = artist_all_lyrics.songs[i].id
                artist_id = artist_all_lyrics.id
                artist_name = artist_all_lyrics.songs[i].artist
    # upper case    
                lyric_after = lyric_before.split("\n", 1)[1]
                lyric_after = lyric_after.upper()

    # letters list to be searched   
                english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
                                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                number_list = []
    
                for i in english_alphabet:
                    
                    number_list.append(lyric_after.count(i))
    
                zipped_dict = dict(zip(english_alphabet, number_list))
                
   # assignment to variables 
                info_dict = {"artist_name": artist_name,
                             "artist_id": artist_id,
                             "song_name": song_name,
                             "song_id": song_id,
                             "song_lyric": lyric_after.lower()}
    
                info_dict.update(zipped_dict)
    
                last_list = [info_dict]
    
                frame = pd.DataFrame(last_list, columns=info_dict.keys())
    
                df = df.append(frame, True)
    
            except (AttributeError, IndexError):
    
                continue

    # output             
    df.to_excel(dataset_name+".xlsx", index =False)
    df.to_csv(dataset_name, index=False)
    
    return df