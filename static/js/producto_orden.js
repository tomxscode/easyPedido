const
  busquedaInput = document.getElementById('buscarProductos'),
  coindicencias = document.getElementById('coindicencias')
  ;

let coincidencias_productos;

fetch(`${SITIO}api/productos`, {
  method: 'GET'
})
  .then(response => response.json())
  .then(data => {
    coincidencias_productos = data;
  })
  .catch(error => {
    console.error(error);
  });

busquedaInput.addEventListener('input', () => {
  coindicencias.innerHTML = '';
  if (busquedaInput.value.trim() == "") {
    return;
  }
  coincidencias_productos.forEach(producto => {
    if (producto.nombre.toLowerCase().includes(busquedaInput.value.toLowerCase())) {
      coindicencias.innerHTML += `
      <li class="list-group-item d-flex justify-content-between align-items-center mt-2">
        ${producto.nombre}
        <span class="badge badge-primary badge-pill">$${producto.precio}</span>
        <button class="btn btn-primary" onclick="agregarProducto(${producto.id})">Agregar</button>
      </li>
      `;
    }
  });
});

const agregarProducto = (id) => {
  Swal.fire({
    title: 'Agregar producto al pedido',
    // Input "cantidad"
    html: `
      <input id="cantidad" type="number" class="form-control" placeholder="Cantidad" min="1" max="100" value="1" required>
      <input id="detalle" type="text" class="form-control" placeholder="Detalle" required>
    `,
    showCancelButton: true,
    confirmButtonText: 'Agregar',
    cancelButtonText: 'Cancelar',
    focusConfirm: false,
    preConfirm: () => {
      const cantidad = Swal.getPopup().querySelector('#cantidad').value;
      const detalle = Swal.getPopup().querySelector('#detalle').value;
      if (!cantidad) {
        Swal.showValidationMessage(`El campo cantidad es obligatorio`);
      }
      return { cantidad: cantidad, detalle: detalle };
    }
  })
    .then((result) => {
      if (result.isConfirmed) {
        const cantidad = result.value.cantidad;
        const detalle = result.value.detalle;
        fetch(`${SITIO}api/agregar_producto_pedido/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            producto: id,
            cantidad: cantidad,
            detalle: detalle,
            pedido: PEDIDO_ID
          })
        })
          .then(response => response.json())
          .then(data => {
            if (data.success) {
              Swal.fire({
                icon: 'success',
                title: 'Producto agregado al pedido',
                showConfirmButton: false,
                timer: 1500
              })
                .then(() => {
                  location.reload();
                });
            } else {
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: data.message
              })
            }
          })
          .catch(error => {
            console.error(error);
          });

      }
    })
}