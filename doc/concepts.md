## concepts

### parametre (parameter) - param en abrégé

un parametre est une valeur individuelle (scalar) ou une structure formée d'autres paramêtres.
un parametre décrit une valeur potentielle d'une application ou système, qui doit être évaluée en fonction
d'un contexte. 
la fonction d'évaluation est une composition d'évaluations successives effectuées par transitions sur le graphe reliant le parametre à ses contenants respectifs jusqu'au niveau applicatif ou système (bottom-up hierarchical navigation) - désigné par le terme "pliage à droite" (right-fold)

exemple: navigation hiérarchique vers le haut (sens des flêches), évaluation par pliage en sens inverse en partant de l'application 
```
json_ktext      --jsonget()--> json_config --endswith()--> <app archive> --warfile()--> paragraph-ui

pom_xml_version --xpath()-->   pom_xml     --endswith()--> <app archive> --warfile()--> paragraph-ui
pom_xml_version --xpath()-->   pom_xml     --applfile()-------------------------------> paragraph-ui
```

### localisation (location) - loc en abrégé

une loc est une expression détaillant comment extraire la valeur d'un parametre, en fonction de son contenant le plus
proche
cette expression prend le plus souvent la forme d'un prédicat de type prolog
exemple:   
```
loc: xpath(//'context-root'(text))
```
ce prédicat peut faire référence à des variables (en majuscule), auquel cas il décrit un générateur d'une ou plusieurs valeurs lors de l'évaluation du parametre
exemple 1: 
```
loc: phrase(js_dcg:angular_module_decl(Val))
``` 
va générer la liste des déclarations de modules Angular au sein d'une application web.
exemple 2: 
le parametre "class_annotation" du pavage "java" définit par exemple cette loc: 
```
loc: dcg:java_class_annotation(Aname, Aprops)
``` 
et va générer la liste des annotations de classes java au sein d'une application.
le parametre "jpa_database_table" est définit comme suit
```
isa: java:class_annotation
loc: q(Aname='Table', Aprops)
``` 
et va générer la liste des annotations d'entités JPA et leur propriétés au sein d'une application java.

### contenants (containers)

un contenant est soit une structure logique (parametre) ou une resource physique (fichier, archive, page web)

### pavage (pavement)

un pavage est un graphe définissant les parametres et leur contenants pour un domaine d'application limité
certains pavages peuvent définir un espace de nom (namespace) référençable par d'autre pavages
exemple: l'annotation JPA (java persistence) "jpa_database_table" est une annotation java, et définit un parametre par référence à un parametre "class_annotation" du pavement "java".

### para-graphe (para-graph)

un para-graphe est une composition de pavages, qui servent à décrire un sous-ensemble de parametres d'une application
  ou d'un système. Cette composition est effectuée par référencement des pavages à l'aide de leur tags respectifs.

### contexte évaluatif (scoper)
#### input scoper
le contexte d'entrée (input scoper) restreint le champ de recherche pour la fonction d'évaluation (paramv)
exemple: "[ag('incodam'), ve('2.5.1')]" restreint l'évaluation aux applications du group 'incodam' en version 2.5.1 
#### output scoper
chaque transition lors de l'évaluation par paramv génère un contexte de sortie (output scoper), qui représente le chemin actuel de recherche dans le para-graphe.
Pour chaque valeur générée par la fonction d'évaluation, il est possible d'appliquer une contrainte sur un des éléments du contexte de sortie. Cette fonctionalité permet par exemple de "chaîner" des appels paramv.
exemple de chaînage: "af" signifie "application file" 
``` 
paramv('maven:pom_xml_version',Version,[ag('incodam')],OutScoper), 
member(af(file(_PomXml)),OutScoper), 
paramv('maven:property',Property,[ag('incodam'),af(_PomXml),_])
```
permet de synchroniser l'extraction de différentes informations de build maven (version de module et ses propriétés) 
sur le même contenant (maven pom.xml)


