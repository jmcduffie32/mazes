function getMaze(algo, scale, columns, rows) {
  fetch('/maze?' + new URLSearchParams({ algo, scale, columns, rows }))
    .then(response => response.text())
    .then(data => {
      Alpine.store('data').maze = data;
    })
}

document.addEventListener('alpine:init', () => {
  Alpine.store('data', {
    maze: ''
  })

  getMaze('binary_tree', 10, 4, 4)
})
