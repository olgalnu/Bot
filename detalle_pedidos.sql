CREATE TABLE `luna_baby`.`detalle_pedidos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pedido_id` INT NOT NULL,
  `producto_id` INT NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`id`),
  FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`)
);