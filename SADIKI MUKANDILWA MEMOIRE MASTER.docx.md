

Par 

SADIKI MUKANDILWA Denis

# **Table des matières** {#table-des-matières}

**[Table des matières](#table-des-matières)**	[1](#table-des-matières)

[**LISTE DES ABREVIATIONS ET SIGLES**	3](#liste-des-abreviations-et-sigles)

[**LISTE DES TABLEAUX**	5](#liste-des-tableaux)

[**LISTE DES FIGURES**	6](#liste-des-figures)

[**EPIGRAPHIE**	7](#epigraphie)

[**DEDICACES**	8](#dedicaces)

[**REMERCIEMENTS**	9](#remerciements)

[**RESUME**	10](#resume)

[**Introduction**	11](#introduction)

[**1.1.**	**Problématique**	11](#problématique)

[**1.2.**	**Questions de recherche et hypothèses**	14](#questions-de-recherche-et-hypothèses)

[**1.3.**	**Objectifs**	14](#objectifs)

[**1.4.**	**Intérêt de la recherche**	15](#intérêt-de-la-recherche)

[**1.5.**	**Canevas du travail**	16](#canevas-du-travail)

[**CHAPITRE 1 :** REVUE DE LA LITTÉRATURE	17](#chapitre-1-:-revue-de-la-littérature)

[**1.1. Biodiversité, faune sauvage et enjeux de conservation en milieu tropical**	17](#1.1.-biodiversité,-faune-sauvage-et-enjeux-de-conservation-en-milieu-tropical)

[**1.2. Inventaires fauniques et méthodes de suivi de la faune sauvage**	18](#1.2.-inventaires-fauniques-et-méthodes-de-suivi-de-la-faune-sauvage)

[**1.3. Limites des méthodes classiques de traitement des données issues des caméras pièges**	19](#1.3.-limites-des-méthodes-classiques-de-traitement-des-données-issues-des-caméras-pièges)

[**1.4. Fondements théoriques de l’intelligence artificielle et de l’apprentissage profond**	19](#1.4.-fondements-théoriques-de-l’intelligence-artificielle-et-de-l’apprentissage-profond)

[**1.5. Applications de l’intelligence artificielle aux inventaires fauniques**	20](#1.5.-applications-de-l’intelligence-artificielle-aux-inventaires-fauniques)

[**1.6. Défis et perspectives de l’intelligence artificielle pour le suivi faunique en Afrique tropicale**	21](#1.6.-défis-et-perspectives-de-l’intelligence-artificielle-pour-le-suivi-faunique-en-afrique-tropicale)

[**1.7. Concepts clés de l’étude**	21](#1.7.-concepts-clés-de-l’étude)

[**CHAPITRE 2 : MATERIEL ET METHODES**	23](#chapitre-2 :-materiel-et-methodes)

[**2.1. Milieu**	23](#2.1.-milieu)

[**Situation géographique**	23](#situation-géographique)

[**2.2. Approche méthodologique**	23](#2.2.-approche-méthodologique)

[**CHAPITRE 3 :** RESULTATS ET DISCUSSION	24](#chapitre-3 :-resultats-et-discussion)

[**3.1. RESULTATS**	24](#3.1.-resultats)

[**3.2. DISCUSSION**	24](#3.2.-discussion)

[**CONCLUSION ET RECOMMANDATIONS**	25](#conclusion-et-recommandations)

[**Références bibliographiques**	26](#références-bibliographiques)

# **LISTE DES ABREVIATIONS ET SIGLES** {#liste-des-abreviations-et-sigles}

**A **:

**B **:

**CNN **: Convolutional Neural Networks CNN (réseaux de neurones convolutifs)

**D **:

**E **:

**F **:

**G **:

**H **:

**IA **: Intelligence Arficielle

**J **:

**K **:

**LSTM **: 

**M **:

**N **:

**O **:

**P **:

**Q** :

**RDC **: République Démocratique du Congo

**RNN** : Réseaux de neurones récurrents (RNN)

**S** :

**T **:

**U **:

**V **:

**W **:

**X **:

**Y **:

**Z **:

# **LISTE DES TABLEAUX** {#liste-des-tableaux}

# **LISTE DES FIGURES** {#liste-des-figures}

# **EPIGRAPHIE** {#epigraphie}

*« Tu commences à exister sur cette terre quand tu te découvres réellement peu importe ton âge »*

**Denis SADIKI**

**« ***Avant d’avoir les cheveux blancs, il faut d’abord les avoir eus les noirs*** »**

**Bernard Dadié**

**«** *Est orphelin celui qui a perdu l’espoir et non ses parents*** »**

**Proverbe Baoulé**

**« ***Pour bâtir haut, il faut creuser bas*** »**

**Proverbe Chinois**

# **DEDICACES** {#dedicaces}

*A mon Dieu Tout Puissant créateur de toutes choses qui nous a donné le souffle de vie durant toute la période de notre vie et son assistance pendant nos études. Nous sommes infiniment reconnaissants pour sa bonté, sa gloire et sa protection.* 

*A celui qui pour moi est l’incarnation de la paternité parfaite mon père Denis SADIKI ;* 

*A la femme la plus forte, la plus belle et la plus courageuse qui existe Helene MUKANDALA ma mère ;* 

*A mes frères Vicky ABELI et Glody ISSA ;* 

*A ma soeur Merdie MWAMINI ;* 

*A ma belle-soeur Belotte MAYINDOMBE ;* 

*A mes trois filles Chloé-Grâce, Tehilla-Mila et Eliorah AMANI ABELI mes photocopies ;* 

*A celle qui depuis l’éternité a été choisi pour être notre compagne ;* 

*A la grande famille de l’école du dimanche de l’église Vie Eternelle.* 

	*Je dédie ce travail \!* 

**SADIKI MUKANDILWA Denis**

# **REMERCIEMENTS** {#remerciements}

Avant toutes choses nous rendons grâce à celui en qui nous trouvons la force et la capacité d’exister, celui en qui nous terminons notre premier cycle universitaire. Gloire et louange à notre Seigneur Jésus-Christ. 

Nous exprimons notre profonde gratitude à toutes les personnes qui ont contribué de près ou de loin à la réalisation de ce travail. Tout d'abord, nous adressons nos remerciements au professeur OPELELE OMENO Michel pour sa précieuse direction tout au long de cette étude. 

A ma famille restreinte que j’aime de tout cœur. 

Un remerciement particulier est adressé à mon ami depuis l’école secondaire qui a rendu possible ce travail dans la partie architecture et implémentation du modèle d’intelligence artificielle Brummel DUASENGE MAYANO. 

A nos encadreurs académiques Joseph ABEDI, Gaëtan BAYA, Josué AUSSE, Josué ENGOMBE, pour leur guidance et leur expertise. 

A mes compagnons de lutte Divin NTUKU, Godefroid KITAMA, Guy LIYONGO et Sammy MOMBALINGO, mes frères de la galère…

A mes fils et filles Helene BINDA, Axel NTUMBA, MacDean TSHISUMPA, je vous aime tous.

A mes amis qui me soutiennent Jelordie, Exaucé, Jason et Skynet, recevez par ces mots, l’expression de ma gratitude

Enfin, nous remercions tous les lecteurs de ce travail et leur souhaitons une agréable lecture.

# **RESUME** {#resume}

**Mots clés **: *Intelligence Artificielle, Inventaire faunique, Apprentissage profond (deep learning), Réseaux de neurones convolutifs, Caméras pièges, Biais d’identification.*

# **Introduction** {#introduction}

1. ## **Problématique** {#problématique}

La biodiversité mondiale traverse actuellement une crise sans précédent, marquée par une accélération significative de l’érosion des espèces, particulièrement au sein des écosystèmes forestiers tropicaux. Ces écosystèmes, qui abritent une part majeure de la diversité biologique mondiale, subissent de fortes pressions anthropiques liées notamment à la déforestation, à la fragmentation des habitats, à l’exploitation forestière, à la surexploitation des ressources fauniques et aux changements d’usage des terres (Dirzo et *al.*, 2014 ; FAO, 2020). Ces perturbations entraînent un déclin rapide des populations animales, compromettant le fonctionnement des écosystèmes et la fourniture de services écosystémiques essentiels au bien-être humain (Cardinale et *al*., 2012).

Dans ce contexte, l’inventaire et le suivi de la faune sauvage constituent des outils fondamentaux pour la conservation et la gestion durable des écosystèmes. Ils permettent d’évaluer l’état des populations animales, d’analyser leurs dynamiques spatio-temporelles et d’orienter les décisions de gestion fondées sur des données scientifiques fiables (Yoccoz et *al*., 2001). Au cours des dernières décennies, les avancées technologiques ont profondément transformé les méthodes de collecte des données fauniques, notamment grâce à l’essor des caméras pièges, qui se sont imposées comme un outil central du suivi faunique en milieu forestier tropical (O’Connell et *al*., 2011).

Les caméras pièges permettent une collecte non invasive des données, une couverture spatiale étendue et une détection efficace des espèces rares, nocturnes ou cryptiques (Burton et *al*., 2015). Toutefois, le déploiement massif de ces dispositifs a conduit à une augmentation exponentielle du volume de données collectées. Un seul programme de suivi peut générer plusieurs centaines de milliers d’images en quelques mois, rendant leur traitement manuel particulièrement long, parfois difficilement reproductible (Swanson et *al*., 2015).

En effet, le traitement des images issues des caméras pièges repose encore majoritairement sur l’identification visuelle manuelle des espèces. Cette approche présente plusieurs limites majeures, elle est fortement dépendante de l’expertise des observateurs, sujette à des biais cognitifs et à une variabilité inter-analystes, et devient rapidement inadaptée face aux volumes massifs de données générés (Meek et *al*., 2014). Ces contraintes méthodologiques limitent la rapidité de production des résultats scientifiques et freinent leur intégration opérationnelle dans les processus de prise de décision en matière de conservation (Wearn & Glover-Kapfer, 2019).

Dans ce contexte, l’intelligence artificielle, et plus particulièrement l’apprentissage profond (*deep learning*), apparaît comme une solution innovante et prometteuse pour optimiser le traitement des données issues des caméras pièges. Les algorithmes d’apprentissage profond permettent d’automatiser l’identification et le comptage des espèces animales à partir d’images, avec des niveaux de précision comparables, voir supérieurs à ceux des experts humains, tout en réduisant considérablement le temps de traitement et les coûts associés (Norouzzadeh et *al*., 2018).

Parmi ces algorithmes, les réseaux de neurones convolutifs (*Convolutional Neural Networks*, CNN) constituent aujourd’hui la référence pour l’analyse automatique des images. Leur architecture permet l’extraction automatique de caractéristiques visuelles complexes telles que les formes, les textures et les motifs, rendant possible l’identification robuste des espèces animales même dans des conditions environnementales variables (LeCun et *al*., 2015). D’autres familles de modèles, telles que les réseaux de neurones récurrents et certaines méthodes d’apprentissage supervisé, complètent ces approches pour l’analyse temporelle, acoustique ou spatiale des données fauniques (Christin et *al*., 2019).

En Afrique tropicale, et plus particulièrement en République Démocratique du Congo, pays clé du bassin du Congo et hotspot mondial de biodiversité, l’intégration opérationnelle de l’intelligence artificielle dans les programmes de suivi faunique demeure encore limitée. Cette situation contraste avec l’intensité des pressions anthropiques exercées sur la faune sauvage et avec l’existence de volumes importants de données issues des caméras pièges, dont le potentiel scientifique et opérationnel reste insuffisamment valorisé (Maisels et *al*., 2013). Plusieurs études menées en Afrique centrale mettent en évidence des phénomènes de défaunation et soulignent la nécessité de renforcer les outils de suivi et de gestion de la faune sauvage (Abernethy et *al*., 2016).

Malgré les avancées observées à l’échelle internationale, peu de travaux ont évalué de manière systématique l’apport de l’intelligence artificielle au traitement des données issues des caméras pièges en contexte tropical africain. Les spécificités écologiques de ces milieux, caractérisées par une forte diversité spécifique, des conditions environnementales complexes et des contraintes logistiques et financières importantes, soulèvent des défis méthodologiques qui nécessitent des approches adaptées (Beery et *a*l., 2019).

Dès lors, la problématique centrale de cette recherche peut être formulée comme suit, malgré la disponibilité croissante des données issues des caméras pièges, leur exploitation demeure limitée par les contraintes du traitement manuel. Il s’agit donc de déterminer dans quelle mesure l’intégration de l’intelligence artificielle, en particulier des modèles d’apprentissage profond basés sur les réseaux de neurones convolutifs, peut améliorer l’efficacité, la précision et la reproductibilité des inventaires fauniques à partir des images de caméras pièges dans les aires protégées de la République Démocratique du Congo (Schneider et *al.*, 2020).

2. ## **Questions de recherche et hypothèses** {#questions-de-recherche-et-hypothèses}

Afin de répondre à cette problématique, cette étude s’articule autour de deux questions de recherche principales et deux hypothèses sont émises dont :

1) *La première question de recherche vise à déterminer si l’intégration des modèles d’apprentissage profond dans le traitement des images issues des caméras pièges permet-elle d’améliorer la performance globale des inventaires fauniques, notamment en termes de précision de classification des espèces, de rapidité d’analyse des données et de fiabilité des informations produites pour le suivi et la gestion de la faune sauvage ?*  
   La première hypothèse stipule que l’utilisation des algorithmes d’intelligence artificielle, en particulier les modèles d’apprentissages profonds basés sur les réseaux de neurones convolutifs, amélioreraient significativement la détection, la classification et l’analyse des espèces animales à partir des images de caméras pièges, par rapport aux méthodes classiques d’identification visuelle manuelle.  
2) *La deuxième question de recherche s’intéresse à savoir si les modèles d’apprentissage profond réduisent-ils les biais d’identification et améliorent-ils la standardisation et la reproductibilité des résultats issus du traitement des données fauniques en contexte tropical africain *?  
   La deuxième hypothèse suggère que les approches basées sur l’apprentissage profond permettent de réduire significativement les biais liés à l’analyse manuelle des données fauniques, tout en produisant des résultats plus standardisés, reproductibles et adaptés au contexte tropical à forte diversité spécifique.

   3. ## **Objectifs**  {#objectifs}

L’objectif général de cette recherche est d’évaluer l’apport de l’intelligence artificielle, en particulier des algorithmes d’apprentissage profond, dans l’optimisation du traitement des données issues des inventaires fauniques par caméras pièges, afin d’améliorer la précision, la rapidité, la fiabilité et la reproductibilité du suivi de la faune sauvage en milieu tropical.

De manière spécifique, il s’agit de (d’):

* comparer quantitativement les performances des méthodes classiques de traitement des données fauniques et celles des approches basées sur l’apprentissage profond, en terme de précision de classification, de temps de traitement et de fiabilité des résultats  
* évaluer la contribution des modèles d’apprentissage profond à la réduction des biais d’identification, à l’amélioration de la standardisation des résultats et à la reproductibilité des données fauniques issues des images de caméras pièges.

  4. ## **Intérêt de la recherche** {#intérêt-de-la-recherche}

Cette recherche présente un intérêt scientifique, méthodologique, opérationnel et socio-économique pour la conservation de la biodiversité en milieu tropical. Sur le plan scientifique, elle contribue à l’enrichissement des connaissances sur l’application de l’intelligence artificielle à l’analyse des données fauniques, tout en comblant un déficit de littérature dans les contextes tropicaux africains, étant donné que la démarche méthodologique met en évidence le potentiel des modèles d’apprentissage profond comme alternative efficace aux méthodes classiques de traitement des données provenant des caméras pièges.

Enfin, l’automatisation du traitement des données issues de ces caméras offre des perspectives de réduction des coûts de suivi, d’optimisation des actions de conservation et de valorisation durable des écosystèmes forestiers tropicaux sur le plan socioéconomique.

5. ## **Canevas du travail** {#canevas-du-travail}

Hormis l'introduction et la conclusion, cette étude est organisée en trois chapitres distincts. Le premier chapitre traite de la revue de la littérature, explorant les travaux existant sur le sujet. Le deuxième chapitre expose le contexte de l'étude, décrivant le milieu d'étude ainsi que le matériel et la méthodologie utilisés pour mener la recherche. Enfin, le troisième chapitre expose les résultats obtenus et propose une discussion approfondie de ces résultats, mettant en lumière leurs implications et leur importance dans le domaine étudié.

# **CHAPITRE 1 :** Revue de la littérature {#chapitre-1-:-revue-de-la-littérature}

Ce chapitre a pour objectif de situer la présente recherche dans l’état actuel des connaissances scientifiques. Il examine les principaux travaux relatifs à la biodiversité et à la conservation de la faune sauvage, aux méthodes d’inventaires fauniques, aux limites des approches classiques de traitement des données issues des caméras pièges, ainsi qu’aux fondements et applications de l’intelligence artificielle dans le suivi faunique. Enfin, il met en évidence les défis spécifiques liés à l’intégration de ces approches en Afrique tropicale et définit les concepts clés mobilisés dans cette étude.

## **1.1. Biodiversité, faune sauvage et enjeux de conservation en milieu tropical** {#1.1.-biodiversité,-faune-sauvage-et-enjeux-de-conservation-en-milieu-tropical}

La biodiversité mondiale connaît une régression accélérée, particulièrement marquée dans les écosystèmes tropicaux qui abritent pourtant la majorité des espèces animales et végétales de la planète (Dirzo et *al*., 2014 ; IPBES, 2019). Plusieurs études mettent en évidence une diminution rapide des populations animales, phénomène largement attribué aux pressions anthropiques croissantes telles que la déforestation, la fragmentation des habitats, l’exploitation forestière, l’expansion agricole et la chasse (Laurance et *al*., 2014 ; FAO, 2020).

La perte de la faune sauvage, communément désignée sous le terme de *défaunation*, ne se limite pas à une simple réduction du nombre d’espèces. Elle affecte profondément le fonctionnement des écosystèmes tropicaux, notamment les processus de dispersion des graines, la régulation des populations biologiques et la résilience écologique face aux perturbations environnementales (Terborgh et *al*., 2008 ; Bello et *al*., 2015). A long terme, ces déséquilibres compromettent la capacité des écosystèmes à fournir des services écosystémiques essentiels au bien-être humain (Cardinale et *al*., 2012).

Dans ce contexte, la conservation de la faune sauvage apparaît comme un enjeu majeur pour la durabilité des écosystèmes forestiers tropicaux. Le suivi régulier et fiable des populations animales constitue une condition indispensable à l’élaboration et à l’évaluation des stratégies de gestion et de conservation des ressources naturelles (Yoccoz et *al.*, 2001). Toutefois, dans de nombreuses régions tropicales, notamment en Afrique centrale, le manque de données fiables et actualisées sur la faune sauvage demeure un obstacle important à une gestion efficace (Maisels et *al*., 2013).

## **1.2. Inventaires fauniques et méthodes de suivi de la faune sauvage** {#1.2.-inventaires-fauniques-et-méthodes-de-suivi-de-la-faune-sauvage}

Les inventaires fauniques regroupent l’ensemble des méthodes visant à identifier, quantifier et suivre les espèces animales présentes dans un espace donné. Historiquement, ces inventaires reposaient sur des techniques classiques telles que les transects linéaires, les observations directes ou indirectes (empreintes, fèces, cris) et les enquêtes auprès des populations locales (Buckland et *al*., 2001). Bien que ces approches aient permis des avancées significatives dans la connaissance de la faune sauvage, elles présentent des limites liées à la détectabilité imparfaite des espèces, aux contraintes logistiques et à la subjectivité des observateurs (Kéry & Royle, 2016).

Avec le développement des technologies de surveillance écologique, les caméras pièges se sont imposées comme un outil central du suivi faunique, en particulier en milieu forestier tropical où l’observation directe est souvent difficile (O’Connell et *al*., 2011). Ces dispositifs automatiques permettent une collecte non invasive des données, une surveillance continue et une détection efficace des espèces rares, nocturnes ou cryptiques (Burton et *al*., 2015). Ils offrent ainsi une amélioration notable de la qualité et de la quantité des données collectées (Rowcliffe et *al.*, 2008).

Cependant, l’augmentation du nombre de caméras déployées et la durée prolongée des campagnes de suivi ont entraîné une croissance exponentielle des volumes de données générées. Cette évolution a déplacé le principal défi des inventaires fauniques, qui ne réside plus uniquement dans la collecte des données mais dans leur traitement et leur analyse efficace (Swanson et *al*., 2015).

## **1.3. Limites des méthodes classiques de traitement des données issues des caméras pièges** {#1.3.-limites-des-méthodes-classiques-de-traitement-des-données-issues-des-caméras-pièges}

Malgré les avantages indéniables des caméras pièges pour la collecte des données fauniques, le traitement de ces données repose encore majoritairement sur l’identification visuelle manuelle des espèces. Cette approche présente plusieurs limites majeures. Elle est particulièrement chronophage et mobilise des ressources humaines importantes, ce qui augmente les coûts des programmes de suivi (Meek et *al.*, 2014).

Par ailleurs, l’identification manuelle est fortement dépendante de l’expertise individuelle des observateurs. Cette dépendance entraîne des biais d’identification, une variabilité inter-analystes et une faible reproductibilité des résultats (Fegraus et *al*., 2011). Ces limites sont d’autant plus problématiques que les volumes de données à traiter sont importants, rendant difficile une exploitation rapide et standardisée des informations collectées (Wearn & Glover-Kapfer, 2019).

Ces contraintes méthodologiques réduisent la capacité des gestionnaires et des chercheurs à valoriser pleinement les données issues des caméras pièges et retardent leur intégration dans les processus de prise de décision en matière de conservation (Geldmann et *al*., 2019).

## **1.4. Fondements théoriques de l’intelligence artificielle et de l’apprentissage profond** {#1.4.-fondements-théoriques-de-l’intelligence-artificielle-et-de-l’apprentissage-profond}

L’intelligence artificielle désigne l’ensemble des techniques informatiques visant à simuler certaines capacités cognitives humaines telles que l’apprentissage, la reconnaissance de formes et la prise de décision (Russell & Norvig, 2021). Parmi ses sous-domaines, l’apprentissage profond occupe une place centrale en raison de sa capacité à traiter de grandes quantités de données complexes à l’aide de réseaux de neurones artificiels à plusieurs couches (Goodfellow et *al.*, 2016).

Les réseaux de neurones convolutifs constituent une classe d’algorithmes particulièrement adaptée à l’analyse automatique des images. Leur architecture permet d’extraire automatiquement des caractéristiques visuelles pertinentes, telles que les formes, les textures et les motifs, sans nécessiter une définition manuelle préalable de ces caractéristiques (LeCun et *al*., 2015). Cette capacité rend les réseaux de neurones convolutifs particulièrement performants pour l’identification automatique des espèces animales à partir d’images issues des caméras pièges (Schneider et *al*., 2018).

D’autres familles d’algorithmes complètent ces approches, notamment les réseaux de neurones récurrents pour l’analyse temporelle et acoustique, ainsi que des méthodes d’apprentissage supervisé telles que les forêts aléatoires et les algorithmes de *gradient boosting* (Cutler et *al*., 2007). Néanmoins, les performances de ces modèles dépendent fortement de la qualité, de la quantité et de la représentativité des données d’entraînement (Christin et *al*., 2019).

## **1.5. Applications de l’intelligence artificielle aux inventaires fauniques** {#1.5.-applications-de-l’intelligence-artificielle-aux-inventaires-fauniques}

De nombreuses études ont démontré l’efficacité de l’intelligence artificielle dans l’analyse des données issues des caméras pièges. Les travaux pionniers montrent que les réseaux de neurones convolutifs peuvent atteindre des niveaux de précision comparables, voir supérieur, à ceux des experts humains pour l’identification et le comptage des espèces animales (Norouzzadeh et *al*., 2018). En outre, ces approches permettent de réduire considérablement le temps de traitement des données et d’améliorer la standardisation des analyses (Beery et *al*., 2019).

Toutefois, la majorité de ces études ont été menées dans des contextes écologiques tempérés, principalement en Amérique du Nord, en Europe et en Asie orientale (Tabak et *al*., 2019). Les milieux tropicaux, caractérisés par une forte diversité spécifique, des conditions environnementales complexes et une hétérogénéité des habitats, restent encore sous-représentés dans la littérature scientifique relative à l’application de l’intelligence artificielle au suivi faunique (Willie et *al.*, 2022).

## **1.6. Défis et perspectives de l’intelligence artificielle pour le suivi faunique en Afrique tropicale** {#1.6.-défis-et-perspectives-de-l’intelligence-artificielle-pour-le-suivi-faunique-en-afrique-tropicale}

En Afrique tropicale, l’intégration de l’intelligence artificielle dans les programmes de suivi faunique demeure encore limitée. Les principales contraintes identifiées concernent le manque de jeux de données annotées, les capacités techniques et infrastructurelles limitées, ainsi que l’absence de cadres méthodologiques adaptés aux réalités locales (Wearn et *al*., 2020).

En République Démocratique du Congo, plusieurs études ont mis en évidence des phénomènes de défaunation et une sous-exploitation des données issues des caméras pièges, malgré l’importance stratégique du pays pour la conservation de la biodiversité mondiale (Abernethy et *al*., 2016 ; Plumptre et *al*., 2016). Cette situation souligne la nécessité de développer des approches innovantes, robustes et transférables, capable de renforcer le suivi et la gestion de la faune sauvage tout en tenant compte des contraintes écologiques, logistiques et institutionnelles propres au contexte congolais.

## **1.7. Concepts clés de l’étude** {#1.7.-concepts-clés-de-l’étude}

* **Inventaire faunique** : ensemble des méthodes visant à identifier, quantifier et suivre les espèces animales au sein d’un écosystème (Buckland et *al*., 2001).

* **Caméras pièges** : dispositifs automatiques de capture d’images ou de vidéos déclenchés par le mouvement ou la chaleur d’un animal 

* **Intelligence artificielle** : ensemble de techniques informatiques permettant à un système de reproduire certaines fonctions cognitives humaines (Russell & Norvig, 2021).

* **Apprentissage profond** : sous-domaine de l’intelligence artificielle reposant sur des réseaux de neurones artificiels à plusieurs couches (Goodfellow et *al*., 2016).

* **Réseaux de neurones convolutifs** : algorithmes d’apprentissage profond spécialisés dans le traitement automatique des images 

* **Biais d’identification** : erreurs ou variations liées à la subjectivité humaine dans l’analyse et l’interprétation des données fauniques 

# **CHAPITRE 2 : MATERIEL ET METHODES** {#chapitre-2 :-materiel-et-methodes}

Ce chapitre expose le contexte de l'étude, décrivant le milieu d'étude ainsi que le matériel et la méthodologie utilisés pour mener la recherche.

## **2.1. Milieu** {#2.1.-milieu}

### **Situation géographique** {#situation-géographique}

## 

## **2.2. Approche méthodologique** {#2.2.-approche-méthodologique}

# **CHAPITRE 3 :** RESULTATS ET DISCUSSION {#chapitre-3 :-resultats-et-discussion}

Ce chapitre expose les résultats obtenus et propose une discussion approfondie de ces derniers, mettant en lumière leurs implications et leur importance dans le domaine étudié

## **3.1. RESULTATS** {#3.1.-resultats}

## **3.2. DISCUSSION** {#3.2.-discussion}

# **CONCLUSION ET RECOMMANDATIONS** {#conclusion-et-recommandations}

# **Références bibliographiques**  {#références-bibliographiques}

* Abernethy, K., Coad, L., Taylor, G., Lee, M. E., & Maisels, F. (2016). *Extents and causes of defaunation in African tropical forests: Implications for conservation*. Biological Conservation, 198, 7–17.   
* Beery, S., Morris, D., & Yang, S. (2019). *Efficient pipeline for species identification and counting in camera trap images*. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops* (pp. 1–9). IEEE.   
* Bello, C., Galetti, M., Pizo, M. A., & Morellato, L. P. C. (2015). *Defaunation affects carbon storage in tropical forests*. Science Advances, 1(2), e1501105.   
* Burton, A. C., Neilson, E., Moreira, D., Ladle, A., Steenweg, R., Fisher, J. T., ... & Boutin, S. (2015). *Wildlife camera trapping: A review and recommendations for linking surveys to ecological processes*. Journal of Applied Ecology, 52(3), 675–685.   
* Buckland, S. T., Anderson, D. R., Burnham, K. P., & Laake, J. L. (2001). *Introduction to distance sampling: Estimating abundance of biological populations*. Oxford University Press.  
* Cardinale, B. J., Duffy, J. E., Gonzalez, A., Hooper, D. U., Perrings, C., Venail, P., ... & Naeem, S. (2012). *Biodiversity loss and its impact on humanity*. Nature, 486(7401), 59–67.   
* Christin, S., Hervet, É., & Lecomte, N. (2019). *Applications for deep learning in ecology*. Methods in Ecology and Evolution, 10(10), 1632–1644.   
* Cutler, D. R., Edwards, T. C., Beard, K. H., Cutler, A., Hess, K. T., Gibson, J., & Lawler, J. J. (2007). *Random forests for classification in ecology*. Ecology, 88(11), 2783–2792.   
* Dirzo, R., Young, H. S., Galetti, M., Ceballos, G., Isaac, N. J. B., & Collen, B. (2014). *Defaunation in the Anthropocene*. Science, 345(6195), 401–406.   
* FAO. (2020). *The State of the World’s Forests 2020: Forests, biodiversity and people*. Food and Agriculture Organization of the United Nations.   
* Fegraus, E. H., Lin, J. F., Ahumada, J. A., & Kays, R. (2011). *Maximizing the value of camera trap surveys*. Wildlife Society Bulletin, 35(1), 1–10.   
* Geldmann, J., Barnes, M., Coad, L., Craigie, I. D., Hockings, M., & Burgess, N. D. (2019). *Effectiveness of terrestrial protected areas in reducing habitat loss and population declines*. Biological Conservation, 237, 289–297.   
* Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press.  
* IPBES. (2019). *Global assessment report on biodiversity and ecosystem services*. Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services.   
* Kéry, M., & Royle, J. A. (2016). *Applied hierarchical modeling in ecology: Analysis of distribution, abundance and species richness in R and BUGS* (Vol. 1). Academic Press.  
* Laureance, W. F., Sayer, J., & Cassman, K. G. (2014). *Agricultural expansion and its impacts on tropical nature*. Trends in Ecology & Evolution, 29(2), 107–116.   
* LeCun, Y., Bengio, Y., & Hinton, G. (2015). *Deep learning*. Nature, 521(7553), 436–444.   
* Maisels, F., Strindberg, S., Blake, S., Wittemyer, G., Hart, J., Williamson, E. A., ... & Wilkie, D. (2013). *Devastating decline of forest elephants in Central Africa*. PLoS ONE, 8(3), e59469.   
* Meek, P. D., Ballard, G. A., Fleming, P. J., Schaefer, M., Williams, W., Falzon, G., & Kavanagh, R. P. (2014). *Camera traps can be heard and seen by animals*. PLoS ONE, 9(10), e110832.   
* Norouzzadeh, M. S., Nguyen, A., Kosmala, M., Swanson, A., Palmer, M. S., Packer, C., & Clune, J. (2018). *Automatically identifying, counting, and describing wild animals in camera-trap images with deep learning*. Proceedings of the National Academy of Sciences, 115(25), E5716–E5725.   
* O’Connell, A. F., Nichols, J. D., & Karanth, K. U. (2011). *Camera traps in animal ecology: Methods and analyses*. Springer.  
* Plumptre, A. J., Maisels, F., & Croes, B. (2016). *Conservation of biodiversity in Central Africa: A review of threats and strategies*. Biological Conservation, 195, 20–33.   
* Rowcliffe, J. M., Field, J., Turvey, S. T., & Carbone, C. (2008). *Estimating animal density using camera traps without the need for individual recognition*. Journal of Applied Ecology, 45(4), 1228–1236.   
* Russell, S., & Norvig, P. (2021). *Artificial intelligence: A modern approach* (4ᵉ éd.). Pearson.  
* Schneider, S., Taylor, G. W., & Kremer, S. (2018). *Deep learning object detection for wildlife monitoring*. Ecological Informatics, 48, 27–34.   
* Schneider, S., Taylor, G., Linquist, S., & Kremer, S. (2020). *Monitoring wildlife with deep learning: Past, present, and future directions*. Ecological Informatics, 55, 101019\.   
* Swanson, A., Kosmala, M., Lintott, C., Simpson, R., Smith, A., & Packer, C. (2015). *Snapshot Serengeti, high-frequency annotated camera trap images of 40 mammalian species in an African savanna*. Scientific Data, 2, 150026\.   
* Tabak, M. A., Norouzzadeh, M. S., Wolfson, D. W., Sweeney, S. J., Vercauteren, K. C., Snow, N. P., ... & Miller, R. S. (2019). *Machine learning to classify animal species in camera trap images: Applications in ecology*. Methods in Ecology and Evolution, 10(4), 585–590.   
* Terborgh, J., Lopez, L., Nuñez, P., Rao, M., Shahabuddin, G., Orihuela, G., ... & Balbas, L. (2008). *Tree recruitment in an empty forest*. Ecology, 89(6), 1757–1768.   
* Wearn, O. R., & Glover-Kapfer, P. (2019). *Camera-trapping for conservation: A guide to best-practices*. Biological Conservation, 233, 116–123.   
* Wearn, O. R., Rowcliffe, M., Carbone, C., & Foster, S. (2020). *The potential for deep learning to revolutionize ecological monitoring*. Ecological Applications, 30(3), e02010.   
* Willie, J., Ndang’ang’a, P., & Mwangi, R. (2022). *Challenges of applying artificial intelligence for wildlife monitoring in tropical Africa*. Conservation Science and Practice, 4(8), e12789.   
* Yoccoz, N. G., Nichols, J. D., & Boulinier, T. (2001). *Monitoring of biological diversity in space and time*. Trends in Ecology & Evolution, 16(8), 446–453. 

Annexe