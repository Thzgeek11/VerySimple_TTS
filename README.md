# Documentation du Module `VerySimpleTTS`

Le module `VerySimpleTTS` permet de générer des fichiers audio à partir de texte en utilisant un modèle de synthèse vocale (TTS). Il est conçu pour être simple à utiliser, tout en offrant des fonctionnalités de base pour la gestion des voix et des fichiers de sortie.

---

## Installation

### Dépendances
Assurez-vous d'avoir installé les dépendances suivantes :
```bash
pip install TTS torch
```

### Téléchargement
Placez le fichier `verysimple_tts.py` dans votre projet.

---

## Utilisation

### Initialisation
Importez et initialisez le module :
```python
from verysimple_tts import SimpleTTS

# Initialisation avec les dossiers par défaut
tts = SimpleTTS()

# Initialisation avec des dossiers personnalisés
tts = SimpleTTS(voice_folder='chemin/vers/voix', output_dir='chemin/sortie')
```

---

## Méthodes

### `list_voices()`
Retourne la liste des voix disponibles dans le dossier `voice_folder`.

**Exemple :**
```python
voix_disponibles = tts.list_voices()
print(voix_disponibles)
```

---
s
### `generate_speech(text, voice_name)`
Génère un fichier audio à partir du texte fourni, en utilisant la voix spécifiée.

**Paramètres :**
- `text` (str) : Le texte à convertir en parole.
- `voice_name` (str) : Le nom de la voix à utiliser (doit correspondre à un fichier `.wav` dans le dossier `voice_folder`).

**Retourne :**
- Le chemin du fichier audio généré.

**Exemple :**
```python
fichier_audio = tts.generate_speech(
    text="Bonjour, ceci est une démonstration.",
    voice_name="ma_voix"
)
print(f"Fichier généré : {fichier_audio}")
```

---

### `clean_text(text)`
Nettoie le texte en supprimant les caractères spéciaux indésirables.

**Paramètres :**
- `text` (str) : Le texte à nettoyer.

**Retourne :**
- Le texte nettoyé.

**Exemple :**
```python
texte_propre = tts.clean_text("Ceci *est# un@ texte!")
print(texte_propre)  # Affiche : "Ceci est un texte"
```

---

## Structure des Dossiers

### Dossier des Voix (`voice_folder`)
- Contient des fichiers `.wav` utilisés comme modèles de voix.
- Le nom du fichier (sans l'extension) est utilisé comme nom de voix.
- Exemple : `ma_voix.wav` → Nom de voix : `"ma_voix"`.

### Dossier de Sortie (`output_dir`)
- Les fichiers audio générés sont enregistrés dans un sous-dossier nommé selon la date actuelle (`jour-mois-année`).
- Exemple de structure :
  ```
  output/
  ├── 01-01-2024/
  │   ├── 1_ma_voix_14h30.wav
  │   └── 2_autre_voix_15h00.wav
  └── 02-01-2024/
      └── 1_ma_voix_09h15.wav
  ```

---

## Gestion des Erreurs

Le module lève des exceptions dans les cas suivants :
- **Dossier voix introuvable** : Si le dossier `voice_folder` n'existe pas.
- **Aucune voix disponible** : Si aucun fichier `.wav` n'est trouvé dans `voice_folder`.
- **Voix inconnue** : Si le nom de voix fourni ne correspond à aucun fichier.
- **Texte vide** : Si le texte fourni est vide après nettoyage.

---

## Exemple Complet

```python
from verysimple_tts import SimpleTTS

# Initialisation
tts = SimpleTTS()

# Liste des voix disponibles
print("Voix disponibles:", tts.list_voices())

# Génération de parole
try:
    fichier_audio = tts.generate_speech(
        text="Bonjour, ceci est une démonstration du module TTS simplifié.",
        voice_name="ma_voix"  # Remplacez par un nom de voix existant
    )
    print(f"Fichier généré avec succès: {fichier_audio}")
except Exception as e:
    print(f"Erreur: {e}")
```

---

## Licence
Ce module est fourni sous licence MIT. Utilisez-le librement dans vos projets.

