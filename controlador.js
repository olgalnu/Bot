const conexion = require("./conexion")
module.exports = {
    insertar(nombre, apellido, correo, direccion, telefono) {
        return new Promise((resolve, reject) => {
            conexion.query(
              `INSERT INTO clientes (nombre, apellido, correo_electronico, direccion_envio, telefono)
               VALUES (?, ?, ?, ?, ?)`,
              [nombre, apellido, correo, direccion, telefono],
              (err, resultados) => {
                if (err) reject(err);
                else resolve(resultados.insertId);
              }
            );
        });
    },
    obtener() {
        return new Promise((resolve, reject) => {
            conexion.query(
              `SELECT id, nombre, apellido, correo_electronico, direccion_envio, telefono
               FROM clientes`,
              (err, resultados) => {
                if (err) reject(err);
                else resolve(resultados);
              }
            );
        });
    },
    eliminar(id) {
        return new Promise((resolve, reject) => {
            conexion.query(
              `DELETE FROM clientes WHERE id = ?`,
              [id],
              (err) => {
                if (err) reject(err);
                else resolve();
              }
            );
        });
    },
};
      