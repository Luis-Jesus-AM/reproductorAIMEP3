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

-- Volcando estructura para tabla reproducto_p3.artista
CREATE TABLE IF NOT EXISTS `artista` (
  `id_artista` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nacionalidad` VARCHAR(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_artista`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando estructura para tabla reproducto_p3.album
CREATE TABLE IF NOT EXISTS `album` (
  `id_album` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `año_lanzamiento` VARCHAR(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_artista` INT NOT NULL,
  PRIMARY KEY (`id_album`),
  FOREIGN KEY (`id_artista`) REFERENCES `artista`(`id_artista`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando estructura para tabla reproducto_p3.genero
CREATE TABLE IF NOT EXISTS `genero` (
  `id_genero` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando estructura para tabla reproducto_p3.cancion
CREATE TABLE IF NOT EXISTS `cancion` (
  `id_cancion` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `duracion_segundos` INT DEFAULT NULL,
  `ruta_archivo` VARCHAR(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_album` INT DEFAULT NULL,
  `id_genero` INT NOT NULL,
  PRIMARY KEY (`id_cancion`),
  FOREIGN KEY (`id_album`) REFERENCES `album`(`id_album`),
  FOREIGN KEY (`id_genero`) REFERENCES `genero`(`id_genero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando estructura para tabla reproducto_p3.playlist
CREATE TABLE IF NOT EXISTS `playlist` (
  `id_playlist` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_playlist`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando estructura para tabla reproducto_p3.playlist_cancion
CREATE TABLE IF NOT EXISTS `playlist_cancion` (
  `id_playlist` INT NOT NULL,
  `id_cancion` INT NOT NULL,
  `orden` INT NOT NULL,
  FOREIGN KEY (`id_playlist`) REFERENCES `playlist`(`id_playlist`),
  FOREIGN KEY (`id_cancion`) REFERENCES `cancion`(`id_cancion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando estructura para tabla reproducto_p3.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` INT AUTO_INCREMENT PRIMARY KEY,
  `nombre` VARCHAR(50) NOT NULL,
  `apellido` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `fecha_registro` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `ultimo_acceso` TIMESTAMP NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando estructura para tabla reproducto_p3.reset_tokens
CREATE TABLE IF NOT EXISTS `reset_tokens` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `id_usuario` INT NOT NULL,
  `token` VARCHAR(255) NOT NULL,
  `expira` DATETIME NOT NULL,
  FOREIGN KEY (`id_usuario`) REFERENCES `usuarios`(`id_usuario`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Limpieza de datos inicial
DELETE FROM `album`;
DELETE FROM `artista`;
DELETE FROM `cancion`;
DELETE FROM `genero`;
DELETE FROM `playlist`;
DELETE FROM `playlist_cancion`;
DELETE FROM `usuarios`;
DELETE FROM `reset_tokens`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
