const dropdown = document.getElementById('dropdown');
const logout = document.getElementById('logout');
const button = document.getElementById('button');
const messages = document.querySelectorAll('.messages li');


try{
  button.addEventListener('click', () => {
    dropdown.classList.toggle('show');
    try {
      logout.classList.toggle('hide');
    }
    catch {
      console.log('no logout');
    }
    // logout.classList.toggle('hide');
    console.log('click');
  });
}
catch {}

messages.forEach(message => {
  setTimeout(() => {
    message.style.display = 'none';
  }, 1500);
});