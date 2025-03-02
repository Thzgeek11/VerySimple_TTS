from TTS.api import TTS
import datetime
import torch
import time
import os
import re

class SimpleTTS:
    def __init__(self, voice_folder='Voix', output_dir='output'):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.voice_folder = voice_folder
        self.output_dir = output_dir
        self.current_date = datetime.datetime.now().strftime('%d-%m-%Y')
        
        # Initialisation du modèle
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
        
        # Configuration des dossiers
        self._scan_voice_files()
        self._create_output_directory()
        
    def _scan_voice_files(self):
        """Scan le dossier des voix disponibles"""
        if not os.path.exists(self.voice_folder):
            raise FileNotFoundError(f"Dossier voix introuvable: {self.voice_folder}")
            
        self.voices = {}
        for f in os.listdir(self.voice_folder):
            if f.endswith(".wav"):
                name = f[:-4]
                self.voices[name] = os.path.join(self.voice_folder, f)
                
        if not self.voices:
            raise ValueError("Aucun fichier .wav trouvé dans le dossier voix")

    def _create_output_directory(self):
        """Crée le dossier de sortie"""
        self.date_dir = os.path.join(self.output_dir, self.current_date)
        os.makedirs(self.date_dir, exist_ok=True)
        
    def _generate_filename(self, voice_name):
        """Génère un nom de fichier unique"""
        num = len(os.listdir(self.date_dir)) + 1
        return f"{num}_{voice_name}_{time.strftime('%Hh%M')}.wav"

    def clean_text(self, text):
        """Nettoie le texte d'entrée"""
        return re.sub(r"[*#©/|\-]", "", text).strip()

    def list_voices(self):
        """Liste les voix disponibles"""
        return list(self.voices.keys())

    def generate_speech(self, text, voice_name):
        """
        Génère un fichier audio à partir du texte
        Retourne le chemin du fichier généré
        """
        if voice_name not in self.voices:
            raise ValueError(f"Voix inconnue: {voice_name}. Voix disponibles: {self.list_voices()}")
            
        cleaned_text = self.clean_text(text)
        if not cleaned_text:
            raise ValueError("Le texte ne peut pas être vide après nettoyage")
            
        file_path = os.path.join(self.date_dir, self._generate_filename(voice_name))
        
        self.tts.tts_to_file(
            text=cleaned_text,
            speaker_wav=self.voices[voice_name],
            language="fr",
            file_path=file_path
        )
        
        return file_path

# Exemple d'utilisation
if __name__ == "__main__":
    tts = SimpleTTS()
    
    print("Voix disponibles:", tts.list_voices())
    
    # Génération d'un exemple
    try:
        generated_file = tts.generate_speech(
            text="Bonjour, ceci est une démonstration du module TTS simplifié.",
            voice_name="ma_voix"  # Remplacez par un nom de voix existant
        )
        print(f"Fichier généré avec succès: {generated_file}")
    except Exception as e:
        print(f"Erreur: {e}")