# Projet

L'objectif de ce repo est de faire le tour des fonctionnalités Django via des projets pouvant être déployé après leur réalisation.
Vous pouvez démarrer dans l'ordre qui vous semble le plus judicieux ou correspondant le plus à vos attentes.

# Squelette

Le projet dj_postgres_skeleton est un squelette comprenant une configuration Docker pour le Django ainsi que la base de donnée.
Il vous permettra d'éviter les tâches répétitives de configuration et de vous concentrer uniquement sur le métier.

Pour créer votre projet à partir de ce squelette, voici la procèdure à suivre:

```
git clone git@github.com:felixbouazza/personnal_projects.git
cd personnal_projects
cp -r dj_postgres_skeleton <nom_du_nouveau_projet>
cd <nom_du_nouveau_projet>
mv dj_postgres_skeleton <nom_du_nouveau_projet>
```

Rechercher ensuite toutes les occurences de `dj_postgres`, `dj_postgres_skeleton`, `dj-postgres` et `dj-postgres-skeleton` et renommer les avec le nom de votre projet. Si votre nom de projet contient plusieurs mots, il faut absolument respecter les `_` et `-` d'origine

### Configuration de base

Python: 3.11
Django: 4.2
Postgres: 15.2
Gestionnaire de dépendance : Poetry

### Commandes utiles

Lancer le projet:

```bash
docker-compose up --build
```

Lancer un shell via django-extensions:

```bash
docker-compose exec dj-postgres-back ./manage.py shell_plus
```

Linter le projet

```bash
# il vous faudra en amont les droits d'exécution sur le fichier `chmod +x lintall.sh`
./lintall.sh
```

# Voici quelques idées de projet

Blog : Créez un blog avec Django où les utilisateurs peuvent s'inscrire, se connecter, créer, lire, mettre à jour et supprimer des articles de blog. Vous pouvez également ajouter des fonctionnalités telles que la recherche d'articles, les commentaires sur les articles, et la gestion des utilisateurs et des rôles.

Système de gestion de tâches : Développez une application de gestion de tâches où les utilisateurs peuvent créer, organiser et suivre leurs tâches. Vous pouvez ajouter des fonctionnalités telles que la création de tâches récurrentes, l'assignation de tâches à des utilisateurs spécifiques, et la possibilité de définir des rappels pour les tâches.

Plateforme de questions/réponses : Créez une plateforme de questions/réponses similaire à Stack Overflow où les utilisateurs peuvent poser des questions, répondre aux questions d'autres utilisateurs, voter pour les meilleures réponses, et marquer les questions et réponses comme résolues.

Gestionnaire d'événements : Développez une application de gestion d'événements où les utilisateurs peuvent créer, gérer et participer à des événements. Vous pouvez ajouter des fonctionnalités telles que la création d'événements publics ou privés, l'invitation d'autres utilisateurs à des événements, et la possibilité de partager des événements sur les réseaux sociaux.

Réseau social : Créez un mini-réseau social où les utilisateurs peuvent créer des profils, se connecter avec d'autres utilisateurs, publier des messages, commenter et aimer les messages d'autres utilisateurs, et gérer leur liste d'amis. Vous pouvez également ajouter des fonctionnalités supplémentaires comme la messagerie instantanée entre utilisateurs et la possibilité de partager du contenu multimédia.

Boutique en ligne : Développez une boutique en ligne où les utilisateurs peuvent parcourir et acheter des produits, gérer leur panier d'achat, passer des commandes et effectuer des paiements. Vous pouvez également ajouter des fonctionnalités telles que la recherche de produits, la gestion des stocks, la gestion des commandes et la génération de factures.

Plateforme de partage de fichiers : Créez une application de partage de fichiers où les utilisateurs peuvent télécharger, partager et gérer des fichiers. Vous pouvez ajouter des fonctionnalités telles que la gestion des autorisations d'accès aux fichiers, la recherche de fichiers, et la possibilité de commenter et de noter les fichiers.

Plateforme de blogging multi-utilisateurs : Développez une plateforme de blogging qui permet à plusieurs utilisateurs de créer et de gérer leurs propres blogs. Vous pouvez ajouter des fonctionnalités telles que la personnalisation des blogs, la gestion des auteurs et des éditeurs, et la possibilité de suivre les blogs d'autres utilisateurs.

Système de réservation : Créez une application de réservation pour un service spécifique, comme la réservation de chambres d'hôtel, de tables de restaurant ou de billets d'événements. Vous pouvez ajouter des fonctionnalités telles que la recherche de disponibilité, la sélection de dates et d'horaires, et la gestion des réservations pour les utilisateurs.

Forum de discussion : Développez une plateforme de forum de discussion où les utilisateurs peuvent créer des sujets de discussion, participer à des discussions, et échanger des messages avec d'autres utilisateurs. Vous pouvez ajouter des fonctionnalités telles que la création de catégories de discussion, la recherche de sujets, et la possibilité de suivre les discussions et les utilisateurs.

Plateforme d'apprentissage en ligne : Créez une plateforme d'apprentissage en ligne où les utilisateurs peuvent s'inscrire à des cours, accéder au contenu du cours, interagir avec les instructeurs et les autres étudiants, et passer des évaluations. Vous pouvez ajouter des fonctionnalités telles que la gestion des cours, le suivi de la progression de l'apprentissage, et la génération de certificats d'achèvement.

Journal de voyage : Développez une application de journal de voyage où les utilisateurs peuvent créer et partager leurs expériences de voyage, télécharger des photos, ajouter des itinéraires et marquer leurs destinations préférées. Vous pouvez ajouter des fonctionnalités telles que la cartographie des destinations, la recherche de journaux de voyage par lieu, et la possibilité de commenter et d'aimer les journaux de voyage d'autres utilisateurs.

Système de gestion d'équipe : Créez une application de gestion d'équipe pour un projet spécifique, où les utilisateurs peuvent collaborer, assigner des tâches, suivre les progrès, et partager des documents. Vous pouvez ajouter des fonctionnalités telles que la gestion des membres d'équipe, la communication interne, et la génération de rapports sur les progrès du projet.

Plateforme de vente aux enchères : Développez une plateforme de vente aux enchères où les utilisateurs peuvent créer et enchérir sur des articles, gérer leurs enchères, et gérer leurs articles en vente. Vous pouvez ajouter des fonctionnalités telles que la gestion des paiements, la gestion des enchères gagnantes, et la gestion des commentaires sur les articles.

Application de suivi de fitness : Créez une application de suivi de fitness où les utilisateurs peuvent enregistrer leurs activités physiques, suivre leur progression, fixer des objectifs, et partager leurs réalisations. Vous pouvez ajouter des fonctionnalités telles que le suivi des statistiques de santé, la planification d'entraînements, et la possibilité de se connecter avec d'autres utilisateurs pour la compétition et la motivation.