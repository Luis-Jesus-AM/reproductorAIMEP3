-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.4.7 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.13.0.7147
-- --------------------------------------------------------
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
-- Volcando estructura de base de datos para reproducto_p3
CREATE DATABASE IF NOT EXISTS `reproducto_p3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `reproducto_p3`;
-- Volcando estructura para tabla reproducto_p3.album
CREATE TABLE IF NOT EXISTS `album` (
  `id_album` int NOT NULL DEFAULT (0),
  `titulo` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `año_lanzamiento` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_artista` int NOT NULL DEFAULT (0),
  PRIMARY KEY (`id_album`) USING BTREE,
  KEY `FK_artista` (`id_artista`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
-- Volcando datos para la tabla reproducto_p3.album: 0 rows
DELETE FROM `album`;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
-- Volcando estructura para tabla reproducto_p3.artista
CREATE TABLE IF NOT EXISTS `artista` (
  `id_artista` int NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `nacionalidad` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id_artista`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
-- Volcando datos para la tabla reproducto_p3.artista: 0 rows
DELETE FROM `artista`;
/*!40000 ALTER TABLE `artista` DISABLE KEYS */;
/*!40000 ALTER TABLE `artista` ENABLE KEYS */;
-- Volcando estructura para tabla reproducto_p3.cancion
CREATE TABLE IF NOT EXISTS `cancion` (
  `id_cancion` int NOT NULL,
  `titulo` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `duracion_segundos` int DEFAULT NULL,
  `ruta_archivo` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_album` int DEFAULT NULL,
  `id_genero` int NOT NULL,
  PRIMARY KEY (`id_cancion`),
  KEY `FK_album` (`id_album`),
  KEY `FK_genero` (`id_genero`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
-- Volcando datos para la tabla reproducto_p3.cancion: 0 rows
DELETE FROM `cancion`;
/*!40000 ALTER TABLE `cancion` DISABLE KEYS */;
/*!40000 ALTER TABLE `cancion` ENABLE KEYS */;
-- Volcando estructura para tabla reproducto_p3.genero
CREATE TABLE IF NOT EXISTS `genero` (
  `id_genero` int NOT NULL,
  `nombre` int NOT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
-- Volcando datos para la tabla reproducto_p3.genero: 0 rows
DELETE FROM `genero`;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
/*!40000 ALTER TABLE `genero` ENABLE KEYS */;
-- Volcando estructura para tabla reproducto_p3.playlist
CREATE TABLE IF NOT EXISTS `playlist` (
  `id_playlist` int NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_creacion` timestamp NOT NULL,
  PRIMARY KEY (`id_playlist`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
-- Volcando datos para la tabla reproducto_p3.playlist: 0 rows
DELETE FROM `playlist`;
/*!40000 ALTER TABLE `playlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `playlist` ENABLE KEYS */;
-- Volcando estructura para tabla reproducto_p3.playlist_cancion
CREATE TABLE IF NOT EXISTS `playlist_cancion` (
  `id_playlist` int NOT NULL,
  `id_cancion` int NOT NULL,
  `orden` int NOT NULL,
  KEY `FK_playlist` (`id_playlist`),
  KEY `FK_cancion` (`id_cancion`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
-- Volcando datos para la tabla reproducto_p3.playlist_cancion: 0 rows
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` INT AUTO_INCREMENT PRIMARY KEY,
  `nombre` VARCHAR(50) NOT NULL,
  `apellido` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `fecha_registro` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `ultimo_acceso` TIMESTAMP NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;2
DELETE FROM `playlist_cancion`;
/*!40000 ALTER TABLE `playlist_cancion` DISABLE KEYS */;
/*!40000 ALTER TABLE `playlist_cancion` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;











