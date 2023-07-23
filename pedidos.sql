CREATE TABLE `luna_baby`.`pedidos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `numero_pedido` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `cliente_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
);