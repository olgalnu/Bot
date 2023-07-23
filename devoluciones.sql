CREATE TABLE `luna_baby`.`devoluciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pedido_id` INT NOT NULL,
  `cliente_id` INT NOT NULL,
  `producto_id` INT NOT NULL,
  `razon` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`id`)
);