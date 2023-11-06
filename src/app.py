import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIEND_ID")
client_secret = os.environ.get("CLIENT_SECRET")

print(client_id)
print(client_secret)

from dotenv import load_dotenv
import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el CLIENT_ID y CLIENT_SECRET desde las variables de entorno
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Configurar la autenticación con las claves
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = Spotify(auth_manager=auth_manager)

artist_id = "52iwsT98xCoGgiGntTiR7K"
# Obtener las 10 canciones principales del artista
top_tracks = sp.artist_top_tracks(artist_id)

# Imprimir las 10 canciones principales
print(f"Las 10 canciones principales de {top_tracks['tracks'][0]['artists'][0]['name']} son:")
for track in top_tracks['tracks'][:10]:
    print(f"{track['name']} - {', '.join([artist['name'] for artist in track['artists']])}")


# Crear un DataFrame a partir de los datos de las canciones principales
df = pd.json_normalize(top_tracks['tracks'])

# Seleccionar las columnas de interés
df = df[['name', 'duration_ms', 'popularity']]

# Obtener el top 3 de canciones más populares
top3 = df.sort_values(by='popularity', ascending=False).head(3)

print(top3)

df_top3 = df.sort_values(by='popularity', ascending=False).head(3)


plt.barh(df_top3['name'], df_top3['popularity'])

# Configura las etiquetas de los ejes
plt.xlabel('Popularidad')
plt.ylabel('Canción')
plt.title('Las Tres Canciones Más Populares')

# Muestra el gráfico
plt.show()



