const dropdown = document.getElementById('dropdown');
const button = document.getElementById('button');

button.addEventListener('click', function(i = $(this)){
    dropdown = i.parent().find('.faq-answer');
    dropdown.classList.toggle('visible');
    console.log('click');
});