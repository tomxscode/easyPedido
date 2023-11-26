function cocinaVerPedido(id) {
  fetch(`${SITIO}api/cocina/pedidos/ver_pedido/${id}`, {
    method: 'GET'
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      if (data.success) {
        // Enviar un Swal con los datos del pedido
        /* 
          cuerpo de la respuesta:
          
  {estado: 'En espera', pedido: 1, productos: Array(4), success: true}
  estado
  : 
  "En espera"
  pedido
  : 
  1
  productos
  : 
  Array(4)
  0
  : 
  {cantidad: 1, detalle: '2', estado: 1, id: 1, producto: 3}
  1
  : 
  {cantidad: 1, detalle: 'Sin comentarios', estado: 1, id: 2, producto: 2}
  2
  : 
  {cantidad: 1, detalle: '', estado: 1, id: 3, producto: 3}
  3
  : 
  {cantidad: 3, detalle: '2 de azucar', estado: 1, id: 4, producto: 1}
  length
  : 
  4
  [[Prototype]]
  : 
  Array(0)
  success
  : 
  true
        */
        Swal.fire({
          title: `Pedido #${data.pedido}`,
          html: `
          <p>Estado: ${data.estado}</p>
          <p>Productos:</p>
          <ul class="list-group">
            ${data.productos.map(producto => `
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <p>
                ${producto.nombre}
                <br>
                <small>${producto.detalle}</small>
              </p>
              <span class="badge badge-primary badge-pill">${producto.cantidad}</span>
            </li>
            `).join('')}
          </ul>
        `,
          showCancelButton: true,
          confirmButtonText: 'Aceptar',
          cancelButtonText: 'Cancelar'
        });
      }
    })
    .catch(error => {
      console.error('Error:', error);
    })
}