document.getElementById('reviewForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const gameNameField = document.getElementById('gameName');
    const reasonField = document.getElementById('reason');
    const successMessage = document.getElementById('successMessage');

    let isValid = true;

    if (gameNameField.value.trim() === '') {
        showTooltip(gameNameField, 'Vul de naam van de game in.');
        isValid = false;
    }

    if (reasonField.value.trim() === '') {
        showTooltip(reasonField, 'Geef een reden op.');
        isValid = false;
    }

    if (isValid) {
        successMessage.style.display = 'block';

        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 3000);

        document.getElementById('reviewForm').reset();
    } else {
        successMessage.style.display = 'none';
    }
});

document.getElementById('reviewForm').addEventListener('input', function () {
    document.getElementById('successMessage').style.display = 'none';
    removeTooltips();
});

function showTooltip(element, message) {
    removeTooltips();
    const tooltip = document.createElement('div');
    tooltip.classList.add('tooltip-error');
    tooltip.innerHTML = `<i class='fas fa-exclamation-circle' style='margin-right: 5px;'></i>${message}`;
    document.body.appendChild(tooltip);
    
    const rect = element.getBoundingClientRect();
    tooltip.style.position = 'absolute';
    tooltip.style.left = `${rect.left + window.scrollX}px`;
    tooltip.style.top = `${rect.top + window.scrollY - tooltip.offsetHeight - 10}px`;
    tooltip.style.backgroundColor = 'white';
    tooltip.style.color = '#e63946';
    tooltip.style.padding = '8px';
    tooltip.style.border = '1px solid #e63946';
    tooltip.style.borderRadius = '5px';
    tooltip.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
    tooltip.style.fontSize = '0.9rem';
    tooltip.style.zIndex = '1000';
    
    const arrow = document.createElement('div');
    arrow.style.position = 'absolute';
    arrow.style.left = '10px';
    arrow.style.bottom = '-5px';
    arrow.style.width = '0';
    arrow.style.height = '0';
    arrow.style.borderLeft = '5px solid transparent';
    arrow.style.borderRight = '5px solid transparent';
    arrow.style.borderTop = '5px solid #e63946';
    tooltip.appendChild(arrow);

    setTimeout(() => {
        tooltip.remove();
    }, 3000);
}

function removeTooltips() {
    document.querySelectorAll('.tooltip-error').forEach(tooltip => tooltip.remove());
}
