# 🌱 Système d’Irrigation Intelligent avec Raspberry Pi

## 📌 Présentation du projet

Le **Système d’Irrigation Intelligent** est un projet embarqué basé sur un Raspberry Pi permettant d’autatiser l’arrosage des plantes selon l’humidité du sol.

Le système surveille en temps réel l’état du sol grâce à un capteur d’humidité.  
Lorsque le sol devient sec, une pompe à eau est automatiquement activée pour irriguer la plante. Une fois le sol suffisamment humide, la pompe s’arrête automatiquement.

Le projet intègre également :
- Un écran LCD pour afficher l’état du système
- Des LEDs de signalisation
- Un contrôle automatique via les GPIO du Raspberry Pi

Ce projet a pour objectif de réduire le gaspillage d’eau et d’automatiser l’irrigation de manière intelligente.

---

# 🛠️ Composants matériels

- Raspberry Pi
- Capteur d’humidité du sol
- Écran LCD (I2C)
- Pompe à eau
- Module relais
- LED rouge
- LED verte
- Breadboard
- Fils de connexion
- Alimentation

---

# 💻 Logiciels et bibliothèques

- Python 3
- Bibliothèque `RPi.GPIO`
- Bibliothèque `rpi_lcd`

Installation des bibliothèques :

```bash
pip install RPi.GPIO
pip install rpi-lcd
```

---

# ⚙️ Configuration GPIO

| Composant | GPIO |
|------------|------------|
| LED Rouge | GPIO 27 |
| LED Verte | GPIO 22 |
| Capteur d’humidité | GPIO 4 |
| Pompe à eau | GPIO 17 |

---

# 🚀 Fonctionnalités

✅ Surveillance de l’humidité du sol  
✅ Activation automatique de la pompe  
✅ Affichage des informations sur écran LCD  
✅ Indication visuelle avec LEDs  
✅ Contrôle via Raspberry Pi GPIO  
✅ Application embarquée développée en Python  
✅ Solution IoT pour l’agriculture intelligente  

---

# 🔄 Fonctionnement du système

## 🌵 Sol Sec
Lorsque le capteur détecte un sol sec :
- La pompe s’active automatiquement
- La LED rouge s’allume
- L’écran LCD affiche :
  - "DRY SAND"
  - "WATERING"

## 💧 Sol Humide
Lorsque le sol devient humide :
- La pompe s’arrête
- La LED verte s’allume
- L’écran LCD affiche :
  - "WET SAND"

---

# 🧠 Technologies utilisées

- Python
- Raspberry Pi
- Systèmes embarqués
- GPIO
- IoT
- Communication I2C

---

# 📸 Aperçu du projet

Ajoutez vos images dans le dossier `images`.

Exemple :

```markdown
![Système d’irrigation intelligent](images/projet.jpg)
```

---

# ▶️ Exécution du projet

Cloner le dépôt GitHub :

```bash
git clone https://github.com/votre-utilisateur/smart-irrigation.git
```

Accéder au dossier du projet :

```bash
cd smart-irrigation
```

Lancer le programme :

```bash
python3 main.py
```

---

# 📋 Exemple de sortie

```text
Dry Sand
Watering...

Wet Sand
Pump OFF
```

---

# 🎯 Objectifs du projet

- Automatiser l’irrigation des plantes
- Réduire la consommation d’eau
- Apprendre la programmation GPIO avec Raspberry Pi
- Appliquer les concepts IoT dans l’agriculture
- Développer des applications embarquées sous Linux

---

# 👨‍💻 Auteur

**Abdelhak Rezma**  
Ingénieur en électronique de communication


