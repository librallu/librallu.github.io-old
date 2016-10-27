Expérience Générateur de Mots
#############################

:Date: 2016-10-27 01:00
:Category: experiments
:Tags: polymer, experiment, mots
:Slug: experiment-words-generator
:Author: Luc Libralesso
:Summary: Une expérience - Générateur de texte aléatoire
:Image: /images/words-cover.png

Vous avez toujours eu envie de générer votre propre `lipsum <http://lipsum.com/>`_, utilisant vos
mots a vous ?

Maintenant vous pouvez avec cette `application <https://librallu.github.io/polymer-gen-words/>`_.

Daniel Shiffman sur sa `chaîne youtube <https://www.youtube.com/user/shiffman>`_ a présenté
récemment un challenge qui visait à faire un générateur de texte. Il m'a beaucoup inspiré,
ce qui m'a donné l'envie de faire le mien. Si vous êtes intéressés par la programmation en
JavaScript, je vous conseille vivement d'aller voir sa chaîne, elle est vraiment bien (en anglais par contre).

Avec cette app, vous aurez la possibilité de donner en entrée un texte et sera calculé
quand vous cliquerez sur le bouton "generate", un texte étant inspiré de ce que qui a
été entré.
Pour les exemples, j'ai pris deux textes (un en français et un en anglais).

Il y a un autre champ "order". Celui-ci, si il est faible (proche de 1) aura tendence à générer des mots nouveaux,
tandis que si on lui donne une grande valeur, plus le texte généré collera avec le texte original.
Ce paramètre permet donc de jouer sur le niveau d'apprentissage du programme.
