CREATE TABLE `luna_baby`.`clientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  `apellido` VARCHAR(50) NOT NULL,
  `correo_electronico` VARCHAR(100) NOT NULL,
  `direccion_envio` VARCHAR(200) NOT NULL,
  `telefono` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
);