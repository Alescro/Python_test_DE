## Python_test_DE



``` README.md```



#### 1. Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ? ###


* Pandas est très efficace avec les petites données (généralement de 100 Mo à 1 Go), sur de grosses volumétries de données il est normal de rencontrer de faibles performances et un temps d'exécution long qui se traduit par une utilisation insuffisante de la mémoire.
  
* Les données volumineuses sont généralement stockées dans des **clusters** de calcul pour une meilleure évolutivité et une meilleure tolérance aux pannes. On peut considérer l'implémentation d'un écosystème Big data Cloud (AWS, Hadoop, AZure) en utilisant des outils comme Spark par exemple et une plateforme de traitement de big data comme Databricks


#### 2. Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ? ###

* Passer sur un environnement Cloud avec un framework Spark et un hébergement des clusters sur Databricks. Cela permet de faire tourner plusieurs **workers** qui gèrent et traitent les **chunks** de large datasets, le tout géré par un **driver node**. La nature distribuée de Spark permet de faire évoluer le système jusqu'à des To de données. Jamais limité par la mémoire vive d'une seule machine. Le renseignement d'un paramètre utile comme le spark.sql.shuffle.partitions permettrait des performances optimales.
* Une façon d'utiliser Pandas avec de grandes données sur des machines locales (avec certaines contraintes de mémoire) serait de réduire l'utilisation de la mémoire des données.
* Filtrer certaines colonnes non essentielles dès la lecture des fichiers pour économiser plus de mémoire.
* Conversion des fichiers d'entrée csv en tables Delta cela aurait pour conséquence une augmentation de la vitesse de lecture et un contrôle de validation du schéma des données d'entrée. Cette méthode serait notamment une très bonne adaptation au sources de données en streaming.

