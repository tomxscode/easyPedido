function verProducto(id) {
  fetch(`${SITIO}api/productos/${id}`, {
    method: "GET"
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        console.log(data)
        let producto = data
        // Mostrar SweetAlert con la información del producto
        Swal.fire({
          title: producto.nombre,
          html: `
        <div class="container">

        <div class="row">
          <div class="col-md-4">
            <img src="${SITIO}static/images/${producto.imagen}" class="img-fluid">
          </div>
      
          <div class="col-md-8">
            <h3>${producto.nombre}</h3>
            
            <ul class="list-group">
              <li class="list-group-item">
                Precio: $${producto.precio}
              </li>
              <li class="list-group-item">
                Descripción: ${producto.descripcion}
              </li>
            </ul>
      
          </div>
        </div>
      
      </div>
        `,
          showCancelButton: false,
          confirmButtonText: 'Cerrar'
        });

      } else {
        // Mostrar un SweetAlert de error
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'El producto no existe o no tienes acceso a el',
          showConfirmButton: false,
          timer: 3000
        });
      }
    })
    .catch(error => console.log(error))
}