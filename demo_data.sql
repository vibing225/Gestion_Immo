-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 05 juin 2026 à 19:19
-- Version du serveur : 9.1.0
-- Version de PHP : 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gestion_immo`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add client', 7, 'add_client'),
(26, 'Can change client', 7, 'change_client'),
(27, 'Can delete client', 7, 'delete_client'),
(28, 'Can view client', 7, 'view_client'),
(29, 'Can add logement', 8, 'add_logement'),
(30, 'Can change logement', 8, 'change_logement'),
(31, 'Can delete logement', 8, 'delete_logement'),
(32, 'Can view logement', 8, 'view_logement'),
(33, 'Can add reservation', 9, 'add_reservation'),
(34, 'Can change reservation', 9, 'change_reservation'),
(35, 'Can delete reservation', 9, 'delete_reservation'),
(36, 'Can view reservation', 9, 'view_reservation'),
(37, 'Can add image logement', 10, 'add_imagelogement'),
(38, 'Can change image logement', 10, 'change_imagelogement'),
(39, 'Can delete image logement', 10, 'delete_imagelogement'),
(40, 'Can view image logement', 10, 'view_imagelogement');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$zzdjmN7Lrhs1NAAYuDXQtA$UPhexZAZGdP97ZEbwlxNvmIgWy73PMMktsbMEMhqIQE=', '2026-06-05 17:28:25.682028', 1, 'Hamza', '', '', 'hamzatibab40@gmail.com', 1, 1, '2026-06-05 16:44:51.965478');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Déchargement des données de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2026-06-05 17:30:47.510574', '1', 'Appartement moderne à Conakry', 1, '[{\"added\": {}}]', 8, 1),
(2, '2026-06-05 17:32:01.598867', '2', 'Villa avec piscine à Kipé', 1, '[{\"added\": {}}]', 8, 1),
(3, '2026-06-05 17:35:10.399264', '3', 'Studio meublé à Labé', 1, '[{\"added\": {}}]', 8, 1),
(4, '2026-06-05 17:36:28.013617', '4', 'Appartement vue mer à Kaloum', 1, '[{\"added\": {}}]', 8, 1),
(5, '2026-06-05 17:37:34.538047', '5', 'Maison traditionnelle à Dixinn', 1, '[{\"added\": {}}]', 8, 1),
(6, '2026-06-05 17:38:41.887404', '6', 'Loft design à Lambanyi', 1, '[{\"added\": {}}]', 8, 1),
(7, '2026-06-05 17:39:45.109312', '7', 'Duplex spacieux à Sonfonia', 1, '[{\"added\": {}}]', 8, 1),
(8, '2026-06-05 17:40:56.268808', '8', 'Chambre d’hôte à Matoto', 1, '[{\"added\": {}}]', 8, 1),
(9, '2026-06-05 17:41:57.023057', '9', 'Résidence sécurisée à Nongo', 1, '[{\"added\": {}}]', 8, 1),
(10, '2026-06-05 17:42:54.576247', '10', 'Appartement cosy à Taouyah', 1, '[{\"added\": {}}]', 8, 1),
(11, '2026-06-05 18:47:14.437066', '1', 'Camara Moussa', 1, '[{\"added\": {}}]', 7, 1),
(12, '2026-06-05 18:47:45.341656', '2', 'Sow Aliou', 1, '[{\"added\": {}}]', 7, 1),
(13, '2026-06-05 18:52:51.922712', '3', 'Sylla Mabinty', 1, '[{\"added\": {}}]', 7, 1),
(14, '2026-06-05 18:53:29.723879', '4', 'Diallo Kadiatou', 1, '[{\"added\": {}}]', 7, 1),
(15, '2026-06-05 18:54:10.351345', '5', 'Camara Saran', 1, '[{\"added\": {}}]', 7, 1),
(16, '2026-06-05 18:55:11.805779', '6', 'Sow Alpha Moussa', 1, '[{\"added\": {}}]', 7, 1),
(17, '2026-06-05 18:56:04.552339', '7', 'Louis Yapi', 1, '[{\"added\": {}}]', 7, 1),
(18, '2026-06-05 18:56:38.969018', '8', 'Kanté Mariame', 1, '[{\"added\": {}}]', 7, 1),
(19, '2026-06-05 18:57:49.631942', '9', 'Guilavogui Mathieu', 1, '[{\"added\": {}}]', 7, 1),
(20, '2026-06-05 18:58:19.584017', '10', 'Kolié Solange', 1, '[{\"added\": {}}]', 7, 1),
(21, '2026-06-05 18:59:20.182462', '1', 'Camara Moussa - Appartement moderne à Conakry', 1, '[{\"added\": {}}]', 9, 1),
(22, '2026-06-05 19:00:31.439070', '2', 'Sow Aliou - Villa avec piscine à Kipé', 1, '[{\"added\": {}}]', 9, 1),
(23, '2026-06-05 19:01:24.448905', '3', 'Sylla Mabinty - Studio meublé à Labé', 1, '[{\"added\": {}}]', 9, 1),
(24, '2026-06-05 19:02:24.597121', '4', 'Diallo Kadiatou - Appartement vue mer à Kaloum', 1, '[{\"added\": {}}]', 9, 1),
(25, '2026-06-05 19:03:06.968020', '5', 'Camara Saran - Maison traditionnelle à Dixinn', 1, '[{\"added\": {}}]', 9, 1),
(26, '2026-06-05 19:04:36.205931', '6', 'Sow Alpha Moussa - Loft design à Lambanyi', 1, '[{\"added\": {}}]', 9, 1),
(27, '2026-06-05 19:06:07.101001', '7', 'Louis Yapi - Duplex spacieux à Sonfonia', 1, '[{\"added\": {}}]', 9, 1),
(28, '2026-06-05 19:07:05.913668', '8', 'Guilavogui Mathieu - Chambre d’hôte à Matoto', 1, '[{\"added\": {}}]', 9, 1),
(29, '2026-06-05 19:08:00.881376', '9', 'Kanté Mariame - Résidence sécurisée à Nongo', 1, '[{\"added\": {}}]', 9, 1),
(30, '2026-06-05 19:08:42.835682', '10', 'Kolié Solange - Appartement cosy à Taouyah', 1, '[{\"added\": {}}]', 9, 1),
(31, '2026-06-05 19:10:28.574606', '1', 'Image 1 de Appartement moderne à Conakry', 1, '[{\"added\": {}}]', 10, 1),
(32, '2026-06-05 19:10:54.708120', '2', 'Image 2 de Villa avec piscine à Kipé', 1, '[{\"added\": {}}]', 10, 1),
(33, '2026-06-05 19:11:12.717366', '3', 'Image 3 de Studio meublé à Labé', 1, '[{\"added\": {}}]', 10, 1),
(34, '2026-06-05 19:11:47.529190', '4', 'Image 4 de Appartement vue mer à Kaloum', 1, '[{\"added\": {}}]', 10, 1),
(35, '2026-06-05 19:12:12.222550', '5', 'Image 5 de Maison traditionnelle à Dixinn', 1, '[{\"added\": {}}]', 10, 1),
(36, '2026-06-05 19:12:29.261794', '6', 'Image 6 de Loft design à Lambanyi', 1, '[{\"added\": {}}]', 10, 1),
(37, '2026-06-05 19:12:46.855567', '7', 'Image 7 de Duplex spacieux à Sonfonia', 1, '[{\"added\": {}}]', 10, 1),
(38, '2026-06-05 19:13:01.789879', '8', 'Image 8 de Chambre d’hôte à Matoto', 1, '[{\"added\": {}}]', 10, 1),
(39, '2026-06-05 19:13:19.423289', '9', 'Image 9 de Résidence sécurisée à Nongo', 1, '[{\"added\": {}}]', 10, 1),
(40, '2026-06-05 19:13:39.561122', '10', 'Image 10 de Appartement cosy à Taouyah', 1, '[{\"added\": {}}]', 10, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'principale', 'client'),
(8, 'principale', 'logement'),
(9, 'principale', 'reservation'),
(10, 'principale', 'imagelogement');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-06-05 16:27:56.855172'),
(2, 'auth', '0001_initial', '2026-06-05 16:27:57.894583'),
(3, 'admin', '0001_initial', '2026-06-05 16:27:58.113286'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-06-05 16:27:58.128904'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-06-05 16:27:58.128904'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-06-05 16:27:58.232497'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-06-05 16:27:58.262162'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-06-05 16:27:58.309031'),
(9, 'auth', '0004_alter_user_username_opts', '2026-06-05 16:27:58.309031'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-06-05 16:27:58.355867'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-06-05 16:27:58.355867'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-06-05 16:27:58.371513'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-06-05 16:27:58.402719'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-06-05 16:27:58.449582'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-06-05 16:27:58.496447'),
(16, 'auth', '0011_update_proxy_permissions', '2026-06-05 16:27:58.512067'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-06-05 16:27:58.571215'),
(18, 'principale', '0001_initial', '2026-06-05 17:10:28.642351'),
(19, 'principale', '0002_alter_client_id_alter_imagelogement_id_and_more', '2026-06-05 17:10:29.223633'),
(20, 'principale', '0003_imagelogement_description', '2026-06-05 17:10:29.306821'),
(21, 'sessions', '0001_initial', '2026-06-05 17:10:29.366167');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('tick9d51h7obrwe6m1qh2zw1v2zj0v3m', '.eJxVjDsOwjAQBe_iGln-YK-Xkp4zROvsggPIluKkQtwdIqWA9s3Me6mB1qUMa5d5mFidlFWH3y3T-JC6Ab5TvTU9trrMU9abonfa9aWxPM-7-3dQqJdv7Y0IWA5XsRIcYDI-ADEEz0lySt56iIAi8ZiJxcTEzmJAhyZixKzeH9DzNww:1wVYLJ:kzIYWPHgWdYdr5G_hGyNYotAgAM0yyqPqrjvtBoMpcM', '2026-06-19 17:28:25.690551');

-- --------------------------------------------------------

--
-- Structure de la table `principale_client`
--

DROP TABLE IF EXISTS `principale_client`;
CREATE TABLE IF NOT EXISTS `principale_client` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `principale_client`
--

INSERT INTO `principale_client` (`id`, `nom`, `email`, `telephone`) VALUES
(1, 'Camara Moussa', 'hbdgat67@gmail.com', '621993467'),
(2, 'Sow Aliou', 'sowaliou56@gmail.com', '662908754'),
(3, 'Sylla Mabinty', 'symab65@gmail.com', '656862987'),
(4, 'Diallo Kadiatou', 'kadialo776@gmail.com', '654876234'),
(5, 'Camara Saran', 'saracam76@gmail.com', '627345678'),
(6, 'Sow Alpha Moussa', 'sowmoussa09@gmail.com', '610987345'),
(7, 'Louis Yapi', 'yapift08@gmail.com', '611098765'),
(8, 'Kanté Mariame', 'kant4re@gmail.com', '621627384'),
(9, 'Guilavogui Mathieu', 'mathieugui25@gmail.com', '629876325'),
(10, 'Kolié Solange', 'solangek87@gmail.com', '660784263');

-- --------------------------------------------------------

--
-- Structure de la table `principale_imagelogement`
--

DROP TABLE IF EXISTS `principale_imagelogement`;
CREATE TABLE IF NOT EXISTS `principale_imagelogement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `logement_id` bigint NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `principale_imagelogement_logement_id_b5169832` (`logement_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `principale_imagelogement`
--

INSERT INTO `principale_imagelogement` (`id`, `image`, `logement_id`, `description`) VALUES
(1, 'logements/pexels-memory-lane-2157293172-35829896.jpg', 1, ''),
(2, 'logements/pexels-artbovich-5998117.jpg', 2, ''),
(3, 'logements/pexels-artbovich-6447384.jpg', 3, ''),
(4, 'logements/pexels-athena-2962140.jpg', 4, ''),
(5, 'logements/pexels-aysegul-aytoren-46790226-36200375.jpg', 5, ''),
(6, 'logements/istockphoto-1394249756-1024x1024.jpg', 6, ''),
(7, 'logements/istockphoto-1752692636-1024x1024.jpg', 7, ''),
(8, 'logements/istockphoto-1445520806-1024x1024.jpg', 8, ''),
(9, 'logements/istockphoto-1177402756-1024x1024.jpg', 9, ''),
(10, 'logements/istockphoto-2180053464-1024x1024.jpg', 10, '');

-- --------------------------------------------------------

--
-- Structure de la table `principale_logement`
--

DROP TABLE IF EXISTS `principale_logement`;
CREATE TABLE IF NOT EXISTS `principale_logement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titre` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `adresse` varchar(255) NOT NULL,
  `ville` varchar(100) NOT NULL,
  `prix_par_nuit` decimal(10,2) NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `principale_logement`
--

INSERT INTO `principale_logement` (`id`, `titre`, `description`, `adresse`, `ville`, `prix_par_nuit`, `disponible`) VALUES
(1, 'Appartement moderne à Conakry', '2 chambres, salon lumineux, cuisine équipée, proche du centre-ville', 'Miniere', 'Conakry', 350000.00, 1),
(2, 'Villa avec piscine à Kipé', '4 chambres, grand jardin, piscine privée, quartier résidentiel calme', 'Kipé', 'Conakry', 1199999.96, 1),
(3, 'Studio meublé à Labé', 'Studio cosy, meublé, idéal pour étudiants, accès facile aux transports', 'Kouroula', 'Labé', 320000.00, 1),
(4, 'Appartement vue mer à Kaloum', '3 chambres, balcon avec vue sur l’océan, proche du port', 'Kaloum', 'Conakry', 800000.00, 1),
(5, 'Maison traditionnelle à Dixinn', '2 chambres, style guinéen, ambiance chaleureuse, quartier animé', 'Dixinn', 'Cokary', 300000.00, 1),
(6, 'Loft design à Lambanyi', 'Loft spacieux, décoration moderne, grandes baies vitrées', 'Lambanyi', 'Conakry', 500000.00, 1),
(7, 'Duplex spacieux à Sonfonia', '3 chambres, 2 salons, cuisine moderne, quartier résidentiel', 'Sonfonia', 'Conakry', 599999.98, 1),
(8, 'Chambre d’hôte à Matoto', 'Chambre simple, prix abordable, accueil chaleureux.', 'Matoto', 'Conakry', 149999.97, 1),
(9, 'Résidence sécurisée à Nongo', 'Appartement dans résidence gardée, proche du stade, 2 chambres.', 'Nongo', 'Ratoma', 400000.00, 0),
(10, 'Appartement cosy à Taouyah', '2 chambres, salon confortable, quartier animé avec commerces.', 'Taouyah', 'Conakry', 350000.00, 1);

-- --------------------------------------------------------

--
-- Structure de la table `principale_reservation`
--

DROP TABLE IF EXISTS `principale_reservation`;
CREATE TABLE IF NOT EXISTS `principale_reservation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_arrivee` date NOT NULL,
  `date_depart` date NOT NULL,
  `statut` varchar(50) NOT NULL,
  `montant_total` decimal(10,2) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  `logement_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `principale_reservation_client_id_814190df` (`client_id`),
  KEY `principale_reservation_logement_id_1e7d481d` (`logement_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `principale_reservation`
--

INSERT INTO `principale_reservation` (`id`, `date_arrivee`, `date_depart`, `statut`, `montant_total`, `client_id`, `logement_id`) VALUES
(1, '2026-06-05', '2026-06-09', 'CONFIRMEE', 1400000.00, 1, 1),
(2, '2026-06-20', '2026-07-05', 'CONFIRMEE', 17999999.40, 2, 2),
(3, '2026-06-15', '2026-06-30', 'CONFIRMEE', 4800000.00, 3, 3),
(4, '2026-06-25', '2026-08-05', 'EN_ATTENTE', 32800000.00, 4, 4),
(5, '2026-07-05', '2026-12-05', 'EN_ATTENTE', 45900000.00, 5, 5),
(6, '2026-06-17', '2026-08-17', 'REFUSEE', 30500000.00, 6, 6),
(7, '2026-06-12', '2026-06-20', 'EN_ATTENTE', 4799999.84, 7, 7),
(8, '2026-08-22', '2026-10-22', 'CONFIRMEE', 9149998.17, 9, 8),
(9, '2027-02-05', '2027-03-05', 'EN_ATTENTE', 11200000.00, 8, 9),
(10, '2026-06-07', '2026-06-09', 'CONFIRMEE', 700000.00, 10, 10);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
