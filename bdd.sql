SQLite format 3   @     �                                                               � -�   �    	�  � �              ��tablebesoinsbesoinsCREATE TABLE besoins(
            id_besoin INTEGER PRIMARY KEY,
            intitule TEXT,
            primaire INTEGER)��tablesystemesystemeCREATE TABLE systeme(
            id_systeme INTEGER PRIMARY KEY,
            exigences TEXT,
            caracteristique TEXT)P++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)�[�tableexigencesexigencesCREATE TABLE exigences(
            idex INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            besoin INT,
            intitule TEXT,
            critere TEXT,
            espece INTEGER,
            niveau INT,
            resultat INT,
            conclusion INT,
            exigence_mere INTEGER)��{tablepiecespiecesCREATE TABLE pieces(
            id_piece INTEGER PRIMARY KEY,
            nom_piece TEXT,
            couleur INT      � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   bamboulienoire    H �t�\�x' � � H                                        O U11Commander de manière télé-opéré
Cahier des chargesBesoins de ServiceG W1Détecter les dimensions de la pièce
ImpliciteBesoins de ServiceC
 Q 1Reconnaître la forme de la pièceImpliciteBesoins de ServiceO	 U11Commander de manière télé-opéréCahier des chargesBesoins de ServiceL a1Apprécier la longueur d'onde de la pièceImpliciteBesoins de ServiceE U 1Reconnaître la couleur de la pièceImpliciteBesoins de ServiceM e	1Rester en équilibre l'ordre du déplacementImpliciteBesoins de ServiceN U	11Commander de manière télé-opéréCahier des chargesBesoins de Servicel �	11Transférer la pièce d'une zone à l'autre dans un temps limitéCahier des chargesBesoins de ServiceX i	11Évacuer la pièce dans la zone correspondanteCahier des chargesBesoins de ServiceM e	1Acheminer la pièces dans la zone de travailImpliciteBesoins de Service; A 1Gérer le flux des piècesImpliciteBesoins de Service   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          )Wsqlitebrowser_rename_column_new_table
exigences                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 �    ����x' � � H                                        O U11Commander de manière télé-opéré
Cahier des chargesBesoins de ServiceG W1Détecter les dimensions de la pièce
ImpliciteBesoins de ServiceC
 Q 1Reconnaître la forme de la pièceImpliciteBesoins de ServiceO	 U11Commander de manière télé-opéréCahier des chargesBesoins de ServiceL a1Apprécier la longueur d'onde de la pièceImpliciteBesoins de ServiceE U 1Reconnaître la couleur de la pièceImpliciteBesoins de ServiceM e	1Rester en équilibre l'ordre du déplacementImpliciteBesoins de ServiceN U	11Commander de manière télé-opéréCahier des chargesBesoins de Servicel �	11Transférer la pièce d'une zone à l'autre dans un temps limitéCahier des chargesBesoins de ServiceX i	11Évacuer la pièce dans la zone correspondanteCahier des chargesBesoins de ServiceM e	1Acheminer la pièces dans la zone de travailImpliciteBesoins de Service; A 1Gérer le flux des piècesImpliciteBes   !                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     � m��9 � �              ��tablebesoinsbesoinsCREATE TABLE besoins(
            id_besoin INTEGER                   ��tablebesoinsbesoinsCREATE TABLE besoins(
            id_besoin INTEGER PRIMARY KEY,
            intitule TEXT,
            primaire INTEGER)��tablesystemesystemeCREATE TABLE systeme(
            id_systeme INTEGER PRIMARY KEY,
            exigences TEXT,
            caracteristique TEXT)P++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)   *�tableexigencesexigencesCREATE T�##�otabletestresultstestresultsCREATE TABLE testresults(
            idex INTEGER PRIMARY KEY,
            critere TEXT,
            niveau INT)��tablesystemesystemeCREATE TABLE systeme(
            id_systeme INTEGER PRIMARY KEY,
            exigences TEXT,
            caracteristique TEXT)��{tablepiecespiecesCREATE TABLE pieces(
            id_piece INTEGER PRIMARY KEY,
            nom_piece TEXT,
            couleur INTEGER)5 � ��                                �V	WW�tablesqlitebrowser_rename_column_new_tablesqlitebrowser_rename_column_new_table
CREATE TABLE `sqlitebrowser_rename_column_new_table` (
	`idex`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`type`	TEXT,
	`besoin`	INT,
	`intitule`	TEXT,
	`critere`	TEXT,
	`espece`	TEXT,
	`niveau`	INT,
	`resultat`	INT,
	`conclusion`	INT,
	`exigence_mere`	INTEGER
)�-�1tablebesoinsbesoinsCREATE TABLE "besoins" (
	`id_besoin`	INTEGER,
	`intitule`	TEXT,
	`primaire`	INTEGER,
	`origine`	TEXT,
	`nature`	TEXT,
	PRIMARY KEY(`id_besoin`)
)   �##�otabletestresultstestresultsCREATE TABLE testresults(
            idex INTEGER PRIMARY KEY,
            critere TEXT,
            niveau INT)  4�tablebesoinsbesoinsCREATE TABLE beso�	�Stableexigencesexigences
CREATE TABLE "exigences" (
	`idex`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`type`	TEXT,
	`besoin`	INT,
	`intitule`	TEXT,
	`critere`	TEXT,
	`espece`	TEXT,
	`niveau`	INT,
	`resultat`	INT,
	`conclusion`	INT,
	`exigence_mere`	INTEGER
)� _	�t&��dO;(_�                                                                                                                                                                                                                                                                                                                                 E  M9   Le système doitmanger des abresffExigence d'efficacité>   ?9  Assurer le fonctionnementkkExigence de sécurité   A M-   Le système doitmanger des abresffLe système doit 
      ffef 	      sebjj    	   sardoud 5  	?+  doit transporter la piecebras metallique3% D  [+  doit arrêter de faire son leche-bottesbras metallique3% @  	S+  doit arrêter de faire sa chochottebras metallique3% K  	i+  doit supporter un effort lie a l'environnementbras metallique3% H  	e+  	doit tenir compte des dimensions de la piecebras metallique3% ?  	S+  	doit supporter le poids de la piecebras metallique3%   
 ! �\�o��( � w !     T! m !5Avoir un bouton pour démarrer le tri de couleurOpérateurBesoin de contrainteN  Q 15Respecter les dimensions maximalesCahier des chargesBesoin de contrainte_ � 5Utiliser l'énergie électrique fournie (piles ou batterie)ImpliciteBesoin de contraintej � 9Etre transportable et stockable dans une boite de dimension raisonnableEquipeBesoin d'environnementd �	 9S'adapter aux conditions mécaniques : vibrations, gravité…ImpliciteBesoin d'environnements �' 9S'adapter aux conditions Environnementales : température, pression, lumièreImpliciteBesoin d'environnementp �! 9S'adapter à l'Environnement imposé : dimensions de la zone de travail…ImpliciteBesoin d'environnementy �7 5Assurer la transmission des instructions entre l'opérateur et la brique intelligenteImpliciteBesoin de sécuritéJ I 15Rester dans la zone de travailCahier des chargesBesoin de sécuritéV q !5Arrêter le mouvement en cas de perte d'équilibreOpérateurBesoin de sécurité    % �R��S��L � � %       ^  !7Apprentissage du fonctionnement de l'interface opérateurOpérateurBesoin d'intéractionj � #7Permettre à l'opérateur de télécharger un programme facilement MaintenanceBesoin d'intéractionY u !7Envoyer et recevoir des informations à l'opérateurOpérateurBesoin d'intéractionu �+ !7Permettre à l'opérateur de sélectionner facilement le mode de fonctionnementOpérateurBesoin d'intéraction4 - 7Saisir la pièceImpliciteBesoin d'intéractionX q #7Les batteries doivent être accessibles facilementMaintenanceBesoin d'intéractionV q !5Pouvoir être facilement maniable par l'opérateurOpérateurBeosin d'efficacitéG U 5Stocker l'intégralité du programmeImpliciteBeosin d'efficacité\  5Pouvoir être sur batterie pendant 6 heures sans rechargeImpliciteBeosin d'efficacitéT ] 15Réaliser un tri en moins de 30 secondesCahier des chargesBeosin d'efficacitéV w 1Les éléments doivent être alimentés par des pilesImpliciteBesoins de Service   ~ �M���~   T!     T! m !5Avoir un bouton pour démarrer le tri de couleurOpérateurBesoin de contrainteN  Q 15Respecter les dimensions maximalesCahier des chargesBesoin de contrainte_ � 5Utiliser l'énergie électrique fournie (piles ou batterie)ImpliciteBesoin de contraintej � 9Etre transportable et stockable dans une boite de dimension raisonnableEquipeG( S !5Respecter les délais de ProductionM. ETIENNEBesoin de contrainteN' c 5Respecter le règlement du concours ROBAFISImpliciteBesoin de contrainteh& � !5Utliser le logiciel LEGO EV3 pour programmer la brique intelligenteOpérateurBesoin de contrainteq% � 15Utiliser des briques LEGO fournies dans le kit Mindstorms uniquementCahier des chargesBesoin de contrainteW$ s !5Etre retiré de la zone de travail par l'opérateurOpérateurBesoin de contrainteY# w !5Etre déposé par l'opérateur sur la zone de travailOpérateurBesoin de contrainteV" q !5Avoir un bouton pour démarrer le tri dimensionnelOpérateurBesoin de contrainte