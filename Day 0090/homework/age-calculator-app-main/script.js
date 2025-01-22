document.getElementById('age-form')
addEventListener('submit', function(event) {
    event.preventDefault();

    const day = parseInt(document.getElementById('day').value);
    const month = parseInt(document.getElementById('month').value);
    const year = parseInt(document.getElementById('year').value);
    const errorMessage = document.getElementById('error-message');
    const resultDiv = document.getElementById('result');

    // Reset messages
    errorMessage.innerText = '';
    resultDiv.innerText = '';

    const today = new Date();
    const birthDate = new Date(year, month - 1, day);

    // Validation checks
    if (!day || !month || !year) {
        errorMessage.innerText = 'All fields are required.';
        return;
    }
    if (day < 1 || day > 31 || month < 1 || month > 12) {
        errorMessage.innerText = 'Invalid day or month.';
        return;
    }
    if (birthDate > today) {
        errorMessage.innerText = 'Date cannot be in the future.';
        return;
    }
    if ((month === 4 || month === 6 || month === 9 || month === 11) && day > 30) {
        errorMessage.innerText = 'Invalid date for the selected month.';
        return;
    }
    if (month === 2 && day > (isLeapYear(year) ? 29 : 28)) {
        errorMessage.innerText = 'Invalid date for February.';
        return;
    }

    // Calculate age
    const ageInMilliseconds = today - birthDate;
    const ageDate = new Date(ageInMilliseconds);
    const years = ageDate.getUTCFullYear() - 1970;
    const months = ageDate.getUTCMonth();
    const days = ageDate.getUTCDate() - 1;

    resultDiv.innerHTML = `<h2>${years} Years, ${months} Months, ${days} Days</h2>`;
});

// Leap year check function
function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}