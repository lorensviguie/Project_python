# **Project python**
*Groupe n°15 : MACE Léo, DERONNE Mathis, VIGUIS Lorens*  

## Prérequis 
**[🐍Python v3.10](https://www.python.org/downloads/) [📚Ursina](https://www.ursinaengine.org) [📚Numpy](https://numpy.org)**

# Duck.exe

Duck.exe est un jeu dans lequel vous incarnerez un canard qui a pour objectif de récupérer un coffre au trésor.
Pour ce faire vous devrez parcourir un monde remplis de monstre pouvant vous tuez en seulement quelque attaque alors faites bien attention à vous.

Dans ce jeu vous allez avoir la possibilité de choisir une classe parmis le 3 classes suivante :
- **Mage :** Grâce à leur magie, les canards mage réduissent de 20% les dommages qu'ils subissent.
- **Warrior :** Grâce à leur musculatures imposante, les canards warrior augmentent leur puissance d'attaque de 3 unités.
- **Thief :** Grâce à leurs armes spécialisé pour les missions discrètes, les carnards Thief voient leurs attaques ignorer la défense de leurs adversaires.

Mais faites attention et observez bien votre environnement, celui-ci pourrait bien vous cacher quelques secrets.
Comme nous sommes gentils, nous acceptons humblement de vous présentez quelques spécificités présente dans l'environnement de Duck.exe.

### **Des sols cassable :** 

<img src="./Assets/soldestructible.png" alt="image" width="50" height="auto">

Ces sols ont la faculté de pouvoir être détruit en quelques coup de bec, ils pourraient bien bloquer l'accès à quelques chemins intéressant.

### **Des boutons :**

<img src="./Assets/levierOn.png" alt="image" width="50" height="auto">
<img src="./Assets/levierOff.png" alt="image" width="50" height="auto">

Des boutons pouvant être activés sont cachés dans l'environnement, l'activation de certains d'entre eux seront peut-être nécessaire pour atteindre le trésor tant convoité.

### **Des zones activables :**

<img src="./Assets/activablesol.png" alt="image" width="50" height="auto">

Ces zones semble être alimentés par quelque chose, il doit sûrement être possible de couper leur alimentation, qui sait, il se passera peut-être quelque chose.

### **Des points de régénération :**

<img src="./Assets/health.png" alt="image" width="50" height="auto">

Les combats vont sûrement vous fatiguer ou bien vous blesser, des points de régénération sont présent afin de vous soigner un peu.

### **Le trésor :**

<img src="./Assets/end.png" alt="image" width="50" height="auto">

Vous ne vous aventurez pas dans le danger pour aucune raison. La raison la voici, un magnifique coffre au trésor, source d'envie.

<br>
<br>

> ***Toutes les manières sont bonne pour atteindre son objectif, mais se battre n'est pas forcément la meilleure d'entre elle.***

<br>
<br>
<br>

## Fonctionalités :

<br>

```
- Déplacements horizontaux|verticaux

- Système de gravité

- Gestion des collisions

- Interraction avec l'environnement

- Système de combat

- Gestion de classes

- Gestion de la vie du personnage

- Apparition de la map en suivant l'avancé du joueur

- Système d'activation des trait de vision des monstres|joueur via une variable

- Système de visualisation de la carte via un variable
```