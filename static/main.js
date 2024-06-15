function getMaze(params) {
  fetch('/maze?' + new URLSearchParams(params))
    .then(response => response.text())
    .then(data => {
      Alpine.store('data').maze = data;
    })
}

document.addEventListener('alpine:init', () => {
  Alpine.store('data', {
    maze: ''
  })

  getMaze({algo:'binary_tree', scale:10, rows:4, columns:4, seed:10100,showDistances:true, startingCell:'0,0'})
})
