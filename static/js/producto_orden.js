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
      <li class="list-group-item d-flex justify-content-between align-items-center">
        ${producto.nombre}
        <span class="badge badge-primary badge-pill">$${producto.precio}</span>
        <button class="btn btn-primary" onclick="agregarProducto(${producto.id})">Agregar</button>
      </li>
      `;
    }
  });
});