CREATE TABLE `luna_baby`.`comentarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pedido_id` INT NOT NULL,
  `nombre_cliente` VARCHAR(100) NOT NULL,
  `puntuacion` INT NOT NULL,
  `comentario` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`id`)
);