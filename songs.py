'''
Name: Sophia Medallada
Project: Taylor Swift Eras Tour Song Mood Recommender
Purpose: Recommend a song based on their current mood
'''
def read_eras(file_path): #reads the eras.txt file and splits it up into 3 different categories: song, album and mood
    eras_dict = {}
    eras_file = open(file_path, 'r')
    for line in eras_file:
        song, album, mood = map(str.strip, line.split('\t'))
        eras_dict[song] = {'Album': album, 'Mood': mood}
    return eras_dict

def song_recommend(eras_dict, mood): #gets the mood from user and checks to see if the mood equals to the song that's based on it
    rec_song = [song for song, info in eras_dict.items() if info['Mood'].lower() == mood.lower()]
    if rec_song:
        print(f"Recommended songs for {mood} mood:")
        for song in rec_song:
            print(f"Song: {song}, Album: {eras_dict[song]['Album']}")
    else:
        print(f"No songs found for {mood} mood.")

file_path = 'eras.txt'
song_data = read_eras(file_path)

print('Taylor Swift Eras Tour Song mood Recommender')
user_mood = input("Which mood are you in? (Romantic, Happy, Sad, Powerful, Calm, Powerful, Proud): ")
song_recommend(song_data, user_mood)
