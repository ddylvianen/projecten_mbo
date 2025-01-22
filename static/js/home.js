const dropdown = document.getElementById('dropdown');
const button = document.getElementById('button');
const messages = document.querySelectorAll('.messages li');


button.addEventListener('click', () => {
  dropdown.classList.toggle('show');
  console.log('click');
});

messages.forEach(message => {
  setTimeout(() => {
    message.style.display = 'none';
  }, 5000);
});