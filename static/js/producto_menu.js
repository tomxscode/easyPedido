function eliminarProducto(id) {
  // Enviar un SweetAlert2 para confirmar la eliminación
  Swal.fire({
    title: '¿Estás seguro?',
    text: "No podrás revertir esto!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, eliminar!',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      // Pantalla de carga en SweetAlert
      fetch(`${SITIO}admin/producto/eliminar/${id}`, {
        method: 'DELETE'
      })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            Swal.fire({
              title: 'Eliminado!',
              text: 'El producto fue eliminado con éxito. Espera 2 segundos para continuar...',
              icon: 'success',
              timer: 2000,
              showConfirmButton: false
            }).then(() => {
              location.reload();
            });
          } else {
            Swal.fire(
              'Error!',
              data.message,
              'error'
            );
          }
        })
    }
  });
}