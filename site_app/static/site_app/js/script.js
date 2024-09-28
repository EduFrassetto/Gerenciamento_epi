console.log('Script carregado');

function confirmDelete(resource){
    console.log("Deseja realmente excluir");
    return confirm(`Deseja realmente excluir o ${resource}?`);}