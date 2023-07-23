CREATE TABLE `luna_baby`.`pagos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pedido_id` INT NOT NULL,
  `cliente_id` INT NOT NULL,
  `tarjeta_credito` VARCHAR(50) NOT NULL,
  `monto` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`id`)
);