-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 22-11-2021 a las 14:10:07
-- Versión del servidor: 8.0.21
-- Versión de PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `abarrotes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

DROP TABLE IF EXISTS `carrito`;
CREATE TABLE IF NOT EXISTS `carrito` (
  `idUsuario` int DEFAULT NULL,
  `idSession` varchar(100) DEFAULT NULL,
  `idProducto` int DEFAULT NULL,
  `cantidadC` int DEFAULT NULL,
  `activo` tinyint(1) DEFAULT NULL,
  KEY `idUsuario` (`idUsuario`),
  KEY `idProducto` (`idProducto`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`idUsuario`, `idSession`, `idProducto`, `cantidadC`, `activo`) VALUES
(1, 'p2o5korqjos6c3qhfaeihvkngo', 1, 2, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 2, 1, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 4, 3, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 1, 15, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 2, 20, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 3, 10, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 5, 10, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 6, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 15, 2, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 17, 10, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 16, 10, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 15, 4, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 18, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 19, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 24, 11, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 22, 10, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 1, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 2, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 3, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 4, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 4, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 5, 4, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 6, 3, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 17, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 16, 4, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 15, 2, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 18, 4, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 19, 4, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 20, 4, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 21, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 22, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 23, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 24, 2, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 25, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 26, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 27, 5, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 27, 41, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 28, 1500, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 29, 2500, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 29, 2500, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 30, 2, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 31, 10, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 32, 20, 0),
(1, 'p2o5korqjos6c3qhfaeihvkngo', 34, 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

DROP TABLE IF EXISTS `categoria`;
CREATE TABLE IF NOT EXISTS `categoria` (
  `idCategoria` int NOT NULL AUTO_INCREMENT,
  `nombreCategoria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`idCategoria`, `nombreCategoria`) VALUES
