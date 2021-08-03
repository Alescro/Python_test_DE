## Python_test_DE

This project contributes to create a nested JSON file refering to the dependencies of each drugs and their mentioning in articles from different journals according to the following rules:
* drug is considered as mentioned in PubMed article or in clinical test if it's mentioned in publication title.
* drug is considered as mentioned bu journal if it is mentioned in publication issued by this journal.

All input files are located in ```resources/inputs``` folder.
They are: 
 - clinical_trials.csv
 - drugs.csv
 - pubmed.csv
 - pubmed.json

There is also an ad-hoc feature to help us find the journal which mentions the most of distinct drugs

## How to set up the environment : 

On PyCharm:
Configure Python Interpreter > Add interpreter > Choose an already existing interpreter or create a new one.

* Simply Run DrugsETL.py for the Extract-Transform-Load part of the pipeline, writing a Nested JSON output in ```resources/outputs``` folder.
* Simply Run AdhocTreatment.py for the specific data treatment showing the top journals mentioning the most distinct drugs in their articles.

A job scheduler like Airflow would be able to run the code in the 'utils' folder with python utils (helpers) that could be launched from the 'main' folder.




##
## Questions (in French):


#### 1. Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ? ###


* Pandas est très efficace avec les petites données (généralement de 100 Mo à 1 Go), sur de grosses volumétries de données il est normal de rencontrer de faibles performances et un temps d'exécution long qui se traduit par une utilisation insuffisante de la mémoire.
  
* Les données volumineuses sont généralement stockées dans des **clusters** de calcul pour une meilleure évolutivité et une meilleure tolérance aux pannes. On peut considérer l'implémentation d'un écosystème Big data Cloud (AWS, Hadoop, AZure) en utilisant des outils comme Spark par exemple et une plateforme de traitement de big data comme Databricks


#### 2. Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ? ###

* Passer sur un environnement Cloud avec un framework Spark et un hébergement des clusters sur Databricks. Cela permet de faire tourner plusieurs **workers** qui gèrent et traitent les **chunks** de large datasets, le tout géré par un **driver node**. La nature distribuée de Spark permet de faire évoluer le système jusqu'à des To de données. Jamais limité par la mémoire vive d'une seule machine. Le renseignement d'un paramètre utile comme le spark.sql.shuffle.partitions permettrait des performances optimales.
* Une façon d'utiliser Pandas avec de grandes données sur des machines locales (avec certaines contraintes de mémoire) serait de réduire l'utilisation de la mémoire des données.
* Filtrer certaines colonnes non essentielles dès la lecture des fichiers pour économiser plus de mémoire.
* Conversion des fichiers d'entrée csv en tables Delta cela aurait pour conséquence une augmentation de la vitesse de lecture et un contrôle de validation du schéma des données d'entrée. Cette méthode serait notamment une très bonne adaptation au sources de données en streaming.

