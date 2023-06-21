function getZero(number) {
    if (number < 10) {
        return `0${number}`
    }
    else {
        return `${number}`
    }
}

const stopDateInput = document.getElementById('id_stop_date');
stopDateInput.addEventListener('click', function() {
    if (stopDateInput.value == '') {
        let dateToday = new Date()
        let day = dateToday.getDate()
        let mounth = dateToday.getMonth() + 1
        let year = dateToday.getFullYear()
        stopDateInput.value = `${getZero(day)}.${getZero(mounth)}.${getZero(year)}`
    }
})