CREATE TABLE `luna_baby`.`inventario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `producto_id` INT NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`)
);