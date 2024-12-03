const dropdown = document.getElementById('dropdown');
const button = document.getElementById('button');

button.addEventListener('click', () => {
  dropdown.classList.toggle('show');
  console.log('click');
});