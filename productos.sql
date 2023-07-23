CREATE TABLE `luna_baby`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `descripcion` TEXT NOT NULL,
  `precio` DECIMAL(10,2) NOT NULL,
  `categoria` VARCHAR(50) NOT NULL,
  `tamano` VARCHAR(20),
  `edad_recomendada` VARCHAR(20),
  PRIMARY KEY (`id`)
);