(1, 'Alimentos y Despensa'),
(2, 'Lacteos '),
(3, 'Carnes Frias'),
(4, 'Bebidas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE IF NOT EXISTS `cliente` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `usuario` int DEFAULT NULL,
  `dp` int DEFAULT NULL,
  PRIMARY KEY (`idCliente`),
  KEY `usuario` (`usuario`),
  KEY `dp` (`dp`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`idCliente`, `usuario`, `dp`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallecompra`
--

DROP TABLE IF EXISTS `detallecompra`;
CREATE TABLE IF NOT EXISTS `detallecompra` (
  `idCompra` int NOT NULL AUTO_INCREMENT,
  `idUser` varchar(50) DEFAULT NULL,
  `idSession` varchar(100) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `idDireccion` int DEFAULT NULL,
  `metodoPago` int DEFAULT NULL,
  PRIMARY KEY (`idCompra`),
  KEY `idUser` (`idUser`),
  KEY `idDireccion` (`idDireccion`),
  KEY `metodoPago` (`metodoPago`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `detallecompra`
--

INSERT INTO `detallecompra` (`idCompra`, `idUser`, `idSession`, `total`, `idDireccion`, `metodoPago`) VALUES
(1, '1', 'p2o5korqjos6c3qhfaeihvkngo', '99.06', 1, 2),
(2, '1', 'p2o5korqjos6c3qhfaeihvkngo', '1466.01', 1, 2),
(3, '1', 'p2o5korqjos6c3qhfaeihvkngo', '1505.99', 1, 3),
(4, '1', 'p2o5korqjos6c3qhfaeihvkngo', '2138.45', 1, 1),
(5, '1', 'p2o5korqjos6c3qhfaeihvkngo', '2457.60', 1, 2),
(6, '1', 'p2o5korqjos6c3qhfaeihvkngo', '6034.23', 1, 1),
(7, '1', 'p2o5korqjos6c3qhfaeihvkngo', '6049.18', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `direccion`
--

DROP TABLE IF EXISTS `direccion`;
CREATE TABLE IF NOT EXISTS `direccion` (
  `idDirec` int NOT NULL AUTO_INCREMENT,
  `calle` varchar(50) DEFAULT NULL,
  `inte` varchar(2) DEFAULT NULL,
  `exte` varchar(2) DEFAULT NULL,
  `col` varchar(50) DEFAULT NULL,
  `mun` varchar(50) DEFAULT NULL,
  `est` varchar(50) DEFAULT NULL,
  `cp` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`idDirec`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `direccion`
--

INSERT INTO `direccion` (`idDirec`, `calle`, `inte`, `exte`, `col`, `mun`, `est`, `cp`) VALUES
(1, 'Lago Neila', '05', '49', 'Paseos del Lago 2', 'Zumpango de Ocampo', 'Mexico', '55607');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

DROP TABLE IF EXISTS `empleado`;
CREATE TABLE IF NOT EXISTS `empleado` (
  `idEmpleado` int NOT NULL AUTO_INCREMENT,
  `usuario` int DEFAULT NULL,
  `dp` int DEFAULT NULL,
  `curp` varchar(18) DEFAULT NULL,
  `rfc` varchar(13) DEFAULT NULL,
  `cargo` varchar(20) DEFAULT NULL,
  `sueldo` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`idEmpleado`),
  KEY `usuario` (`usuario`),
  KEY `dp` (`dp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodopago`
--

DROP TABLE IF EXISTS `metodopago`;
CREATE TABLE IF NOT EXISTS `metodopago` (
  `idPago` int NOT NULL AUTO_INCREMENT,
  `namep` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idPago`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `metodopago`
--

INSERT INTO `metodopago` (`idPago`, `namep`) VALUES
(1, 'Credito'),
(2, 'Debito'),
(3, 'Efectivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personaldates`
--

DROP TABLE IF EXISTS `personaldates`;
CREATE TABLE IF NOT EXISTS `personaldates` (
  `idDp` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `app` varchar(50) DEFAULT NULL,
  `apm` varchar(50) DEFAULT NULL,
  `telF` varchar(12) DEFAULT NULL,
  `telM` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idDp`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `personaldates`
--

INSERT INTO `personaldates` (`idDp`, `nombre`, `app`, `apm`, `telF`, `telM`) VALUES
(1, 'Kevin Omar', 'Lazaro ', 'Ortega', '2483412026', '5585099538');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

DROP TABLE IF EXISTS `productos`;
CREATE TABLE IF NOT EXISTS `productos` (
  `idProducto` int NOT NULL AUTO_INCREMENT,
  `nomPro` varchar(50) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  `tipoCantidad` int DEFAULT NULL,
  `cantidad` decimal(10,2) DEFAULT NULL,
  `cantidadT` decimal(10,2) DEFAULT NULL,
  `direccion` varchar(150) DEFAULT NULL,
  `subCategoria` int DEFAULT NULL,
  PRIMARY KEY (`idProducto`),
  KEY `subCategoria` (`subCategoria`),
  KEY `tipoCantidad` (`tipoCantidad`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`idProducto`, `nomPro`, `precio`, `costo`, `tipoCantidad`, `cantidad`, `cantidadT`, `direccion`, `subCategoria`) VALUES
(1, 'Sabritas Adobadas', '11.10', '14.43', 2, '78.00', '100.00', 'img/adobadas.jfif', 2),
(2, 'Alpura 1L Chocolate', '19.50', '25.35', 2, '124.00', '150.00', 'img/alpura 1l chocolate.jfif', 7),
(3, 'Alpura 1L Clasica', '19.00', '24.70', 2, '55.00', '70.00', 'img/alpura 2l clasica.jfif', 7),
(4, 'Crema Alpura 1/4', '11.50', '14.95', 2, '7.00', '20.00', 'img/alpura cuarto.jfif', 5),
(5, 'Crema Alpura 1/2', '23.00', '29.90', 2, '1.00', '15.00', 'img/alpura medio.jfif', 5),
(6, 'Chipotles La Costeña', '15.00', '19.50', 2, '1.00', '9.00', 'img/chipotles.jfif', 1),
(17, 'Coca-Cola 600 ml', '12.00', '15.60', 2, '15.00', '10.00', 'img/coca 600 deshechable.jfif', 8),
(16, 'Coca-Cola 2.5L retornable', '20.00', '26.00', 2, '1.00', '15.00', 'img/coca 2.5 lt retornable.jfif', 8),
(15, 'Coca-Cola 1.3L', '15.38', '19.99', 2, '2.00', '10.00', 'img/coca 1.3.jfif', 8),
(18, 'Coca-Cola lata', '12.00', '15.60', 2, '1.00', '10.00', 'img/coca lata.jfif', 8),
(19, 'Costeña Chicharos', '9.00', '11.70', 2, '1.00', '10.00', 'img/costeña chicharos.jfif', 1),
(20, 'Frijoles Bayos Enteros', '13.00', '16.90', 2, '6.00', '10.00', 'img/costeña frijole bayos enteros.jfif', 1),
(21, 'Frijoles Bayos Refritos', '13.00', '16.90', 2, '7.00', '12.00', 'img/costeña frijole bayos refritos.jfif', 1),
(22, 'Frijoles Negros Enteros', '13.00', '16.90', 2, '15.00', '10.00', 'img/costeña frijole negros enteros.jfif', 1),
(23, 'Frijoles Negros Refritos', '13.00', '16.90', 2, '10.00', '15.00', 'img/costeña frijole negros refritos.jfif', 1),
(24, 'Doritos Queso', '10.50', '13.65', 2, '2.00', '15.00', 'img/doritos queso.jfif', 2),
(25, 'Flamin Hot', '11.50', '14.95', 2, '5.00', '10.00', 'img/flamin hot no crujientes.jfif', 2),
(26, 'Flamin Hot Receta Crujiente', '11.50', '14.95', 2, '10.00', '15.00', 'img/flamin hot.jfif', 2),
(27, 'Sabritas Habanero', '11.50', '14.95', 2, '4.00', '50.00', 'img/Habanero.jfif', 2),
(28, 'Jamon Pavo', '458.00', '595.40', 1, '3500.00', '5000.00', 'img/jamon pavo.jfif', 6),
(29, 'Jamon Pierna', '482.00', '626.60', 1, '-211.00', '4789.00', 'img/jamon pierna.jfif', 6),
(30, 'Jarrito Limon 600ml', '7.00', '9.10', 2, '13.00', '15.00', 'img/jarrito Limon.jfif', 8),
(31, 'Lala 1 Galon', '29.00', '37.70', 2, '5.00', '15.00', 'img/leche lala galon.jfif', 7),
(32, 'Nescafe Chico', '7.00', '9.10', 2, '0.00', '20.00', 'img/nescafe clasico chico.jfif', 3),
(33, 'Jarrito tutifruti 600ml', '11.50', '14.95', 2, '15.00', '15.00', 'img/jarrito Mandarina.jfif', 8),
(34, 'Jarrito Mandarina 600ml', '11.50', '14.95', 2, '10.50', '11.50', 'img/jarrito Naranja.jfif', 8),
(35, 'Jarrito Toronja 600ml', '11.50', '14.95', 2, '10.00', '10.00', 'img/jarrito Toronja.jfif', 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subcategoria`
--

DROP TABLE IF EXISTS `subcategoria`;
CREATE TABLE IF NOT EXISTS `subcategoria` (
  `idSCategoria` int NOT NULL AUTO_INCREMENT,
  `nomCategoria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idSCategoria`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `subcategoria`
--

INSERT INTO `subcategoria` (`idSCategoria`, `nomCategoria`) VALUES
(1, 'Enlatados'),
(2, 'Frituras'),
(3, 'Cafe y te'),
(4, 'Quesos'),
(5, 'Cremas'),
(6, 'Embutidos'),
(7, 'Leches'),
(8, 'Refrescos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipocantidad`
--

DROP TABLE IF EXISTS `tipocantidad`;
CREATE TABLE IF NOT EXISTS `tipocantidad` (
  `idCant` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idCant`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `tipocantidad`
--

INSERT INTO `tipocantidad` (`idCant`, `nombre`) VALUES
(1, 'Gramaje'),
(2, 'Pieza');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `unioncsc`
--

DROP TABLE IF EXISTS `unioncsc`;
CREATE TABLE IF NOT EXISTS `unioncsc` (
  `categoria` int DEFAULT NULL,
  `SubCategoria` int DEFAULT NULL,
  KEY `categoria` (`categoria`),
  KEY `SubCategoria` (`SubCategoria`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `unioncsc`
--

INSERT INTO `unioncsc` (`categoria`, `SubCategoria`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(3, 6),
(2, 7),
(4, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `unionpdd`
--

DROP TABLE IF EXISTS `unionpdd`;
CREATE TABLE IF NOT EXISTS `unionpdd` (
  `idDp` int DEFAULT NULL,
  `idDirec` int DEFAULT NULL,
  KEY `idDirec` (`idDirec`),
  KEY `idDp` (`idDp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `unionpdd`
--

INSERT INTO `unionpdd` (`idDp`, `idDirec`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contra` varchar(50) DEFAULT NULL,
  `tipo` int DEFAULT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUser`, `nom`, `email`, `contra`, `tipo`) VALUES
(1, 'Kenay', 'omarlazor@hotmail.com', 'c6d89b5ac23ce943b5a178fccfbf5e7b', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
